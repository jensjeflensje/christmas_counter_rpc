import pypresence as rpc
import time
import datetime
import math

presence = rpc.Presence("658591535180414996")
presence.connect()

while True:
    delta = datetime.datetime(2019, 12, 25) - datetime.datetime.now()
    days = delta.days
    days_text = "dagen"
    if days == 1:
        days_text = "dag"
    hours = math.floor(delta.seconds / 3600)
    minutes = math.ceil(delta.seconds / 60) - (hours * 60)
    minutes_text = "minuten"
    if minutes == 1:
        minutes_text = "minuut"
    presence.update(state=f"{days} {days_text}, {hours} uur en {minutes} {minutes_text}", details="Het is kerst over:",
                    small_image="kerstboom",
                    small_text="Jingle bells...",
                    large_image="jens",
                    large_text="Gemaakt door Jens 💻 Jederu™#5961")
    time.sleep(15)
