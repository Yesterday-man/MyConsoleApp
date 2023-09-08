import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = "everyday.no.everyday.4649@gmail.com"
receiver = "everyday.no.everyday.4649@gmail.com"

message = f"""\
Subject: Hellow Mr and Ms
To: {receiver}
From: {sender}

Build is finshed"""


msg = MIMEMultipart()

zip_filename = "publish-output.zip"
zip_attachment = open("../publish-output.zip","rb")

attachment = MIMEBase('application','octet-stream')

attachment.set_payload((zip_attachment).read())

encoders.encode_base64(attachment)
attachment.add_header('Content_Disposition',"attachment; filename= %s" % zip_filename)

msg.attach(attachment)

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login("f67a47abcc6cc4", "ce1f9486228ef4")
    server.sendmail(sender, receiver, message)
