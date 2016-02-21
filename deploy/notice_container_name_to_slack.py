import time
from slackclient import SlackClient
import argparse
from latest_container_name import find_latest

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--message', default="hoge", type=str,  help='message')
    parser.add_argument('--channel', default="hoge", type=str,  help='message')
    parser.add_argument('--token', default="hoge", type=str,  help='message')
    args = parser.parse_args()
    sc = SlackClient(args.token)
    sc.rtm_connect()
    #sc.rtm_send_message(channel=args.channel, message="{} でデプロイしましたですよ".format(find_latest().id))
    sc.rtm_send_message(channel=args.channel, message="{} でデプロイしましたですよ〜".format(find_latest()))
