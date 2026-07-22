
class ConnectionManager:
        
        CONNECTION_TEMPLATE = {
            
        "postgres": 
             "postgresql://{username}:{password}@{host}:{port}/{database}",

        "mysql":
             "mysql://{username}:{password}@{host}:{port}/{database}",

        "mongodb":
             "mongodb://{username}:{password}@{host}:{port}/{database}",

        "redis":
             "redis://:{password}@{host}:{port}"
             
        }
        
        def database_connection_url_generator(
         self , engine , username , password , database ,host , port 
           ) :
        
            template = self.CONNECTION_TEMPLATE.get(engine)
            
            return template.format(
                
                username = username ,
                password = password ,
                database = database ,
                host = host ,
                port = port 
                
            )
                
            
        