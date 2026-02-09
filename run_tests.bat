@echo off

echo Activating virtual environment...
call .venv\Scripts\activate

echo Running pytest...
pytest -v -s --alluredir=allure-results

echo Opening Allure report...
allure serve allure-results

pause


