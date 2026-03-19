import unittest
from base64 import b64encode

from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    # GET /

    def test_health_check(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.get_json()['ok'])

    # POST /dimensions

    def test_dimensions_valid_image(self):
        res = self.client.post('/dimensions', json={'image': b64encode(b'test').decode()})
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn('height', data)
        self.assertIn('length', data)
        self.assertIn('weight', data)

    def test_dimensions_with_data_uri_prefix(self):
        img = 'data:image/png;base64,' + b64encode(b'test').decode()
        res = self.client.post('/dimensions', json={'image': img})
        self.assertEqual(res.status_code, 200)

    def test_dimensions_missing_body(self):
        res = self.client.post('/dimensions', content_type='application/json')
        self.assertEqual(res.status_code, 400)
        errors = res.get_json()
        self.assertEqual(errors[0]['message'], 'Incorrect JSON body')

    def test_dimensions_missing_image_field(self):
        res = self.client.post('/dimensions', json={'foo': 'bar'})
        self.assertEqual(res.status_code, 400)
        errors = res.get_json()
        self.assertEqual(errors[0]['message'], 'Missing parameter')
        self.assertEqual(errors[0]['field'], 'image')

    def test_dimensions_invalid_base64(self):
        res = self.client.post('/dimensions', json={'image': '!!!not-base64!!!'})
        self.assertEqual(res.status_code, 400)
        errors = res.get_json()
        self.assertEqual(errors[0]['message'], 'Invalid base64 representation')

    # Error handlers

    def test_404(self):
        res = self.client.get('/nonexistent')
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.get_json()['error'], 'Not found')

    def test_405(self):
        res = self.client.delete('/dimensions')
        self.assertEqual(res.status_code, 405)
        self.assertEqual(res.get_json()['error'], 'Method not allowed')

    # GET /dimensions not allowed

    def test_dimensions_get_not_allowed(self):
        res = self.client.get('/dimensions')
        self.assertEqual(res.status_code, 405)


if __name__ == '__main__':
    unittest.main()
