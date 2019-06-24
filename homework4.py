#!/usr/bin/python
import requests
import argparse

version = "0.9"
token = '7c187cd9203eb03cffb2acbf1f4cfee61f8e1532'
parser = argparse.ArgumentParser()
parser.add_argument('-user', nargs = 1, help = "write github username", required = True)
parser.add_argument('-repo', nargs = 1, help = "write name of repo", required = True)
parser.add_argument('-field', nargs = 1, help = "write argument likes id, title, html_url etc... ", required = True)
parser.add_argument('-v', action = 'version', version = 'Lastpull 0.9')

args = parser.parse_args()
if args.field[0]:

    b = requests.get('https://api.github.com/repos/' + args.user[0] + '/' + args.repo[0] + '/pulls',
                     auth = ('woraccmsq', token))
    print(b.json()[0][args.field[0]])

else:
    print('bed arguments')

