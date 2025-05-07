import unittest
from login import login  # assume login is a function in login.py

class TestLogin(unittest.TestCase):

    def test_correct(self):
        self.assertTrue(login("admin", "1234"))

    def test_wrong(self):
        self.assertTrue(login("user", "pass"))  # ❌ this fails
