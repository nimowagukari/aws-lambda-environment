package main

import (
	"context"
	"fmt"

	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-lambda-go/lambdacontext"
)

func main() {
	lambda.Start(handleRequest)
}

func handleRequest(ctx context.Context, event interface{}) (string, error) {
	// 現時点では LambdaContext の有無で挙動は変えない為、２つ目の返り値は捨てる
	lc, _ := lambdacontext.FromContext(ctx)
	fmt.Printf("event: %#v\n", event)
	fmt.Printf("context: %#v\n", lc)
	return "Hello, World.", nil
}
