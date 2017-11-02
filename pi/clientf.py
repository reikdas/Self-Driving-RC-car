import socket               # Import socket module
import cv2
import numpy as np
import time
import pickle

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # ipManSaysHi...Awwwwww
port = 5555             # Reserve a port for your service.
s.connect((host, port))

def capture():
	cap=cv2.VideoCapture(0)
	ret,frame=cap.read()
	time.sleep(2)
	rval,imgencode=cv2.imencode(".jpg",frame,[1,90])
	data1=pickle.dumps(imgencode)
	s.sendall(data1)
	cap.release()

while True:
	capture()
	k=s.recv(1024)
	#time.sleep(4)
	print (k.decode('utf-8'))

s.close()


