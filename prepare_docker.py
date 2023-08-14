import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class DockerComposeSetupTool:
    def prepare_docker_environment_variables(self):
        env_variable_groups = [
        {   
            "for": ["server_gateway"],
            "values": {
                "DOCKER_ID": os.environ.get("DOCKER_ID", ""),
                "DOCKER_PASSWORD": os.environ.get("DOCKER_PASSWORD", ""),
                "DOCKER_IMAGE_NAME": os.environ.get("DOCKER_IMAGE_NAME", ""),
                "IMAGE_BUILD_NUMBER": os.environ.get("IMAGE_BUILD_NUMBER", ""),
                "API_MAX_REQUESTS_PER_DAY": os.environ.get("API_MAX_REQUESTS_PER_DAY", "5"),
                "API_SECONDS_IN_DAY": os.environ.get("API_SECONDS_IN_DAY", "86400"),
                "REDIS_HOST": os.environ.get("REDIS_HOST", ""),
                "REDIS_PASSWORD": os.environ.get("REDIS_PASSWORD", ""),
                "SERVER_PROTOCOL": os.environ.get("SERVER_PROTOCOL", ""),
                "SERVER_GATEWAY_PORT": os.environ.get("SERVER_GATEWAY_PORT", ""),
                "SERVER_JPG_PORT": os.environ.get("SERVER_JPG_PORT", ""),
                "SERVER_PNG_PORT": os.environ.get("SERVER_PNG_PORT", ""),
                "SERVER_WEBP_PORT": os.environ.get("SERVER_WEBP_PORT", "")
            }
        },{
            "for": ["server_jpg"],
            "values": {
                "DOCKER_ID": os.environ.get("DOCKER_ID", ""),
                "DOCKER_PASSWORD": os.environ.get("DOCKER_PASSWORD", ""),
                "DOCKER_IMAGE_NAME": os.environ.get("DOCKER_IMAGE_NAME", ""),
                "IMAGE_BUILD_NUMBER": os.environ.get("IMAGE_BUILD_NUMBER", ""),
                "SERVER_JPG_PORT": os.environ.get("SERVER_JPG_PORT", ""),
                "AWS_S3_BUCKET": os.environ.get("AWS_S3_BUCKET", ""),
                "AWS_OBJECT_EXPIRES_IN": int(os.environ.get("AWS_OBJECT_EXPIRES_IN", "0")),
                "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID", ""),
                "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY", ""),
                "AWS_DEFAULT_REGION": os.environ.get("AWS_DEFAULT_REGION", "")
            }
        }, {
            "for": [ "server_png"],
            "values": {
                "DOCKER_ID": os.environ.get("DOCKER_ID", ""),
                "DOCKER_PASSWORD": os.environ.get("DOCKER_PASSWORD", ""),
                "DOCKER_IMAGE_NAME": os.environ.get("DOCKER_IMAGE_NAME", ""),
                "IMAGE_BUILD_NUMBER": os.environ.get("IMAGE_BUILD_NUMBER", ""),
                "SERVER_PNG_PORT": os.environ.get("SERVER_PNG_PORT", ""),
                "AWS_S3_BUCKET": os.environ.get("AWS_S3_BUCKET", ""),
                "AWS_OBJECT_EXPIRES_IN": int(os.environ.get("AWS_OBJECT_EXPIRES_IN", "0")),
                "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID", ""),
                "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY", ""),
                "AWS_DEFAULT_REGION": os.environ.get("AWS_DEFAULT_REGION", "")
            }
        }, {
            "for": ["server_webp"],
            "values": {
                "DOCKER_ID": os.environ.get("DOCKER_ID", ""),
                "DOCKER_PASSWORD": os.environ.get("DOCKER_PASSWORD", ""),
                "DOCKER_IMAGE_NAME": os.environ.get("DOCKER_IMAGE_NAME", ""),
                "IMAGE_BUILD_NUMBER": os.environ.get("IMAGE_BUILD_NUMBER", ""),
                "SERVER_WEBP_PORT": os.environ.get("SERVER_WEBP_PORT", ""),
                "AWS_S3_BUCKET": os.environ.get("AWS_S3_BUCKET", ""),
                "AWS_OBJECT_EXPIRES_IN": int(os.environ.get("AWS_OBJECT_EXPIRES_IN", "0")),
                "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID", ""),
                "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY", ""),
                "AWS_DEFAULT_REGION": os.environ.get("AWS_DEFAULT_REGION", "")
            }
        }]
        
        for folder in os.listdir("microservices"):
            if folder == "server":
                continue
            
            if os.path.exists("microservices/{}/.env".format(folder)):
                os.remove("microservices/{}/.env".format(folder))
            

            with open("microservices/{}/.env".format(folder), "w+", encoding="utf-8") as f:
                for env_variable_group in env_variable_groups:
                    if folder in env_variable_group["for"]:
                        for key, value in env_variable_group["values"].items():
                            f.write("{}=\"{}\"\n".format(key, value))
    
    def run(self):
        self.prepare_docker_environment_variables()

            
if __name__ == "__main__":
    setup_tool = DockerComposeSetupTool()
    setup_tool.run()