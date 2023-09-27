# NCU Checkin System

## Installation and Setup

0. **Download `anaconda` and set anaconda to environment variable**

1. **Open your cmd**

2. **Create conda env**
    ```bash= 
    conda create --name `your_env_name` python==3.9.12
    ```

3. **Activate conda env**
    ```bash= 
    conda activate `your_env_name`
    ```

4. **Clone to your folder**
    ```bash= 
    cd `your_path`/
    git clone https://github.com/a0950088/Checkin-System.git
    ```

5. **Install requirements.txt**
    ```bash= 
    cd `your_path`/Checkin-System
    pip install -r requirements.txt
    ```

6. **Open run.bat and set path and conda env**
    ```bash=
    cd `your_path`/Checkin-System
    call conda activate `your_env_name`
    call python checkin.py
    REM pause
    ```
    REM 是註解，如果需要查看 terminal log 可將REM拿掉

7. **Set your protal account as system environment variable**
    
    ![](https://i.imgur.com/OBdl6F5.png)

8. **Set windows scheduler**
    * 設定兩種時間(以間隔8小時為例)
        1. 固定簽到時間(Ex: 早上10:00)
        2. 固定簽退時間(Ex: 晚上18:30)
    * 可以參考[這裡](https://titangene.github.io/article/set-up-windows-task-scheduler-to-periodically-execute-python-crawler.html)

9. **Open `config.json` and set your project**
    ```python
    {
        "project1": {
            "projectName": str, # checkin project name
            "checkinHour": int, # required checkin hour
            "message": str, # sign out message
            "date": [str, str, ...] # checkin time (timestamp format "%Y-%m-%d %H:%M:%S")
        },
        "project2": { # example
            "projectName": "工讀：112-1資工系辦工讀生",
            "checkinHour": 8,
            "message": "協助系辦事務",
            "date": [
                "2023-10-10 10:00:00",
                "2023-10-10 18:30:00",
                "2023-10-11 10:00:00",
                "2023-10-11 18:30:00",
            ]
        },
        ...
    }
    ```

## Notice

* 可從 `log.txt` 查看log message

* Windows排程記得早上跟晚上都要設(早上簽到晚上簽退)

## Issue

* 如果簽到退間隔(checkinHour)不一樣的話要另外再設windows排程
* 這個Error暫時忽略他(不會影響簽到簽退) `POST https://portal.ncu.edu.tw/leaving error message: ('Connection aborted.', ConnectionResetError(10054, '遠端主機已強制關閉一個現存的連線。', None, 10054, None)) `