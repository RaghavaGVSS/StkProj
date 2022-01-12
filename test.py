from  validate_email import validate_email
import smtplib
# is_valid= validate_email(email_address='gattupalli.manisarma@gmail.com', check_format=True, check_blacklist=True, check_dns=True, dns_timeout=10, check_smtp=True, smtp_timeout=10, smtp_helo_host='my.host.name', smtp_from_address='my@from.addr.ess', smtp_debug=False)
# print(is_valid)

# server=s.SMTP("shanmukhagvs@gmail.com",587)
# s.starttls;s.login("shanmukhagvs@gmail.com","Vilan@!@")
# s.sendmail("shanmukhagvs@gmail.com","gattupalli.manisarma@gmail.com",msg)

# def ml():
#     try:
#        smtpObj = smtplib.SMTP('localhost')
#        smtpObj.sendmail("shanmukhagvs@gmail.com", "gattupalli.manisarma@gmail.com", msg)
#        print("Successfully sent email")
#     except smtplib.SMTPException:
#        print("Error: unable to send email")
# ml()


import smtplib

# creates SMTP session
email = smtplib.SMTP('smtp@gmail.com', 587)

# TLS for security
email.starttls()

# authentication
# compiler gives an error for wrong credential.
email.login("shanmukhagvs@gmail.com", "Vilan@!@")
msg= "U r getting this mail because of registering"
# message to be sent
# message = "message_to_be_send"

# sending the mail
email.sendmail("shanmukhagvs@gmail.com", "gattupalli.manisarma@gmail.com", msg)

# terminating the session
email.quit()
