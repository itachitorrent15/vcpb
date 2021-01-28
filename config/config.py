# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 2474105
API_HASH = "ac4e6398505b50f0e8e2aa040db8b4f3"

# Get this from @Botfather
TOKEN = "1545484097:AAG7kTPC2T9688RlEHLqzIfFmwMouSZBH5w"

# Your MongoDB URI (using a database named "vcpb"), if you don't provide, you can't use the playlist feature and wont see now playing message
MONGO_DB_URI = "mongodb+srv://erich:erich@vcpb.ak2yd.mongodb.net/<dbname>?retryWrites=true&w=majority"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    1392695109,
    907978575
]

# The ID of the group where your bot streams
GROUP = -1001270284941

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = False

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 5

# No need to touch the following.
LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
SUDO_FILTER = filters.user(SUDO_USERS)
