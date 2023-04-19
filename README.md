# NCU Checkin System

## Notice

* 環境變數和`checkin.py`要記得改

* Windows排程記得早上跟晚上都要設(早上簽到晚上簽退)

* 不一定要用.bat檔，想在排程裡設定路徑也可以

* 也可以手動直接跑`checkin.py`簽到簽退

* Request Error log 和 簽到簽退時間 會存在`log.txt`

* `run.bat` line 4 可以把REM(註解)拿掉，程式啟動時就有terminal log可以看

## User Define

### NCU Portal

* Go to Windows environment variable to set user account and password
    * `NCU_Portal`: "Account:Password"

### Checkin Data

* Python Line 42-44 in `checkin.py`
    * `REQUIRE_SIGNIN_TIME`: int # 簽到時數
    * `projectName`: str # 簽到工作/計畫名稱
    * `signoutMsg`: str # 簽退內容

### Setting run.bat
```bash=
cd /d {Your Path}/check-in_System
call conda activate {your conda environment}
call python checkin.py
REM pause
```

### Windows 排程設定
請參考：https://titangene.github.io/article/set-up-windows-task-scheduler-to-periodically-execute-python-crawler.html