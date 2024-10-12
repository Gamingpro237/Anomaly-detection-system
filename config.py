# Azure Event Hub Configuration
EVENT_HUB_CONNECTION_STR = "Your_Azure_Event_Hub_Connection_String"
EVENT_HUB_NAME = "your-event-hub-name"

# Azure OpenAI Configuration
OPENAI_API_KEY = "Your_Azure_OpenAI_API_Key"
OPENAI_API_BASE = "https://your-openai-resource.openai.azure.com/"
OPENAI_API_VERSION = "2023-05-15"

# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
KAFKA_TOPIC = 'real_time_data'

# Alerting Configuration
ALERT_EMAIL = "your_email@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_smtp_username"
SMTP_PASSWORD = "your_smtp_password"

# Other Configurations
ANOMALY_THRESHOLD = 3.0  # For standard deviation-based anomaly detection
