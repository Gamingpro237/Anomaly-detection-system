import numpy as np
from sklearn.linear_model import LinearRegression
from utils import send_alert

class AnomalyDetector:
    def __init__(self, threshold=3.0):
        self.threshold = threshold
        self.data_points = []

    def detect(self, value, sensor_id):
        self.data_points.append(value)
        if len(self.data_points) < 30:
            return False  # Not enough data to detect anomalies

        mean = np.mean(self.data_points)
        std = np.std(self.data_points)

        if abs(value - mean) > self.threshold * std:
            alert_message = f"Anomaly detected for Sensor {sensor_id}: Value={value}, Mean={mean:.2f}, Std={std:.2f}"
            print(alert_message)
            send_alert(alert_message)
            return True
        return False

