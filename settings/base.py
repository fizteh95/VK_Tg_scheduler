from os import getenv

DB_DRIVER = getenv("DB_DRIVER", "postgresql+asyncpg")
DB_USER = getenv("DB_USER", "postgres")
DB_PASSWORD = getenv("DB_PASSWORD", "postgres")
DB_HOST = getenv("DB_DRIVER", "localhost")
DB_PORT = getenv("DB_PORT", "5432")
DB_NAME = getenv("DB_NAME", "postgres")

TEST_DB_NAME = getenv("TEST_DB_NAME", "postgres_test")
