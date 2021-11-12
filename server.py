# Daniel Miao
# 010839033
import socket


class Account:

    def __init__(self):
        # Initialize our account and set a temp variable
        self.account_balance = int(100)
        self.temp_balance = self.account_balance

    # Withdraw method
    def withdraw(self, amount, client):
        self.account_balance -= amount  # Adjust account balance

        # Error checking for overdraft
        if self.account_balance < 0:

            self.account_balance = self.temp_balance  # Reset account value if overdraft
            # For server output
            print("Sorry, attempting to withdraw $%.1f when you only have $%.1f" % (amount, self.temp_balance))
            # For client output
            confirm = "Sorry, attempting to withdraw $%.1f when you only have $%.1f" % (amount, self.temp_balance)
            client.send(confirm.encode())
        else:
            # Confirmation
            self.temp_balance = self.account_balance  # Adjust temp variable
            print("Withdrew $%.1f successfully" % amount)  # For server output
            confirm = "Withdrew $%.1f successfully" % amount  # For client output
            client.send(confirm.encode())

    # Deposit method
    def deposit(self, amount, client):
        self.account_balance += amount  # Adjust account balance
        self.temp_balance = self.account_balance  # Adjust temp variable

        # Confirmation
        print("Deposited $%.1f successfully" % amount)  # For server output
        confirm = "Deposited $%.1f successfully" % amount  # For client output
        client.send(confirm.encode())

    # Balance check method
    def balance(self, client):
        print("Remaining balance is $%.1f" % self.account_balance)  # For server output
        confirm = "Remaining balance is $%.1f" % self.account_balance  # For client output
        client.send(confirm.encode())

    # Error message method
    def incorrect(self, client):
        print("Sorry, detected an invalid input")  # For server output
        confirm = "Sorry, detected an invalid input"  # For client output
        client.send(confirm.encode())


class Server:
    host = socket.gethostname()  # Acquire machine name
    port = 12345  # Reserving port
    s = socket.socket()  # Socket object
    s.bind((host, port))  # Bind to port
    s.listen(5)  # Waiting for the client
    server_obj = Account()

    while True:
        client, address = s.accept()  # Create client connection
        print('Got connection from', address)
        user_input = client.recv(1024).decode()

        # Deposit Function
        if user_input == '1':
            # Prompting user for desired deposit amount
            client.send("How much would you like to deposit?".encode())

            # Error Handling for floats
            try:
                amount = int(client.recv(1024).decode())
            except ValueError:
                # Send error message to user
                server_obj.incorrect(client)
                continue

            # Error Handling for negative numbers
            if amount > 0:
                # Depositing money to the account
                server_obj.deposit(amount, client)
            else:
                # Send error message to user
                server_obj.incorrect(client)

        # Withdraw Function
        elif user_input == '2':
            # Prompting user for desired withdrawal amount
            client.send("How much would you like to withdraw?".encode())

            # Error Handling for floats
            try:
                amount = int(client.recv(1024).decode())
            except ValueError:
                # Send error message to user
                server_obj.incorrect(client)
                continue

            # Error Handling for negative numbers
            if amount > 0:
                # Withdrawing money from account
                server_obj.withdraw(amount, client)
            else:
                # Send error message to user
                server_obj.incorrect(client)

        # Check balance function
        elif user_input == '3':
            # Displaying the current balance
            server_obj.balance(client)

        # Close server connection function
        elif user_input == '4':
            # Exiting
            client.send("Thank you choosing Bank's Banks".encode())

        # Check for unexpected values (redundant, but failsafe)
        else:
            print("Incorrect input, please try again")
            client.send("Incorrect input, please try again".encode())
        client.close()  # Close the connection
