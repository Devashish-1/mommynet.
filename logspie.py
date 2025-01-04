import random
import datetime
import matplotlib.pyplot as plt
import plotly.graph_objects as go



def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_logs(num_entries):
    logs = []
    mitigation_counts = {"Mitigated": 0, "Blocked": 0}

    for _ in range(num_entries):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_ip = generate_ip()
        protocol = "TCP"
        attack_type = "SYN Flood"
        packet_count = random.randint(1000, 50000)
        mitigation_status = random.choice(["Mitigated", "Blocked"])

        mitigation_counts[mitigation_status] += 1

        log_entry = (
            f"{timestamp} | {source_ip} | {protocol} | {attack_type} | "
            f"{packet_count} | {mitigation_status}\n"
        )
        logs.append(log_entry)

    return logs, mitigation_counts

def write_logs_to_file(filename, logs):
    with open(filename, "w") as file:
        file.write("Date/Time           | Source IP        | Protocol  | Attack Type | Packet Count | Mitigation Status\n")
        file.write("-------------------------------------------------------------------------------------------------------\n")
        file.writelines(logs)
        
def create_pie_chart(mitigation_counts):
    labels = list(mitigation_counts.keys())
    sizes = list(mitigation_counts.values())
    colors = ["#66b3ff", "#ff9999"]

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
    plt.title("Mitigation Status Distribution")
    plt.axis("equal")
    plt.show()
def create_interactive_pie_chart(mitigation_counts):
    labels = list(mitigation_counts.keys())
    sizes = list(mitigation_counts.values())

    fig = go.Figure(
        data=[go.Pie(labels=labels, values=sizes, hole=0.3)]
    )
    fig.update_traces(hoverinfo="label+percent", textinfo="value", textfont_size=20)
    fig.update_layout(title_text="Mitigation Status Distribution (Interactive)")
    fig.show()

def main():
    log_file = "anomalylogger.log"
    num_entries = 50  
    logs, mitigation_counts = generate_logs(num_entries)

    # Write logs to a file
    write_logs_to_file(log_file, logs)
    print(f"Generated {num_entries} log entries and saved to {log_file}")

    # Generate visualizations
    print("Creating pie charts...")
    create_pie_chart(mitigation_counts)
    create_interactive_pie_chart(mitigation_counts)

if __name__ == "__main__":
    main()
