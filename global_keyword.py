#!/usr/bin/python3
"""Alta3 | TRPatrick
   Global Keyword"""
  
counter = 0
  
def increment_counter():
    global counter
    counter += 1
    print("Counter:", counter)
  
def main():
    # For loop to repeat the increment_counter() function 5 times
    for _ in range(5):
        increment_counter()
  
if __name__ == "__main__":
    main()

