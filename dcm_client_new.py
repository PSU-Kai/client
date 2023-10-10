import os
import requests
import csv

# Define the path to the CSV file
csv_file_path = '/home/pi/client/data.csv'

# Function to read the last row of CSV and extract values
def read_last_row(csv_file_path):
    try:
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
            if len(rows) >= 2:  # Check if there are at least 2 rows (header + data)
                last_row = rows[-1]  # Get the last row
                energy_take = float(last_row[0])  # Extract energy_take from the last row
                duration = float(last_row[1])  # Extract duration from the last row
                power = float(last_row[2])  # Extract power from the last row
                interval = float(last_row[3])  # Extract interval from the last row
                return interval, duration, power, energy_take
            else:
                print(f"Not enough rows in {csv_file_path} to extract data.")
    except FileNotFoundError:
        print(f"CSV file not found at {csv_file_path}")
    except Exception as e:
        print(f"Error reading CSV: {str(e)}")
    return None, None, None, None

path = os.getcwd()
c_cert_file_path = path + '/cert/client.crt'
c_key_file_path = path + '/cert/client.key'
certServer = path + '/cert/derms.crt'

host_name = 'psupwrlabderms.ddns.net'
host_port = 443
host_address = f'https://{host_name}:{host_port}'

# Read values from the last row of CSV
interval, duration, power, energy_take = read_last_row(csv_file_path)

if interval is not None:
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <Order>
      <Id>78913</Id>
      <to>gsp</to>
      <from>client</from>
      <Customer>SPC_1</Customer>
      <message>Start Service?</message>
      <Interval>{interval}</Interval>
      <Duration>{duration}</Duration>
      <Power>{power}</Power>
      <EnergyTake>{energy_take}</EnergyTake>
    </Order>"""
    headers = {'Content-Type': 'application/xml'}

    r = requests.post(host_address, data=xml, verify=certServer, headers=headers, cert=(c_cert_file_path, c_key_file_path))
    
    print(f"Response from server:\n{r.text}")  # Print the server's response
    
    print(f"Status Code: {r.status_code}")
else:
    print("CSV values not available, request not sent.")
