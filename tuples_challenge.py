#!/usr/bin/python3
"""Alta3 | TRPatrick
   Capitols and Coordinates Tuple Demo"""
 
# Objective 1: Practical Use Case
def min_max(numbers):
    """Return the minimum and maximum of a list."""

    # Return a tuple containing the minimum and maximum values from the iterable
    return min(numbers), max(numbers) 
 
def main():
    """Demonstrating Tuples"""
    numbers = [5, 1, 8, 3, 2]
    min_num, max_num = min_max(numbers)
    print(f"Minimum: {min_num}, Maximum: {max_num}")
 
    # Objective 2: Creating a tuple
    coordinates = (10.0, 20.0)
    print(f"Coordinates: {coordinates}")
 
    # Objective 3: Tuple unpacking
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}, Longitude: {longitude}")
 
    # Bonus 1: Using a tuple as keys in a dictionary
    capitals = {
        (35.6895, 139.6917): "Tokyo",
        (40.7128, -74.0060): "New York",
        (48.8566, 2.3522): "Paris"
    }
 
    # Extra Fun: Adding a new capital
    capitals[(55.7558, 37.6173)] = "Moscow"
 
    # Extra Fun: Retrieving a capital by coordinates
    print(f"The capital of Japan is: {capitals[(35.6895, 139.6917)]}")
 
    # Bonus 2: Iterate over a Tuple using a For Loop
    for coords, capital in capitals.items():
        print(f"Coordinates: {coords} - Capital: {capital}")

if __name__ == "__main__":
    main()

