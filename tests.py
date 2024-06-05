import unittest
from flask import Flask, render_template, request
import math
from app import app, cot, toradians, func

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.pi=3.141

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1 class="title">Trigonometric functions</h1>', response.data)

    def test_form_route1(self):
        response = self.app.post('/', data=dict(
            func='sin',
            num_2='90',
            units='degrees',
            accuracy='5'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1.00000', response.data)

    def test_form_route2(self):
        response = self.app.post('/', data=dict(
            func='cos',
            num_2='30',
            units='degrees',
            accuracy='2'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'0.87', response.data)

    def test_form_route3(self):
        response = self.app.post('/', data=dict(
            func='tg',
            num_2='3.14',
            units='radians',
            accuracy='3'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'tg(3.14)=-0.002', response.data)

    def test_form_route4(self):
        response = self.app.post('/', data=dict(
            func='ctg',
            num_2='1.5707',
            units='radians',
            accuracy='6'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ctg(1.5707)=0.000096', response.data)

    def test_hello_route(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>me</h1>', response.data)

if __name__ == '__main__':
    unittest.main()
