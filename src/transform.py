import pandas as pd


def transform(raw):
    frames = []

    for item in raw:
        # Support both real API responses and test data
        hourly = item.get("hourly", item.get("data"))

        if hourly is None:
            raise ValueError("Weather data is missing hourly information")

        df = pd.DataFrame(hourly)
        df["city"] = item["city"]
        frames.append(df)

    if not frames:
        return pd.DataFrame()

    df = pd.concat(frames, ignore_index=True)

    df = df.rename(columns={
        "time": "recorded_at",
        "temperature_2m": "temp_c",
        "relative_humidity_2m": "humidity_pct",
        "precipitation": "rain_mm",
    })

    df["recorded_at"] = pd.to_datetime(df["recorded_at"])
    df = df.dropna()
    df = df.drop_duplicates(subset=["city", "recorded_at"])
    df["temp_f"] = (df["temp_c"] * 9 / 5 + 32).round(1)

    return df
