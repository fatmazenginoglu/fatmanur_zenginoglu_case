Fatmanur Zenginoglu Case

Web Automation

* A web test automation framework has been created using Python, Pytest, and Selenium WebDriver, supporting both Chrome and Firefox, following the validation conditions and requirements in the documentation.
* BDD has not been used in the web automation execution.
* A function has been added to the conftest.py file to capture screenshots in case of an error. Screenshots are saved in the reports/screenshots folder.
* Tests can be executed selectively in Chrome or Firefox. The default browser is set to Chrome.
* The files are structured according to POM (Page Object Model) requirements.

File Structure:

fatmanur_zenginoglu_case/
│─── web_automation/
│    ├─── test_insider.py      # Test file
│    ├─── pages/               # POM page objects
│    │    ├─── __init__.py     # Python package initializer
│    │    ├─── career_page.py  # CareerPage POM file
│    │    ├─── home_page.py    # HomePage POM file
│    ├─── driver_setup.py      # WebDriver initialization file
│    ├─── conftest.py          # Pytest configuration file
│    ├─── reports/             # Allure reports
│    ├─── pytest.ini           # Pytest configuration file

Steps to Run Web Test Automation:

- To capture error screenshots along with the Allure report, run the following command:
pytest --browser=chrome --alluredir=reports/allure-results

- To view the Allure report in HTML format, run:
allure serve reports/allure-results

Web Test Automation Execution Results:

* A video recording of the test execution is included in the files.
* During the test execution, job listings for "Quality Assurance" are verified based on title, department, and location.
* After filtering, three job listings appear: two with "Quality Assurance" in the title and one with "QA".
* As per the provided document, only "Quality Assurance" should be considered, leading to a test failure for the "QA" job listing.
* A screenshot is taken of the job listings page upon failure.
* The test continues execution even if it fails or passes to allow further observation.

Load_Test

A load test has been created on JMeter with six different scenarios: common_keyword, long_query, empty_query, special_characters, numeric_query, and large_response. The test execution variables are defined as follows:

Users: 1
Ramp-up period: 0
Loop count: 100, 1000, 10000 (to increase load incrementally)

Steps to Run Load Test:
1. Move the .jmx file from the repository into the /bin directory of the installed JMeter program.
2. Execute the following commands to run tests with increasing loads:

jmeter -n -t N11_Search_Module_Load_Test.jmx -Jloop=100 -l results_100.jtl
jmeter -n -t N11_Search_Module_Load_Test.jmx -Jloop=1000 -l results_1000.jtl
jmeter -n -t N11_Search_Module_Load_Test.jmx -Jloop=10000 -l results_10000.jtl

3. Each result file can be analyzed using Excel or Notepad.
4. To merge multiple JTL files and generate a consolidated report, run:

jmeter-plugins-manager merge results_100.jtl results_1000.jtl results_10000.jtl -o merged_results.jtl

Note: The JMeter Merge Result plugin must be installed.

5. To generate a report with graphs and analysis in HTML format, run:
jmeter -g merged_results.jtl -o report_folder

6. Additional JMeter reports include:

View Results Tree
Simple Data Writer (file extension must be changed)
Aggregate Graph

Load Test Result Analysis:

Response Time Distribution:
Response times vary over time, with noticeable spikes at certain points.
In particular, response times exceeding 4 seconds indicate potential performance degradation under high load.

HTTP Response Code Distribution:
While most responses are 200 (Successful), there are also occurrences of 301 redirects and other response codes.

Concurrent Requests Over Time:
The number of concurrent requests processed during the test fluctuates.
To analyze how high load impacts response time, this graph should be interpreted alongside the response time data.

Connection and Response Delay Analysis:
Latency (Response Delay) and Connect Time show fluctuations.
At certain points, connection time exceeds 900 ms, leading to a corresponding increase in response latency.

API_Automation

API test automation for pet endpoints has been implemented using Python, Pytest, and Requests. 
A total of 43 test cases (positive and negative) were created for 7 endpoints.- test_pet_upload_image.py

API Test Files:

fatmanur_zenginoglu_case/
│─── api_automation/                          # Main directory for API automation tests
│    ├─── tests/    
│    │    ├─── pet/                           # Contains test scripts related to the "pet" API
│    │    │    ├─── test_pet_upload_image.py  # Tests for uploading images to a pet
│    │    │    ├─── test_create_pet.py        # Tests for creating a new pet
│    │    │    ├─── test_find_pets_by_status.py  # Tests for retrieving pets by status
│    │    │    ├─── test_get_pet_by_id.py     # Tests for retrieving a pet by its ID
│    │    │    ├─── test_update_pet.py        # Tests for updating pet details
│    │    │    ├─── test_update_pet_by_form.py  # Tests for updating a pet using form data
│    │    │    ├─── test_delete_pet_by_id.py  # Tests for deleting a pet by its ID
│    │    │    ├─── __init__.py               # Makes "pet" a package for module imports
│    │    ├─── __init__.py                    # Makes "tests" a package for module imports
│    │
│    ├─── reports/                            # Directory for test reports
│    │    ├─── allure-results/                # Raw Allure result files
│    │    ├─── allure-report/                 # Generated Allure HTML report
│    │    │    ├─── index.html                # Main HTML report file
│
│    ├─── pages/                              # Contains API interaction classes
│    │    ├─── pet_api.py                     # Class for interacting with the pet API
│    │    ├─── __init__.py                    # Makes "pages" a package for module imports
│
│    ├─── utils/                              # Utility modules
│    │    ├─── config.py                      # Configuration file
│    │    ├─── __init__.py                    # Makes "utils" a package for module imports
│
│    ├─── pytest.ini                          # Pytest configuration file
│    ├─── requirements.txt                    # Dependencies for the project
│    ├─── .gitignore                          # Ignore unnecessary files (e.g., __pycache__, logs, reports)

