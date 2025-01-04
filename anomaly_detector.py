import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime

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
        self.normal_threshold = 1000

    def simulate_packet(self):
        metadata = self.metadata_generator.generate_packet_metadata()
        packet_count = random.randint(300, 2000)
        return packet_count, metadata

def plot_graph(simulator):
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    packet_details = []
    sc = ax.scatter([], [], color="blue", label="Packet Count")
    line, = ax.plot([], [], color="blue")
    threshold_line = ax.axhline(simulator.normal_threshold, color="red", linestyle="--", label="Threshold")
    hover_annotation = ax.annotate(
        "", xy=(0, 0), xytext=(10, 10),
        textcoords="offset points",
        bbox=dict(boxstyle="round", fc="w"),
        arrowprops=dict(arrowstyle="->")
    )
    hover_annotation.set_visible(False)

    def update(frame):
        packet_count, metadata = simulator.simulate_packet()
        x_data.append(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])
        y_data.append(packet_count)
        packet_details.append(metadata)
        line.set_data(range(len(x_data)), y_data)
        sc.set_offsets(np.c_[range(len(x_data)), y_data])
        ax.set_xlim(0, len(x_data))
        ax.set_ylim(0, max(y_data) + 100)
        return line, sc

    def on_hover(event):
        if event.inaxes == ax:
            for i, (x, y) in enumerate(zip(range(len(x_data)), y_data)):
                if abs(event.xdata - x) < 0.5 and abs(event.ydata - y) < 50:
                    status = "Harmful" if y > simulator.normal_threshold else "Normal"
                    metadata = packet_details[i]
                    hover_annotation.xy = (x, y)
                    hover_annotation.set_text(f"Time: {x_data[i]}\nPackets: {y}\nStatus: {status}\nProtocol: {metadata['protocol']}\nSource IP: {metadata['src_ip']}\nDestination IP: {metadata['dest_ip']}\nSource Port: {metadata['src_port']}\nDestination Port: {metadata['dest_port']}\nSize: {metadata['packet_size']} bytes\nLatency: {metadata['latency']} ms")
                    hover_annotation.set_visible(True)
                    fig.canvas.draw_idle()
                    return
            hover_annotation.set_visible(False)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", on_hover)
    ani = FuncAnimation(fig, update, interval=500)
    ax.set_title("Real-Time Packet Monitoring with Threshold")
    ax.set_xlabel("Time")
    ax.set_ylabel("Packet Count")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    simulator = TrafficSimulator()
    plot_graph(simulator)
