from sqlalchemy import create_engine

from settings import get_settings

SETTINGS = get_settings()

engine = create_engine(
    f"{SETTINGS.db_config.dialect}+{SETTINGS.db_config.driver}://{SETTINGS.db_config.username}:{SETTINGS.db_config.password}@{SETTINGS.db_config.host}:{SETTINGS.db_config.port}/{SETTINGS.db_config.database}"
)
