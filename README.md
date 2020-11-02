# api_service_and_tests

This is a sample project with simple web-service on Flask and automation api tests for it.

**Notes:**
- Web-service support only GET and POST requests.
- It hasn't got any validation yet, so validation tests marked as x-fail.

**How to run:**
* Make sure you have Python 3.8+ installed
* Clone the current repository: 
`git clone https://github.com/teplota/api_service_and_tests.git`
* Prepare virtualenv:
`python3 -m venv api_service_and_tests`
`source api_service_and_tests/bin/activate`
* Change directory:
`cd /path/to/api_service_and_tests`
* Install dependencies:
`pip install -r requirements.txt`
* Run service.py with command:
`python service/service.py`
* Run tests with command:
`pytest`
