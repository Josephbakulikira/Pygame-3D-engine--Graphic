from utils.mesh.base import Mesh
from utils.triangle import Triangle
from utils.vector import Vector3, Vector2
from math import sin, cos, pi

def translate(value, min1, max1, min2, max2):
    return min2 + (max2 - min2) * ((value-min1)/(max1-min1))

def CubeTriangles(color):
    return [
    Triangle( Vector3(-1.0, -1.0, -1.0,), Vector3(-1.0, 1.0, -1.0), Vector3(1.0, 1.0, -1.0), color),
    Triangle( Vector3(-1.0, -1.0, -1.0,), Vector3(1.0, 1.0, -1.0), Vector3(1.0, -1.0, -1.0), color),

    Triangle( Vector3(1.0, -1.0, -1.0), Vector3(1.0, 1.0, -1.0), Vector3(1.0, 1.0, 1.0), color),
    Triangle( Vector3(1.0, -1.0, -1.0), Vector3(1.0, 1.0, 1.0), Vector3(1.0, -1.0, 1.0), color),

    Triangle( Vector3(1.0, -1.0, 1.0), Vector3(1.0, 1.0, 1.0), Vector3(-1.0, 1.0, 1.0), color),
    Triangle( Vector3(1.0, -1.0, 1.0), Vector3(-1.0, 1.0, 1.0), Vector3(-1.0, -1.0, 1.0), color),

    Triangle( Vector3(-1.0, -1.0, 1.0), Vector3(-1.0, 1.0, 1.0), Vector3(-1.0, 1.0, -1.0), color),
    Triangle( Vector3(-1.0, -1.0, 1.0), Vector3(-1.0, 1.0, -1.0), Vector3(-1.0, -1.0, -1.0), color),

    Triangle( Vector3(-1.0, 1.0, -1.0), Vector3(-1.0, 1.0, 1.0), Vector3(1.0, 1.0, 1.0), color),
    Triangle( Vector3(-1.0, 1.0, -1.0), Vector3(1.0, 1.0, 1.0), Vector3(1.0, 1.0, -1.0), color),

    Triangle( Vector3(1.0, -1.0, 1.0), Vector3(-1.0, -1.0, 1.0), Vector3(-1.0, -1.0, -1.0), color),
    Triangle( Vector3(1.0, -1.0, 1.0), Vector3(-1.0, -1.0, -1.0), Vector3(1.0, -1.0, -1.0), color),
]

def SphereTriangles(color,n_subdivision=10, radius=1):
    #simple UV SPHERE

    meshData = []
    vertices  = []
    #adding top vertex
    vertices.append(Vector3(0, radius, 0))
    #generate vertices of the sphere
    for i in range(n_subdivision):
        phi = pi * (i+1) / n_subdivision
        for j in range(n_subdivision):
            theta = 2 * pi * j / n_subdivision
            x = radius * sin(phi) * cos(theta)
            y = radius * cos(phi)
            z = radius * sin(phi) * sin(theta)
            vertices.append(Vector3(x, y, z))
    #add bottom vertex
    vertices.append(Vector3(0, -radius, 0))

    #add top and bottom triangles
    for i in range(n_subdivision):
        i0 = i + 1
        i1 = (i+1) % n_subdivision + 1
        meshData.append(Triangle(vertices[0], vertices[i1], vertices[i0], color) )
        i0 = i + n_subdivision * (n_subdivision - 2) + 1
        i1 = (i+1) % n_subdivision + n_subdivision * (n_subdivision - 2) + 1
        meshData.append( Triangle(vertices[-1], vertices[i1], vertices[i0], color) )

    for j in range(n_subdivision-2):
        j0 = j * n_subdivision + 1
        j1 = (j+1) * n_subdivision + 1
        for i in range(n_subdivision):
            i0 = j0 + i
            i1 = j0 + (i + 1) % n_subdivision
            i2 = j1 + (i + 1) % n_subdivision
            i3 = j1 + i
            meshData.append( Triangle(vertices[i0], vertices[i1], vertices[i2], color))
            meshData.append( Triangle(vertices[i0], vertices[i2], vertices[i3], color))

    return meshData


def PlaneTriangles(color, resolution):
    print("df")
