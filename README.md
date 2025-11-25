# Automated Service Health Monitor & Telemetry Tool

## 📌 Overview
A robust Python-based monitoring tool designed to track the availability, latency, and reliability of distributed web services. This project mimics enterprise-grade **Observability Pipelines** by implementing structured logging, automated health checks, and failure resilience.

It is designed to run continuously, capturing real-time telemetry data to enable data-driven incident retrospectives and root cause analysis.

## ⚙️ Engineering Highlights
* **Resilient Architecture:** Implements strict **timeouts** and robust `try/catch` exception handling to prevent the monitor itself from crashing during network outages or target service failures.
* **Structured Telemetry:** Logs granular data points (Timestamp, Target URL, Status Code, Latency in ms) to a persistent file (`system_health.log`) for historical analysis.
* **Log Analysis Engine:** Includes a separate parsing module using **RegEx** to calculate aggregate metrics like **Average Latency** and **System Uptime %** from raw log data.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Core Libraries:** `requests` (HTTP calls), `logging` (Telemetry), `re` (Data Parsing), `time`/`datetime`.

## 📂 Project Structure
* `monitor.py`: The main service that performs health checks and writes to the log.
* `analyze_logs.py`: A utility script that parses the log file to generate uptime reports.
* `system_health.log`: The generated telemetry file (created automatically).

## 💻 How to Run

### 1. Install Dependencies
```bash
pip install requests
````

### 2\. Start Monitoring

Run the monitor script. It will check the target services every 60 seconds (configurable).

```bash
python monitor.py
```

*Output:*

```text
[Scan started at 10:00:01]
✅ SUCCESS: [https://www.google.com](https://www.google.com) | Latency: 120.5ms | Status: 200
⚠️ FAILURE: [https://httpstat.us/503](https://httpstat.us/503) | Status: 503
```

### 3\. Analyze Telemetry

After running the monitor for a while, run the analyzer to see the health report:

```bash
python analyze_logs.py
```

*Output:*

```text
--- Telemetry Report ---
Total Requests: 50
Error Rate: 2.0%
Average System Latency: 115.4ms
```
## 📝 Sample Telemetry Log
The system generates structured logs designed for easy parsing:
```text
2025-11-25 10:00:01 - INFO - SUCCESS: [https://www.google.com](https://www.google.com) | Latency: 120.5ms | Status: 200
2025-11-25 10:00:02 - WARNING - FAILURE: [https://httpstat.us/503](https://httpstat.us/503) | Status: 503
2025-11-25 10:00:03 - CRITICAL - DOWN: [https://expired.badssl.com](https://expired.badssl.com) | Status: Unreachable
```

```
```
