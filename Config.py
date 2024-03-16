import os
import loguru


ENVIRONMENT = os.environ.get('ENVIRONMENT', False)
LOGGER = loguru.logger
if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    OWNER_ID = os.environ.get('OWNER_ID', 6258709129)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 12799559 # api id here
    OWNER_ID = 1137799257
    API_HASH = "077254e69d93d08357f25bb5f4504580"
    BOT_TOKEN = "6762340943:AAGWlaIy43vk8hB9-0zxWdbWVdCNygKLDpM"
    DATABASE_URL = "postgres://cgofceil:6Hka0htlKsErFBUdYqGgNmDKQiXkiCsm@flora.db.elephantsql.com/cgofceil"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "@xenonbots" # must join channel link here
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
