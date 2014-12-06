from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACf0027f784ea3bc216836afc2bbc4004d" 
AUTH_TOKEN = "fbe55d3c4254086da12de6b62f3a5d23" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

def send_multiple_messages(messages):
	lst=[]
	for dicts in messages:	
		the_body=dicts['body']
		the_phone=dicts['phone']
		func_ret= send_message(body=the_body,phone=the_phone)
		lst.append(func_ret)
	return lst

def send_message(body=None, phone=None):
	the_phone=phone 
	the_body=body
	
	if the_phone!="07438483904":
		return "invalid_number"
	if not the_body or not isinstance(the_body, int):
		return "invalid_body"
	
	ali = client.messages.create(to=the_phone, from_="+441290211149", body=the_body)
	
	return ali.status
