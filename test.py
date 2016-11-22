#!/usr/bin/env python2
import unittest
import json

from server import engine, app


class TestCase(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        engine.execute("""DROP TABLE IF EXISTS test;""")
        engine.execute("""CREATE TABLE IF NOT EXISTS test (
          id bigint,
          name text,
          year text,
          school text,
          text text
        );""")
        engine.execute("""INSERT INTO test VALUES (
          123456,
          'sample_name',
          'sample_year',
          'sample_school',
          'sample_text'
        );""")

        self.app = app.test_client()
        return self.app

    def tearDown(self):
        engine.execute("""DROP TABLE IF EXISTS test;""")

    def test_web_post(self):
        print '### TESTCASE: POST ###'
        response = self.app.post('/api/comments', data = dict(
            name='peng',
            year='2018',
            school='Barnard',
            text='Hello World! This is test content.'
        ))
        print '\n'
        assert response.status_code == 200
        
        
    def test_web_get(self):
        print '### TESTCASE: GET ###'
        response = self.app.get('/api/comments')
        print '\n'
        assert response.status_code == 200
        
        
if __name__ == '__main__':
    unittest.main()
