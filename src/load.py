import os
from sqlalchemy import create_engine, text


def get_engine():
    url = os.getenv("DATABASE_URL", "sqlite:///weather.db")
    return create_engine(url)


def load(df):
    engine = get_engine()

    with engine.begin() as conn:

        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS weather (
                city TEXT NOT NULL,
                recorded_at TIMESTAMP NOT NULL,
                temp_c REAL,
                humidity_pct REAL,
                rain_mm REAL,
                temp_f REAL,
                PRIMARY KEY (city, recorded_at)
            )
        """))

        df.to_sql(
            "weather_staging",
            conn,
            if_exists="replace",
            index=False
        )

        if engine.dialect.name == "sqlite":
            conn.execute(text("""
                INSERT OR IGNORE INTO weather
                SELECT city, recorded_at, temp_c,
                       humidity_pct, rain_mm, temp_f
                FROM weather_staging
            """))

        elif engine.dialect.name == "postgresql":
            conn.execute(text("""
                INSERT INTO weather
                SELECT city, recorded_at, temp_c,
                       humidity_pct, rain_mm, temp_f
                FROM weather_staging
                ON CONFLICT (city, recorded_at) DO NOTHING
            """))

        conn.execute(text("DROP TABLE weather_staging"))

    return len(df)
