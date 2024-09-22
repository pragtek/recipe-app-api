from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):

    def test_add(self):
        res = calc.add(10,2)
        self.assertEqual(res, 12)

    def test_subtract(self):
        res = calc.subtract(10,5)
        self.assertEqual(res, 5)
    