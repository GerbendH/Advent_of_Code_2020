from file_loading import load_file_readlines

class Cube:
    def __init__(self, coordinates, value):
        self.coor = coordinates
        self.value = value
        self.new_value = ''
        self.nb = self.calculate_neighbours()

    def calculate_neighbours(self):
        neighbours = [[self.coor[0] + i, self.coor[1] + j, self.coor[2] + k] for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1, 0, 1) if not (i == j == k == 0)]
        return neighbours


class Grid:
    def __init__(self):
        self.cubes = []
        self.x_range = []
        self.y_range = []
        self.z_range = []

    def add_cube(self, coordinate, value):
        self.cubes.append(Cube(coordinate, value))


def conway_cubes():
    cube_file = "input.txt"
    cube_data = load_file_readlines(cube_file)

    conway_grid = Grid




    print(cube_data)

if __name__ == '__main__':
    conway_cubes()

