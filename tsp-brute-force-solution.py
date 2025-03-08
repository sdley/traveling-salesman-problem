from itertools import permutations  # Importing permutations function to generate all possible routes

def calculate_distance(route, distances):
    """
    Calculate the total distance of a given route based on the distance matrix.
    
    Parameters:
    route (list): A list representing the order in which cities are visited.
    distances (list of list): A 2D matrix where distances[i][j] represents the distance from city i to city j.
    
    Returns:
    int: The total distance traveled in the given route.
    """
    total_distance = 0  # Initialize total distance to zero
    
    # Loop through the route and accumulate distances between consecutive cities
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    
    # Add the distance from the last city back to the starting city to complete the tour
    total_distance += distances[route[-1]][route[0]]
    
    return total_distance  # Return the computed total distance

def brute_force_tsp(distances):
    """
    Solve the Traveling Salesman Problem (TSP) using the brute force approach.
    
    Parameters:
    distances (list of list): A 2D matrix representing distances between cities.
    
    Returns:
    tuple: (shortest_route, min_distance) where
        shortest_route (list): The optimal order of visiting cities including returning to the start.
        min_distance (int): The minimum distance for the optimal route.
    """
    n = len(distances)  # Number of cities
    cities = list(range(1, n))  # List of cities excluding the starting city (assumed to be 0)
    
    shortest_route = None  # Variable to store the best (shortest) route
    min_distance = float('inf')  # Initialize minimum distance with a very high value
    
    # Generate all possible permutations of cities (excluding the starting city)
    for perm in permutations(cities):
        current_route = [0] + list(perm)  # Form a complete route by adding the starting city at the beginning
        current_distance = calculate_distance(current_route, distances)  # Calculate the distance of the current route
        
        # Check if the current route has a shorter distance than the previously found shortest route
        if current_distance < min_distance:
            min_distance = current_distance  # Update the minimum distance
            shortest_route = current_route  # Update the shortest route found
    
    shortest_route.append(0)  # Append the starting city at the end to complete the tour
    
    return shortest_route, min_distance  # Return the shortest route and its total distance

# Distance matrix representing the distances between cities
distances = [
    [0, 2, 2, 5, 9, 3],
    [2, 0, 4, 6, 7, 8],
    [2, 4, 0, 8, 6, 3],
    [5, 6, 8, 0, 4, 9],
    [9, 7, 6, 4, 0, 10],
    [3, 8, 3, 9, 10, 0]
]

# Solve the TSP using brute force method
route, total_distance = brute_force_tsp(distances)

# Print the optimal route and its total distance
print("Route:", route)
print("Total distance:", total_distance)
