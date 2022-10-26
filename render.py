import pygame
from utils import *
from polygon import Polygon
import numpy as np


def Render(polygons, display, theta, setting, animation=0, stereo=True, showSphere=True, showStereo=True, showlines=True, showvertices=True):
    for polygon in polygons:
        previous_vertex = None
        previous_projection = None
        for index, vertex in enumerate(polygon.vertices):
            vertex = np.matmul(yRot(theta), vertex.ToMatrix())
            # vertex = np.matmul(yRot(theta), vertex)
            vertex = MatrixToVertex(vertex)

            sphere_scale = 200
            v = vertex.translatetoScreen(-1, 1, 0, sphere_scale)
            # add screen offsets
            x = v.x + setting.width // 2 - sphere_scale//2
            y = v.y + setting.height // 2 - sphere_scale//2

            # Stereographic projection
            projected_scale = sphere_scale//2

            stereo_projection = StereographicProjection(
                None, None, vertex, projected_scale)
            s_x = stereo_projection[0] + setting.width//2
            s_y = stereo_projection[1] + setting.height//2

            if previous_vertex and showSphere and showlines:
                
                if index % 2:
                    pygame.draw.line(display, setting.blue,
                                    (x, y), previous_vertex, 2)
                else:
                    pygame.draw.line(display, setting.yellow,
                                    (x, y), previous_vertex, 2)

            if previous_projection and showStereo and showlines:
                
                if index % 2 == 0:
                    pygame.draw.line(display, setting.blue,
                                    (s_x, s_y), previous_projection, 1)
                else:
                    pygame.draw.line(display, setting.yellow,
                                     (s_x, s_y), previous_projection, 1)
            previous_vertex = (x, y)
            previous_projection = (s_x, s_y)

            # draw projected vertices
            if showStereo and showvertices:
                pygame.draw.circle(display, setting.white, (s_x, s_y), 1)
            # draw vertices
            if showSphere and showvertices:
                pygame.draw.circle(display, setting.white, (x, y), 1)
