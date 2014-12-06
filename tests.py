import unittest
from send import send_message

# This is a function that test basic functionality of the send
# message function that Ali created
def test_send_message():
	print "Testing send message..."

	rCode = send_message(body="It works", to="07438483904")

	print "Successful" if rCode else "[ERROR]"

	return True


if __name__ == '__main__':
	print "Running main program..."
	test_send_message()
