#!/usr/bin/env python

import commands

def post_slack(message, slack_channel_name, slack_webhook_url):
    command_str = ('curl -X POST --data-urlencode "payload={\\"channel\\": \\"%s\\", \\"text\\": \\"%s\\"}" \'%s\'' % (slack_channel_name, message, slack_webhook_url))
    print('command_str  : ' + command_str + ' )')
    commands.getstatusoutput(command_str)
    print('post to slack ( message : ' + message + ' )')


