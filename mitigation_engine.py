import socket
import threading
import time
import random

class MitigationEngine:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.attack_count = 0
        self.mitigated_requests = 0
        self.last_mitigation_time = time.time()

    def simulate_requests(self):
        return [f"Connection {i} from IP {self.ip}" for i in range(1, 501)] 

    def mitigate_attack(self):
        print(f"\n[INFO] Analyzing traffic from IP: {self.ip} on port: {self.port}")
        
        connections = self.simulate_requests()
        
        self.attack_count += len(connections)
        current_time = time.time()

        print(f"Total attack count from IP {self.ip}: {self.attack_count}")
        print(f"Time since last mitigation: {round(current_time - self.last_mitigation_time, 2)} seconds")

        # If more than 1000 requests within the last 10 seconds, mitigate (drop connections)
        if self.attack_count > 1000 and current_time - self.last_mitigation_time < 10:
            self.mitigated_requests += len(connections)
            print(f"[ALERT] Rate limiting triggered - Dropping {len(connections)} connections from IP: {self.ip}")
            
            for connection in connections:
                print(f"[DROPPED] {connection} on port {self.port}")
            
            # Reset attack count after mitigation
            self.attack_count = 0
            self.last_mitigation_time = current_time
            print(f"[INFO] Mitigation complete. Resetting attack counter.")
        elif current_time - self.last_mitigation_time >= 10:
            # Reset the attack count after 10 seconds\
            print(f"[INFO] Resetting attack count and mitigation status for IP: {self.ip}")
            self.attack_count = 0
            self.last_mitigation_time = current_time

    def print_summary(self):
        print(f"\n[SUMMARY] IP: {self.ip}")
        print(f"Total requests mitigated so far: {self.mitigated_requests}")
        print(f"Time since last mitigation: {round(time.time() - self.last_mitigation_time, 2)} seconds")
        print(f"Attack count: {self.attack_count}")
        print("-" * 50)

a = MitigationEngine("175.176.187.102", 80)

for _ in range(20):  
    a.mitigate_attack()
    a.print_summary()
    time.sleep(0.5) 
