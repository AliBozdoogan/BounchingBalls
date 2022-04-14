import pygame
from math import *

SIZE = 800  # for windows size
SPEED = 0.02  # for rotate speed
window = pygame.display.set_mode((SIZE, SIZE))  # create window
clock = pygame.time.Clock()  # for time

projection_matrix = [[1, 0, 0],  # we have to use projection matrix to create something in 3D
                     [0, 1, 0],
                     [0, 0, 0]]  # this is constant

cube_points = []  # this is for locations of balls
cube_points[0] = [[-1], [-1], [1]]
cube_points[1] = [[1], [-1], [1]]
cube_points[2] = [[1], [1], [1]]
cube_points[3] = [[-1], [1], [1]]


def multiply_matrix(x, y):  # it define to matrix multiplication with manuel
    x_rows = len(x)  # to get how many row
    x_cols = len(x[0])  # to get how many coloumns

    y_rows = len(y)  # to get how many row
    y_cols = len(y[0])  # to get how many coloumns

    product = [[0 for _ in range(y_cols)] for _ in range(x_rows)]  # Dot product matrix dimentions = x_rows x y_cols

    if x_cols == y_rows:  # to matrix multiplicaton first matrix coloums and second matrix rows should be equal in math
        for a in range(x_rows):
            for b in range(y_cols):
                for c in range(y_rows):
                    product[a][b] += a[a][c] * b[c][b]  # dot product when equal row and col in matrix
    return product


angle_x = angle_y = angle_z = 0  # when rotate balls we have to define angle
while True:
    clock.tick(60)
    window.fill((0, 0, 0))
    rotation_x = [[1, 0, 0],
                  [0, cos(angle_x), -sin(angle_x)],
                  [0, sin(angle_x), cos(angle_x)]]  # these are rotation matrixs, they are constant always

    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                  [0, 1, 0],
                  [-sin(angle_y), 0, cos(angle_y)]]

    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                  [sin(angle_z), cos(angle_z), 0],
                  [0, 0, 1]]

    points = [0 for _ in range(len(cube_points))]  # to get how many balls

    for point in cube_points:
        rotate_x = multiply_matrix(rotation_x, point)  # rotate to x direction
        rotate_y = multiply_matrix(rotation_y, rotate_x)  # rotate to y direction
        rotate_z = multiply_matrix(rotation_z, rotate_y)  # rotate to z direction
        point_2d = multiply_matrix(projection_matrix,
                              rotate_z)  # to create z plane, we have to dot product projection matrix with rotate_z

    pygame.display.update()