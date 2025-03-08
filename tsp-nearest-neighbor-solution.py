def nearest_neighbor_tsp(distances):
    """
    Solve the Traveling Salesman Problem (TSP) using the Nearest Neighbor Heuristic.
    
    Parameters:
    distances (list of list): A 2D matrix representing the distances between cities.
    
    Returns:
    tuple: (route, total_distance) where
        route (list): The order of cities visited, starting and ending at city 0.
        total_distance (int): The total distance traveled for the obtained route.
    """
    n = len(distances)  # Number of cities
    visited = [False] * n  # Track whether a city has been visited
    route = [0]  # Start from city 0
    visited[0] = True  # Mark the starting city as visited
    total_distance = 0  # Initialize total distance to zero

    # Iterate to visit all cities except the starting city
    for _ in range(1, n):
        last = route[-1]  # Get the last visited city
        nearest = None  # Variable to store the nearest unvisited city
        min_dist = float('inf')  # Initialize minimum distance with a high value
        
        # Find the nearest unvisited city
        for i in range(n):
            if not visited[i] and distances[last][i] < min_dist:
                min_dist = distances[last][i]  # Update the minimum distance
                nearest = i  # Update the nearest city
        
        # Add the nearest city to the route
        route.append(nearest)
        visited[nearest] = True  # Mark the city as visited
        total_distance += min_dist  # Accumulate the travel distance

    # Complete the tour by returning to the starting city
    total_distance += distances[route[-1]][0]
    route.append(0)  # Add the starting city at the end

    return route, total_distance  # Return the route and its total distance

# Distance matrix representing distances between cities
distances = [
    [0, 2, 2, 5, 9, 3],
    [2, 0, 4, 6, 7, 8],
    [2, 4, 0, 8, 6, 3],
    [5, 6, 8, 0, 4, 9],
    [9, 7, 6, 4, 0, 10],
    [3, 8, 3, 9, 10, 0]
]

# Solve the TSP using the Nearest Neighbor Heuristic
route, total_distance = nearest_neighbor_tsp(distances)

# Print the obtained route and total distance
print("Route:", route)
print("Total distance:", total_distance)
