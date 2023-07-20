import math
import pygame
import sys

pygame.init()

window_width = 400
window_height = 400

window = pygame.display.set_mode((window_width, window_height))

cube_vertices = [[-50, -50, 50],
                [50, -50, 50],
                [50, 50, 50],
                [-50, 50, 50],
                [-50, -50, -50],
                [50, -50, -50],
                [50, 50, -50],
                [-50, 50, -50]]

cube_edges = [(0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 4),
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7)]

cube_vertices_large = [[-100, -100, 100],
                    [100, -100, 100],
                    [100, 100, 100],
                    [-100, 100, 100],
                    [-100, -100, -100],
                    [100, -100, -100],
                    [100, 100, -100],
                    [-100, 100, -100]]

notcube_edges = []
for i in range(8):
    for j in range(i+1,8):
        if bin(i^j).count("1") == 1:
            notcube_edges.append((i,j))

for i in range(8):
    for j in range(8):
        if i != j and (i,j) not in notcube_edges:
            notcube_edges.append((i,j))

vertices = cube_vertices + cube_vertices_large
edges = cube_edges + [(i,j+8) for (i,j) in notcube_edges]

angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    rotation_matrix_x = [[1, 0, 0],
                        [0, math.cos(angle), math.sin(angle)],
                        [0, -math.sin(angle), math.cos(angle)]]

    rotation_matrix_y = [[math.cos(angle), 0, -math.sin(angle)],
                        [0, 1, 0],
                        [math.sin(angle), 0, math.cos(angle)]]

    rotated_vertices = []
    window.fill((255, 255, 255))
    for vertex in vertices:
        rotated_vertex_x = [sum([rotation_matrix_x[i][j] * vertex[j] for j in range(3)]) for i in range(3)]
        rotated_vertex_xy = [sum([rotation_matrix_y[i][j] * rotated_vertex_x[j] for j in range(3)]) for i in range(3)]
        rotated_vertices.append(rotated_vertex_xy)
        
    for edge in edges:
        pygame.draw.line(window, (0, 0, 0), 
                        (rotated_vertices[edge[0]][0] + window_width/2, 
                        rotated_vertices[edge[0]][1] + window_height/2), 
                        (rotated_vertices[edge[1]][0] + window_width/2, 
                        rotated_vertices[edge[1]][1] + window_height/2), 2)

    angle += 0.0005 # Adjust Speed

    pygame.display.update()