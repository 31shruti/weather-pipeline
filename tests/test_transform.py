from src.transform import transform


def test_transform_dedupes_and_converts():
    raw = [{
        "city": "Jaipur",
        "data": {
            "time": ["2026-01-01T00:00", "2026-01-01T00:00"],
            "temperature_2m": [10.0, 10.0],
            "relative_humidity_2m": [50, 50],
            "precipitation": [0.0, 0.0],
        },
    }]
    df = transform(raw)
    assert len(df) == 1
    assert df.loc[0, "temp_f"] == 50.0