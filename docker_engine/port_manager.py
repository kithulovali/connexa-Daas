import socket 

class PortManager :

    def allocate_host_port(self):
    
         with socket.socket() as s :
               s.bind(("",0)) 
               
               return s.getsockname()[1] 
    

        