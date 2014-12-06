import unittest
from send import send_message
from twilio import TwilioRestException

# This is a class that will test basic functionality of the send
# message function that Ali created
class TestSendPyModule(unittest.TestCase):

    def test_valid_params(self):
    	ret_msg = send_message(body="Test 1", phone="07438483904")
        self.assertTrue(ret_msg is not "failed")

    def test_null_phone(self):
    	ret_msg = send_message(body="Test 2")
        self.assertTrue(ret_msg is not "failed")

    def test_null_body(self):
    	ret_msg = send_message(phone="07438483904")
        self.assertTrue(ret_msg is not "failed")

    def test_null_body_and_phone(self):
    	ret_msg = send_message()
        self.assertTrue(ret_msg is not "failed")

    def test_null_empty_body(self):
    	ret_msg = send_message(body="")
        self.assertTrue(ret_msg is not "failed")

if __name__ == '__main__':
	print "Running main program..."
	unittest.main()
