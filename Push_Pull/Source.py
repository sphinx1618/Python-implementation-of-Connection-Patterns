import zmq, time, pickle, sys, random
print("WELCOME TO OUR ZOMATO FOOD DELIVERY APPLICATION")
print("\nHere, we deliver quality food to our customers")

server_number=1
try:
	server_number = int(sys.argv[1])
except:
	server_number=1

Name = input("Enter the Name of Restaurant: ")
Num = int(input("Enter the number of orders to be delivered: "))

context = zmq.Context()
SRC = '127.0.0.1'
PORT = str(3015 + server_number) 


s = context.socket(zmq.PUSH)


p = "tcp://"+ SRC +":"+ PORT
s.bind(p)

for i in range(Num):
	workload = random.randint(2,5)
	s.send(pickle.dumps({'name':Name, 'order_id':i,'workload':workload}))
	time.sleep(0.5)
	
