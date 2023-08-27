# At first install Pretty error package with pip install pretty-errors

import numpy as np 
import pretty_errors

def some_function(input_dict):
    try:
        # Check if the input is a dictionary
        if not isinstance(input_dict, dict):
            raise ValueError("Input must be a dictionary")

        # Extract values from the dictionary
        keys = input_dict.keys()
        values = input_dict.values()

        # Perform calculations on the values
        sum_values = sum(values)
        mean_value = sum_values / len(values)
        squared_values = [x ** 2 for x in values]

        # Simulate a potential KeyError
        missing_value = input_dict["missing_key"]

        # Simulate a potential IndexError
        last_value = values[len(values)]

        # Simulate a potential ZeroDivisionError
        division_result = sum_values / 0

        return {
            "keys": keys,
            "sum": sum_values,
            "mean": mean_value,
            "squared_values": squared_values,
            "missing_value": missing_value,
            "last_value": last_value,
            "division_result": division_result
        }
    except Exception as e:
        return f"An error occurred: {str(e)}"

input_dict = {"a": 1, "b": 2, "c": 3}
result = some_function(input_dict)
print(result)
