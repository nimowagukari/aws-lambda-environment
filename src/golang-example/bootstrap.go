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

func handleRequest(ctx context.Context, event struct{}) (string, error) {
	lc, _ := lambdacontext.FromContext(ctx)
	fmt.Printf("event: %#v\n", event)
	fmt.Printf("context: %#v\n", lc)
	return "Hello, World.", nil
}
