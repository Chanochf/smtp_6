import socket
import SMTP_protocol
import base64

IP = "0.0.0.0"
CLIENT_NAME = "client.net"
# Add the minimum required fields to the email
EMAIL_TEXT =   \
    "From: ...\r\n" \
    "..." \
    "..." \
    "..." \
    "..." \
    ""


def create_EHLO():
    return "EHLO {}\r\n".format(CLIENT_NAME).encode()


def create_LOGIN():
    return "AUTH LOGIN\r\n".encode()
# More functions must follow, in the form of create_EHLO, for every client message

def create_User(user):
    return base64.b64encode(user.encode())
# ...

def main():
    # Connect to server
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("127.0.0.1", SMTP_protocol.PORT))
    # 1 server welcome message
    # Check that the welcome message is according to the protocol
    response = my_socket.recv(1024).decode()
    if response.startswith(SMTP_protocol.SMTP_SERVICE_READY):
        message = create_EHLO()
        my_socket.send(message)
    else: return    
    # 2 EHLO message
    
    response = my_socket.recv(1024).decode()
    print(response)
    if not response.startswith(SMTP_protocol.REQUESTED_ACTION_COMPLETED):
        print("Error connecting")
        my_socket.close()
        return

    # 3 AUTH LOGIN
    message = create_LOGIN()
    my_socket.send(message)

    if not response.startswith(SMTP_protocol.AUTH_INPUT):
       print("Error connecting")
       my_socket.close()
       return
    # 4 User
    user = "barbie"
   
    message = create_User(user)
    my_socket.send(message.encode())

    # 5 password
    password = "helloken"

    # 6 mail from

    # 7 rcpt to

    # 8 data

    # 9 email content

    # 10 quit

    print("Closing\n")
    my_socket.close()


if __name__ == "__main__":
    main()