Negative and Positive Test Scenarios Prepared for 7 Endpoints:

- test_pet_upload_image.py

Positive Test Cases:
test_upload_pet_image_success - Upload a valid image file
Description: Sends a request to upload a valid image file for a pet.
Expected Result: The request should return a 200 status code, and the response should contain "File uploaded to" in the message.

Negative Test Cases:
test_upload_pet_image_invalid_pet - Upload an image for a non-existent pet
Description: Attempts to upload an image for a pet ID that does not exist in the database.
Expected Result: The request should return a 200 status code, but the response should indicate that the pet ID does not exist.
test_upload_pet_image_empty_metadata - Upload an image with empty metadata
Description: Uploads an image file without providing any metadata.
Expected Result: The request should return a 200 status code, and the response should contain "code" and "message" fields.
test_upload_pet_excel_file - Upload an unsupported file type (Excel)
Description: Attempts to upload a non-image file (Excel spreadsheet) as a pet image.
Expected Result: The request should return a 200 status code, but the response should indicate that an unsupported file type was uploaded.
test_upload_pet_image_empty_file - Upload only metadata without a file
Description: Sends a request with metadata but does not include an actual file.
Expected Result: The request should return a 500 Internal Server Error, indicating that the image file is required; however, during test execution, the status code returns 400 instead of 500, causing the test to fail.

- test_upload_pet_image.py

Positive Test Cases:
test_upload_pet_image_success - Upload a valid image file
Description: Sends a request to upload a valid image file for a pet.
Expected Result: The request should return a 200 status code, and the response should contain "File uploaded to" in the message.

Negative Test Cases:
test_upload_pet_image_invalid_pet - Upload an image for a non-existent pet
Description: Attempts to upload an image for a pet ID that does not exist in the database.
Expected Result: The request should return a 200 status code, but the response should indicate that the pet ID does not exist.
test_upload_pet_image_empty_metadata - Upload an image with empty metadata
Description: Uploads an image file without providing any metadata.
Expected Result: The request should return a 200 status code, and the response should contain "code" and "message" fields.
test_upload_pet_excel_file - Upload an unsupported file type (Excel)
Description: Attempts to upload a non-image file (Excel spreadsheet) as a pet image.
Expected Result: The request should return a 200 status code, but the response should indicate that an unsupported file type was uploaded.
test_upload_pet_image_empty_file - Upload only metadata without a file
Description: Sends a request with metadata but does not include an actual file.
Expected Result: The request should return a 500 Internal Server Error, indicating that the image file is required; however, during test execution, the status code returns 400 instead of 500, causing the test to fail.

- test_create_pet.py

Positive Test Cases:
test_create_pet_success - Adding a valid pet
Description: Sends a request to add a valid pet with an ID and name.
Expected Result: The request should return a 200 status code, and the response should contain the pet name "Golden Retriever".
test_create_pet_with_different_category - Adding a pet with a different category and tag
Description: Sends a request to create a pet with different category and tag values.
Expected Result: The request should return a 200 status code, and the response should contain "category": {"name": "Cat"}.

Negative Test Cases:
test_create_pet_without_name - Sending a request without the name field
Description: Attempts to create a pet without providing a name.
Expected Result: The request should return a 200 status code, but behavior depends on API handling.
test_create_pet_without_photo_urls - Sending a request without the photoUrls field
Description: Sends a request to create a pet without providing any photo URLs.
Expected Result: The request should return a 200 status code.
test_create_pet_with_invalid_status - Sending a request with an invalid status value
Description: Attempts to create a pet with a status value that is not recognized by the API.
Expected Result: The request should return a 200 status code, but behavior depends on API handling.
test_create_pet_with_empty_body - Sending a completely empty JSON request
Description: Tries to create a pet by sending an empty JSON body.
Expected Result: The request should return a 200 status code.
test_create_pet_with_string_id - Sending the id field as a string
Description: Attempts to create a pet using a string value for the id field instead of an integer.
Expected Result: The request should return a 500 status code, indicating a server error.
test_create_pet_with_get_method - Trying to create a pet using the GET method
Description: Sends a request using the GET method instead of POST to create a pet.
Expected Result: The request should return a 405 status code, indicating that the method is not allowed.

