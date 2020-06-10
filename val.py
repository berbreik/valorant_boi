from twilio.rest import Client 
 
account_sid = 'AC67961737dcdb46a7c74526d8250b20df' 
auth_token = 'be4c34a2e54cec3b3691035632f25495' 
client = Client(account_sid, auth_token) 
def wastmes():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+919131346359' 
                          ) 
    print(message.sid)