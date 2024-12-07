# creating the surface geometry for the in freecad

import FreeCAD as App
import Part

# Dimensions for the gyroids
size = 2.0              # size of the gyroids
radius = 0.5            # radius of the arc
thickness = 0.1


# Creating the cordinate points for the gyroid structures
point1 = App.Vector(0, 0, 0)
point2 = App.Vector(size, 0, 0)
point3 = App.Vector(size, 0, size)
point4 = App.Vector(size, size, size)
point5 = App.Vector(0, size, size)
point6 = App.Vector(0, size, 0)


point7 = App.Vector(size-radius, 0, size/2)
point8 = App.Vector(size, size/2, size-radius)
point9 = App.Vector(size/2, size-radius, size)
point10 = App.Vector(radius, size, size/2)
point11 = App.Vector(0, size/2, radius)
point12 = App.Vector(size/2, radius, 0)

curve1 = Part.Arc(point2,point7,point3)
curve2 = Part.Arc(point3,point8,point4)
curve3 = Part.Arc(point4,point9,point5)
curve4 = Part.Arc(point5,point10,point6)
curve5 = Part.Arc(point6,point11,point1)
curve6 = Part.Arc(point1,point12,point2)

# make the wire and create the face show it
wire1 = Part.Wire([curve1.toShape(),curve2.toShape(),curve3.toShape(),curve4.toShape(),curve5.toShape(),curve6.toShape()])
Part.show(wire1)
face1 = Part.makeFilledFace(wire1.Edges)
Part.show(face1)

# thickened the surface


