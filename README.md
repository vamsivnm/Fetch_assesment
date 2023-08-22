# Assesment

My understanding about this requirement:
The requirement is to implement a health-check system for HTTP endpoints defined in a YAML configuration file. Every 15 seconds, the health of each endpoint should be checked. An endpoint is considered "UP" if it returns an HTTP 2xx response within 500ms. The cumulative availability percentage for each domain (extracted from the endpoint URLs) is to be logged after each cycle.
My approach about this implementation:

Parsing YAML: I utilized the PyYAML library to read and parse the configuration file.
Checking Health: The requests library helps in sending HTTP requests to the endpoints. Response codes and time are used to determine if an endpoint is "UP".
Domain Tracking: I used Python dictionaries (domain stats) to keep track of the number of successful and total health checks for each domain. The urlparse function assists in extracting domain names from URLs.
Logging: After each cycle, the script calculates and logs the availability percentage for each domain.

To implement the desired functionality, I will use Python and some popular third-party libraries: requests (for sending HTTP requests) and PyYAML (for reading the YAML files).

Here's a step-by-step plan for the program:

1.	Parse the given YAML file to extract endpoint details.
2.	Loop indefinitely, sending HTTP requests to each endpoint every 15 seconds.
3.	Determine the health of each endpoint.
4.	Calculate and log the availability percentage for each domain.
Prerequisites:
First, you need to install the necessary libraries:

pip install requests pyyaml

How to run:
•	Two files are there with this attachment. 
health_check.py is the code file and config.yaml is the sample provided in this assignment.
•	Put these files in a folder. 
•	Open Command prompt or Anaconda prompt and navigate to the folder where you have placed the above two files.
•	Run the program using below command,

python health_check.py config.yaml
below is the command I used in my anaconda prompt.
First line is the command and rest all are results.
 

The program will start logging availability percentages every 15 seconds until you manually stop it.


How this code is working to fulfil the requirements:

•	The script starts by reading the endpoints from the given YAML configuration file.
•	For each endpoint, it sends an HTTP request and determines if it's "UP" based on the given conditions.
•	Statistics (number of successful and total checks) for each domain are stored and updated in the domain stats dictionary.
•	After completing the health check for all endpoints in a cycle, the availability percentage for each domain is calculated and logged.
•	The script then waits for 15 seconds before starting the next cycle.
•	This continuous loop ensures that the health of each endpoint is checked every 15 seconds, and the desired logging is performed after each cycle.

