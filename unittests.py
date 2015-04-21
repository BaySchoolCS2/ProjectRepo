#! venv/bin/python
import application
from application.collections import User
import pymongo
import unittest
from werkzeug.security import generate_password_hash


class AppTestCase(unittest.TestCase):
    def login(self, email, password):
        return self.app.post('/login', data = dict(
            email = email,
            password = password
        ), follow_redirects = True)

    def logout(self):
        return self.app.get('/logout', follow_redirects = True)
    def setUp(self):
        application.app.config["MONGODB_SETTINGS"] = {
            'db' : 'project_test',
            'host' : 'localhost',
            'port' : 27017
        }
        self.app = application.app.test_client()
    def tearDown(self):
        pymongo.MongoClient().drop_database('project_test')

    def test_createTestUser(self):
        user = User(email="test@test.com",
                    alias="testUser1",
                    password=generate_password_hash("testPassword")
                )
        user.save()

    def test_login_logout(self):
        rv = self.login("test@test.com", "testPassword")
        assert 'Log in' not in rv.data
        rv = self.logout()
        assert 'Log in' in rv.data
        rv = self.login("test@test.com", "notTestPassword")
        print rv.data
        assert 'Wrong password' in rv.data
        rv = self.login("notTest@test.com", "testPassword")
        assert 'Wrong email' in rv.data

if __name__ == '__main__':
    unittest.main()
