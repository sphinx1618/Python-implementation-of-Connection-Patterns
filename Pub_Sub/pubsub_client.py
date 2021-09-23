import zmq,time
import threading 


Subscribed=[""]*5
Publishers=["Entertainment","News","Sports","Politics","Facts"]
print("WELCOME TO OUR TEXTUAL YOUTUBE APPLICATION")
print("\nHere, we deliver quality messages from our recognised publishers.")
print("You can subscribe to as many subscribers tou want.")
print("Here's the list of our publishers:")
print("______________________________________________________________________")
print("|                   PUBLISHERS:-                                     | Wanna Subscribe?")
print("|____________________________________________________________________|(yes/no)")
Subscribed[0]=input("|      1). | Entertainment |                                         |")
Subscribed[1]=input("|      2). | News          |                                         |")
Subscribed[2]=input("|      3). | Sports        |                                         |")
Subscribed[3]=input("|      4). | Politics      |                                         |")
Subscribed[4]=input("|      5). | Facts         |                                         |")

print("|__________|_______________|_________________________________________|")
print("\n                 Great setting things up for you!!")
print("                            ALL DONE!! ")
print("\n___________________________Your Feed____________________________________")

for i in range(5):
	if(Subscribed[i]=="Yes" or Subscribed[i]=="yes" or Subscribed[i]=="YES"):
		Subscribed[i]=1
	else:
		Subscribed[i]=0


def listener(publisher):
	context = zmq.Context()
	s = context.socket(zmq.SUB)
	PORT=str(1618+publisher)
	p = "tcp://127.0.0.1:"+PORT
	s.connect(p)
	s.setsockopt_string(zmq.SUBSCRIBE, "")
	while(True): 
		tm = s.recv_string() # receive a message
		print("\n"+Publishers[publisher]+" published something : ")
		print(tm)
			

for i in range(5):
	if(Subscribed[i]==1):
		
		t1 = threading.Thread(target=listener, args=(i,))
		t1.start()


