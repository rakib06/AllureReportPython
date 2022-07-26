# AllureReportPython

```cmd
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
scoop install allure
allure --version
```


## Run
```bash
pytest -v -s --alluredir=".\allure-report-demo\reports" .\allure-report-demo\test_demo.py
allure serve .\allure-report-demo\reports\
```
