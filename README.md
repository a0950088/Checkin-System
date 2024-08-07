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
   8.1 **開啟工作排成器**
       * win+R 輸入 `compmgmt.msc`
       ![image](https://github.com/user-attachments/assets/e577add5-ed2b-42ac-898b-9de972b6b940)
       ![image](https://github.com/user-attachments/assets/5aadc25c-e4a0-4c76-8b25-2bd8ac568f06)

   8.2 **建立工作**
       * 點選建立工作
       ![image](https://github.com/user-attachments/assets/c7bae3a5-dc22-4a86-96c5-31c03309d59e)
       * 設定內容
       ![image](https://github.com/user-attachments/assets/beed09fc-b231-471b-88e2-45dac273d544)
       * 設定觸發程序 (以簽到簽退時間間隔8小時為例)
            1. 點選新增，設定固定簽到時間(Ex: 早上10:00)
               ![image](https://github.com/user-attachments/assets/03ee63c5-10cd-4292-8224-90afea9909e4)
            2. 點選新增，設定固定簽退時間(Ex: 晚上18:30)
               ![image](https://github.com/user-attachments/assets/ca814a66-b08c-4f6e-a87c-a1f73ac5c2bd)
           **設定完畢後如下圖**
           ![image](https://github.com/user-attachments/assets/91a41b70-418d-4ce2-8a93-e2c5dd24b4f2)
       * 設定動作
           1. 點選新增，加入`run.bat`的路徑
               ![image](https://github.com/user-attachments/assets/814c3165-c09e-4075-b677-641e2c83f9a9)
           **設定完畢後如下圖**
           ![image](https://github.com/user-attachments/assets/bcc340ef-4214-45dc-b7b1-afd8d632b5c2)
       * 其他設定 (參考用)
           ![image](https://github.com/user-attachments/assets/cf239c47-7b73-42fe-8acd-4298b683c48d)
           ![image](https://github.com/user-attachments/assets/e8b23ec3-16f5-4dbd-8085-71f7eb87dabf)
   8.3 **檢查排成**
       * 建立完畢會出現在上面
       ![image](https://github.com/user-attachments/assets/839466cd-9a08-4761-b6d3-1ce8124dc665)

   排成設定的參考資料在[這裡](https://titangene.github.io/article/set-up-windows-task-scheduler-to-periodically-execute-python-crawler.html)

10. **Open `config.json` and set your project**
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
