import smtplib as smtp
from getpass import getpass

email = "your email"
password = "pass"
dest_email = "aim"

# header
subject = "IP"

text = "text"

message = f"From: {email}\nTo: {dest_email}\nSubject: {subject}\n\n{text}"


def send_message(email, password, dest_email, message):

	try:
		port = 465
		server = smtp.SMTP_SSL('smtp.yandex.com', port)# u can use any email server
		# low bug level misses
		server.set_debuglevel(1)
		# test server work
		server.ehlo(email)
		# login
		server.login(email, password)
		server.auth_plain()

		# send mail
		server.sendmail(email, dest_email, message)

	except Exception as e:
		print(e)

	# finall quit of server
	finally:
		server.quit()



if __name__ == "__main__":
	send_message(email, password, dest_mail, message)
