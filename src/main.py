from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import os

def hydration_notification():
        data = "Take a sip of water!"
        title = "Hydrate yourself!"
        tags = "droplet"
        push_notification(data, title, tags)

def pee_notification():
        data = "Go pee!"
        title ="Do you need to pee?!"
        tags = "toilet"
        push_notification(data, title, tags)

def stretch_notification():
        data = "Stretch your legs!"
        title = "Time to do a stretch!"
        tags = "lotus_position_woman"
        push_notification(data, title, tags)

def eye_strain_notification():
        data = "Look away from the screen!"
        title = "Be careful of eye strain!"
        tags = "eyes"
        push_notification(data, title, tags)

def walk_notification():
        data = "Take a walk!"
        title = "Walk time!"
        tags = "walking_man"
        push_notification(data, title, tags)
    
def prayer_notification():
        data = "Take a moment to pray our Lord Jesus Christ that he may deliver us guidance AND a baby!"
        title = "Prayer time!"
        tags = "pray"
        push_notification(data, title, tags)

def push_notification(data, title, tags):
    requests.post(os.getenv('SERVER_AND_TOPIC'),
    data,
    headers={
        "Title" : title,
        "Tags" : tags,
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}"
    })

def main():
# Create a scheduler instance
    scheduler = BlockingScheduler()

    # Schedule the job to run every 30 minutes
    scheduler.add_job(hydration_notification, 'interval', minutes=1)
    scheduler.add_job(pee_notification, 'interval', minutes=1)
    scheduler.add_job(stretch_notification, 'interval', minutes=1)
    scheduler.add_job(eye_strain_notification, 'interval', minutes=1)
    scheduler.add_job(walk_notification, 'interval', minutes=1)
    scheduler.add_job(prayer_notification, 'interval', minutes=1)

    try:
        # Start the scheduler
        scheduler.start()
    except KeyboardInterrupt:
        # Stop the scheduler if interrupted
        scheduler.shutdown()

if __name__ == '__main__':
    main()