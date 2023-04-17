# NCU Checkin System

## User Define

### NCU Portal

:::info
* Go to Windows environment variable to set user account and password
    * `NCU_Portal`: "Account:Password"
:::

### Checkin Data

:::info
* Python Line 42-44
    * `REQUIRE_SIGNIN_TIME`: int # 簽到時數
    * `projectName`: str # 簽到工作/計畫名稱
    * `signoutMsg`: str # 簽退內容
:::

### Setting run.bat

:::info
cd /d {Your Path}/check-in_System
call conda activate {your conda environment}
call python checkin.py
REM pause
:::
