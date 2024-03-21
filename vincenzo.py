class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class GoldenPoint(Point):
    pass

class SilverPoint(Point):
    def __init__(self, x, y, score):
        super().__init__(x, y)
        self.score = score

'''class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell() for _ in range(width)] for _ in range(height)]

    def add_golden_point(self, x, y):
        self.grid[y][x].has_golden_point = True

    def add_silver_point(self, x, y, score):
        self.grid[y][x].has_silver_point = True
        self.grid[y][x].silver_point_score = score

    def has_golden_point(self, x, y):
        return self.grid[y][x].has_golden_point

    def has_silver_point(self, x, y):
        return self.grid[y][x].has_silver_point

    def get_silver_point_score(self, x, y):
        return self.grid[y][x].silver_point_score'''

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell() for _ in range(width)] for _ in range(height)]

    def add_golden_point(self, x, y):
        self.grid[y][x].has_golden_point = True

    def add_silver_point(self, x, y, score):
        self.grid[y][x].has_silver_point = True
        self.grid[y][x].silver_point_score = score

    def has_golden_point(self, x, y):
        return self.grid[y][x].has_golden_point

    def has_silver_point(self, x, y):
        return self.grid[y][x].has_silver_point

    def get_silver_point_score(self, x, y):
        return self.grid[y][x].silver_point_score

    def get_neighbors(self, current):
        neighbors = []
        x, y = current
        if x > 0:
            neighbors.append((x - 1, y))  # Left neighbor
        if x < self.width - 1:
            neighbors.append((x + 1, y))  # Right neighbor
        if y > 0:
            neighbors.append((x, y - 1))  # Upper neighbor
        if y < self.height - 1:
            neighbors.append((x, y + 1))  # Lower neighbor
        return neighbors

    def get_neighbors_with_direction(self, current_tile):
        x, y = current_tile
        neighbors = self.get_neighbors(current_tile)
        neighbors_with_direction = {}
        for neighbor_x, neighbor_y in neighbors:
            direction = None
            if neighbor_x == x - 1:
                direction = 'west'
            elif neighbor_x == x + 1:
                direction = 'east'
            elif neighbor_y == y - 1:
                direction = 'north'
            elif neighbor_y == y + 1:
                direction = 'south'
            neighbors_with_direction[(neighbor_x, neighbor_y)] = direction
        return neighbors_with_direction

    def get_possible_directions(self, next_tile):
        x, y = next_tile
        directions = []
        if x > 0 and not self.has_golden_point(x - 1, y):
            directions.append('west')
        if x < self.width - 1 and not self.has_golden_point(x + 1, y):
            directions.append('east')
        if y > 0 and not self.has_golden_point(x, y - 1):
            directions.append('north')
        if y < self.height - 1 and not self.has_golden_point(x, y + 1):
            directions.append('south')
        return directions

class Cell:
    def __init__(self):
        self.has_golden_point = False
        self.has_silver_point = False
        self.silver_point_score = 0

class Tile:
    def __init__(self, tile_id, cost, quantity):
        self.tile_id = tile_id
        self.cost = cost
        self.quantity = quantity
        self.directions = {
            'north': False,
            'south': False,
            'east': False,
            'west': False
        }
    
    def set_direction(self, direction):
        if direction in self.directions:
            self.directions[direction] = True
    
    def use_tile(self):
        self.quantity -= 1
    
    def can_move(self, direction):
        return self.directions[direction]
    
    def can_move(self, direction):
        return self.directions[direction] != (0, 0)
    
    def __str__(self):
        return f"Tile ID: {self.tile_id}, Cost: {self.cost}, Quantity: {self.quantity}, Directions: {self.directions}"


# Allowed directions for each tile ID
allowed_directions_map = {
    '3': ['east', 'west'],
    '5': ['south', 'east'],
    '6': ['west', 'south'],
    '7': ['north', 'south', 'east'],
    '9': ['north', 'east'],
    '96': ['west', 'north'],
    'A': ['north', 'west'],
    'A5': ['north', 'east'],
    'B': ['north', 'east', 'west'],
    'C': ['north', 'south'],
    'C3': ['north', 'south', 'east'],
    'D': ['north', 'south', 'east'],
    'E': ['north', 'south', 'west'],
    'F': ['north', 'south', 'east', 'west']
}

