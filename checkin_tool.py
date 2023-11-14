import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup as BS
import parsers
import log

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
ENDPOINT_URL = "https://portal.ncu.edu.tw/endpoint?openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.mode=checkid_setup&openid.return_to=https%3A%2F%2Fcis.ncu.edu.tw%2FHumanSys%2Flogin&openid.realm=https%3A%2F%2Fcis.ncu.edu.tw&openid.ns.ax=http%3A%2F%2Fopenid.net%2Fsrv%2Fax%2F1.0&openid.ax.mode=fetch_request&openid.ax.type.user_roles=http%3A%2F%2Faxschema.org%2Fuser%2Froles&openid.ax.type.contact_email=http%3A%2F%2Faxschema.org%2Fcontact%2Femail&openid.ax.type.contact_name=http%3A%2F%2Faxschema.org%2Fcontact%2Fname&openid.ax.type.contact_ename=http%3A%2F%2Faxschema.org%2Fcontact%2Fename&openid.ax.type.student_id=http%3A%2F%2Faxschema.org%2Fstudent%2Fid&openid.ax.type.alunmi_leaveSem=http%3A%2F%2Faxschema.org%2Falunmi%2FleaveSem&openid.ax.required=user_roles&openid.ax.if_available=contact_email%2Ccontact_name%2Ccontact_ename%2Cstudent_id%2Calunmi_leaveSem&openid.identity=https%3A%2F%2Fportal.ncu.edu.tw%2Fuser%2F&openid.claimed_id=https%3A%2F%2Fportal.ncu.edu.tw%2Fuser%2F"
NCU_HOST = "https://portal.ncu.edu.tw/login"
LEAVE_URL = "https://portal.ncu.edu.tw/leaving"
HOST = "https://cis.ncu.edu.tw/HumanSys/home"
NCU_CHECKIN_HOST = "https://cis.ncu.edu.tw/HumanSys/student/stdSignIn"
NCU_CHECKIN_CREATE = "https://cis.ncu.edu.tw/HumanSys/student/stdSignIn/create"
NCU_POST_CHECKIN_CREATE = "https://cis.ncu.edu.tw/HumanSys/student/stdSignIn_detail"

CURRENT_TIME = datetime.now()

# Set Account/Password In Environment Variables -> NCU_PORTAL = account:password
userinfo = os.environ['NCU_PORTAL'].split(":")
ACCOUNT = userinfo[0]
PASSWORD = userinfo[1]

def HttpMethod(url, method, session, cookies=None, data=None):
    if method == 'GET':
        res = session.get(url, cookies=cookies, params=data)
    elif method == 'POST':
        res = session.post(url, cookies=cookies, data=data)
    return res, session

def GetPortalLoginPayload(session):
    xsrf = session.cookies.get_dict()['XSRF-TOKEN']
    payload = {
        'username': ACCOUNT,
        'password': PASSWORD,
        '_csrf': xsrf,
        'language': 'CHINESE',
    }
    # sess = session.cookies.get_dict()['SESSION']
    # portal = session.cookies.get_dict()['portal']
    return payload

def GetPortalLeavingPayload(session):
    xsrf = session.cookies.get_dict()['XSRF-TOKEN']
    payload = {
        'chineseName': "人事系統",
        'englishName': "人事系統",
        '_csrf': xsrf
    }
    return payload

