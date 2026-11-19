import logging

from src.extract import extract_all
from src.transform import transform
from src.load import load

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def run():
    logging.info("Extracting data")
    raw = extract_all()
    logging.info("Transforming data")
    df = transform(raw)
    logging.info("Loading %s rows", len(df))
    load(df)
    logging.info("Pipeline finished")


if __name__ == "__main__":
    run()