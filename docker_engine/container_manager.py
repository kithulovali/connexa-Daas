
class ContainerManager :
    
    def __init__(self,
                 client ,
                 image_manager ,
                 network_manager,
                 volume_manager,
                 port_manager,
                 databases,
                 name_generator,
                 resource_manager
                 ):
        self.client = client
        self.name_generator = name_generator
        self.image_manager = image_manager 
        self.network_manager = network_manager 
        self.volume_manager = volume_manager 
        self.port_manager = port_manager
        self.resource_manager = resource_manager
        self.databases = databases
        
    def create_database_instance(self, db):
        
        config = self.databases[db.engine]
        
        image  = config["image"]
        container_port = config["container_port"]
        network = config["network"]
        volume_path = config["mount_path"]
        resources = config["resources"]
        environment = config["build_environment"](db)
        
        container_name = self.name_generator.container_name_generator(db)
        volume_name = self.name_generator.volume_name_generator(db)
        
        self.image_manager.ensure_database_engine_exists(image)
        self.network_manager.ensure_database_network_exists(network)
        self.volume_manager.ensure_volume_data_exists_or_create(volume_name)
    
        host_port = self.port_manager.allocate_host_port()
        
        resource_config = self.resource_manager.set_container_resources(
            resources
        )
        
        database_instance_config = {
            
            "image": image ,
            "name": container_name ,
            "detach" : True ,
            "environment": environment ,
            "network":network,
            
            "ports" :{
                f"{container_port}/tcp":host_port
            },
            
            "volumes":{
                
                volume_name :{
                    "bind":volume_path,
                    "mode":"rw"
                },
            },
            
        }
        
        database_instance_config.update(
            resource_config
        )
        
        database_instance = self.client.containers.run(
            **database_instance_config
        )
        
        return database_instance 
    
    def list_all_database_instance(self):
        return self.client.containers.list(all =True)
    
    def remove_existing_database_instance(self,container_name:str):
        container = self.client.containers.get(container_name)
        container.remove(force = True)
        return container
        
         
    