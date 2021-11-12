Daniel Miao
UID: 010839033

An automated bank teller program that utilizes socket programming, 
should keep server alive so that a client can exit and re-enter the same account
and preserve the data.

This program should run like:
Run server.py with localhost and port number
Run client.py with localhost and port number.
Client should prompt user with 1-4
1 should Desposit
2 should Withdraw
3 should check for Account Balance
4 should close client connection

Error handling should be active on both the function selections
and the function inputs, not allowing either string, negative
numbers, or float types.
