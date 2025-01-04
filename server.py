import http.server
import socketserver
import json
from collections import Counter
import os

# Read logs from the anomalylogger.log file
def parse_logs():
    logs = []
    attack_types = []
    if os.path.exists("anomalylogger.log"):
        with open("anomalylogger.log", "r") as log_file:
            for line in log_file:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    timestamp, source_ip, attack_type, magnitude = parts
                    logs.append({
                        "timestamp": timestamp.strip(),
                        "source_ip": source_ip.strip(),
                        "attack_type": attack_type.strip(),
                        "magnitude": int(magnitude.strip())
                    })
                    attack_types.append(attack_type.strip())
    return logs, attack_types

# Serve data to HTML
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/logs':
            logs, attack_types = parse_logs()
            attack_count = Counter(attack_types)

            # Prepare data to send to HTML
            response_data = {
                "logs": logs,
                "attack_summary": attack_count
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())
        else:
            super().do_GET()

# Start the server
PORT = 8080
handler = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    httpd.serve_forever()
