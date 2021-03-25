# 使い方

## 事前準備

* RDS及びRDS Proxyを用意する。テーブルも作っておく。
* RDS Proxy経由でINSERTする方のLambdaは同一VPCで揃えること。
* SQSを用意する。

## SQSにメッセージを送る

sqs_insert_lambda内のlambda_function.pyを使用する

## SQSトリガーからRDS Proxy経由でINSERTする

* pymysqlをインストールする

```
pip install pymysql -t /path/to/sqs_to_rds_lambda
```

* lambda_function.py内の接続情報を環境に合わせて変更する
* zipで固めてLambdaにアップロード
