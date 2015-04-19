import unittest
import application
import pymongo


class AppTestCase(unittest.TestCase):
    def setUp(self):
        application.app.config["MONGODB_SETTINGS"] = {
            'db': 'project_test',
            'host': 'localhost',
            'port': 27017
        }
        self.app = application.app.test_client()
    def tearDown(self):
        pymongo.connect().drop_database('project_test')

    def test_createTestUser():
        pass
if __name__ == '__main__':
    unittest.main()
