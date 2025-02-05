# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28549267"))
API_HASH = getenv("API_HASH", "b2526517ed963b1951a811b24bc29a4e")
BOT_TOKEN = getenv("BOT_TOKEN", "7472562415:AAGgwS6eQ_945W7enn3PhYoVfluxD_xvSDw")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8054489757").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Mmanjhu:O9UjosQUi9wWkfAd@cluster0.ukzu1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "5"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
