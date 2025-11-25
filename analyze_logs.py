# analyze_logs.py
import re

def analyze_performance():
    latencies = []
    error_count = 0
    total_requests = 0

    with open('system_health.log', 'r') as f:
        for line in f:
            total_requests += 1
            if "SUCCESS" in line:
                # Extract the number using Regex (The "Engineering" way)
                match = re.search(r"Latency: (\d+\.\d+)ms", line)
                if match:
                    latencies.append(float(match.group(1)))
            else:
                error_count += 1

    if latencies:
        avg_latency = sum(latencies) / len(latencies)
        print(f"--- Telemetry Report ---")
        print(f"Total Requests: {total_requests}")
        print(f"Error Rate: {round((error_count/total_requests)*100, 2)}%")
        print(f"Average System Latency: {round(avg_latency, 2)}ms")

if __name__ == "__main__":
    analyze_performance()