import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def run():
    env_variables = {
        "DOCKER_ID": os.environ.get("DOCKER_ID", ""),
        "SERVER_DOCKER_IMAGE_NAME": os.environ.get("SERVER_DOCKER_IMAGE_NAME", ""),
        "SERVER_DOCKER_IMAGE_BUILD_NUMBER": os.environ.get("SERVER_DOCKER_IMAGE_BUILD_NUMBER", ""),
        "SERVER_HOST_NAME": os.environ.get("SERVER_HOST_NAME", ""),
        "SERVER_POD_PORT": os.environ.get("SERVER_POD_PORT", ""),
        "SERVER_SERVICE_NODE_PORT": os.environ.get("SERVER_SERVICE_NODE_PORT", ""),
        "AWS_S3_BUCKET": os.environ.get("AWS_S3_BUCKET", ""),
        "AWS_OBJECT_EXPIRES_IN": int(os.environ.get("AWS_OBJECT_EXPIRES_IN", "0")),
        "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID", ""),
        "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY", ""),
        "AWS_DEFAULT_REGION": os.environ.get("AWS_DEFAULT_REGION", "")
    }

    # Create folder "../.circleci/kubernetes/base_src" if it doesn't exist
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

if __name__ == "__main__":
    run()