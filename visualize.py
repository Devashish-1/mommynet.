import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

class DataVisualizer:
    def __init__(self):
        self.packet_data = [] 

    def capture_data(self, packet_count, anomaly_score, mitigated_requests):
        timestamp = len(self.packet_data) + 1 
        self.packet_data.append((timestamp, packet_count, anomaly_score, mitigated_requests))

    def simulate_data(self, anomaly_detector, mitigation_engine):
        for _ in range(50): 
            packet_count = random.randint(300, 2000)
            anomaly_score = anomaly_detector.detect_anomaly(packet_count)
            mitigated_requests = mitigation_engine.mitigated_requests

            if anomaly_score:
                print(f"Anomaly Detected: {anomaly_score}")
            mitigation_engine.mitigate_attack()

            self.capture_data(packet_count, anomaly_score if anomaly_score else 0, mitigated_requests)

    def visualize_data_3d(self):
        times = np.array([data[0] for data in self.packet_data])
        packet_counts = np.array([data[1] for data in self.packet_data])
        anomaly_scores = np.array([data[2] for data in self.packet_data])
        mitigated_requests = np.array([data[3] for data in self.packet_data])

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.plot(times, packet_counts, anomaly_scores, label="Packet Traffic", color='blue')
        sc = ax.scatter(times, packet_counts, anomaly_scores, c=mitigated_requests, cmap='coolwarm')

        cbar = plt.colorbar(sc)
        cbar.set_label('Mitigated Requests')

        ax.set_xlabel('Time')
        ax.set_ylabel('Packet Count')
        ax.set_zlabel('Anomaly Score')
        ax.set_title('3D Visualization of Traffic Anomalies and Mitigations')

        plt.show()

if __name__ == "__main__":
    from anomaly_detector import AnomalyDetector
    from mitigation_engine import MitigationEngine

    detector = AnomalyDetector(threshold=-0.3)
    mitigation_engine = MitigationEngine(ip="175.176.187.102", port=80)

    visualizer = DataVisualizer()

    visualizer.simulate_data(detector, mitigation_engine)
    visualizer.visualize_data_3d()
