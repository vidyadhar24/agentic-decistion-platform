from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

'''
# BaseSettings:
    - automatically searches for an Lords environment variables from.ENV files
    - we can read the variable name by using os.getenv() / but it doesn't load the env variables
    - it just reads them after pydantic_settings loads them
    - Note that, here, we didn't use python's module python-dotenv (or load_env())
    - it also validate the types and start up and cast strings into Python data typestypes e.g.,    string "8000" -> int 8000

# SecretStr
    -  security Raper data type for sensitive text like API ki passwords tokens, et cetera
    -it prevents sensitive information to be displayed and the terminal output race back or even it also prevents from leaking in the logs
    - we must call SecretStr.get_secret_value() to get the actual value of the secret

    '''

class AppSettings(BaseSettings):
    # use os.getenv() to read the variables from the .env
    model_name: str = os.getenv('MODEL_NAME')

    # for screts, it must match with how the screat's name is in the .env
    groq_api_key: SecretStr

    # there are the additional instructions to handle these settings
    model_config = SettingsConfigDict(
        env_file='.env',
        case_sensitive=True,
        extra='ignore'
    )


settings = AppSettings()
print(settings) # MODEL_NAME='openai/gpt-oss-120b' GROQ_API_KEY=SecretStr('**********')
# print(SecretStr.get_secret_value(settings.groq_api_key))