- test_find_pets_by_status.py

Positive Test Cases:
Retrieve pets with status=available
Description: Sends a request to fetch all pets that have the status "available".
Expected Result: The request should return a 200 status code, and the response should be a list of pets.
Retrieve pets with status=pending
Description: Sends a request to fetch all pets that have the status "pending".
Expected Result: The request should return a 200 status code, and the response should be a list of pets.
Retrieve pets with status=sold
Description: Sends a request to fetch all pets that have the status "sold".
Expected Result: The request should return a 200 status code, and the response should be a list of pets.

Negative Test Cases:
Send request with an invalid status
Description: Attempts to fetch pets using an invalid status value (e.g., "invalid").
Expected Result: The request should return a 400 status code, and the response should be an empty list [].
Make a request without sending any status parameter
Description: Attempts to fetch pets without providing the required status query parameter.
Expected Result: The request should return a 400 status code, but instead returns 200, causing the test to fail.

- test_get_pet_by_id.py

Positive Test Cases:
test_get_pet_by_valid_id - Retrieve pet details with a valid pet ID
Description: Attempts to retrieve pet details using a valid pet ID (1020).
Expected Result: The request should return a 200 status code, and the response should contain the pet ID 1020 and name "Bulldog".

Negative Test Cases:
test_get_pet_by_invalid_id - Send request with an invalid pet ID (petId="invalid")
Description: Attempts to retrieve pet details using a non-numeric pet ID ("invalid").
Expected Result: The request should return a 404 status code.

-test_update_pet.py

Positive Test Cases:
test_update_pet_success - Successfully updating an existing pet
Description: Sends a request to update an existing pet’s name.
Expected Result: The request should return a 200 status code, and the response should contain the updated pet name "Golden Retriever Updated".
Negative Test Cases:
test_update_pet_invalid_id - Updating with an invalid ID (string)
Description: Attempts to update a pet using an invalid (non-numeric) pet ID.
Expected Result: The request should return a 500 status code.

- delete_pet_by_id.py

Positive Test Cases:
test_delete_existing_pet - Delete a pet using a valid pet ID
Description: Creates a pet and then deletes it using a valid pet ID.
Expected Result: The request should return a 200 status code, indicating the pet was successfully deleted.

Negative Test Cases:
test_delete_pet_by_invalid_id - Send a request with an invalid ID (petId="invalid")
Description: Attempts to delete a pet using an invalid (non-numeric) pet ID.
Expected Result: The request should return a 404 status code.
test_delete_non_existent_pet - Send a request to delete a pet that does not exist (petId=9999999)
Description: Tries to delete a pet using a pet ID that does not exist in the system.
Expected Result: The request should return a 404 status code.
test_delete_pet_by_negative_id - Send a request to delete a pet using a negative ID (petId=-1)
Description: Attempts to delete a pet using a negative pet ID.
Expected Result: The request should return a 404 status code.

Steps to Run API Automation:
- To generate an HTML report, run the following command:
 
  pytest --html=report.html

- To generate a more visually enhanced Allure report, execute the following commands in order:

  pytest --alluredir=report/allure-results >> sonuçları kaydet
  allure generate report/allure-results -o report/allure-report --clean >> HTML rapor oluştur
  allure open report/allure-report >> raporu tarayıcıda aç

Analysis of API Automation Test Results:
A total of 43 tests were executed, with 38 passing and 5 failing.

Detailed Analysis of Failed Tests:

1. test_find_pets_by_invalid_status (test_find_pets_by_status.py & test_get_pet_by_id.py)

Expected Result: 400 (Bad Request)
Actual Result: 200 (Success)
Issue: The API accepts a request with an invalid status parameter ("invalid") and returns a 200 OK response. However, the expected behavior should be a 400 Bad Request error.

2. test_find_pets_without_status (test_find_pets_by_status.py & test_get_pet_by_id.py)

Expected Result: 400 (Bad Request)
Actual Result: 200 (Success)
Issue: The API accepts requests without the status parameter and returns a 200 OK response. The test expects the API to return a 400 Bad Request error. The API might be assigning a default value to the missing status parameter.

3. test_upload_pet_image_empty_file (test_pet_upload_image.py)

Expected Result: 500 (Internal Server Error)
Actual Result: 400 (Bad Request)
Issue: When trying to upload an empty file, the API returns a 400 Bad Request response instead of the expected 500 Internal Server Error. The API likely considers empty file uploads as a client error.

Solutions:
- Possible API Fixes
Implement validation for invalid or missing status values:
The API should reject invalid values like status=invalid with a 400 Bad Request error.
If the API assigns a default value when the status parameter is missing, the test should be updated to reflect this new behavior.
The response code for empty file uploads should be corrected:
Should the API return 500 instead of 400? Or should the test be updated to expect 400? This should be discussed with the backend team.

- Test Code Updates
If the API continues to accept invalid status values, update the test expectation to 200 OK.
If the API is expected to return 400 for empty file uploads, update the test case accordingly.







