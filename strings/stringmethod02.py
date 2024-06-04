
#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com
Improved by: ChatGPT"""

def main():
    """ Run-time code demonstrating string split and join methods with enhancements """
    
    # Create a small string
    lilstring = "Alta3 Research offers classes on Python coding"
    
    # Split the string into a list of words
    newlist = lilstring.split(" ")  # This returns a list
    print("List after splitting the string by spaces:", newlist)
    
    # Handle edge cases where the string could be empty or have multiple spaces
    if not lilstring.strip():
        print("The original string is empty or contains only whitespace.")
    else:
        # Remove any extra spaces
        cleanlist = lilstring.split()
        print("List after removing extra spaces:", cleanlist)
    
    # Create a list of strings representing parts of an IP address
    myiplist = ["192", "168", "0", "12"]
    
    # Check for non-string elements in the IP list and convert them to strings if necessary
    myiplist = [str(part) for part in myiplist]
    
    # Join the list into a single IP address string
    singleip = ".".join(myiplist)
    
    # Display the resulting IP address
    print("IP address after joining the list:", singleip)
    
    # Additional functionality: join the list with a different delimiter
    hyphenated_ip = "-".join(myiplist)
    print("IP address with hyphens:", hyphenated_ip)

    # Edge case: handling an empty list for IP address parts
    empty_ip_list = []
    empty_ip_result = ".".join(empty_ip_list)
    print("Result of joining an empty IP list:", empty_ip_result)
    
    # Advanced usage: replace spaces with underscores in the original string
    underscored_string = "_".join(lilstring.split())
    print("String with spaces replaced by underscores:", underscored_string)

# Call our main function
if __name__ == "__main__":
    main()
