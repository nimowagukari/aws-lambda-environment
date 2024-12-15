import json
from aws_lambda_powertools.utilities.typing import LambdaContext


def lambda_handler(event: dict[str, str], context: LambdaContext) -> str:
    print(json.dumps(event))
    ctx: dict[str, str | int] = {
        "aws_request_id": context.aws_request_id,
        "function_name": context.function_name,
        "function_version": context.function_version,
        "invoked_function_arn": context.invoked_function_arn,
        "log_group_name": context.log_group_name,
        "log_stream_name": context.log_stream_name,
        "memory_limit_in_mb": context.memory_limit_in_mb,
    }
    print(json.dumps(ctx))
    return "Hello, World."
