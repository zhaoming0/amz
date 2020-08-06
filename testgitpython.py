from git import Repo
import os
import subprocess
import sys
import time
from shutil import copyfile


repo = Repo('.')
# print(repo)
# print(repo.active_branch)
# repo.index.add(['1.csv'])
# repo.index.commit('test gitpython 2348')
# subprocess.check_call(['git', 'push', 'origin', 'master'])
for i in (os.listdir('.')):
    if i.endswith('csv') and 'Second-collection' in i:
        commitName = (i.split('.')[0])
        copyfile(i, 'test.csv')
        repo.index.add(['test.csv'])
        repo.index.commit(commitName)
        subprocess.check_call(['git', 'push', 'origin', 'master'])
        time.sleep(10)

