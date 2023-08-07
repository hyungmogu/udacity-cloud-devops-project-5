import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class KubernetesSetupTool:
    def prepare_manifest(self):
        env_variables = {
            "DOCKER_ID": os.environ.get("DOCKER_ID", ""),
            "REDIS_HOST": os.environ.get("REDIS_HOST", ""),
            "REDIS_PASSWORD": os.environ.get("REDIS_PASSWORD", ""),
            "API_MAX_REQUESTS_PER_DAY": os.environ.get("API_MAX_REQUESTS_PER_DAY", ""),
            "API_SECONDS_IN_DAY": os.environ.get("API_SECONDS_IN_DAY", ""),
            "DOCKER_IMAGE_NAME" : os.environ.get("DOCKER_IMAGE_NAME", ""),
            "IMAGE_BUILD_NUMBER" : os.environ.get("IMAGE_BUILD_NUMBER", ""),
            "SERVER_GATEWAY_PORT" : os.environ.get("SERVER_GATEWAY_PORT", ""),
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

    def run(self):
        self.prepare_manifest()


if __name__ == "__main__":
    setup_tool = KubernetesSetupTool()
    setup_tool.run()