#!/usr/bin/env python3
"""
temp_conversion_tool.py

A simple temperature conversion tool demonstrating
the use of global variables and functions in Python.
"""

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factor.
    Formula: (F - 32) * 5/9
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factor.
    Formula: (C * 9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    """
    Main function to handle user input and display temperature conversions.
    """
    try:
        # Prompt user for temperature value
        temperature_input = input("Enter the temperature to convert: ")
        temperature = float(temperature_input)  # validate input

        # Prompt user for unit type
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == "C":
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"Invalid temperature. Please enter a numeric value. ({e})")


if __name__ == "__main__":
    main()
