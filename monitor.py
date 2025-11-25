import requests
import time
import logging
from datetime import datetime

# We configure logging to save data to a file instead of just printing to console.
# This creates a persistent record of system behavior.
logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# List of endpoints to monitor
# In a real scenario, this might come from a configuration file.
TARGET_URLS = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.microsoft.com",
    "https://httpstat.us/503"  # A fake URL that always returns a 503 Error (to test your logic)
]

def check_service_health(url):
    try:
        # We time how long the request takes.
        start_time = time.time()
        
        # --- JD KEYWORD: "Safety Mechanisms" ---
        # strictly enforcing a timeout. If a server hangs, we don't want OUR monitor to freeze.
        response = requests.get(url, timeout=5) 
        
        latency = round((time.time() - start_time) * 1000, 2) # Convert to ms

        # --- JD KEYWORD: "Reliability" ---
        if response.status_code == 200:
            log_msg = f"SUCCESS: {url} | Latency: {latency}ms | Status: {response.status_code}"
            print(f"✅ {log_msg}")
            logging.info(log_msg)
        else:
            log_msg = f"FAILURE: {url} | Status: {response.status_code}"
            print(f"⚠️ {log_msg}")
            logging.warning(log_msg)

    except requests.exceptions.Timeout:
        # --- JD KEYWORD: "Incident Retrospectives" ---
        # We capture specific errors so we know WHY it failed later.
        log_msg = f"TIMEOUT: {url} took longer than 5s"
        print(f"❌ {log_msg}")
        logging.error(log_msg)

    except requests.exceptions.ConnectionError:
        log_msg = f"DOWN: {url} is unreachable"
        print(f"❌ {log_msg}")
        logging.critical(log_msg)
        
    except Exception as e:
        # Catch-all to ensure the monitor NEVER crashes
        logging.error(f"SYSTEM ERROR checking {url}: {str(e)}")

def start_monitoring(interval=60):
    print(f"--- Starting Telemetry Monitor (Interval: {interval}s) ---")
    print("Press Ctrl+C to stop.\n")
    
    try:
        while True:
            print(f"\n[Scan started at {datetime.now().strftime('%H:%M:%S')}]")
            for url in TARGET_URLS:
                check_service_health(url)
            
            # Wait for next cycle
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\n--- Monitoring Stopped by User ---")

if __name__ == "__main__":
    start_monitoring(interval=10) # Checks every 10 seconds for demo purposes