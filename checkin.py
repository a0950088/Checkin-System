import os
import requests
from lxml import html, etree
from datetime import datetime
from bs4 import BeautifulSoup as BS

HOST = "https://cis.ncu.edu.tw/HumanSys/home"
NCU_HOST = "https://portal.ncu.edu.tw/login"
LEAVE_URL = "https://portal.ncu.edu.tw/leaving"
NCU_CHECKIN_HOST = "https://cis.ncu.edu.tw/HumanSys/student/stdSignIn"
NCU_CHECKIN_CREATE = "https://cis.ncu.edu.tw/HumanSys/student/stdSignIn/create"
NCU_POST_CHECKIN_CREATE = "https://cis.ncu.edu.tw/HumanSys/student/stdSignIn_detail"

LOGIN_URL = "https://cis.ncu.edu.tw/HumanSys/login"
ENDPOINT_URL = "https://portal.ncu.edu.tw/endpoint?openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.mode=checkid_setup&openid.return_to=https%3A%2F%2Fcis.ncu.edu.tw%2FHumanSys%2Flogin&openid.realm=https%3A%2F%2Fcis.ncu.edu.tw&openid.ns.ax=http%3A%2F%2Fopenid.net%2Fsrv%2Fax%2F1.0&openid.ax.mode=fetch_request&openid.ax.type.user_roles=http%3A%2F%2Faxschema.org%2Fuser%2Froles&openid.ax.type.contact_email=http%3A%2F%2Faxschema.org%2Fcontact%2Femail&openid.ax.type.contact_name=http%3A%2F%2Faxschema.org%2Fcontact%2Fname&openid.ax.type.contact_ename=http%3A%2F%2Faxschema.org%2Fcontact%2Fename&openid.ax.type.student_id=http%3A%2F%2Faxschema.org%2Fstudent%2Fid&openid.ax.type.alunmi_leaveSem=http%3A%2F%2Faxschema.org%2Falunmi%2FleaveSem&openid.ax.required=user_roles&openid.ax.if_available=contact_email%2Ccontact_name%2Ccontact_ename%2Cstudent_id%2Calunmi_leaveSem&openid.identity=https%3A%2F%2Fportal.ncu.edu.tw%2Fuser%2F&openid.claimed_id=https%3A%2F%2Fportal.ncu.edu.tw%2Fuser%2F"

REQUIRE_SIGNIN_TIME = 8
current_time = datetime.now()
session = requests.session()
userinfo = os.environ['NCU_PORTAL'].split(":")
ACCOUNT = userinfo[0]
PASSWORD = userinfo[1]

try:
    res = session.get(ENDPOINT_URL)
    # print("-----------------------------")
    # print(res.status_code)
    # print(res.cookies)
    # print(session.cookies)
    # print("-----------------------------")
    sess = session.cookies.get_dict()['SESSION']
    xsrf = session.cookies.get_dict()['XSRF-TOKEN']
    portal = session.cookies.get_dict()['portal']
    cookies = res.cookies

    payload = {
        'username': ACCOUNT,
        'password': PASSWORD,
        '_csrf': xsrf,
        'language': 'CHINESE',
    }
    print("GET ", ENDPOINT_URL, "Success")
except Exception as err:
    print("GET ", ENDPOINT_URL, "Failed")
    print("Error: ", err)

try:
    res = session.post(NCU_HOST, data=payload, cookies=cookies)
    # print("-----------------------------")
    # print(res.status_code)
    # print(res.cookies)
    # print(session.cookies)
    # print("-----------------------------")
    cookies = session.cookies
    sess = session.cookies.get_dict()['SESSION']
    xsrf = session.cookies.get_dict()['XSRF-TOKEN']
    payload = {
        'chineseName': "人事系統",
        'englishName': "人事系統",
        '_csrf': xsrf
    }
    print("POST ", NCU_HOST, "Success")
except Exception as err:
    print("POST ", NCU_HOST, "Failed")
    print("Error: ", err)
    
try:
    res = session.post(LEAVE_URL, data=payload, cookies=cookies)
    # print("-----------------------------")
    # print(res.status_code)
    # print(res.cookies)
    # print(session.cookies)
    # print("-----------------------------")
    print("POST ", LEAVE_URL, "Success")
except Exception as err:
    print("POST ", LEAVE_URL, "Failed")
    print("Error: ", err)

try:
    res = session.get(HOST)
    content = res.content.decode('utf-8')
    page = BS(content, features='lxml')
    # print("-----------------------------")
    # print(res.status_code)
    # print(res.cookies)
    # print(session.cookies)
    # print("-----------------------------")
    node = page.find('div', {'class': 'name-line'})
    print(node.contents)
    # tree = html.fromstring(res.text)
    # user = list(set(tree.xpath('//div[@class="name-line"]')))[0]
    # print(etree.tostring(user))
    # print(res.url)
    cookies = dict(res.cookies)
    cookies['locale'] = session.cookies.get_dict()['locale']
    cookies['BIGipServerpool-cis'] = session.cookies.get_dict()['BIGipServerpool-cis']
    print("GET ", HOST, "Success")
