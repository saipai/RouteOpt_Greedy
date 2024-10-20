import random
random.seed(42)
import numpy as np
import matplotlib.pyplot as plt

# Parameters
n_locations = 10  # 10 delivery locations
drones = 2  # Number of drones
warehouse = (0, 0)  # Starting point for both drones

# Generate random coordinates for the 10 delivery locations
locations = [(random.uniform(5, 30), random.uniform(5, 30)) for _ in range(n_locations)]
locations.insert(0, warehouse)  # Add the warehouse as the starting point (index 0)
print(locations)

# Calculate distance between two points
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix for all locations
distance_matrix = np.zeros((n_locations + 1, n_locations + 1))
for i in range(n_locations + 1):
    for j in range(n_locations + 1):
        distance_matrix[i, j] = distance(locations[i], locations[j])

def greedy_solution():
    # Initialize: both drones start at the warehouse
    drone1_route = [0]  # 0 represents the warehouse
    drone2_route = [0]
    
    # Set of unvisited locations
    unvisited = set(range(1, n_locations + 1))
    
    # Positions of the drones (both start at the warehouse)
    drone1_pos = 0
    drone2_pos = 0
    
    while unvisited:
        # Drone 1 selects the nearest unvisited location
        nearest1 = min(unvisited, key=lambda loc: distance_matrix[drone1_pos][loc])
        drone1_route.append(nearest1)
        unvisited.remove(nearest1)
        drone1_pos = nearest1  # Move drone 1 to the selected location
        
        if unvisited:
            # Drone 2 selects the nearest unvisited location
            nearest2 = min(unvisited, key=lambda loc: distance_matrix[drone2_pos][loc])
            drone2_route.append(nearest2)
            unvisited.remove(nearest2)
            drone2_pos = nearest2  # Move drone 2 to the selected location
    
    # Return to warehouse
    drone1_route.append(0)
    drone2_route.append(0)
    
    # Calculate the total distance traveled by each drone
    total_distance_drone1 = sum(distance_matrix[drone1_route[i]][drone1_route[i+1]] for i in range(len(drone1_route) - 1))
    total_distance_drone2 = sum(distance_matrix[drone2_route[i]][drone2_route[i+1]] for i in range(len(drone2_route) - 1))
    
    return drone1_route, drone2_route, total_distance_drone1 + total_distance_drone2

# Example run
drone1_route, drone2_route, total_distance_greedy = greedy_solution()

drone1_route, drone2_route, total_distance_greedy

print(drone1_route)
print(drone2_route)

print(total_distance_greedy)