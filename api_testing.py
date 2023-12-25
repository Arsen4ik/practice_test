import requests
import logging
import os
import unittest

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'logs_for_api.log')


def configure_logging(name, file=log_file):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


main_logger = configure_logging('main')


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = main_logger

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                response = requests.get(url)

            elif request_type == 'POST':
                response = requests.post(url, data=data)
                stop_flag = True
            elif request_type == 'DELETE':
                response = requests.delete(url)
                stop_flag = True
            elif request_type == 'PUT':
                response = requests.put(url, data=data)
                stop_flag = True

            if not expected_error and response.status_code == 200:
                stop_flag = True
                break

        # log part
        self.logger.debug(f'{request_type} example')
        self.logger.debug(response.url)
        self.logger.debug(response.status_code)
        self.logger.debug(response.reason)
        self.logger.debug(response.text)
        self.logger.debug(response.json())
        self.logger.debug('-----------')

        return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.status_code

    def post(self, endpoint, body):
        url = f'{self.base_url}/{endpoint}/'
        response = self._request(url, 'POST', data=body)
        return response.status_code

    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.status_code

    def put(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'PUT', data=body)
        return response.status_code


class JsonRequest(BaseRequest):
    def __init__(self):
        super().__init__('http://localhost:3000')

    def get_color(self, entity_id):
        return self.get('color', entity_id)

    def put_color(self, entity_id, data):
        return self.put('color', entity_id, data)

    def delete_color(self, entity_id):
        return self.delete('color', entity_id)

    def get_person(self, entity_id):
        return self.get('person', entity_id)

    def put_person(self, entity_id, data):
        return self.put('person', entity_id, data)

    def delete_person(self, entity_id):
        return self.delete('person', entity_id)

    def get_product(self, entity_id):
        return self.get('product', entity_id)

    def put_product(self, entity_id, data):
        return self.put('product', entity_id, data)

    def delete_product(self, entity_id):
        return self.delete('product', entity_id)

    def get_city(self, entity_id):
        return self.get('city', entity_id)

    def put_city(self, entity_id, data):
        return self.put('city', entity_id, data)

    def delete_city(self, entity_id):
        return self.delete('city', entity_id)

    def get_shop(self, entity_id):
        return self.get('shop', entity_id)

    def put_shop(self, entity_id, data):
        return self.put('shop', entity_id, data)

    def delete_shop(self, entity_id):
        return self.delete('shop', entity_id)


class TestJsonRequests(unittest.TestCase):
    def setUp(self):
        self.json_request = JsonRequest()

    def test_get_color(self):
        id = 2
        data = self.json_request.get_color(id)
        self.assertEqual(data, 200)

    def test_put_color(self):
        data = {
            "id": 2,
            "color": "red",
        }
        result = self.json_request.put_color(data['id'], data)
        self.assertEqual(result, 200)

    def test_delete_color(self):
        id = 2
        data = self.json_request.delete_color(id)
        self.assertEqual(data, 200)

    def test_get_person(self):
        id = 2
        data = self.json_request.get_person(id)
        self.assertEqual(data, 200)

    def test_put_person(self):
        data = {
            'id': 2,
            'name': 'new name',
            'phone_number': '777777777'
        }
        result = self.json_request.put_person(data['id'], data)
        self.assertEqual(result, 200)

    def test_delete_person(self):
        id = 2
        result = self.json_request.delete_person(id)
        self.assertEqual(result, 200)

    def test_get_product(self):
        id = 2
        data = self.json_request.get_product(id)
        self.assertEqual(data, 200)

    def test_put_product(self):
        data = {
            'id': 2,
            'name': 'new product',
            'price': 7878,
            'category': 'new hz'
        }
        result = self.json_request.put_product(data['id'], data)
        self.assertEqual(result, 200)

    def test_delete_product(self):
        id = 2
        result = self.json_request.delete_product(id)
        self.assertEqual(result, 200)

    def test_get_city(self):
        id = 2
        projects_data = self.json_request.get_city(id)
        self.assertEqual(projects_data, 200)

    def test_put_city(self):
        data = {
            'id': 2,
            'name': 'new name',
            'description': 'lorem insup ...'
        }
        result = self.json_request.put_city(data['id'], data)
        self.assertEqual(result, 200)

    def test_delete_city(self):
        id = 2
        result = self.json_request.delete_city(id)
        self.assertEqual(result, 200)

    def test_get_shop(self):
        id = 2
        data = self.json_request.get_shop(id)
        self.assertEqual(data, 200)

    def test_put_shop(self):
        data = {
            "id": 2,
            "name": "new name",
            "contact_person": "new contact",
            "email": "gglol@ya.us"
        }
        result = self.json_request.put_shop(data['id'], data)
        self.assertEqual(result, 200)

    def test_delete_shop(self):
        id = 2
        result = self.json_request.delete_shop(id)
        self.assertEqual(result, 200)