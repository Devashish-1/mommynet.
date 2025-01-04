MommyNet: Advanced DDoS Protection Solution

Overview

MommyNet is an innovative Distributed Denial of Service (DDoS) protection solution designed to detect, mitigate, and log DDoS attacks in real-time. Leveraging the power of artificial intelligence (AI) and self-learning algorithms, MommyNet ensures uninterrupted service for critical infrastructure by dynamically adapting to evolving cyber threats. Its precision traffic analysis differentiates legitimate traffic from attacks, providing robust and scalable protection across cloud platforms.

Key Features

Real-Time Detection: AI-driven algorithms enable immediate detection of DDoS attacks, identifying malicious patterns with high accuracy.

Automated Mitigation: Attacks are countered automatically, reducing response time and minimizing manual intervention.

Comprehensive Logging: All detected and mitigated events are logged in a structured database and visualized in a web-based dashboard for easy monitoring.

Scalability: Seamlessly scales across cloud platforms to handle varying traffic loads.

User-Friendly Interface: A dashboard provides a detailed overview of detected threats, mitigation actions, and system status.

Folder Structure

MommyNet/
├── static/
├── templates/         # HTML templates for the web dashboard
├── alert_dashboard.py # Flask app for the web interface
├── anomaly_detector.py # Detection logic for identifying anomalies
├── mitigation_engine.py # Logic for automated mitigation
├── logger.py           # Handles logging of events into the database
├── email_notifier.py   # Sends email alerts for critical events
├── traffic_analyzer.py # Analyzes network traffic for anomalies
├── config.py           # Configuration settings
├── response.json      # Sample response data
├── main.py            # Entry point for the application
└── visualize.py       # Visualization of traffic data

How It Works

1. Traffic Monitoring

The traffic_analyzer.py module monitors incoming and outgoing traffic in real-time, collecting data on packets, source IPs, destinations, and other metadata.

2. Anomaly Detection

The anomaly_detector.py module leverages AI algorithms to detect irregular patterns in traffic that indicate potential DDoS attacks. It uses:

Pattern Matching: Matches traffic against known attack signatures.

Behavioral Analysis: Identifies deviations from normal traffic behavior.

3. Automated Mitigation

The mitigation_engine.py module automatically initiates mitigation measures such as:

Blocking suspicious IPs.

Rate-limiting traffic from suspected sources.

Redirecting traffic for further analysis.

4. Event Logging

The logger.py module records all detected anomalies and mitigation actions into a SQLite database, capturing:

Event category (e.g., DDoS detection, mitigation).

Severity level.

Detailed messages.

Timestamps.

5. Web-Based Dashboard

The alert_dashboard.py module provides a web-based interface to:

Visualize logs in a tabular format.

Filter and search logs by category, severity, and time range.

Monitor real-time events and system health.

6. Email Notifications

The email_notifier.py module sends email alerts for critical events, ensuring that administrators are promptly informed of high-severity incidents.

Installation

Prerequisites

Python 3.8+

pip package manager

SQLite

Steps

Clone the Repository:

git clone https://github.com/your-repo/MommyNet.git
cd MommyNet

Install Dependencies:

pip install -r requirements.txt

Set Up the Database:

python logger.py  # Initializes the SQLite database

Run the Application:

python alert_dashboard.py

Access the Dashboard:
Open http://localhost:5000 in your web browser.

Usage

Monitoring Traffic

The system continuously analyzes network traffic for potential threats. Detected anomalies are automatically logged and mitigated.

Viewing Logs

Access the dashboard at /logs to:

View all logged events.

Search and filter logs based on specific criteria.

Receiving Alerts

Critical events trigger email notifications sent to the configured recipients.

Example Scenario

DDoS Attack Detected:

Traffic spikes are identified by the anomaly detector.

The system classifies the event as a DDoS attack.

Mitigation Initiated:

Traffic from suspicious IPs is blocked.

Anomaly details are logged in the database.

Alert Sent:

An email notification is sent to the administrator with event details.

Logs Updated:

The dashboard displays the event with a timestamp, severity, and mitigation actions.

Future Enhancements

Advanced Threat Intelligence: Integration with global threat intelligence feeds for enhanced detection.

Customizable Mitigation Rules: User-defined rules for specific scenarios.

Cloud Integration: Automated deployment across cloud platforms like AWS and Azure.

Machine Learning Models: Improved AI algorithms for predictive analytics.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contribution

We welcome contributions! Please open an issue or submit a pull request for review.

Contact

For queries or feedback, please contact:

Name: Devashish Sharma

Email: devashishsharma5000@gmail.com
