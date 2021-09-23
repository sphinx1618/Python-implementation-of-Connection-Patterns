import zmq,sys,time
context = zmq.Context()

server_number=1
try:
	server_number = int(sys.argv[1])
except:
	server_number=1

p="tcp://127.0.0.1:1618"
articles={}
if(server_number==1):
	print("\n        Initiated Repository 1 !!")
	print("______________________________________________")
	p = "tcp://127.0.0.1:1618" # how and where to connect
	for i in range(10):
		articles[i+1]="Hello! This is article "+str(i+1)+" of Repository 1. Thanks for requesting it!"
else:
	print("\n        Initiated Repository 2 !!")
	print("______________________________________________")
	p = "tcp://127.0.0.1:1619" # how and where to connect
	for i in range(10):
		articles[i+1]="Hello! This is article "+str(i+1)+" of Repository 2. Thanks for requesting it!"
# create reply socket
# bind socket to address
# bind socket to address
s = context.socket(zmq.REP)
s.bind(p)
while True: 
	Req = int(s.recv_string())
	if Req != -1:
		print("\nRepository",server_number,"recieved a request for article",Req)
		print("Replying....")
		Rep=articles[1]
		try:
			Rep=articles[Req]
		except:
			Rep="Repository Not Found!!"
			print("Repository Not found!")
		s.send_string(Rep)

	# else:
	# 	s.send_string("Closed Repository "+str(server_number))
	# 	time.sleep(3)
	# 	break
