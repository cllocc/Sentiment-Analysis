import private

TRACK_TERMS = ["bitcoin", "btc"]
CONNECTION_STRING = "sqlite:///tweets.db, encoding = UTF-8"
CSV_NAME = "tweets.csv"
TABLE_NAME = "crypto"

try:
    from private import *
except Exception:
    pass