import re
import datetime
import urllib
import requests
import argparse
from marathon import MarathonClient

MARATHON_URL = 'http://10.141.141.10:8080/'


c = MarathonClient(MARATHON_URL)

def convert_datetime(date_string):
    return datetime.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%fZ')


def find_latest():
    apps = c.list_apps(**{'labels': {'environment': 'staging',
                                     'name': 'test1',
                                     'deploy_by': 'jenkins'}})
    latest_app = apps[0]
    for app in apps:
        if convert_datetime(app.version) > \
                convert_datetime(latest_app.version):
            latest_app = app
    return MARATHON_URL + "ui/#/apps/" + urllib.parse.quote(latest_app.id, safe="")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #parser.add_argument('image_name', help='project_name via test1', type=str)
    parser.add_argument('--version', required=False, type=int,  help='project-version')
    args = parser.parse_args()
    #print (find_latest().id)
