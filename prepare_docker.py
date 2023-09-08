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
                "IMAGE_BUILD_NUMBER": os.environ.get("IMAGE_BUILD_NUMBER", "")
            }
        },{
            "for": ["server_jpg"],
            "values": {
                "DOCKER_ID": os.environ.get("DOCKER_ID", ""),
                "DOCKER_PASSWORD": os.environ.get("DOCKER_PASSWORD", ""),
                "DOCKER_IMAGE_NAME": os.environ.get("DOCKER_IMAGE_NAME", ""),
                "IMAGE_BUILD_NUMBER": os.environ.get("IMAGE_BUILD_NUMBER", "")
            }
        }, {
            "for": [ "server_png"],
            "values": {
                "DOCKER_ID": os.environ.get("DOCKER_ID", ""),
                "DOCKER_PASSWORD": os.environ.get("DOCKER_PASSWORD", ""),
                "DOCKER_IMAGE_NAME": os.environ.get("DOCKER_IMAGE_NAME", ""),
                "IMAGE_BUILD_NUMBER": os.environ.get("IMAGE_BUILD_NUMBER", "")
            }
        }, {
            "for": ["server_webp"],
            "values": {
                "DOCKER_ID": os.environ.get("DOCKER_ID", ""),
                "DOCKER_PASSWORD": os.environ.get("DOCKER_PASSWORD", ""),
                "DOCKER_IMAGE_NAME": os.environ.get("DOCKER_IMAGE_NAME", ""),
                "IMAGE_BUILD_NUMBER": os.environ.get("IMAGE_BUILD_NUMBER", "")
            }
        }]

        for folder in os.listdir("microservices"):
            # if it's not a folder, then continue
            if not os.path.isdir("microservices/{}".format(folder)):
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