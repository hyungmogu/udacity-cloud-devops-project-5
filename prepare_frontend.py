import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class FrontendSetupTool:
    def prepare_frontend_environment_variables(self):
        env_variable_groups = {
            "IS_PRODUCTION": os.environ.get("IS_PRODUCTION", "false")
        }
        
        if os.path.exists("frontend/.env"):
            os.remove("frontend/.env")


        with open("frontend/.env", "w+", encoding="utf-8") as f:
            for key, value in env_variable_groups.items():
                f.write("{}=\"{}\"\n".format(key, value))
    
    def run(self):
        self.prepare_frontend_environment_variables()

            
if __name__ == "__main__":
    setup_tool = FrontendSetupTool()
    setup_tool.run()