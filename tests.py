import unittest
from send import send_message, send_multiple_messages
from twilio import TwilioRestException

# This is a class that will test basic functionality of the send
# message function that Ali created
class TestSendMessage(unittest.TestCase):

    def test_valid_params(self):
    	ret_msg = send_message(body="Test 1", phone="07438483904")
        self.assertEqual(str(ret_msg), "queued")

    def test_null_phone(self):
    	ret_msg = send_message(body="Test 2")
        self.assertEqual(str(ret_msg), "invalid_number")

    def test_null_body(self):
    	ret_msg = send_message(phone="07438483904")
        self.assertEqual(str(ret_msg), "invalid_body")

    def test_null_body_and_phone(self):
    	ret_msg = send_message()
        self.assertEqual(str(ret_msg), "invalid_number")

    def test_null_empty_body(self):
    	ret_msg = send_message(body="", phone="07438483904")
        self.assertEqual(str(ret_msg), "invalid_body")

    def test_invalid_body(self):
    	ret_msg = send_message(body=100, phone="07438483904")
        self.assertEqual(str(ret_msg), "queued")

class TestSendMultipleMessages(unittest.TestCase):

	def test_one_valid_message(self):
		messages = [{ 'body': 'This is a valid body', 'phone': "07438483904" }]
		ret_arr = send_multiple_messages(messages)
		self.assertTrue(str(ret_arr[0])=='queued')

	def test_multiple_valid_messages(self):
		messages = [  { 'body': 'This is multiple message 1', 'phone': "07438483904" }
					, { 'body': 'This is multiple message 2', 'phone': "07438483904" }
					, { 'body': 'This is multiple message 3', 'phone': "07438483904" }]
		ret_arr = send_multiple_messages(messages)
		self.assertTrue(str(ret_arr[0])=='queued')
		self.assertTrue(str(ret_arr[1])=='queued')
		self.assertTrue(str(ret_arr[2])=='queued')

	def test_multiple_invalid_messages(self):
		messages = []
		messages = [  { 'body': None, 'phone': None }
					, { 'body': 'This is message 3', 'phone': "074" }
					, { 'body': None, 'phone': "07438483904" }]
		ret_arr = send_multiple_messages(messages)
		self.assertTrue(str(ret_arr[0])=='invalid_number')
		self.assertTrue(str(ret_arr[1])=='invalid_number')
		self.assertTrue(str(ret_arr[2])=='invalid_body')

if __name__ == '__main__':
	print "Running main program..."
	unittest.main()


