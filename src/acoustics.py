#filename: acoustics.py
#author: Nate Lee
#description: calculates the reverberation time (RT60) using sabines formula (single band)
"""Core sabine RT60 calculation (single band)"""

def rt60_sab(volume_m3: float, absorption_area_m2: float):
    """
    Parameters:
        volume_m3 = is the total room volume in cubic meters
        absorption_area_m2 = the total absorbtion area in square meters
    Returns: 
        float: estimated RT60 in seconds
    Does:
        Computes the RT60 using sabines formula:
            0.161 * volume_m3 / absorption_area_m2
        also raises a ValueError if absorption_area_m2 <=0
    """
    if (absorption_area_m2 <= 0):
        raise ValueError("The absorption area must be positive.")
    return float(0.161 * volume_m3 / absorption_area_m2)

