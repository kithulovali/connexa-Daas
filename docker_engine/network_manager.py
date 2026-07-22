
class NetworkManager:
    
    def __init__(self ,client):
        
        self.client = client 
        
    def check_database_network_exists(self,network_name:str):
      return   self.client.networks.get(network_name)
    
    def create_new_database_network(self, network_name:str):
      return   self.client.networks.create( 
                                    name = network_name,
                                    driver ="bridge" )
    
    def ensure_database_network_exists(self ,network_name:str):
        
        if not self.client.networks.get(network_name) :
            self.create_new_database_network(network_name)
            
    #@admin
    def delete_existing_network(self,network_name:str):
        network = self.client.networks.get(network_name)
        network.remove(force=True)

        
    #@admin   
    def list_all_database_networks(self):
        networks = self.client.networks.list()
        for u in networks :
         print(u.name)    