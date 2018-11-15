from contextlib import suppress
from invoke import task
import json
import os
from collections import UserDict

REPORTS_DIRECTORY = 'reports'
SCOUT2_AWS_CONFIG = 'scout2-report/inc-awsconfig/aws_config.js'


def parse(data):
    return json.loads(data.split('=', 1)[1])


def delete_keys(dictionary):
    del dictionary['last_run']
    del dictionary['services']['sns']['targets']

def save_to_file(filename):
    os.makedirs(REPORTS_DIRECTORY, exist_ok=True)
    with open(SCOUT2_AWS_CONFIG, 'r') as f:
        data = f.read()
        json_data = parse(data)
    with open("{}/{}".format(REPORTS_DIRECTORY, filename), 'w') as f:
        f.write(json.dumps(json_data, indent=4, sort_keys=True))

@task
def save_current(ctx):
    ctx.run('Scout2 --no-browser --force')
    save_to_file('current.json')

@task
def save_desired(ctx):
    save_to_file('desired.json')

@task
def compare(ctx):
    save_current(ctx)
    with open("{}/{}".format(REPORTS_DIRECTORY, 'desired.json'), 'r') as f:
        desired = json.loads(f.read())
    with open("{}/{}".format(REPORTS_DIRECTORY, 'current.json'), 'r') as f:
        current = json.loads(f.read())
    delete_keys(desired)
    delete_keys(current)
    assert desired == current
