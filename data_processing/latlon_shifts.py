import numpy as np


def random_adjust_deg(lat, lon, max_distance_deg=0.5):
    # Generate a random direction in radians
    direction = np.random.uniform(0, 2 * np.pi)

    # Generate a random distance within the specified maximum distance
    distance = np.random.uniform(0, max_distance_deg)

    # Calculate the new latitude
    new_lat = lat + distance * np.cos(direction)
    if new_lat > 90: new_lat = 180 - new_lat        # Force upper limit to 90 (randomness is still preserved)
    if new_lat < -90: new_lat = -180 - new_lat      # Force lower limit to -90 (randomness is still preserved)
    
    # Calculate the new longitude
    new_lon = lon + distance * np.sin(direction)
    new_lon = ((new_lon + 180) % 360) - 180         # Force the output between -180 to 180


    return (new_lat, new_lon)
