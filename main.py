from data_consumer import DataConsumer
from anomaly_detection import AnomalyDetector
from document_analysis import DocumentAnalyzer
from config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC

def main():
    consumer = DataConsumer(KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC)
    detector = AnomalyDetector(threshold=3.0)
    analyzer = DocumentAnalyzer()

    for data in consumer.consume_data():
        value = data.get("value")
        sensor_id = data.get("sensor_id")
        document = data.get("document")

        # Anomaly Detection
        is_anomaly = detector.detect(value, sensor_id)

        # Document Analysis
        if document:
            analysis = analyzer.analyze_document(document)
            # Here, you can store or further process the analysis as needed

if __name__ == "__main__":
    main()
