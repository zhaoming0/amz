from git import Repo
import os
import subprocess
import sys
import time
from shutil import copyfile


repo = Repo('.')
while True:
    time_now = time.strftime("%H:%M:%S", time.localtime())
    if time_now == "07:00:00":
        print(time_now)
        time.sleep(1)
        for i in (os.listdir('.')):
            if i.endswith('csv') and i != 'test.csv':
                print(i)
                commitName = (i.split('.')[0])
                copyfile(i, 'test.csv')
                repo.index.add(['test.csv'])
                repo.index.commit(commitName)
                subprocess.check_call(['git', 'push', 'origin', 'master'])
                time.sleep(10)

