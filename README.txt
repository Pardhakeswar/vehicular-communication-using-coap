---> Used coapthon python library for establishing the coap server and client communication


=================Establishing  a coapserver.py=====================

python coapserver.py <server_ip>


=================Client querying or updating a resource ==========================

python coapclinet -o <Method> -p <url>
<url> = coap://<server_ip:5683>/<object>


========================connection usng nearby client ================================

if any client is not able to connect to server but need to communicate 
it can establish the connection by running the script ;

python connection_using_nearby_client.py <ip_Nearby_client> <port_no_nearbyclient> <ip_coapserver> <Method> <Object_requesting>


