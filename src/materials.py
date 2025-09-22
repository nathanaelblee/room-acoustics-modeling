#filename: materials.py
#author: Nate Lee
#description: loads and validates single-band (500 Hz) absorption coefficients from data/materials.yaml

import yaml

def load_materials(path):
    """
    Parameters:
        path(str): path to the YAML file that list the material and their respective absorption coefficient (a single value for around 500 Hz).
    Return:
        dict: returns a dict of all of the materials (str) and their absorption coefficients (float) in alphabetic order
    Does:
        opens and reads a YAML file at the given path, validates that the file contents form a dictionary, converts each abs coeff to a float, and checks that the coeff is between 0 and 1. It raises a ValueError if any validation fails.
    """
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    
    if not isinstance(data, dict):
        raise ValueError("The materials.yaml file must map names to numbers")
    
    for name, value in data.items():
        data[name] = float(value)
        if data[name] < 0 or data[name] > 1:
            raise ValueError ("Absorption coeff must be between 0 and 1")
            
    return data

def list_materials(materials):
    """
    Parameters:
        materials (dict): dictionary of material names and their absorption coefficients
    Return:
        list: sorts the material names in alphabetic order
    Does:
        Takes a dictionary of materials and returns a list of all the materials names in alphabetic order for easier selection
    """
    return sorted(materials.keys()) #returns material names alphabetically
