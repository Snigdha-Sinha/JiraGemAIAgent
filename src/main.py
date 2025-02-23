
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from views.home_view import home_router
from views.code_view import code_router
from logger.custom_logger import Logger

import uvicorn


class LoadEnvVars:
    """
    """
    @staticmethod
    def load_env_vars() -> None:
        """
        """

        Logger.info(message="Loading Env Vars", stage="START")

        env_path = Path(__file__).parent.parent / ".env"
        load_dotenv(dotenv_path=env_path)

        Logger.info(message="Loaded Env Vars", stage="End")


class InitiateAIServer:
    """
    """
    
    app = FastAPI()
    
    @classmethod
    def include_routers(cls):
        """
        """
        routers = [
            home_router,
            code_router
        ]

        Logger.info(message="Including URL Routers", stage="START")

        for router in routers:
            cls.app.include_router(router)
        
        Logger.info(message="Included URL Routers", stage="END")
            
    @classmethod
    def get_app(cls):
        """
        """
        Logger.info(message="Server Configuring", stage="START")
        
        # Adding all Routers
        cls.include_routers()
        
        Logger.info(message="Server Configured", stage="END")

        return cls.app

# Run the FastAPI application
if __name__ == "__main__":
    """
    """

    Logger.info(message="Initiating Env Var Loader", stage="START")
    LoadEnvVars.load_env_vars()

    Logger.info(message="Initiating Server", stage="START")
    app = InitiateAIServer.get_app()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)