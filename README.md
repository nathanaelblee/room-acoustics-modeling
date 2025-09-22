# room-acoustics-modeling

Author: Nate Lee
Last updated: September 2025
---

## Simulating Room Acoustics:
This is a python tool that simulates and calculates the RT60 (single band around 500 Hz) **estimation of a room's reverberation time** using its dimensions and materials using Sabines Formula:
RT60 = 0.161 × Vol / TotalAbsorption

---

## Goals
Successfully compute RT60 of a rectangular room
Create a simple materials database (with their respective **absorption coefficients**)
Provide clean code to simulate these calculations

---

## This Program
1. Loads sound absorption coefficients from "data/materials.yaml"
2. Accepts room parameters **Length, Width, and Height**
3. Calculates the surface areas and total absorption 
4. Outputs the RT60 in seconds in a report

---

## Features
Takes in room geometry (length, width, and height)
Lets user choose the **materials** for floor, walls, and ceiling
Calculates the **absorption area** and **RT60** at a mid-ranged frequency
Potential expansion to more materials and a different range of frequencies

---

## Installation
**Clone or download repository and intall requirements**
git clone https://github.com/nathanaelblee/room-acoustics-modeling.git
Install dependencies (inside the project root)
cd room-acoustics-modeling
pip install -r requirements.txt

---

## Usage
Run the project from the root:
python src/mainapp.py

---

## Sample Output:
---- Room Acoustics ----
Room: 3.5 m × 4.0 m × 3.5 m  (Volume = 49.00 m³)
Surface areas (m²): {'floor': 14.0, 'ceiling': 14.0, 'walls': 52.5}
Materials: {'floor': 'carpet', 'ceiling': 'concrete_painted', 'walls': 'concrete_painted'}
Total absorption A = 3.50 m²·sabins
Estimated RT60 (Sabine): 2.25 seconds

---

## Testing
The unit tests to validate the Sabine RT60 implementation
python -m pytest

## Future Goals
Implement more materials in database
Multi-band frequency analysis
