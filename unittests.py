import application
from mongoengine import connect
import unittest
from werkzeug.security import generate_password_hash

MONGODB = {
    'db' : 'project_test',
    'host' : 'localhost',
    'port' : 27017
}



class AppTestCase(unittest.TestCase):
    def setUp(self):
        application.app.config["MONGODB_SETTINGS"] = MONGODB
        application.app.config["WTF_CSRF_ENABLED"] = False
        application.app.config["TESTING"] = True
        application.app.secret_key = "TEST KEY"
        self.app = application.app.test_client()

    def tearDown(self):
        connect(
            db = MONGODB['db'],
            host = MONGODB['host'],
            port = MONGODB['port']
        ).drop_database(MONGODB['db'])

    def login(self, email, password):
        return self.app.post('/login', data = dict(
            email = email,
            password = password
        ), follow_redirects = True)

    def logout(self):
        return self.app.get('/logout', follow_redirects = True)

    def signup(self, email, alias, password, password2):
        return self.app.post('/signup', data = dict(
            email =  email,
            alias = alias,
            password = password,
            password2 = password2
        ), follow_redirects = True)

    def test_signup(self):
        rv = self.signup('test@test.com', 'testTest', 'password', 'password')
        assert 'login' in rv.data
        rv = self.signup('derp@derp.com', 'testTest2', 'password', 'password')
        assert 'Email or username' in rv.data
        rv = self.signup('derp@herp.com', 'testTest', 'password', 'password')
        assert 'Email or username' in rv.data
        rv = self.signup('derp@herp.com', 'testTest2', 'password', 'password2')
        assert 'Passwords do no match'
        rv = self.signup('derp@herp.com', 'testTest2', 'pass', 'pass')
        assert 'Password too short'


    # def test_login(self):
    #     rv = self.login("test@test.com", "testPassword")
    #     assert 'Log in' not in rv.data
    #     rv = self.logout()
    #     assert 'Log in' in rv.data
    #     rv = self.login("test@test.com", "notTestPassword")
    #     assert 'Wrong password' in rv.data
    #     rv = self.login("notTest@test.com", "testPassword")
    #     assert 'Wrong email' in rv.data


if __name__ == '__main__':
    unittest.main()
