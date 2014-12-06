from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACf0027f784ea3bc216836afc2bbc4004d" 
AUTH_TOKEN = "fbe55d3c4254086da12de6b62f3a5d23" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 


def send_message(body=None, phone=None):
	the_phone=phone 
	the_body=body
	if range(the_phone)!=11:
		return "invalid phone number"
	if the_body=None:
		the_body="Empty Text"
	ali=client.messages.create(
		to=the_phone, 
		from_="+441290211149", 
		body=the_body,  
	)
	print ali.status
	return ali
