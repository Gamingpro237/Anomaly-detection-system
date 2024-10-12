from datetime import datetime

def get_timestamp():
    return datetime.utcnow().isoformat()

# Import send_alert from alerting.py
from alerting import send_alert