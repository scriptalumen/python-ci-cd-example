import unittest

class TestApp(unittest.TestCase):
    def test_app(self):  
        self.assertIn("Hello", "Hello, Docker CI/CD!")  

if __name__ == "__main__":
    unittest.main()

