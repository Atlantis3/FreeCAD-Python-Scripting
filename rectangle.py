import FreeCAD, Part, Draft

# Create a new document
doc = FreeCAD.newDocument()

# Step 1: Create four points
point1 = FreeCAD.Vector(0, 0, 0)
point2 = FreeCAD.Vector(2, 0, 0)
point3 = FreeCAD.Vector(2, 2, 0)
point4 = FreeCAD.Vector(0, 3, 0)

# Step 2: Create lines between the points
line1 = Part.LineSegment(point1, point2)
line2 = Part.LineSegment(point2, point3)
line3 = Part.LineSegment(point3, point4)
line4 = Part.LineSegment(point4, point1)

# Combine lines into an edge list
edges = [line1.toShape(), line2.toShape(), line3.toShape(), line4.toShape()]

# Step 3: Create a face from the edges
wire = Part.Wire(edges)
face = Part.Face(wire)

# Step 4: Extrude the face to create a 3D shape
extrude = face.extrude(FreeCAD.Vector(0, 0, 5))  # Extrude along Z-axis by 10 units

# Add the extruded shape to the document
doc.addObject("Part::Feature", "Extrusion").Shape = extrude

# Step 5: Publish to a study (assuming you're using a FreeCAD project with an analysis workbench)
# In this case, we'll just create a simple object and link it to a study.
# Note: FreeCAD's FEM module can be used for studies, but it requires specific setup.

# Publish the object to the study (this is just an example as studies setup require more context)
# Assuming you have already created a study in your FreeCAD project.
# You can set the object in the FEM study like this (in case of FEM module):

# study = FreeCAD.ActiveDocument.getObject("Study")
# study.addObject(doc.getObject("Extrusion"))

# Recompute the document to apply changes
doc.recompute()


