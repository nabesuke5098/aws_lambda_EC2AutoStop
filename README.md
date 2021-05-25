# aws_lambda_EC2AutoStop
特定のタグを持つEC2のインスタンスを自動で停止する処理

# 使い方
CloudWatchEventsと組み合わせて活用

CloudWatchEventsのイベントルールを作成
例：　スケジュール　cron式　＊　２１　＊　＊　＊　？　＊
　　 ターゲット　[lambda]

