

from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
subject = "My Subject"
html_content = "<html><body><h1>This is my first transactional email </h1></body></html>"
sender = {"name":"John Doe","email":"ganimoneyyy@gmail.com"}
to = [{"email":"612419104010cse@gmail.com","name":"Jane Doe"}]
cc = [{"email":"shabaripunidha@gmail","name":"Janice Doe"}]
bcc = [{"name":"John Doe","email":"ganimoneyyy@gmail.com"}]
reply_to = {"email":"ganimoneyyy@gmail.com","name":"John Doe"}
headers = {"Some-Custom-Name":"unique-id-1234"}
params = {"parameter":"My param value","subject":"New Subject"}
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=bcc, cc=cc, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)

try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)