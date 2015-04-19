import unittest
import application
import pymongo
from application.collections import User


class AppTestCase(unittest.TestCase):
    def setUp(self):
        application.app.config["MONGODB_SETTINGS"] = {
            'db': 'project_test',
            'host': 'localhost',
            'port': 27017
        }
        self.app = application.app.test_client()
    def tearDown(self):
        pymongo.MongoClient().drop_database('project_test')

    def test_createTestUser(self):
        u = User(email="test@test.com", alias="testUser1") #... continue later
if __name__ == '__main__':
    unittest.main()
