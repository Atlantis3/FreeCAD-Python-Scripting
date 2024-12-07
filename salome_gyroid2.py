#------------------------------------------------------------------------------------
import sys
import salome
salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()

#=======================================================================
#============ Geometry module ==========================================
#=======================================================================
import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS
import numpy as np
geompy = geomBuilder.New()
O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )

# Dimensions for the gyroids
size = 2.0              # size of the gyroids
radius = 0.5            # radius of the arc
thickness = 0.1

# Creating the cordinate points for the gyroid structures
point1 = geompy.MakeVertex(0, 0, 0)
point2 = geompy.MakeVertex(size, 0, 0)
point3 = geompy.MakeVertex(size, 0, size)
point4 = geompy.MakeVertex(size, size, size)
point5 = geompy.MakeVertex(0, size, size)
point6 = geompy.MakeVertex(0, size, 0)


point7 = geompy.MakeVertex(size-radius, 0, size/2)
point8 = geompy.MakeVertex(size, size/2, size-radius)
point9 = geompy.MakeVertex(size/2, size-radius, size)
point10 = geompy.MakeVertex(radius, size, size/2)
point11 = geompy.MakeVertex(0, size/2, radius)
point12 = geompy.MakeVertex(size/2, radius, 0)


curve1 = geompy.MakeInterpol([point2,point7,point3], False, False)
curve2 = geompy.MakeInterpol([point3,point8,point4], False, False)
curve3 = geompy.MakeInterpol([point4,point9,point5], False, False)
curve4 = geompy.MakeInterpol([point5,point10,point6], False, False)
curve5 = geompy.MakeInterpol([point6,point11,point1], False, False)
curve6 = geompy.MakeInterpol([point1,point12,point2], False, False)


#geompy.addToStudy(curve1,'curve1')
#geompy.addToStudy(curve2,'curve2')
#geompy.addToStudy(curve3,'curve3')
#geompy.addToStudy(curve4,'curve4')
#geompy.addToStudy(curve5,'curve5')
#geompy.addToStudy(curve6,'curve6')

gyroid_single_face = geompy.MakeFaceWires([curve1, curve2, curve3, curve4, curve5, curve6], 0)
thickend_gyro = geompy.MakeThickSolid(gyroid_single_face, thickness, [])
Rotation_1 = geompy.MakeRotation(thickend_gyro, OZ, 180*math.pi/180.0)
geompy.TranslateDXDYDZ(Rotation_1, size*2, size, 0)

geompy.addToStudy(thickend_gyro,'thickned_gyro')
geompy.addToStudy(Rotation_1,'Rotation_1')

new_solid = geompy.MakeFuse(thickend_gyro,Rotation_1)
geompy.addToStudy(new_solid,'new_solid')
