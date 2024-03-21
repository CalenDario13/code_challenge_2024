def read_input_file(filename):
    grid_width, grid_height, num_golden_points, num_silver_points, num_tile_types = None, None, None, None, None
    golden_points = []
    silver_points = []
    tile_types = []

    with open(filename, 'r', encoding='utf-8-sig') as file:  # specifying utf-8-sig to handle BOM
        lines = file.readlines()

        # Read the first line containing grid dimensions and point counts
        grid_dimensions = lines[0].strip().split()
        grid_width, grid_height, num_golden_points, num_silver_points, num_tile_types = map(int, grid_dimensions)

        # Read Golden Points
        for line in lines[1:num_golden_points + 1]:
            gx, gy = map(int, line.strip().split())
            golden_points.append((gx, gy))

        # Read Silver Points
        for line in lines[num_golden_points + 1:num_golden_points + num_silver_points + 1]:
            sx, sy, ssc = map(int, line.strip().split())
            silver_points.append((sx, sy, ssc))

        # Read Tile Types
        for line in lines[num_golden_points + num_silver_points + 1:]:
            tile_types.append(line.strip().split())

    return {
        'grid_width': grid_width,
        'grid_height': grid_height,
        'num_golden_points': num_golden_points,
        'num_silver_points': num_silver_points,
        'num_tile_types': num_tile_types,
        'golden_points': golden_points,
        'silver_points': silver_points,
        'tile_types': tile_types
    }
