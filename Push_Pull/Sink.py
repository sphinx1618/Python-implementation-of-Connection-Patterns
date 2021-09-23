import zmq, time, pickle, sys

context = zmq.Context()
results_receiver = context.socket(zmq.PULL)

SRC = '127.0.0.1'
PORT = '3031'
p = "tcp://"+ SRC +":"+ PORT

results_receiver.bind(p)

worker_data = {}
restaurant_data = {}

while True:
    
    result = pickle.loads(results_receiver.recv())
    
    if worker_data.get(result['worker_id'],-1)==-1:
        worker_data[result['worker_id']] = 1
    else:
        worker_data[result['worker_id']] += 1
    
    if restaurant_data.get(result['name'],-1)==-1:
        restaurant_data[result['name']] = 1
    else:
        restaurant_data[result['name']] += 1


    print(worker_data)
    print(restaurant_data)

