import unittest
from send import send_message

# This is a function that test basic functionality of the send
# message function that Ali created
def test_send_message():
	print "Testing send message..."

	print "Testing sending phone number 07438483904"
	rCode = send_message(body="It works", phone="07438483904")
	print "Successful" if not rCode.failed else "[ERROR]"

	print "Testing sending null number"
	rCode = send_message(body="It works")
	print "Successful" if not rCode.failed else "[ERROR]"

	print "Testing sending null body"
	rCode = send_message(phone="07438483904")
	print "Successful" if not rCode.failed else "[ERROR]"

	return True


if __name__ == '__main__':
	print "Running main program..."
	test_send_message()
