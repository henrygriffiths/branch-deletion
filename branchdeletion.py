import subprocess
import os

org = ''
repos = ['']
match = ''


def run(args, returnoutput = False):
    while True:
        try:
            sp = subprocess.run(args, text = True, check = True, capture_output = returnoutput)
            if returnoutput:
                print(sp.stdout)
            return sp.stdout
        except:
            while True:
                print('Running ' + ' '.join(args) + ' Failed.')
                result = input('(R)etry or (C)ontinue? : ')
                if result.lower() == 'r':
                    break
                elif result.lower() == 'c':
                    try:
                        return sp.stderr
                    except:
                        print('FAILED TO RETURN ERROR')
                        return

os.chdir('{}/{}'.format(os.getcwd(), 'repos'))
for repo in repos:
    if not os.path.exists('{}/{}'.format(os.getcwd(), org)):
        os.makedirs('{}/{}'.format(os.getcwd(), org))
    os.chdir('{}/{}'.format(os.getcwd(), org))
    run(['rm', '-rf', repo])
    run(['git', 'clone', 'https://github.com/{}/{}.git'.format(org, repo)])
    os.chdir('{}/{}'.format(os.getcwd(), repo))
    run(['git', 'fetch'])
    branches = run(['git', 'ls-remote', '--heads', 'origin'], returnoutput = True)
    for branch in branches.split('\n'):
        branch = branch[branch.find('refs/heads/'):].replace('refs/heads/', '')
        print(branch)
        if branch.startswith(match):
            run(['git', 'push', 'origin', '--delete', branch])
    os.chdir('{}/../../'.format(os.getcwd()))
os.chdir('{}/../'.format(os.getcwd()))