def parse_tile_input(tile_info):
    tile_id, cost, quantity = tile_info.split()
    tile = Tile(tile_id, int(cost), int(quantity))
    allowed_directions = allowed_directions_map.get(tile_id)
    if allowed_directions:
        for direction in allowed_directions:
            tile.set_direction(direction)
    return tile


# Parse input file
input_file = "data/02-sentimental.txt"  # Change this to your input file name
golden_points = []
silver_points = []
tiles = []

with open(input_file, 'r') as file:
    W, H, GN, SM, TL = map(int, file.readline().split())

    grid = Grid(W, H)

    # Parse Golden Points
    for _ in range(GN):
        x, y = map(int, file.readline().split())
        golden_points.append(GoldenPoint(x, y))

    # Parse Silver Points
    for _ in range(SM):
        x, y, score = map(int, file.readline().split())
        silver_points.append(SilverPoint(x, y, score))

    # Parse Tiles
    for _ in range(TL):
        tile_info = file.readline()

        tiles.append(parse_tile_input(tile_info))

# Print parsed information for verification
print("Grid dimensions:", W, "x", H)
print("Golden Points:")
for point in golden_points:
    print("(", point.x, ",", point.y, ")")
    grid.add_golden_point(point.x, point.y)
print("Silver Points:")
for point in silver_points:
    grid.add_silver_point(point.x, point.y, point.score)
    print("(", point.x, ",", point.y, ") Score:", point.score)
print("Tiles:")
for tile in tiles:
    print("Tile ID:", tile.tile_id, "Cost:", tile.cost, "Quantity:", tile.quantity, "Directions:", tile.directions)


'''import matplotlib.pyplot as plt

def plot_grid(grid, golden_points, silver_points):
    fig, ax = plt.subplots()
    
    # Plot golden points
    for point in golden_points:
        ax.plot(point.x, point.y, 'yo', markersize=10)

    # Plot silver points
    for point in silver_points:
        ax.plot(point.x, point.y, 'co', markersize=8)

    # Plot grid lines
    for y in range(grid.height + 1):
        ax.axhline(y, color='gray', linestyle='-', linewidth=0.5)
    for x in range(grid.width + 1):
        ax.axvline(x, color='gray', linestyle='-', linewidth=0.5)

    ax.set_xticks(range(grid.width))
    ax.set_yticks(range(grid.height))
    ax.set_xlim(-0.5, grid.width - 0.5)
    ax.set_ylim(-0.5, grid.height - 0.5)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')
    plt.gca().invert_yaxis()  # Invert y-axis to match grid coordinates
    plt.show()

# Call plot_grid function
plot_grid(grid, golden_points, silver_points)'''

from queue import PriorityQueue

