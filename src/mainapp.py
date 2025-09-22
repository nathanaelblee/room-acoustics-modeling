#filename: mainapp.py
#author: Nate Lee
#description: this is the main script, it defines the room, loads materials, computes total absorbtions, and returns RT60

import pathlib
from materials import load_materials
from acoustics import rt60_sab

#Built a certain path
BASE_DIR =pathlib.Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR  / "data" / "materials.yaml"

"""
Entry point for the single-band (500 Hz) RT60 calculator
You can run it with:
    python src/mainapp.py
"""

def compute_surface_areas (L: float, W: float, H: float):
    """
    Parameters:
        L (float): length of the room in meters
        W (float): width of the room in meters
        H (float): height of the room in meters
    Return:
        dict: the surface area in m^2 keys, 'floor', 'ceiling', 'walls'
    Does:
        Computes the area of the floor, ceiling, and walls of a rectangular room
    """
    floor = L * W
    ceiling = L * W
    walls = 2 * (L + W) * H
    return {"floor": floor, "ceiling": ceiling, "walls": walls}

def compute_volume (L: float, W: float, H: float):
    """
    Parameters:
        L (float): length of the room in meters
        W (float): width of the room in meters
        H (float): height of the room in meters
    Return:
        float: the rooms volume in cubic meters
    Does:
        Computes the volume of a rect room: L * W * H
    """
    return L * W * H

def total_absorption (surface_areas: dict, surface_to_material: dict, materials: dict):
    """
    Parameters:
        surface_areas (dict): mapping {surface_name: area_m2}
        surface_to_material (dict): mapping {surface_name: material_name}
        materials (dict): mapping {material_name: coeff} from YAML file
    Return:
        float: the total absorption area (A) in m^2 * sabins
    Does:
        It multiplies each surface area by its material absorption coeffs and sums
    """
    A = 0.0
    for surface, area in surface_areas.items():
        mat = surface_to_material[surface]
        A += area * materials[mat]
    return A
        
    
def main():
    """
    Parameters:
        n/a
    Return:
        n/a
    Does:
        Loads the materials data, defines the room size and surface materials, calculates the vol and total absorption area, and prints the RT60 value. Parameters of my dorm room was used.
    """
    # 1) Room geometry (meters)
    L, W, H = 3.5, 4.0, 3.5
    V = compute_volume (L, W, H)
    
    # 2) Surface areas
    areas = compute_surface_areas(L, W, H)
    
    # 3) Assign materials for YAML file
    surface_to_material = {
        "floor": "carpet",
        "ceiling": "concrete_painted",
        "walls": "concrete_painted"
    }
    
    # 4) Load materials abs coefficients
    materials = load_materials(DATA_FILE)
    
    # 5) Calculate total absorption and RT60
    A = total_absorption(areas, surface_to_material, materials)
    rt60 = rt60_sab(V,A)
    
    # 6) Print the results
    print("---- Room Acoustics ----")
    print(f"Room: {L} m × {W} m × {H} m  (Volume = {V:.2f} m³)")
    print(f"Surface areas (m²): {areas}")
    print(f"Materials: {surface_to_material}")
    print(f"Total absorption A = {A:.2f} m²·sabins")
    print(f"Estimated RT60 (Sabine): {rt60:.2f} seconds")
    
if __name__ == "__main__":
    main()