def Checkin(projectName, requireCheckinHour, signoutMsg):
    try:
        session = requests.session()
        res, session = HttpMethod(ENDPOINT_URL, 'GET', session)
        cookies = res.cookies
        print("GET ", ENDPOINT_URL, "Success")
    except Exception as err:
        txt = f"{CURRENT_TIME} >> GET {ENDPOINT_URL} error message: {err} \n"
        log.CheckinLog(txt)
        print("GET ", ENDPOINT_URL, "Failed")
        print("Error: ", err)

    try:
        res, session = HttpMethod(NCU_HOST, 'POST', session, cookies=cookies, data=GetPortalLoginPayload(session))
        cookies = session.cookies
        print("POST ", NCU_HOST, "Success")
    except Exception as err:
        txt = f"{CURRENT_TIME} >> POST {NCU_HOST} error message: {err} \n"
        log.CheckinLog(txt)
        print("POST ", NCU_HOST, "Failed")
        print("Error: ", err)
        
    try:
        res, session = HttpMethod(LEAVE_URL, 'POST', session, cookies=cookies, data=GetPortalLeavingPayload(session))
        print("POST ", LEAVE_URL, "Success")
    except Exception as err:
        txt = f"{CURRENT_TIME} >> POST {LEAVE_URL} error message: {err} \n"
        log.CheckinLog(txt)
        print("POST ", LEAVE_URL, "Failed")
        print("Error: ", err)
        
    try:
        res, session = HttpMethod(HOST, 'GET', session)
        cookies = dict(res.cookies)
        cookies['locale'] = session.cookies.get_dict()['locale']
        
        content = res.content.decode('utf-8')
        page = BS(content, features='lxml')
        username = parsers.ExtractUserName(page)
        print("Login User: ", username)
        print("GET ", HOST, "Success")
    except Exception as err:
        txt = f"{CURRENT_TIME} >> GET {HOST} error message: {err} \n"
        log.CheckinLog(txt)
        print("GET ", HOST, "Failed")
        print("Error: ", err)

    try:
        res, session = HttpMethod(NCU_CHECKIN_HOST, 'GET', session, cookies=cookies)
        cookies = dict(res.cookies)
        cookies['locale'] = session.cookies.get_dict()['locale']
        content = res.content.decode('utf-8')
        page = BS(content, features='lxml')
        ParttimeUsuallyId = parsers.ExtractParttimeUsuallyId(page, projectName)
        token = parsers.ExtractCheckinToken(page)
        print("Checkin Token: ", token)
        print("ParttimeUsuallyId : ", ParttimeUsuallyId)
        if type(ParttimeUsuallyId) != int:
            return
        print("GET ", NCU_CHECKIN_HOST, "Success")
    except Exception as err:
        txt = f"{CURRENT_TIME} >> GET {NCU_CHECKIN_HOST} error message: {err} \n"
        log.CheckinLog(txt)
        print("GET ", NCU_CHECKIN_HOST, "Failed")
        print("Error: ", err)

    try:    
        res, session = HttpMethod(NCU_CHECKIN_CREATE, 'GET', session, cookies=cookies, data={'ParttimeUsuallyId': ParttimeUsuallyId})
        cookies = dict(res.cookies)
        cookies['locale'] = session.cookies.get_dict()['locale']
        
        content = res.content.decode('utf-8')
        page = BS(content, features='lxml')
        idNo = page.find('input', {'id': 'idNo'})
        idNo = idNo.get('value')
        signintime = page.find('div', {'id': 'SigninTime'}).contents
        signouttime = page.find('div', {'id': 'SignoutTime'}).contents
        
        print("idNo: ", idNo)
        print("signintime: ", signintime)
        print("signouttime: ", signouttime)
        
        payload = {
            'functionName' : "doSign",
            'idNo' : idNo,
            'ParttimeUsuallyId' : ParttimeUsuallyId,
            'AttendWork' : "",
            '_token' : token
        }
        print("GET ", NCU_CHECKIN_CREATE, "Success")
    except Exception as err:
        txt = f"{CURRENT_TIME} >> GET {NCU_CHECKIN_CREATE} error message: {err} \n"
        log.CheckinLog(txt)
        print("GET ", NCU_CHECKIN_CREATE, "Failed")
        print("Error: ", err)

    if signintime != []:
        txt = '簽退計畫： '+ projectName +'\n'+'簽退時間： ' + str(CURRENT_TIME) + '\n'
        signintime_hour = int(signintime[0].split(":")[0])
        if CURRENT_TIME.hour - signintime_hour >= requireCheckinHour:
            try:
                payload['AttendWork'] = signoutMsg
                res, session = HttpMethod(NCU_POST_CHECKIN_CREATE, 'POST', session, cookies=cookies, data=payload)
                content = res.content.decode('utf-8')
                print("POST ", NCU_POST_CHECKIN_CREATE, "Success")
                log.CheckinLog(txt)
                return True
            except Exception as err:
                txt = f"POST {NCU_POST_CHECKIN_CREATE} error message: {err} \n"
                log.CheckinLog(txt)
                print("POST ", NCU_POST_CHECKIN_CREATE, "Failed")
                print("Error: ", err)
        else:
            txt = f"簽退時間未滿{requireCheckinHour}小時： " + str(CURRENT_TIME) + '\n'
            log.CheckinLog(txt)
            print("Not Yet To Signout")
    else:
        print("Signin!")
        txt = '簽到計畫： '+ projectName +'\n' + '簽到時間： ' + str(CURRENT_TIME) + '\n'
        try:
            res, session = HttpMethod(NCU_POST_CHECKIN_CREATE, 'POST', session, cookies=cookies, data=payload)
            content = res.content.decode('utf-8')
            print("POST ", NCU_POST_CHECKIN_CREATE, "Success")
            log.CheckinLog(txt)
            return True
        except Exception as err:
            txt = f"{CURRENT_TIME} >> POST {NCU_POST_CHECKIN_CREATE} error message: {err} \n"
            log.CheckinLog(txt)
            print("POST ", NCU_POST_CHECKIN_CREATE, "Failed")
            print("Error: ", err)
    return False