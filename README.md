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
    call python checkin.py -hour 8 -proj "計畫名稱" -msg "工作內容"
    REM pause
    ```
    REM 是註解，如果需要查看 terminal log 可將REM拿掉
    
    ***Arguments***
    * `(int) hour`: 簽到時數 # default = 8
    * `*(str) proj`: 計畫名稱 # default = ""
    * `(str) msg`: 工作內容 # default = "協助計畫執行"

7. **Set your protal account as system environment variable**
    
    ![](https://i.imgur.com/OBdl6F5.png)

8. **Set windows scheduler**
    
    * 可以參考[這裡](https://titangene.github.io/article/set-up-windows-task-scheduler-to-periodically-execute-python-crawler.html)

9. **Check it is work :D**
    
    * 挑個可以簽到的好時辰
    
    * 按下執行按鈕
        ![](https://i.imgur.com/ILH0U2s.png)
    
    * 看一下 `log.txt` 有簽到時間長得像下面那樣就算成功囉 :D
        ![](https://i.imgur.com/QaCOyyP.png)
    
    * 阿如果有 `error message` 的話可能原因如下
        1. `https://portal.ncu.edu.tw/leaving Failed` 很有可能是學校網站被玩壞了 :C
        2. 學校網站更新
        3. 我寫得很爛，請跟我說 :C (或是你很聰明幫我修 :D)

## Notice

* 可從 `log.txt` 查看log message

* Windows排程記得早上跟晚上都要設(早上簽到晚上簽退)

* 不一定要用.bat檔，想在排程裡設定路徑也可以(Google is your friend :D)

* 也可以手動直接跑`checkin.py`簽到簽退喔(記得加args)

* 不一定要用conda跑，只要能自動跑checkin.py的方法都可以，但反正我是用conda :D