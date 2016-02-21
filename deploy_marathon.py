import re
import datetime
import requests
from marathon import MarathonClient

c = MarathonClient("http://10.141.141.10:8080/")

def convert_datetime(date_string):
    return datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")

def find_latest():
    apps = c.list_apps(**{'labels':{'environment': 'staging', 'name': 'test1', "deploy_by": "jenkins"}})
    
    latest_app = apps[0]
    for app in apps:
        if  convert_datetime(app.version) > convert_datetime(latest_app.version):
            latest_app = app
    return latest_app


def deploy(image_name, 
           id=None,
           label_dict={'environment': 'staging', 'name': "test1", "deploy_by": "jenkins"},
           env_dict={},
           args=[],
           cpus=0.1):
    if id == None:
        id = str(int(re.search("(?<=[\w|\.|/])[\d]+$", find_latest().id).group()) + 1)
    else:
        id = str(id)
    to_marathon = {
      "id": image_name + id,
      "cpus": cpus,
      "mem": 0.1,
      "labels": label_dict,
      "instances": 1,
      "container": {
        "type": "DOCKER",
        "docker": {
          "image": image_name,
          "network": "BRIDGE",
          "portMappings": [
            {  "protocol": "tcp", "hostPort": 0, "containerPort": 8000}
          ]
        }
      },
      "env": env_dict,
      "forcePullImage" : True,
      "args": ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    }

    headers = {'content-type': 'application/json'}
    r = requests.post("http://10.141.141.10:8080/v2/apps", json=to_marathon, headers=headers)
    r.raise_for_status()


def remove_all():
    for app in c.list_apps():
        requests.delete("http://10.141.141.10:8080/v2/apps/" + app.id)

def remove_above_latest():
    for app in c.list_apps():
        if app.id != find_latest().id:
            requests.delete("http://10.141.141.10:8080/v2/apps/" + app.id)


if __name__ == "__main__":
    remove_above_latest()
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("image_name", help="project_name via test1",
                                type=str)
    parser.add_argument("--version", required=False, type=int,  help="project-version")
    args = parser.parse_args()
    deploy(image_name=args.image_name, id=args.version)
