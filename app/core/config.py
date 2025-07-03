from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    # 모델 경로
    CNN_MODEL: str = os.getenv("CNN_MODEL", "")


settings = Settings()
