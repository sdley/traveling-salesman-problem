# Traveling Salesman Problem
The Traveling Salesman Problem states that you are a salesperson and you must visit a number of cities or towns.

- **Rules**: Visit every city only once, then return back to the city you started in.

- **Goal**: Find the shortest possible route.

There is almost no other way to find the shortest route than to check all possible routes.

This means that the time complexity for solving this problem is O(n!), which means 720 routes needs to be checked for 6 cities, 40,320 routes must be checked for 8 cities, and if you have 10 cities to visit, more than 3.6 million routes must be checked!

## Traveling Salesman Problem Algorithms
Here are some of the most popular solutions to the Travelling Salesman Problem:

### The brute-force approach
TThe brute-force approach, also known as the naive approach, calculates and compares all possible permutations of routes or paths to determine the shortest unique solution. To solve the TSP using the brute-force approach, you must calculate the total number of routes and then draw and list all the possible routes. Calculate the distance of each route and then choose the shortest one — this is the optimal solution. 

This is only feasible for small problems, rarely useful beyond theoretical computer science tutorials.

The reason why the brute force approach of finding the shortest route (as shown above) is so time consuming is that we are checking all routes, and the number of possible routes increases really fast when the number of cities increases.

### The nearest neighbor method
To implement the nearest neighbor algorithm, we begin at a randomly selected starting point. From there, we find the closest unvisited node and add it to the sequencing. Then, we move to the next node and repeat the process of finding the nearest unvisited node until all nodes are included in the tour. Finally, we return to the starting city to complete the cycle.

While the nearest neighbor approach is relatively easy to understand and quick to execute, it rarely finds the optimal solution for the traveling salesperson problem. It can be significantly longer than the optimal route, especially for large and complex instances. Nonetheless, the nearest neighbor algorithm serves as a good starting point for tackling the traveling salesman problem and can be useful when a quick and reasonably good solution is needed.

This greedy algorithm can be used effectively as a way to generate an initial feasible solution quickly, to then feed into a more sophisticated local search algorithm, which then tweaks the solution until a given stopping condition.