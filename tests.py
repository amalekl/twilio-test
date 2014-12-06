import unittest
from send import send_message, send_multiple_messages
from twilio import TwilioRestException

# This is a class that will test basic functionality of the send
# message function that Ali created
class TestSendMessage(unittest.TestCase):

    def test_valid_params(self):
    	ret_msg = send_message(body="Test 1", phone="07438483904")
        self.assertTrue(ret_msg is "queued")

    def test_null_phone(self):
    	ret_msg = send_message(body="Test 2")
        self.assertTrue(ret_msg is "failed")

    def test_null_body(self):
    	ret_msg = send_message(phone="07438483904")
        self.assertTrue(ret_msg is "queued")

    def test_null_body_and_phone(self):
    	ret_msg = send_message()
        self.assertTrue(ret_msg is "queued")

    def test_null_empty_body(self):
    	ret_msg = send_message(body="")
        self.assertTrue(ret_msg is "queued")

    def test_invalid_body(self):
    	ret_msg = send_message(body=100)
        self.assertTrue(ret_msg is "queued")

class TestSendMultipleMessages(unittest.TestCase):

	def test_one_valid_message(self):
		messages = [{ 'body': 'This is a valid body', 'phone': "07438483904" }]
		ret_arr = send_multiple_messages(messages)
		self.assertTrue(ret_arr[0]=='queued')

	def test_multiple_valid_messages(self):
		messages = [  { 'body': 'This is message 1', 'phone': "07438483904" }
					, { 'body': 'This is message 2', 'phone': "07438483904" }
					, { 'body': 'This is message 3', 'phone': "07438483904" }]
		ret_arr = send_multiple_messages(messages)
		self.assertTrue(ret_arr[0]=='queued')

if __name__ == '__main__':
	print "Running main program..."
	unittest.main()


