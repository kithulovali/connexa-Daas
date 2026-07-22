DATABASE = {
    
    "postgres":{
        
        "image":"postgres:16",
        "container_port":5432,
        "network":"postgresql_network",
        "mount_path":"/var/lib/postgresql/data",
        
        "build_environment":lambda database_env :{
            "POSTGRES_USER":database_env.username,
            "POSTGRES_PASSWORD":database_env.password,
            "POSTGRES_DB":database_env.database
        },
        
        "resources":{
            "cpu":1.5,
            "ram":"500m",
            "storage":"2g"
        },
        
        
    },
    
    "mongo":{
        
        "image":"mongo:8",
        "container_port":27017,
        "network":"mongo_network",
        "mount_path":"/data/db",
        
        "build_environment":lambda database_env :{
            "MONGO_INITDB_ROOT_USERNAME":database_env.username,
            "MONGO_INITDB_ROOT_PASSWORD":database_env.password,
            "MONGO_DATABASE":database_env.database 
        },
        
        "resources":{
            "cpu":2,
            "ram":"500m",
            "storage":"2g"
        },
        
    },
    
    "maria":{
        
        "image":"mariadb:10",
        "container_port":3306,
        "network":"mariadb_network",
        "mount_path":"/var/lib/mysql",
        
        "build_environment": lambda database_env :{
            "MARIADB_USER":database_env.username,
            "MARIADB_PASSWORD":database_env.password,
            "MARIADB_DATABASE":database_env.database       
        },
        
        "resources":{
            "cpu":1.5,
            "ram":"500m",
            "storage":"2g"
        },
        
        
    },
    
    "redis":{
        
        "image":"redis:8",
        "container_port":6379,
        "network":"redis_network",
        "mount_path":"/data",
        
        "build_environment": lambda database_env :{
            "REDIS_PASSWORD":database_env.password
        },
        
        "resources":{
            "cpu":1.5,
            "ram":"500m",
            "storage":"2g"
            
        }
        
        
    }
}