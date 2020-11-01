# api_service_and_tests

This is a sample project with simple web-service on Flask and automation api tests for it.

**Notes:**
- Web-service support only GET and POST requests.
- It hasn't got any validation yet, so validation tests marked as x-fail.

**How to run:**
* Make sure you have Python 3.8+ installed
* Prepare virtualenv 
* Clone the api_service_and_tests repository
* Install dependencies:
`pip install -r requirements.txt`
* Change directory:
`cd /path/to/api_service_and_tests`
* Run service.py with command:
`python service/service.py`
* Run tests with command:
`pytest`

