
from credentials import account_sid, auth_token, my_cell, my_twilio
from twilio.rest import Client 
client = Client(account_sid, auth_token)

my_msg = "Hello World"

message = client.messages.create(to = my_cell, from_= my_twilio, body = my_msg)

print(message)