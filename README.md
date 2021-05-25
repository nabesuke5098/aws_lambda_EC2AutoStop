# aws_lambda_EC2AutoStop<br />
特定のタグを持つEC2のインスタンスを自動で停止する処理<br />
<br />
# 使い方<br />
CloudWatchEventsと組み合わせて活用<br />
<br />
CloudWatchEventsのイベントルールを作成<br />
例：　スケジュール　cron式　＊　２１　＊　＊　＊　？　＊<br />
　　 ターゲット　[lambda]<br />

