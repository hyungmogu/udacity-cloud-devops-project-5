import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class KubernetesSetupTool:
    def prepare_manifest(self):
        env_variables = {
            "DOCKER_ID": os.environ.get("DOCKER_ID", ""),
            "GATEWAY_DOCKER_IMAGE_NAME" : os.environ.get("GATEWAY_DOCKER_IMAGE_NAME", ""),
            "SERVER_JPG_DOCKER_IMAGE_NAME" : os.environ.get("SERVER_JPG_DOCKER_IMAGE_NAME", ""),
            "SERVER_PNG_DOCKER_IMAGE_NAME" : os.environ.get("SERVER_PNG_DOCKER_IMAGE_NAME", ""),
            "SERVER_WEBP_DOCKER_IMAGE_NAME" : os.environ.get("SERVER_WEBP_DOCKER_IMAGE_NAME", ""),
            "GATEWAY_DOCKER_IMAGE_BUILD_NUMBER" : os.environ.get("GATEWAY_DOCKER_IMAGE_BUILD_NUMBER", ""),
            "SERVER_JPG_DOCKER_IMAGE_BUILD_NUMBER" : os.environ.get("SERVER_JPG_DOCKER_IMAGE_BUILD_NUMBER", ""),
            "SERVER_PNG_DOCKER_IMAGE_BUILD_NUMBER" : os.environ.get("SERVER_PNG_DOCKER_IMAGE_BUILD_NUMBER", ""),
            "SERVER_WEBP_DOCKER_IMAGE_BUILD_NUMBER" : os.environ.get("SERVER_WEBP_DOCKER_IMAGE_BUILD_NUMBER", ""),
            "GATEWAY_HOST" : os.environ.get("GATEWAY_HOST", ""),
            "SERVER_JPG_HOST": os.environ.get("SERVER_JPG_HOST", ""),
            "SERVER_PNG_HOST": os.environ.get("SERVER_PNG_HOST", ""),
            "SERVER_WEBP_HOST": os.environ.get("SERVER_WEBP_HOST", ""),
            "GATEWAY_PORT" : os.environ.get("GATEWAY_PORT", ""),
            "SERVER_JPG_PORT" : os.environ.get("SERVER_JPG_PORT", ""),
            "SERVER_PNG_PORT" : os.environ.get("SERVER_PNG_PORT", ""),
            "SERVER_WEBP_PORT" : os.environ.get("SERVER_WEBP_PORT", ""),
            "AWS_S3_BUCKET": os.environ.get("AWS_S3_BUCKET", ""),
            "AWS_OBJECT_EXPIRES_IN": int(os.environ.get("AWS_OBJECT_EXPIRES_IN", "0")),
            "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID", ""),
            "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY", ""),
            "AWS_DEFAULT_REGION": os.environ.get("AWS_DEFAULT_REGION", "")
        }

        # Create folder ".circleci/kubernetes/base_src" if it doesn't exist
        if not os.path.exists(".circleci/kubernetes/base_src"):
            os.makedirs(".circleci/kubernetes/base_src")

        # for each file in .circleci/kubernetes folder with .example.yaml extension,
        # replace the placeholder starting with $ with the value from env_variables
        for file in os.listdir(".circleci/kubernetes/base"):
            if file.endswith(".yaml.example"):
                with open(".circleci/kubernetes/base/{}".format(file), "r") as f:
                    content = f.read()

                for key, value in env_variables.items():
                    content = content.replace("${}".format(key), str(value))

                with open(".circleci/kubernetes/base_src/{}.yaml".format(file.split(".")[0]), "w+") as f:
                    f.write(content)

    def deploy_docker_images(self):
        # for each folder in microservices folder, run docker.sh script
        for folder in os.listdir("microservices"):
            if os.path.isdir("microservices/{}".format(folder)):
                os.system("cd microservices/{} && sh docker.sh".format(folder))

    def run(self):
        self.prepare_manifest()
        self.deploy_docker_images()


if __name__ == "__main__":
    setup_tool = KubernetesSetupTool()
    setup_tool.run()