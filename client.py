#!/usr/bin/env python
#-----------------------------------------------------------------------------
# This example will open a client connection to localhost on the specified
# port. Data is sent to the server and then recv'd from the server. The data 
# received is written to standard out.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Import any needed libraries below
#-----------------------------------------------------------------------------
# We need to use the socket library
import socket


#-----------------------------------------------------------------------------
# Begin the main program.
#-----------------------------------------------------------------------------

# Create a new socket and specify the host and port to connect to
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 80

# Connect to the host and port
sock.connect((host, port))

# Send data to the server.
send = "Sending some data..."
print "Sending -> %s" % (send)
sock.send(send)

# Receive data from the server and print it to standard out.
data = sock.recv(1024)
print "Received -> %s" % (data)