from git import Repo
import os
import subprocess
import sys
import time

repo = Repo('.')
# print(repo)
# print(repo.active_branch)
# repo.index.add(['1.csv'])
# repo.index.commit('test gitpython')
# repo.git.push

gitconfig = {
    'cwd': './blog/public',
    'git': {
        'origin': ['zhaoming0@github.com:akkuman/akkuman.github.io.git', 'master'],
        # 'coding': ['git@git.coding.net:Akkuman/Akkuman.git', 'coding-pages'],
    }
}
 
def main():
      
    # push to every remote repo
    for k,v in gitconfig['git'].items():
        print('----')
        print(k)
        print(v)
        print('+++++++++++++')
        # subprocess.check_call(['git', 'push', k, 'master:%s' % v[1]])
        print(['git', 'push', k, 'master:%s' % v[1]])
 
if __name__ == '__main__':
    # if len(sys.argv) == 2:
    #     if sys.argv[1] == '-h':
    #         print('Usage:\n\t%s [commit_message]' % sys.argv[0])
    main()