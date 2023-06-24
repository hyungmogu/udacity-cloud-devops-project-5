import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def run():
    env_variables = {
        "AWS_S3_BUCKET": os.environ.get("AWS_S3_BUCKET", ""),
        "AWS_OBJECT_EXPIRES_IN": int(os.environ.get("AWS_OBJECT_EXPIRES_IN", "0")),
        "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID", ""),
        "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY", ""),
        "AWS_DEFAULT_REGION": os.environ.get("AWS_DEFAULT_REGION", "")
    }

    # for each file in .circleci/kubernetes folder with .example.yaml extension,
    # replace the placeholder starting with $ with the value from env_variables
    for file in os.listdir(".circleci/kubernetes"):
        if file.endswith(".example.yaml"):
            with open(".circleci/kubernetes/{}".format(file), "r") as f:
                content = f.read()

            for key, value in env_variables.items():
                content = content.replace("${}".format(key), value)

            with open(".circleci/kubernetes/{}.yaml".format(file.split(".")[0]), "w") as f:
                f.write(content)

if __name__ == "__main__":
    run()