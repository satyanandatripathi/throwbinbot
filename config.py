import os

class Var(object):
    api_id = os.environ.get("API_ID", None)
    api_hash = os.environ.get("API_HASH", None)
    token = os.environ.get("TOKEN", None)
    throwbin_api_key = os.environ.get("THROWBIN_API_KEY", None)
