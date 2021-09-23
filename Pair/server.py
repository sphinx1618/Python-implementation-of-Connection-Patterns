import zmq,sys,time
context = zmq.Context()

server_number=1
try:
	server_number = int(sys.argv[1])
except:
	server_number=1

p="tcp://127.0.0.1:1618"
if(server_number==1):
	print("\n        Initiated Customer Care Executive 1 !!")
	print("_________________________________________________________")
	p = "tcp://127.0.0.1:1618" # how and where to connect
else:
	print("\n        Initiated Customer Care Executive 2 !!")
	print("_________________________________________________________")
	p = "tcp://127.0.0.1:1619" # how and where to connect
	
# create reply socket
# bind socket to address
# bind socket to address
s = context.socket(zmq.PAIR)
s.bind(p)

while True: 
	Req = s.recv_string()
	if Req != "STOP":
		print("\nCustomer:",Req)
		Rep=input("Me: ")
		s.send_string(Rep)

	else:
		break
