import os
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, jsonify
from matplotlib.animation import FuncAnimation
import numpy as np
import random
from datetime import datetime

# Flask App
app = Flask(__name__)

# Simulating Packet Metadata and Detection
class PacketMetadataGenerator:
    def __init__(self):
        self.protocols = ["TCP", "UDP", "HTTP", "HTTPS", "FTP", "SSH", "DNS"]
        self.ports = [80, 443, 53, 22, 21, 8080]

    def generate_packet_metadata(self):
        protocol = random.choice(self.protocols)
        src_ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
        dest_ip = f"10.0.{random.randint(0, 255)}.{random.randint(0, 255)}"
        src_port = random.randint(1024, 65535)
        dest_port = random.choice(self.ports)
        packet_size = random.randint(64, 1500)
        latency = round(random.uniform(0.1, 50.0), 3)
        return {
            "protocol": protocol,
            "src_ip": src_ip,
            "dest_ip": dest_ip,
            "src_port": src_port,
            "dest_port": dest_port,
            "packet_size": packet_size,
            "latency": latency
        }

class TrafficSimulator:
    def __init__(self):
        self.metadata_generator = PacketMetadataGenerator()
        self.normal_threshold = 1500

    def simulate_packet(self):
        metadata = self.metadata_generator.generate_packet_metadata()
        packet_count = random.randint(300, 2000)
        return packet_count, metadata

# Data for Visualization
packet_data = []
packet_details = []
simulator = TrafficSimulator()

# Generate Logs Dynamically
def generate_logs():
    packet_count, metadata = simulator.simulate_packet()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Harmful" if packet_count > simulator.normal_threshold else "Normal"
    log_entry = {
        "Date": timestamp.split(" ")[0],
        "Time": timestamp.split(" ")[1],
        "Packet Count": packet_count,
        "Attack Type": "DDoS" if packet_count > simulator.normal_threshold else "None",
        "Mitigation Status": status
    }
    packet_data.append(log_entry)
    packet_details.append(metadata)
    return log_entry

@app.route('/packet_data')
def fetch_packet_data():
    return jsonify(packet_data[-50:])

@app.route('/plot_data')
def plot_data():
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    for entry in packet_data:
        x_data.append(entry["Time"])
        y_data.append(entry["Packet Count"])

    ax.plot(x_data, y_data, label="Packet Count", color="blue")
    ax.axhline(simulator.normal_threshold, color="red", linestyle="--", label="Threshold")
    ax.set_title("Real-Time Packet Monitoring")
    ax.set_xlabel("Time")
    ax.set_ylabel("Packet Count")
    ax.legend()
    plt.xticks(rotation=45)

    chart_path = "static/dynamic_graph.png"
    plt.savefig(chart_path)
    plt.close()
    return jsonify({"graph_path": chart_path})

@app.route('/')
def index():
    return render_template('index.html')

# HTML Template Generation
@app.before_first_request
def setup_html():
    if not os.path.exists("templates"):
        os.mkdir("templates")
    with open("templates/index.html", "w") as file:
        file.write('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Anomaly Logs Visualization</title>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        </head>
        <body>
            <h1>Anomaly Logs Visualization</h1>
            <h2>Dynamic Packet Count Graph</h2>
            <img id="dynamic-graph" src="" alt="Graph will load here">
            <script>
                function updateGraph() {
                    $.getJSON('/plot_data', function(data) {
                        $('#dynamic-graph').attr('src', data.graph_path);
                    });
                }
                setInterval(updateGraph, 2000);
                updateGraph();
            </script>
        </body>
        </html>
        ''')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
