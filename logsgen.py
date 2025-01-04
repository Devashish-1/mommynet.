import random
import datetime

def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_logs(num_entries):
    logs = []
    for _ in range(num_entries):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_ip = generate_ip()
        protocol = "TCP"
        attack_type = "SYN Flood"
        packet_count = random.randint(1000, 50000)
        mitigation_status = random.choice(["Mitigated", "Blocked"])

        log_entry = (
            f"{timestamp} | {source_ip} | {protocol} | {attack_type} | "
            f"{packet_count} | {mitigation_status}\n"
        )
        logs.append(log_entry)
    return logs

def write_logs_to_file(filename, logs):
    with open(filename, "w") as file:
        file.write("Date/Time           | Source IP        | Protocol  | Attack Type | Packet Count | Mitigation Status\n")
        file.write("-------------------------------------------------------------------------------------------------------\n")
        file.writelines(logs)

# Main function to generate and save logs
def main():
    log_file = "anomalylogger.log"
    num_entries = 50  
    logs = generate_logs(num_entries)
    write_logs_to_file(log_file, logs)
    print(f"Generated {num_entries} log entries and saved to {log_file}")

if __name__ == "__main__":
    main()
