# (c) @AbirHasan2005

import os


class Config(object):
    
    SESSION_NAME = "torrent-Search"

    API_ID = 8658860

    API_HASH = "fbb92e01e221f45920e63eb7000e4e38"

    BOT_TOKEN = "5678670362:AAGJZCyW9nK7Oxd6DEHDujPi5nKtJQb2l0c"

    MAX_INLINE_RESULTS = 50
    
    
    
    
    
    SESSION_NAME = os.environ.get("SESSION_NAME")
    API_ID = int(os.environ.get("API_ID", 12345678))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    MAX_INLINE_RESULTS = int(os.environ.get("MAX_INLINE_RESULTS", 50))
