# Parallel Testing - Selenium Python
This project is designed to automate tests for a flight reservation system using pytest, pytest-xdist, and Allure. The tests are executed in parallel to improve runtime and a report is generated using Allure.
It is recommended to open the following project in: VScode

## You will find
- [ ] Design Pattern (Page Object Model)
- [ ] Object-Oriented Programming (OOP)
- [ ] SOLID Principles
- [ ] Reruns

## Create a virtual environment:
Use this command to create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

## Install dependencies:
Use this command to install dependencies:

```bash
pip install -r requirements.txt
```
    
## Running Tests:
Tests are executed using pytest with the pytest-xdist plugin to run tests in parallel:

```bash
pytest -n 6 --maxfail=1 --disable-warnings --tb=short --alluredir=allure-results
```

## Generate the report:
After running the tests, generate the report with the command:

```bash
allure serve allure-results
```

### Recommendations:
Modify Seats: If the RoundWay or OneWay tests fail, adjust the seats as needed in the test files before rerunning the tests.