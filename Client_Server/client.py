import zmq,sys,time
context = zmq.Context()
print("\n                 Welcome to our repositries paltform!!")
print("______________________________________________________________________________")
print("                 _________________________________________                    ")
print("We'll be creating your account in a minute.")
print("We have two repositories. You can connect to either/both of them :)")

s = context.socket(zmq.REQ)
connections=0
con=input("\nConnect to Repository 1? (Yes/No): ")
if(con=="Yes" or con=="YES" or con=="yes"):
	PORT="1618"
	php = "tcp://127.0.0.1:"+ PORT # how and where to connect
	s.connect(php)
	connections+=1
con=input("Connect to Repository 2? (Yes/No): ")
if(con=="Yes" or con=="YES" or con=="yes"):
	PORT="1619"
	php = "tcp://127.0.0.1:"+ PORT # how and where to connect
	s.connect(php)
	connections+=1


print("\nEach repository has 10 articles.")
while(True):
	req=int(input("\nEnter the article number you want to request: "))
	s.send_string(str(req))
	Rep = s.recv_string()
	print(Rep)
	con="No"
	con=input("Want to Stop? (Yes/No) : ")
	if(con=="Yes" or con=="YES" or con=="yes"):
		# s.send_string("-1")
		# temp=s.recv_string()
		# # time.sleep(2)
		# # print(temp)
		# if(connections==2):
		# 	s.send_string("-1")
		time.sleep(1)
		break
	