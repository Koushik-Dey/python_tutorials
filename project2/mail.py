import smtplib as s

obj = s.SMTP("smtp.gmail.com", 587)
obj.ehlo()
obj.starttls()
obj.login("kd89601@gmail.com", "koushik2002@321")
subject = "test python"
body = "I love python"
message = "subject: {}\n\n{}".format(subject, body)

obj.sendmail("kd89601@gmail.com", "kd89601@gmail.com", message)
print("mail sent successfully")

obj.quit()