except Exception as err:
    print("GET ", HOST, "Failed")
    print("Error: ", err)

try:
    res = session.get(NCU_CHECKIN_HOST, cookies=cookies)
    content = res.content.decode('utf-8')
    # print("-----------------------------")
    # print(res.status_code)
    # print(res.cookies)
    # print(session.cookies)
    # print(content)
    # print("-----------------------------")
    page = BS(content, features='lxml')
    node = page.find(id='table1')
    print(node)
    token = page.find('input', {'name': '_token'})
    token = token.get('value')
    print(token)
    cookies = dict(res.cookies)
    cookies['locale'] = session.cookies.get_dict()['locale']
    cookies['BIGipServerpool-cis'] = session.cookies.get_dict()['BIGipServerpool-cis']
    
    ParttimeUsuallyId = 210885
    print("GET ", NCU_CHECKIN_HOST, "Success")
except Exception as err:
    print("GET ", NCU_CHECKIN_HOST, "Failed")
    print("Error: ", err)

try:    
    res = session.get(NCU_CHECKIN_CREATE, cookies=cookies, params={'ParttimeUsuallyId': ParttimeUsuallyId})
    content = res.content.decode('utf-8')
    page = BS(content, features='lxml')
    # print("-----------------------------")
    # print(res.status_code)
    # print(res.cookies)
    # print(session.cookies)
    # print("-----------------------------")
    idNo = page.find('input', {'id': 'idNo'})
    idNo = idNo.get('value')
    print(idNo)
    signintime = page.find('div', {'id': 'SigninTime'})
    # idNo = signtime.get('value')
    signintime = signintime.contents
    print(signintime)
    signouttime = page.find('div', {'id': 'SignoutTime'})
    print(signouttime.contents)
    cookies = dict(res.cookies)
    cookies['locale'] = session.cookies.get_dict()['locale']
    cookies['BIGipServerpool-cis'] = session.cookies.get_dict()['BIGipServerpool-cis']
    payload = {
        'functionName' : "doSign",
        'idNo' : idNo,
        'ParttimeUsuallyId' : ParttimeUsuallyId,
        'AttendWork' : "",
        '_token' : token
    }
    print("GET ", NCU_CHECKIN_CREATE, "Success")
except Exception as err:
    print("GET ", NCU_CHECKIN_CREATE, "Failed")
    print("Error: ", err)

if signintime != []:
    signintime_hour = int(signintime[0].split(":")[0])
    if current_time.hour - signintime_hour >= REQUIRE_SIGNIN_TIME:
        try:
            res = session.post(NCU_POST_CHECKIN_CREATE, cookies=cookies, data=payload)
            content = res.content.decode('utf-8')
            print("-----------------------------")
            print(res.status_code)
            print(res.cookies)
            print(session.cookies)
            print(content)
            print("-----------------------------")
            print("POST ", NCU_POST_CHECKIN_CREATE, "Success")
        except Exception as err:
            print("POST ", NCU_POST_CHECKIN_CREATE, "Failed")
            print("Error: ", err)
    else:
        print("Not Yet")
else:
    print("signintime = []")
'''
1. GET https://portal.ncu.edu.tw/endpoint?openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.mode=checkid_setup&openid.return_to=https%3A%2F%2Fcis.ncu.edu.tw%2FHumanSys%2Flogin&openid.realm=https%3A%2F%2Fcis.ncu.edu.tw&openid.ns.ax=http%3A%2F%2Fopenid.net%2Fsrv%2Fax%2F1.0&openid.ax.mode=fetch_request&openid.ax.type.user_roles=http%3A%2F%2Faxschema.org%2Fuser%2Froles&openid.ax.type.contact_email=http%3A%2F%2Faxschema.org%2Fcontact%2Femail&openid.ax.type.contact_name=http%3A%2F%2Faxschema.org%2Fcontact%2Fname&openid.ax.type.contact_ename=http%3A%2F%2Faxschema.org%2Fcontact%2Fename&openid.ax.type.student_id=http%3A%2F%2Faxschema.org%2Fstudent%2Fid&openid.ax.type.alunmi_leaveSem=http%3A%2F%2Faxschema.org%2Falunmi%2FleaveSem&openid.ax.required=user_roles&openid.ax.if_available=contact_email%2Ccontact_name%2Ccontact_ename%2Cstudent_id%2Calunmi_leaveSem&openid.identity=https%3A%2F%2Fportal.ncu.edu.tw%2Fuser%2F&openid.claimed_id=https%3A%2F%2Fportal.ncu.edu.tw%2Fuser%2F

2. POST https://portal.ncu.edu.tw/login

3. POST https://portal.ncu.edu.tw/leaving

4. GET https://cis.ncu.edu.tw/HumanSys/home

5. GET https://cis.ncu.edu.tw/HumanSys/student/stdSignIn

6. GET https://cis.ncu.edu.tw/HumanSys/student/stdSignIn/create?ParttimeUsuallyId=210885

7. POST https://cis.ncu.edu.tw/HumanSys/student/stdSignIn_detail
json "isOK"

'''