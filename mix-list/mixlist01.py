#!/usr/bin/env python3

def main():
    """Display only IP addresses from the given list."""
    
    # Given list containing various types of items
    iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]
    
    # Initialize an empty list to hold IP addresses
    ip_addresses = []
    
    # Iterate through each item in the list
    for item in iplist:
        # Check if the item is a string and contains three dots
        if isinstance(item, str) and item.count('.') == 3:
            # Split the item by dots and check if all parts are digits
            if all(part.isdigit() for part in item.split('.')):
                ip_addresses.append(item)
    
    # Display the IP addresses
    for ip in ip_addresses:
        print(ip)
