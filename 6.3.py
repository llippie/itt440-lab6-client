import socket
import sys

c_socket = socket.socket()
host = '192.168.56.101'
port = 8889
print('waiting to connect..')
try:
	c_socket.connect((host,port))
except socket.error as e:
	print(str(e))

response = c_socket.recv(1024)
print(response.decode('utf-8'))
print("Choose a mathematical function\n1:log10,2:SquareRoot,3:Exponential,0:quit")
while True:
	choice = input("Function: ")
	c_socket.send(str.encode(choice))
	if choice != '1' and choice != '2' and choice != '3':
		print('disconnected')
		c_socket.send(str.encode('1'))
		break
	while True:
		try:
			num = float(input('Enter a number to calculate: '))
			num = str(num)
			c_socket.send(str.encode(num))
			result = c_socket.recv(1024)
			print(result.decode('utf-8'))
			break
		except ValueError:
			print('Not a Number')
			continue
c_socket.close()
