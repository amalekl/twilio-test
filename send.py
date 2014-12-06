from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACf0027f784ea3bc216836afc2bbc4004d" 
AUTH_TOKEN = "fbe55d3c4254086da12de6b62f3a5d23" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

def send_message(body=None, phone=None):
	return False
