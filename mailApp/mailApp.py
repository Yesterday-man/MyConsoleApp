import smtplib

sender = "everyday.no.everyday.4649@gmail.com"
receiver = "everyday.no.everyday.4649@gmail.com"

message = f"""\
Subject: こんにちは
To: {receiver}
From: {sender}

ビルドはうまくいきましたか？

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login("f67a47abcc6cc4", "ce1f9486228ef4")
    server.sendmail(sender, receiver, message)
