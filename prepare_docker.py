import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def run():
    env_variable_groups = [
    {   
        "for": ["gateway"],
        "values": {
            "API_MAX_REQUESTS_PER_DAY": os.environ.get("API_MAX_REQUESTS_PER_DAY", "5"),
            "API_SECONDS_IN_DAY": os.environ.get("API_SECONDS_IN_DAY", "86400"),
            "REDIS_HOST_LOCAL": os.environ.get("REDIS_HOST_LOCAL", "")
        }
    },{
        "for": ["server-jpg", "server-png", "server-webp"],
        "values": {
            "SERVER_HOST_NAME": os.environ.get("SERVER_HOST_NAME", ""),
            "SERVER_POD_PORT": os.environ.get("SERVER_POD_PORT", ""),
            "SERVER_SERVICE_NODE_PORT": os.environ.get("SERVER_SERVICE_NODE_PORT", ""),
            "AWS_S3_BUCKET": os.environ.get("AWS_S3_BUCKET", ""),
            "AWS_OBJECT_EXPIRES_IN": int(os.environ.get("AWS_OBJECT_EXPIRES_IN", "0")),
            "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID", ""),
            "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY", ""),
            "AWS_DEFAULT_REGION": os.environ.get("AWS_DEFAULT_REGION", "")
        }
    }]
    
    # for each file in microservices folder (except 'server')
    # delete traditional .env file and create a new one with the same name
    for folder in os.listdir("microservices"):
        if folder == "server":
            continue
        
        if os.path.exists("microservices/{}/.env".format(folder)):
            os.remove("microservices/{}/.env".format(folder))
        
        # open utf-8 encoding
        with open("microservices/{}/.env".format(folder), "w+", encoding="utf-8") as f:
            # for each env_variable_group
            for env_variable_group in env_variable_groups:
                # if the folder is in the env_variable_group
                if folder in env_variable_group["for"]:
                    # for each key, value in env_variable_group["values"]
                    for key, value in env_variable_group["values"].items():
                        # write key=value
                        f.write("{}={}\n".format(key, value))
            
if __name__ == "__main__":
    run()