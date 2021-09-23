import zmq, time,sys

context = zmq.Context()
s = context.socket(zmq.PUB)
server_number = int(sys.argv[1])
HOST="127.0.0.1"
PORT={1:"1618",2:"1619",3:"1620",4:"1621",5:"1622"}
Publishers=["Entertainment","News","Sports","Politics","Facts"]
p = "tcp://"+ HOST +":"+ PORT[server_number]
s.bind(p)
print("Hey! Your channel name is ",Publishers[server_number-1])
while True:
	message=input("Enter the message: ")
	s.send_string(message)
	


	