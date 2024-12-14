import json
from aws_lambda_powertools.utilities.typing import LambdaContext


def lambda_handler(event, context: LambdaContext) -> str:
    print(json.dumps(event))
    print(json.dumps(context))
    return "Hello, World."
