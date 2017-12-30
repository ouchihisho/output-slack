# 使い方

```
$ python main.py 'hoge'
```

# 事前準備

## slack webhook

### slackで webhook を設定

slackでwebhookを設定して、webhook用のURLを取得しておく。

### 上記設定を setting.ini に記載

`../setting.ini`  を作成して以下を追記。

```
[slack]
channel_name = #hoge
webhook_url = https://hooks.slack.com/services/fuga
```
