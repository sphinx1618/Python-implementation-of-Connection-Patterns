import zmq,sys,time
context = zmq.Context()
print("\n                 Welcome to our Helpdesk paltform!!")
print("______________________________________________________________________________")
print("                 _________________________________________                    ")
print("We'll be creating your account in a minute.")
print("We have two Customer Care Executives. You can connect to either of them :)")

s = context.socket(zmq.PAIR)
con=int(input("\nConnect to Customer Care Executive 1/2 ? (1/2): "))
if(con==1):
	print("Connecting to the Executive 1.......")
	PORT="1618"
	php = "tcp://127.0.0.1:"+ PORT # how and where to connect
	s.connect(php)
	
elif(con==2):
	print("Connecting to the Executive 2.......")
	PORT="1619"
	php = "tcp://127.0.0.1:"+ PORT # how and where to connect
	


print("\nConnection Successful !!")
print("You can now request any help :)")
while(True):
	req=input("\nMe: ")
	s.send_string(str(req))
	Rep = s.recv_string()
	print("Executive: "+Rep)
	con="No"
	con=input("STOP ? (Yes/No) : ")
	if(con=="yes" or con=="YES" or con=="Yes"):
		time.sleep(1)
		break
	