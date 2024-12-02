Practise with autotests

## prepare venv
python -m venv .venv 
source .venv/bin/activate
pip install -r requirements.txt

## requires selenium grid standalone server 
## https://www.selenium.dev/documentation/grid/getting_started/ 
## pointed to localhost:4444

## start tests
python -m pytest --alluredir reports --clean-alluredir

## report generation with allure
allure serve reports

