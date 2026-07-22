

class VolumeManager :
    
    def __init__(self,client ):
        self.client = client
        
    def check_data_volume_exists(self , 
                                 data_volume_name:str):
        try :
            
         return  self.client.volumes.get(data_volume_name)
         
        except :
            return False
        
        
    def create_new_data_volume(self,
                               data_volume_name:str):
       created_data_volume =  self.client.volumes.create(
            name=data_volume_name
        )
       return created_data_volume
        
    def ensure_volume_data_exists_or_create(
                                  self,
                                  data_volume_name:str
                                  ):
        
        volume = self.check_data_volume_exists(data_volume_name)
        
        if volume :
            return volume
            
        return self.create_new_data_volume(data_volume_name)
            
    def list_all_data_volumes(self):
       return self.client.volumes.list(all=True)
    
    def delete_data_volume(self,
                           data_volume_name:str):
        volume = self.client.volumes.get(data_volume_name)
        return volume.remove(force =True)
    
        
        
    