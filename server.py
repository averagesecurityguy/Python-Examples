#!/usr/bin/env python
#-----------------------------------------------------------------------------
# This example will setup a server on the localhost on the specified port.
# Data is received from the client, processed, and echoed back to the client.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Import any needed libraries below
#-----------------------------------------------------------------------------
# We need to use the socket library
import socket


#-----------------------------------------------------------------------------
# Place any necessary functions below
#-----------------------------------------------------------------------------
def process_data(d):
    # Place any data processing code here.
    
    return d

    
#-----------------------------------------------------------------------------
# Begin the main program.
#-----------------------------------------------------------------------------
    
# Create a new socket and specify the host and port to listen on.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 80

# Bind the socket to a port on the host. If the port is in use you will 
# receive an error.
sock.bind((host,port))

# Tell the socket to start listening for connections. Will handle a maximum of
# one queued connection.
print "Listening..."
sock.listen(1)

# Put the server in a loop that accepts a connection, receives client data,
# processes the data, send the processed data to the client, and close the 
# connection. The loop continues forever.
while True:
    # Accept a connection and receive data
    client, address = sock.accept()
    data = client.recv(1024)
    print "Received <- %s" % (data)
    
    if data:
        # If we received any data processes it and send it back.
        send = process_data(data)
        print "Sent ->: %s" % (send)
        client.send(send)
    
    # Close the client connection
    client.close()