class PathFinder:
    def __init__(self, grid, golden_points, silver_points, tiles):
        self.grid = grid
        self.golden_points = golden_points
        self.silver_points = silver_points
        self.tiles = tiles
        self.current_position = None
        self.current_golden_point = None
        self.path = []
        self.score = 0

    def reconstruct_path(self, came_from, start, end):
        current = end
        path = []
        while current != start:
            path.append((came_from[current][0], current))  # Store tile object and coordinates
            current = came_from[current][0]
        path.append((start, end))
        path.reverse()
        return path

    def find_shortest_path(self):
        self.current_position = self.golden_points[0]
        self.current_golden_point = 0

        while self.current_golden_point < len(self.golden_points) - 1:
            next_golden_point = self.golden_points[self.current_golden_point + 1]
            path_to_next_golden_point = self.find_path_to_golden_point(next_golden_point)
            self.path.extend(path_to_next_golden_point)
            self.current_golden_point += 1


    
    def find_path_to_golden_point(self, next_golden_point):
        start = (self.current_position.x, self.current_position.y)
        end = (next_golden_point.x, next_golden_point.y)

        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == end:
                break

            dicti = self.grid.get_neighbors_with_direction(current)

            for next_tile, direction in dicti.items():
                new_cost = cost_so_far[current] + self.get_tile_cost(current, next_tile)
                if next_tile not in cost_so_far or new_cost < cost_so_far[next_tile]:
                    cost_so_far[next_tile] = new_cost
                    priority = new_cost + self.heuristic(Point(next_tile[0], next_tile[1]), Point(end[0], end[1]))
                    frontier.put(next_tile, priority)
                    came_from[next_tile] = (current, direction)

        path = self.reconstruct_path(came_from, start, end)
        return path


    '''def find_path_to_golden_point(self, next_golden_point):
        # Implement A* search algorithm to find the shortest path to the next golden point
        # Consider collecting silver points along the way to maximize the score
        start = self.current_position
        end = next_golden_point

        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == end:
                break

            for next_tile in self.grid.get_neighbors(current):
                new_cost = cost_so_far[current] + self.get_tile_cost(current, next_tile)
                if next_tile not in cost_so_far or new_cost < cost_so_far[next_tile]:
                    cost_so_far[next_tile] = new_cost
                    priority = new_cost + self.heuristic(next_tile, end)
                    frontier.put(next_tile, priority)
                    came_from[next_tile] = current

        path = []
        current = end
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()

        return path'''

    def get_tile_cost(self, current_tile, next_tile):
        # Calculate the cost of moving from the current tile to the next tile
        # Consider the cost of the tile and any silver points collected
        cost = 0
        for direction, neighbor in self.grid.get_neighbors_with_direction(current_tile):
            if neighbor == next_tile:
                tile = self.select_tile(direction, self.grid.get_possible_directions(next_tile))
                cost += tile.cost
                if self.grid.has_silver_point(next_tile.x, next_tile.y):
                    cost += self.grid.get_silver_point_score(next_tile.x, next_tile.y)
                break
        return cost

    def heuristic(self, current, goal):
        print(current)
        print(goal)
        # Implement a heuristic function to estimate the distance from current to goal
        return abs(current.x - goal.x) + abs(current.y - goal.y)

    def select_tile(self, current_direction, target_directions):
        # Select the most suitable tile based on current direction and target directions
        # Choose the tile with the lowest cost that fulfills movement constraints
        available_tiles = [tile for tile in self.tiles if tile.can_move(current_direction)]
        suitable_tiles = [tile for tile in available_tiles if any(tile.can_move(direction) for direction in target_directions)]
        return min(suitable_tiles, key=lambda tile: tile.cost)

    def generate_output(self):
        # Generate the output file with chosen tiles for each move and the final score
        with open("output.txt", "w") as f:
            for tile in self.path:
                f.write(f"{tile.tile_id} ")
            f.write(f"\nFinal Score: {self.score}")

# Initialize PathFinder
pathfinder = PathFinder(grid, golden_points, silver_points, tiles)

# Find the shortest path between golden points
pathfinder.find_shortest_path()

# Generate output
pathfinder.generate_output()

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#AAAA
#A
'''class PathFinder:
    def __init__(self, grid, golden_points, silver_points, tiles):
        self.grid = grid
        self.golden_points = golden_points
        self.silver_points = silver_points
        self.tiles = tiles
        self.current_position = None
        self.current_golden_point = None
        self.path = []
        self.score = 0

    def find_shortest_path(self):
        # Initialize starting position
        self.current_position = self.golden_points[0]
        self.current_golden_point = 0

        while self.current_golden_point < len(self.golden_points) - 1:
            next_golden_point = self.golden_points[self.current_golden_point + 1]
            path_to_next_golden_point = self.find_path_to_golden_point(next_golden_point)
            self.path.extend(path_to_next_golden_point)
            self.current_golden_point += 1

    def find_path_to_golden_point(self, next_golden_point):
        # Placeholder function to find the path between current and next golden points
        # Implement your pathfinding algorithm here (e.g., A* search)
        # Consider collecting silver points along the way
        # Update self.score accordingly

        # Implement A* search algorithm to find the shortest path to the next golden point
        # Consider collecting silver points along the way to maximize the score
        start = self.current_position
        end = next_golden_point

        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == end:
                break

            for next_tile in self.grid.get_neighbors(current):
                new_cost = cost_so_far[current] + self.get_tile_cost(current, next_tile)
                if next_tile not in cost_so_far or new_cost < cost_so_far[next_tile]:
                    cost_so_far[next_tile] = new_cost
                    priority = new_cost + self.heuristic(next_tile, end)
                    frontier.put(next_tile, priority)
                    came_from[next_tile] = current

        path = []
        current = end
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()

        return path

        pass

    def select_tile(self, current_direction, target_directions):
        # Placeholder function to select the most suitable tile based on current direction and target directions
        # Implement your tile selection logic here



        pass

    def generate_output(self):
        # Placeholder function to generate the output file with chosen tiles for each move
        # Include the final score in the output

        

        pass

# Initialize PathFinder
pathfinder = PathFinder(grid, golden_points, silver_points, tiles)

# Find the shortest path between golden points
pathfinder.find_shortest_path()

# Generate output
pathfinder.generate_output()'''