import unittest
import os
import tempfile
from app import app, allowed_file, count_words

class TestFileUpload(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_allowed_file(self):
        self.assertTrue(allowed_file('sample.txt'))
        self.assertFalse(allowed_file('sample.pdf'))

    def test_get_request(self):
        """Тестирование GET запроса."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Now expecting 200
        self.assertIn('Upload a File'.encode('utf-8'), response.data)

    def test_count_words(self):
        file_path = 'sample.txt'
        with open(file_path, 'w') as f:
            f.write('hello world\nhello python\npython is awesome')

        expected_output = [('hello', 2), ('python', 2), ('world', 1), ('is', 1), ('awesome', 1)]
        self.assertEqual(count_words(file_path), expected_output)

        os.remove(file_path)

    def test_404_error(self):
        """Тестирование 404 ошибки."""
        response = self.client.get('/nonexistent-route')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()