#!/usr/bin/env python3

# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# User Interaction
def main():
    temperature_input = input("Enter the temperature to convert: ")
    if not temperature_input.replace('.', '', 1).lstrip('-').isdigit():
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    temperature = float(temperature_input)

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")
    elif unit == "C":
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")


if __name__ == "__main__":
    main()
