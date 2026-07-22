
class ImageManager: 
    
    def __init__(self,client):
        
        self.client = client 

        
    def check_database_engine_exists(self,database_engine:str) -> True:
       return self.client.images.get(database_engine)

    
    def create_new_database_engine(self,database_engine:str):
       return self.client.images.pull(database_engine)
        
    
    def ensure_database_engine_exists(self,database_engine:str):
        if not self.check_database_engine_exists(database_engine) :
            self.create_new_database_engine(database_engine)
    
    #@admin
    def delete_existing_database_engine(self,database_engine:str):
         return self.client.images.remove(database_engine,force=True)
        
    #@admin
    def list_all_database_engine(self):
        return  self.client.images.list(all=True)
  