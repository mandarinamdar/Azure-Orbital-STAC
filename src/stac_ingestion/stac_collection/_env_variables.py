import os

def get_env_variable(variable_name):
    value = os.getenv(variable_name)
    if value is None:
        raise ValueError(variable_name + " is not set")
    return value

PGHOST = get_env_variable('PGHOST')
PGDATABASE = get_env_variable('PGDATABASE')
PGUSER = get_env_variable('PGUSER')
PGPASSWORD = get_env_variable('PGPASSWORD')

STACCOLLECTION_SERVICE_BUS_CONNECTION_STRING = get_env_variable('STACCOLLECTION_SERVICE_BUS_CONNECTION_STRING')
STACCOLLECTION_SERVICE_BUS_TOPIC_NAME = get_env_variable('STACCOLLECTION_SERVICE_BUS_TOPIC_NAME')
STACCOLLECTION_SERVICE_BUS_SUBSCRIPTION_NAME = get_env_variable('STACCOLLECTION_SERVICE_BUS_SUBSCRIPTION_NAME')
DATA_STORAGE_ACCOUNT_CONNECTION_STRING = get_env_variable('DATA_STORAGE_ACCOUNT_CONNECTION_STRING')
STACCOLLECTION_STORAGE_CONTAINER_NAME = get_env_variable('STACCOLLECTION_STORAGE_CONTAINER_NAME')
AZURE_LOG_CONNECTION_STRING = get_env_variable('AZURE_LOG_CONNECTION_STRING')
