#!/usr/bin/env python
import sys
import json
import subprocess
from ruamel.yaml import YAML
import os

# 1.
version = subprocess.check_output(
    ['python', '-V'], universal_newlines=True).split('\n')[0]
# 2.
virtual_environment = os.popen('pyenv version').read()
# 3.
python_executable_location = sys.executable
# 4.
pip_location = subprocess.check_output(['which', 'pip'], universal_newlines=True).split('\n')[0]
# 5.
pythonpath = sys.path
# 6.
n = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE).stdout.decode('utf-8').split()
a = []
for i in n:
    a += i.split('==')
installed_packages = {x: a[a.index(x) + 1] for x in a if a.index(x) % 2 == 0}
# 7.
site_packages = next(s for s in sys.path if 'site-packages' in s)

data = {}
data['Python info'] = []
data['Python info'].append({
    '1. Version:': version,
    '2. virtual environment :': virtual_environment,
    '3. Python executable location:': python_executable_location,
    '4. pip location:': pip_location,
    '5. PYTHONPATH:': pythonpath,
    '6. Installed packages: name, version -': installed_packages,
    '7. site-packages location:': site_packages
})
with open('python.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

inp = """\
# information about the current versions of python in the system:
condition: result
"""

yaml = YAML()
code = yaml.load(inp)
code['1. Version:'] = version
code['2. virtual environment :'] = virtual_environment
code['3. Python executable location:'] = python_executable_location
code['4. pip location:'] = pip_location
code['5. PYTHONPATH:'] = pythonpath
code['6. Installed packages: name, version -'] = installed_packages
code['7. site-packages location:'] = site_packages

with open('python.yaml', 'w') as outfile:
    yaml.dump(code, outfile)
