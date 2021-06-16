# subscribe to my youtube
# https://www.youtube.com/c/Auctux

import sys
import pygame
from constants import *
from event import HandleEvent
from utils.transform import *
from utils.vector import Vector3
from utils.camera import Camera
from utils.light import Light
from utils.mesh.base import Mesh
from utils.mesh.meshes import *
from utils.mesh.spheres import *
from utils.mesh.point import *
from utils.matrix import *
from utils.tools import *
from utils.world import Scene
from math import pi

screen = pygame.display.set_mode(Size)
clock = pygame.time.Clock()
fps = 60

#mouse setup
pygame.mouse.get_rel()
pygame.mouse.set_visible(True)
a = pygame.event.set_grab(False)

Deer = Mesh()
Deer.triangles = LoadMesh("./assets/deer.obj",(186, 135, 89))

cube = Mesh()
cube.triangles = CubeTriangles(blue)
cube.position = Vector3(0, 1.6, 0)

sphere = Mesh()
sphere.triangles = IcosphereTriangles(orange, 2)
sphere.position = Vector3(0, -1.6, 0)
# sphere2 = Mesh()
# sphere2.triangles = SphereTriangles((255, 255, 255), 20)

scene = Scene()
#add object into the world
scene.world.append(sphere)
scene.world.append(cube)


#camera setup
camera = Camera(Vector3(0, 2, 0),0.1, 1000.0, 70.0)
camera.speed = 0.5
camera.rotationSpeed = 0.8

#light setup
light = Light(Vector3(0.9, 0.9, -1))

angle = 0

moveLight = True

run = True
while run:
    screen.fill(BackgroundColor)
    clock.tick(fps)
    dt = clock.tick(fps)/100
    frameRate = clock.get_fps()
    pygame.display.set_caption(str(frameRate) + " fps")
    camera.HandleInput(dt)
    run = HandleEvent(camera, dt)


    if moveLight == True and light != None:
        mx, my = pygame.mouse.get_pos()
        _x = translateValue( mx, 0,  Width,  -1,  1)
        _y = translateValue( my, 0, Height, -1, 1)
        light = Light(Vector3(-_x, -_y, -1))


    sphere.transform = multiplyMatrix(RotationY(angle), ScalingMatrix(1.5))
    cube.transform = multiplyMatrix(RotationY(-angle), ScalingMatrix(1.2))

    # display scene
    scene.update(dt = dt, camera=camera, light=light, screen=screen,
                fill=True, wireframe=False, vertices=False, depth=True,
                showNormals=False, radius=8, verticeColor=False, wireframeColor=(0, 223,255))

    #p.position.x += angle/10
    pygame.display.flip()
    angle += 0.01

pygame.quit()
sys.exit()
