import socket


# Menu method
def menu():
    print("----Welcome to Bank's Banks----")
    print("Press 1 for Deposit.")
    print("Press 2 for Withdrawal")
    print("Press 3 for Account Balance")
    print("Press 4 to Quit")


host = socket.gethostname()  # Local machine name
port = 12345  # Reserving port


# Constantly prompt until ended
while True:
    s = socket.socket()  # Socket object
    s.connect((host, port))  # Bind to port
    menu()  # Calling menu method to display menu to the user
    print("What would you like to do: ")
    user_input = input()  # Input for service wanted

    # Check that if the input deposit or withdrawal
    if user_input == '1' or user_input == '2':
        msg = str.encode(str(user_input), 'utf-8')
        s.send(msg)
        print(s.recv(1024))
        user_input = input()  # Input for dollar amount
        msg = str.encode(str(user_input), 'utf-8')
        s.send(msg)
        print(s.recv(1024))

    # Check for balance
    elif user_input == '3':
        msg = str.encode(str(user_input), 'utf-8')
        s.send(msg)
        print(s.recv(1024))

    # Check for exit
    elif user_input == '4':
        msg = str.encode(str(user_input), 'utf-8')
        s.send(msg)
        print(s.recv(1024))
        break

    # For not expected values
    else:
        print("Incorrect input, please try again")

    s.close  # Close the socket
