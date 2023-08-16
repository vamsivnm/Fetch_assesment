# Importing necessary modules
import yaml          # To read the YAML configuration file
import requests      # To make HTTP requests
import time          # To introduce sleep intervals between requests
from urllib.parse import urlparse   # To parse URLs and get the domain

# Function to read a YAML configuration file and return the parsed data
def read_yaml_config(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

# Function to perform health check for an HTTP endpoint
def health_check(endpoint):
    # Extracting endpoint details from the input dictionary
    url = endpoint["url"]
    method = endpoint.get("method", "GET")       # Default to GET if method is not provided
    headers = endpoint.get("headers", {})        # Use empty dictionary if headers are not provided
    body = endpoint.get("body")

    # Making the HTTP request and checking its health
    try:
        response = requests.request(method, url, headers=headers, data=body, timeout=0.5)
        return 200 <= response.status_code < 300  # Return True for success response codes (2xx)
    except:
        return False   # Return False if there's an exception (request failure or timeout)

# Main execution function
def main(file_path):
    # Read the configuration from the provided YAML file
    endpoints = read_yaml_config(file_path)

    # Dictionary to store health statistics for each domain
    domain_stats = {}

    # Infinite loop to keep checking health at intervals
    while True:
        for endpoint in endpoints:
            # Extract domain from the URL
            domain = urlparse(endpoint["url"]).netloc
            is_up = health_check(endpoint)
            
            # Initialize domain stats if not already present
            if domain not in domain_stats:
                domain_stats[domain] = {"up": 0, "total": 0}

            # Update domain stats based on health check result
            if is_up:
                domain_stats[domain]["up"] += 1

            domain_stats[domain]["total"] += 1

        # Print the health statistics for each domain
        for domain, stats in domain_stats.items():
            percentage = round(100 * stats["up"] / stats["total"])
            print(f"{domain} has {percentage}% availability percentage")

        # Sleep for 15 seconds before the next round of health checks
        time.sleep(15)

# Standard Python idiom to execute the main function
if __name__ == "__main__":
    import sys   # Importing sys to read command line arguments
    # Check if the YAML file path is provided, else print usage and exit
    if len(sys.argv) < 2:
        print("Usage: python script_name.py config_file_path")
        sys.exit(1)

    # Run the main function with the provided YAML file path
    main(sys.argv[1])
