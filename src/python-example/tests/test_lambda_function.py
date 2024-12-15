from aws_lambda_powertools.utilities.typing import LambdaContext
from lambda_function import lambda_handler
from unittest.mock import Mock
import unittest


class Test_Lambda_Handler(unittest.TestCase):
    def test_lambda_handler(self):
        mock_context = Mock(spec=LambdaContext)
        mock_context.aws_request_id = "aws_request_id"
        mock_context.function_name = "function_name"
        mock_context.function_version = "function_version"
        mock_context.invoked_function_arn = "invoked_function_arn"
        mock_context.log_group_name = "log_group_name"
        mock_context.log_stream_name = "log_stream_name"
        mock_context.memory_limit_in_mb = 123

        self.assertEqual(
            lambda_handler({"event": "event"}, mock_context),
            "Hello, World."
        )


if __name__ == '__main__':
    unittest.main()
