import json
from collections import defaultdict

# Load the JSON file
with open('os_list.json', 'r') as f:
    data = json.load(f)

# Initialize a new dictionary to store the restructured data
restructured_data = {
    "imager": {
        "manufacturers": []
    }
}

# Create a dictionary to hold manufacturers temporarily
manufacturers = defaultdict(list)

# Go through the devices listed in the original file
for device_entry in data['imager']['devices']:
    # Extract manufacturer name from the device name
    manufacturer_name = device_entry['name'].split()[0]
    # Remove manufacturer prefix from the device name to keep it clean
    device_name = " ".join(device_entry['name'].split()[1:])
    
    # Add device entry to the manufacturer's list
    manufacturers[manufacturer_name].append({
        "name": device_name,
        "tags": device_entry['tags'],
        "icon": device_entry['icon']
    })

# Transform the manufacturers dictionary into the desired JSON structure
for manufacturer, devices in manufacturers.items():
    restructured_data['imager']['manufacturers'].append({
        "name": manufacturer,
        "devices": devices
    })

# Save the new JSON structure to a new file
with open('restructured_os_list.json', 'w') as f:
    json.dump(restructured_data, f, indent=4)

print("JSON restructuring completed. Check 'restructured_os_list.json' for the updated file.")
