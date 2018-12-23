import socket                
import sys


print "usage():connection_using_nearby_client.py <ip_Nearby_client> <ip_coapserver> <Method> <Object_requesting>"  
s = socket.socket()          
####################reading out the parameters #########################  
                
ip_server= sys.argv[1]
port = int(sys.argv[2])
ip_coap_server =sys.argv[3]
method = sys.argv[4]
object_req = sys.argv[5]
#post_value = sys.argv[6]
  
# connect to the server on local computer 
s.connect((ip_server, port)) 

if method != "POST":
	s.send("python coapclient.py -o "+method+" -p coap://"+ip_coap_server+":5683/"+object_req)
else:
	post_value = sys.argv[6]
	s.send("python coapclient.py -o "+method+" -p coap://"+ip_coap_server+":5683/"+object_req+" -P "+post_value) 
 
print s.recv(4096) 
s.close()      
