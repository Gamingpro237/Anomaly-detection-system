
# 🛠️ Real-Time Document Analytics and Anomaly Detection System 🚀

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)

## 📖 Overview

Welcome to the **Real-Time Document Analytics and Anomaly Detection System**! This project leverages **Microsoft Fabric's Real-Time Integration (RTI)** and **Artificial Intelligence (AI)** to solve real-world problems by integrating multiple data sources, performing document analysis, and detecting anomalies in real-time. 

### 🧩 Key Features

- **📈 Real-Time Data Integration:** Utilizes Apache Kafka for seamless data streaming and integration from multiple sources.
- **🔍 Document Analysis:** Implements Azure OpenAI services to analyze and extract insights from documents.
- **⚠️ Anomaly Detection:** Employs a custom-trained AI model to identify unusual patterns and trigger alerts.
- **📊 Real-Time Analytics & Monitoring:** Provides continuous monitoring and real-time analytics for actionable insights.
- **📧 Alerting System:** Sends real-time email alerts upon detecting anomalies to ensure prompt responses.

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 📋 Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8+** installed on your system. You can download it from [here](https://www.python.org/downloads/).
- **Microsoft Azure Account** with access to:
  - **Azure OpenAI Service**
  - **Azure Event Hubs**
  - **Azure Storage** (if needed)
- **Apache Kafka** setup for real-time data streaming. You can download it from [here](https://kafka.apache.org/downloads).
- **Git** installed on your system. Download it [here](https://git-scm.com/downloads).
- **SMTP Credentials** for email alerting.

### 🔧 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/real_time_analytics.git
   cd real_time_analytics
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### 📝 Configuration

1. **Set Up Azure Services**

   - **Azure Event Hubs:** Create an Event Hub and obtain the connection string.
   - **Azure OpenAI Service:** Set up the service and obtain the API key and endpoint.

2. **Configure Environment Variables**

   Create a `config.py` file in the project root with the following content. Replace the placeholder values with your actual credentials.

   ```python
   # config.py

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
   ```

### 🏃‍♂️ Running the Project

1. **Start Apache Kafka**

   Ensure that your Kafka server is running. You can start Kafka using the following commands:

   ```bash
   # Start Zookeeper
   bin/zookeeper-server-start.sh config/zookeeper.properties

   # Start Kafka Broker
   bin/kafka-server-start.sh config/server.properties
   ```

2. **Start the Data Producer**

   Open a new terminal window/tab, activate the virtual environment, navigate to the project directory, and run:

   ```bash
   python data_producer.py
   ```

   This script simulates real-time data production by sending random sensor data and document content to the Kafka topic.

3. **Run the Main Orchestrator**

   Open another terminal window/tab, activate the virtual environment, navigate to the project directory, and run:

   ```bash
   python main.py
   ```

   This script consumes data from Kafka, performs anomaly detection, analyzes documents, and sends alerts as necessary.

## 📂 Project Structure

```
real_time_analytics/
├── data_producer.py          # Simulates real-time data production
├── data_consumer.py          # Consumes real-time data from Kafka
├── anomaly_detection.py      # Implements anomaly detection logic
├── document_analysis.py      # Performs document analysis using Azure OpenAI
├── alerting.py               # Handles sending email alerts
├── utils.py                  # Utility functions
├── main.py                   # Orchestrates the data processing workflow
├── config.py                 # Configuration file for credentials and settings
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 📚 Detailed Explanation

### 🔄 Data Integration and RTI

- **Data Producer (`data_producer.py`):** Simulates multiple data sources by generating random sensor data and document content. Sends this data to an Apache Kafka topic in real-time.
- **Data Consumer (`data_consumer.py`):** Listens to the Kafka topic and consumes incoming data in real-time for further processing.

### 🧠 Artificial Intelligence Integration

- **Anomaly Detection (`anomaly_detection.py`):** Utilizes a statistical method to detect anomalies in sensor data. If a sensor value deviates beyond a specified threshold (e.g., 3 standard deviations from the mean), it triggers an alert.
- **Document Analysis (`document_analysis.py`):** Uses Azure OpenAI's GPT model to analyze incoming document content and extract key insights.

### 📈 Real-Time Analytics and Alerting

- **Alerting (`alerting.py`):** Sends real-time email alerts when anomalies are detected in the sensor data.
- **Utilities (`utils.py`):** Contains helper functions like timestamp generation and importing alerting functions.

### 🎛️ Orchestration (`main.py`)

The `main.py` script ties all components together. It continuously consumes data from Kafka, performs anomaly detection, and analyzes documents in real-time.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

## 📄 License

This project is licensed under the [Apache2.0 License](LICENSE).

## 📧 Contact

For any questions or feedback, feel free to reach out at [your_email@example.com](mailto:your_email@example.com).

---

✨ Thank you for checking out the **Real-Time Document Analytics and Anomaly Detection System**! We hope it serves as a valuable tool in integrating real-time data processing with advanced AI capabilities.
```
