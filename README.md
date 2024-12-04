Practise with autotests

## prepare venv
python -m venv .venv   
.venv/Scripts/activate   
pip install -r requirements.txt   

## requires selenium grid standalone server 
https://www.selenium.dev/documentation/grid/getting_started/    
pointed to localhost:4444   

## requires allure   
https://allurereport.org/docs/install/

## start tests
python -m pytest --alluredir reports --clean-alluredir

## report generation with allure
allure serve reports

