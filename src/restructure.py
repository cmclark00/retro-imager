import json

# Load the original JSON
with open('os_list.json', 'r') as f:
    data = json.load(f)

# Create a dictionary to map device tags to manufacturers
device_to_manufacturer = {}

# Populate the device_to_manufacturer map from the "imager" section
for manufacturer in data["imager"]["manufacturers"]:
    manufacturer_name = manufacturer["name"]
    for device in manufacturer["devices"]:
        for tag in device["tags"]:
            device_to_manufacturer[tag] = manufacturer_name

# Initialize the new structure
restructured_data = {
    "os_list": [],
    "imager": {
        "latest_version": "1.6",
        "url": "https://www.raspberrypi.org/software/",
        "default_os": "muOS 2410.1 Banana for RG35XX Plus",
        "embedded_default_os": "muOS 2410.1 Banana for RG35XX Plus",
        "embedded_default_destination": "/dev/mmcblk0p1"
    }
}

# Go through the OS list and reformat the data
for os_entry in data["os_list"]:
    # Create a new entry for each OS in the required format
    new_os_entry = {
        "name": os_entry["name"],
        "description": os_entry["description"],
        "icon": os_entry["icon"],
        "url": os_entry["url"],
        "release_date": os_entry["release_date"],
        "image_download_size": os_entry["image_download_size"],
        "extract_size": os_entry["extract_size"],
        "extract_sha256": os_entry["extract_sha256"],
        "devices": []
    }
    
    # Add compatible device info under "devices" key
    for device in os_entry.get("devices", []):
        manufacturer = device_to_manufacturer.get(device, "Unknown")
        new_device_entry = {
            "name": device,
            "manufacturer": manufacturer,
            "tags": [device],
            "icon": f"https://github.com/cmclark00/retro-imager/blob/dev/src/icons/{device}.png?raw=true"
        }
        new_os_entry["devices"].append(new_device_entry)

    # Add the new OS entry to the restructured data
    restructured_data["os_list"].append(new_os_entry)

# Save the restructured JSON to a new file
with open('restructured_os_list.json', 'w') as f:
    json.dump(restructured_data, f, indent=4)

print("Restructuring completed. Check 'restructured_os_list.json' for the updated file.")
