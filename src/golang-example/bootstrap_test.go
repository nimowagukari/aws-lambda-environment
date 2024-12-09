package main

import (
	"context"
	"testing"
)

func TestHandleRequest(t *testing.T) {
	testcases := []struct {
		name    string
		want    string
		wantErr bool
	}{
		{
			name:    "Test",
			want:    "Hello, World.",
			wantErr: false,
		},
	}

	for _, tc := range testcases {
		t.Run(
			tc.name,
			func(t *testing.T) {
				got, err := handleRequest(context.TODO(), struct{}{})
				if (err != nil) != tc.wantErr {
					t.Error(err)
				}
				if got != tc.want {
					t.Errorf("got: %v, want: %v\n", got, tc.want)
				}
			},
		)
	}
}
