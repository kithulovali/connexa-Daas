
class HardwareManager :

    def set_container_resources(self ,resources):
       
        return {
                    "mem_limit": resources["ram"],
                    "nano_cpus": int(resources["cpu"] * 1_000_000_000)
               }
            

            
            
        
        
