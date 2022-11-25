# class HeldGrid:
#     def __init__(self):
#         self.grid = [[None for _ in range(6)] for _ in range(6)]

#     def get_held_map(self):
#         return self.grid

#     def add_shape_to_held(self, shape) -> None:
#         for i in range(len(shape.units)):
#             self.grid[shape.units[i][0]][shape.units[i][1]] = 3

#     def render(self):
#         for row in range(len(self.grid)):
#             for col in range(len(self.grid[row])):
#                 if self.grid[row][col] != None:
#                     print('U', end=' ')
#                 else:
#                     print('-', end=' ')
#             print()


# class Shape:
#     def __init__(self):
#         self.units = [
#             (2, 1),
#             (2, 2),
#             (2, 3),
#             (3, 2)
#         ]


# shape = Shape()
# held_grid = HeldGrid()

# held_grid.add_shape_to_held(shape)
# held_grid.render()


grid = [[None for _ in range(10)] for _ in range(10)]

grid[0][3] = 3
