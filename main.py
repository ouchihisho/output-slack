#!/usr/bin/env python

import argparse
import io
import ConfigParser
from post_slack import post_slack

config = ConfigParser.ConfigParser()
config.read('../setting.ini')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('stream', help='File to stream to the API')
    args = parser.parse_args()

    slack_channel_name = config.get('slack', 'channel_name')
    slack_webhook_url = config.get('slack', 'webhook_url')
    post_slack(args.stream, slack_channel_name, slack_webhook_url)