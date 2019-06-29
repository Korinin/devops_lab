#!/usr/bin/python
import requests
import argparse

version = "1.0"

parser = argparse.ArgumentParser()
parser.add_argument('-user', nargs=1, help="write github username", required=True)
parser.add_argument('-repo', nargs=1, help="write name of repo", required=True)
parser.add_argument('-field', nargs=1, help="write argument likes id, title etc...", required=True)
parser.add_argument('-token', nargs=1, help="write name of repo", required=True)
parser.add_argument('-login', help="write flag for show login", action='store_true')
parser.add_argument('-ref', help="write flag for show name of pull", action='store_true')
parser.add_argument('-v', action='version', version='Lastpull 0.9')
parser.add_argument('--version', action='version', version='Lastpull 0.9')

args = parser.parse_args()
b = requests.get('https://api.github.com/repos/' + args.user[0] + '/' + args.repo[0] + '/pulls',
                 auth=('woraccmsq', args.token[0]))

if args.field[0]:
    print(b.json()[0][args.field[0]])
else:
    print('bad argument')
if args.login:
    print(b.json()[0]['user']['login'])
if args.ref:
    print(b.json()[0]['head']['ref'])
