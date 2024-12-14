from lambda_function import lambda_handler
import unittest


class Test_Lambda_Handler(unittest.TestCase):
    def test_lambda_handler(self):
        self.assertEqual(lambda_handler(
            {"event": "event"}, {"context": "context"}), "Hello, World.")


if __name__ == '__main__':
    unittest.main()
