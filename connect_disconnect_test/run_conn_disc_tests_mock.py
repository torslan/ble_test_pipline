import logging
import time
import os

# Set up logging
results_dir = os.path.join(os.path.dirname(__file__), 'results')
os.makedirs(results_dir, exist_ok=True)
log_file = os.path.join(results_dir, 'conn_disc_test_results.txt')
logging.basicConfig(filename=log_file, level=logging.INFO)

def mock_test_connect_disconnect():
    logging.info("Starting mock Connectivity/Disconnect test...")

    # Simulate connecting to a mock Bluetooth device
    mock_device = ("AA:BB:CC:DD:EE:FF", "MockConnectivityDevice")

    logging.info(f"Simulated found Bluetooth device {mock_device[1]} with address {mock_device[0]}")
    
    # Simulate connecting
    logging.info(f"Simulating connection to {mock_device[1]}")
    time.sleep(1)  # Simulate connection delay

    # Simulate successful connection
    logging.info(f"Connection to {mock_device[1]} successful")

    # Simulate disconnection
    logging.info(f"Simulating disconnection from {mock_device[1]}")
    time.sleep(1)  # Simulate disconnection delay

    logging.info(f"Disconnection from {mock_device[1]} successful")

if __name__ == "__main__":
    mock_test_connect_disconnect()
