from twilio.rest import TwilioRestClient 
import unittest
 
# put your own credentials here 
ACCOUNT_SID = "ACf0027f784ea3bc216836afc2bbc4004d" 
AUTH_TOKEN = "fbe55d3c4254086da12de6b62f3a5d23" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

def send_message(body=None, phone=None):
	return False

# This is a function that test basic functionality of the send
# message function that Ali created
def test_send_message():
	print "Testing send message..."

	rCode = send_message()

	print "Successful" if rCode else "[ERROR]"

	return True


if __name__ == '__main__':
	print "Running main program..."
	test_send_message()
