#!/usr/bin/env python
import configparser
import json
import os
import time
from datetime import datetime

import psutil


class MinLen:
    """This class set time"""

    def func(self, minutes):
        time_in_minutes = minutes * 60
        return time_in_minutes


def main():
    n = 0
    """ write config from config.ini:"""
    config = configparser.ConfigParser()
    config.sections()
    pathcfg = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini')
    config.read(pathcfg)
    config.sections()
    loadfile = config['common']
    interv = int(loadfile['interval'])
    tm = MinLen()
    print('LOADED SUCCESSFUL!!!')

#   start = time.time()
    while True:
        n += 1
#       now = datetime.now()  # current date and time
        time_stmp = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        cpu = psutil.cpu_percent(interval=1)
        d_mem = psutil.disk_usage('/')
        v_mem = psutil.virtual_memory().percent
        io = psutil.Process().io_counters()
        net = psutil.net_io_counters(pernic=True)
        if loadfile['output'] == 'plane':
# pathdata = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.txt')
            f = open('data.txt', 'a+')
            f.write('\n' + "SNAPSHOT " + str(n) + ": " + str(time_stmp) + ': ')
            f.write(' CpuLoad: ' + str(cpu))
            f.write(' DiskUse: ' + str(d_mem))
            f.write(' MemUse: ' + str(v_mem))
            f.write(' IO: ' + str(io))
            f.write(' Network: ' + str(net))
        elif loadfile['output'] == 'json':
            data = {}
            data['SNAPSHOT ' + str(n)] = []
            data['SNAPSHOT ' + str(n)].append({
                '': time_stmp,
                'CpuLoad': cpu,
                'DiskUse': d_mem,
                'MemUse': v_mem,
                'IO': io,
                'Network': net
            })
            pathjson = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.json')
            with open(pathjson, 'a+') as outfile:
                outfile.write(json.dumps(data) + '\n')
        else:
            print('Write plane or json')
        time.sleep(tm.func(interv))


if __name__ == "__main__":
    main()
