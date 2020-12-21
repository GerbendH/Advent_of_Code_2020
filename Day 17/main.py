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
    def __init__(self, x_r, y_r, z_r):
        self.cubes = []
        self.x_range = x_r
        self.y_range = y_r
        self.z_range = z_r

    def add_cube(self, coordinate, value):
        self.cubes.append(Cube(coordinate, value))

    def expand(self):
        total_x = range(self.x_range[0], self.x_range[1])
        total_y = range(self.y_range[0], self.y_range[1])
        total_z = range(self.z_range[0], self.z_range[1])

        old_range = [[x, y, z] for x in total_x for y in total_y for z in total_z]

        self.x_range[0] -= 1
        self.y_range[0] -= 1
        self.z_range[0] -= 1
        self.x_range[1] += 1
        self.y_range[1] += 1
        self.z_range[1] += 1

        total_x = range(self.x_range[0], self.x_range[1])
        total_y = range(self.y_range[0], self.y_range[1])
        total_z = range(self.z_range[0], self.z_range[1])

        new_range = [[x, y, z] for x in total_x for y in total_y for z in total_z]

        for old in old_range:
            new_range.remove(old)

        for new in new_range:
            self.add_cube(new, '.')

        print(old_range)

    def cube_state_change(self):
        for current_cube in self.cubes:
            nb_values = []
            for other_cube in self.cubes:
                if other_cube.coor in current_cube.nb:
                    nb_values.append(other_cube.value)

            if current_cube.value == '#':
                if nb_values.count('#') == 2 or nb_values.count('#') == 3:
                    current_cube.new_value = '#'
                else:
                    current_cube.new_value = '.'

            if current_cube.value == '.':
                if nb_values.count('#') == 3:
                    current_cube.new_value = '#'
                else:
                    current_cube.new_value = '.'

    def switch_cube_state(self):
        for cube in self.cubes:
            cube.value = cube.new_value

    def run_cycles(self, nb_cycles):
        for cycle in range(0, nb_cycles):
            self.expand()
            self.cube_state_change()
            self.switch_cube_state()

    def count_active_cubes(self):
        nb_cubes = 0
        for cube in self.cubes:
            if cube.value == '#':
                nb_cubes += 1

        return nb_cubes

def handle_row(row, row_nb, grid):
    x_loc = 0
    for cube in row:
        grid.add_cube([x_loc, row_nb, 0], cube)
        x_loc += 1


def conway_cubes():
    cube_file = "input.txt"
    cube_data = load_file_readlines(cube_file)

    conway_grid = Grid([0, len(cube_data)], [0, len(cube_data[0])], [0, 1])

    row_nb = 0
    for row in cube_data:
        handle_row(row, row_nb, conway_grid,)
        row_nb += 1

    conway_grid.run_cycles(6)

    print(conway_grid.count_active_cubes())


if __name__ == '__main__':
    conway_cubes()

