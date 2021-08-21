import unittest

import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_get_response(self):
        response = self.client.put('http://127.0.0.1:5000/sum', json=[1,2,3])
        expected_resp = {'status': 200, 'result': 6}
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.get_json(), expected_resp)
    def test_get_response_error(self):
        response = self.client.put('http://127.0.0.1:5000/sum', json=[1,2,'a'])
        expected_resp = {'status': 400, 'result': "All inputs must be numeric"}
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.get_json(), expected_resp)


if __name__ == "__main__":
    unittest.main()