#!/usr/bin/python3
""" Alta3 | TRPatrick
    Demonstrating String Operations"""


def main():
    """Simple Demonstration of String Operations"""

    # Constructing Strings
    simple_string = "Python strings are powerful!"
    print("Constructed String:", simple_string)

    # Indexing and Slicing
    print("First character:", simple_string[0])
    print("Sliced String:", simple_string[7:14])

    # Escaping Characters
    escape_string = "She said, \"Python is amazing!\""
    print("Escaped String:", escape_string)

    # Quotes and Apostrophes
    quote_string = "It's easy to use apostrophes in strings."
    print("Quote String:", quote_string)

    # Multi-line Strings
    multi_line = """This is the first line.
    This is the second line.
    And this is the third line."""
    print("Multi-line String:\n", multi_line)

if __name__ == "__main__":
   main()

