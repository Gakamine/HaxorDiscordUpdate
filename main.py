from src import Database, Scraper, Webhook
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.getcwd(), '.env'))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
HTB_TOKEN = os.getenv("HTB_TOKEN")

sources=Database.get_sources()
for source in sources:
    users=Database.get_users(source[0])
    for user in users:
        tmp_rooms=Scraper.fetch_rooms(HTB_TOKEN,source[2],user[2])
        if tmp_rooms:
            rooms=Database.check_progress(tmp_rooms,source[0],user[0])
            if rooms:
                for room in rooms:
                    Webhook.push_webhooks(WEBHOOK_URL,user,source,room)
