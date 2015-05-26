#! venv/bin/python
import application
import os
import unittest
from mongoengine import connect

MONGODB = {
    'db' : 'project_test'
}



class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, application.app.config["MONGODB_SETTINGS"] = MONGODB, MONGODB
        application.app.secret_key="TESTING"
        application.app.config["TESTING"] = True
        application.app.config['WTF_CSRF_ENABLED'] = False
        self.app = application.app.test_client()
        #application.init_db()
    def tearDown(self):
        pass
        #connect(MONGODB["db"]).drop_database()
    def login(self, email, password):
        return self.app.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get("/logout", follow_redirects=True)

    def signup(self, email, alias, password, password2=None):
        if password2 == None:
            password2 = password
        return self.app.post('/signup', data=dict(
            email=email,
            alias=alias,
            password=password,
            password2=password2
        ), follow_redirects=True)

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No Posts Found' in rv.data

    def test_signup(self):
        rv = self.signup("admin", "admin", "admin", "admin")
        #print rv.data
        assert "Password too short" in rv.data
        rv = self.signup("admin", "admin", "password", "password2")
        assert "Passwords do not match" in rv.data
        rv = self.signup("admin", "admin", "password")
        assert "Email not correct" in rv.data
        rv = self.signup("admin@test.com", "admin", "password")
        print rv.data
        #assert "Login" in rv.data

    def test_login_logout(self):
        rv = self.login('admin@test.com', 'password')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx@test.com', 'password')
        assert 'Wrong email' in rv.data
        rv = self.login('admin@test.com', 'password1')
        assert 'Invalid password' in rv.data

if __name__ == '__main__':
    unittest.main()
