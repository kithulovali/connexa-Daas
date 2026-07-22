
class NameGenerator :
    
    def container_name_generator(self,db):
        
        return(

            f"{db.engine}-"
            f"db-"
            f"{db.instance_id}"
        ) 
    
    def volume_name_generator(self,db):
        
        return (
            
            f"{db.engine}-"
            f"data-"
            f"{db.instance_id}"
        )
    
   