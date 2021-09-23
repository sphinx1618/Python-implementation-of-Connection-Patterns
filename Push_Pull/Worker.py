import zmq, time, pickle, sys
import threading 

context = zmq.Context()
def func(id):	
	s = context.socket(zmq.PULL)
	con=input("\nConnect to Restaurant 1/2? (1/2): ")
	if(con=="1"):
		PORT="3016"
		php = "tcp://127.0.0.1:"+ PORT # how and where to connect
		s.connect(php)
		
	
	elif(con=="2"):
		PORT="3017"
		php = "tcp://127.0.0.1:"+ PORT # how and where to connect
		s.connect(php)
		

	worker_id = id

	SRC = '127.0.0.1'
	PORT2 = '3031'
	

	
	

	r = context.socket(zmq.PUSH)
	p2 = "tcp://"+ SRC +":"+ PORT2

	
	r.connect(p2)


	while True:
		
		work = pickle.loads(s.recv())
		print("Order Id: ", work['order_id'])
		print("Restaurant Name: ",work['name'])
		print("Order picked by Delivery person: ",worker_id)

		time.sleep(work['workload'])

		r.send(pickle.dumps({'Order_Id': work['order_id'],'worker_id':worker_id,'name':work['name']}))

number = int(sys.argv[1])
func(number)
