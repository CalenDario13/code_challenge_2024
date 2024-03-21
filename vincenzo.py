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
print("Silver Points:")
for point in silver_points:
    print("(", point.x, ",", point.y, ") Score:", point.score)
print("Tiles:")
for tile in tiles:
    print("Tile ID:", tile.tile_id, "Cost:", tile.cost, "Quantity:", tile.quantity, "Directions:", tile.directions)
