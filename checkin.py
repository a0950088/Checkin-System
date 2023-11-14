import json
import log
from checkin_tool import Checkin
from datetime import datetime, timedelta

CURRENT_DATETIME = datetime.now()
SIGN_THRESHOLD = timedelta(minutes=10)

DAILY_LOG = f"Daily check start on : {CURRENT_DATETIME.date()} \n"
log.CheckinLog(DAILY_LOG)

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
    
for data in config:
    project = config[data]
    date_list = project["date"][:]
    for date in date_list:
        timestamp = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        if timestamp.date() == CURRENT_DATETIME.date():
            if abs(CURRENT_DATETIME-timestamp) < SIGN_THRESHOLD:
                #checkin/out
                if Checkin(project["projectName"],project["checkinHour"],project["message"]):
                    # pop success time
                    print("success: ",config[data]["date"].pop(date_list.index(str(timestamp))))
                else:
                    print("Failed")
# update config
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

DAILY_LOG = f"Daily check end! \n"
log.CheckinLog(DAILY_LOG)