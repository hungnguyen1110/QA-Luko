# QA-Luko
##Automated Credit Card Adding Testing:

This is a Python Selenium test example that tests credit card payment on a website.

The test navigates to the website's login page and logs in with predefined test account credentials. Then, it navigates to the payment methods page and proceeds to add a credit card. The test then fills in the credit card details and submits the payment.

The test has two test cases - a successful and an unsuccessful credit card payment. In the successful test case, the test asserts that the success message is displayed on the page after the payment is processed. In the unsuccessful test case, the test asserts that the user is prevented from adding the card due to incorrect credit card details.

This test can be used as an example for a more complex set of tests that ensure the website's payment functionality is working correctly. The code can be modified to include more test cases and edge cases to improve the test coverage.

##Setup
Before running the tests, make sure you have the following installed on your system:

Python 3.x
Selenium Python package (pip install selenium)
ChromeDriver executable (download from here and add to system PATH)


##Test Cases
test_SUCCESSFULL_credit_card_payment
This test case verifies that a credit card payment is successful when valid credit card details are entered. At the end of the add card process, I assert if the return value equal to "Sucess" or not. In this test, I entered the correct information and the actual text match with the desired outcome. Test passed!

test_UNSUCCESSFULL_credit_card_payment
This test case verifies that a credit card payment fails when invalid credit card details are entered. In this case, I entered the card number which is missing 2 digits and then I check if the system react accordingly which is identify the erro and give a message that is "Your card number is incomplete". I assert the actual outcome with the erro message and it matching with eachother. The website react as we expected, it raise the error message when we input a in complete card number. It success in detecting this error and raise the message. Test Passed!   
