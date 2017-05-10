from django.test import TestCase


class TruthTest(TestCase):
    def test_truth(self):
        self.assertEqual(1+1, 2)
