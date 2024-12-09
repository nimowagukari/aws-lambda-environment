# golang-example

これは、go 言語での AWS Lambda の学習用コードです。

## 動作検証

コンテナイメージにインストール済みの [aws-lambda-rie](https://github.com/aws/aws-lambda-runtime-interface-emulator) を利用できます。

```bash
# terminal 1: aws-lambda-rie の実行
aws-lambda-rie go run bootstrap.go

# terminal 2: aws-lambda-rie により起動したエンドポイントへのリクエスト
curl -XPOST "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{}'
```

## 手動デプロイ

事前にあなたの AWS アカウント上に Lambda 関数名：golang-example を作成しておく必要があります。  
設定の詳細については記載しません。

```bash
# 最新コードのビルド＆zip化
go build bootstrap.go
zip bootstrap.zip bootstrap

# デプロイ
aws lambda update-function-code --function-name golang-example --zip-file fileb://bootstrap.zip

```
