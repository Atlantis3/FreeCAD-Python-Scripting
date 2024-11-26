import FreeCAD as App
import Part
import FreeCADGui as Gui

# Create a new document
doc = App.newDocument("RectangleExample3")

# Add a Body to the document
body = doc.addObject('PartDesign::Body', 'Body')

# Define the rectangle dimensions
width = 10  # Width of the rectangle
height = 20  # Height of the rectangle

# Create the rectangle's wire
p1 = App.Vector(0, 0, 0)
p2 = App.Vector(width, 0, 0)
p3 = App.Vector(width, height, 0)
p4 = App.Vector(0, height, 0)

# Create the edges of the rectangle
edge1 = Part.LineSegment(p1, p2).toShape()
edge2 = Part.LineSegment(p2, p3).toShape()
edge3 = Part.LineSegment(p3, p4).toShape()
edge4 = Part.LineSegment(p4, p1).toShape()

# Create a wire from the edges
wire = Part.Wire([edge1, edge2, edge3, edge4])

# Add the wire as a sketch to the body
sketch = body.newObject('Sketcher::SketchObject', 'Sketch')
sketch.addGeometry([
    Part.LineSegment(p1, p2),
    Part.LineSegment(p2, p3),
    Part.LineSegment(p3, p4),
    Part.LineSegment(p4, p1)
])

# Extrude the wire to create a solid
extrusion_height = 5  # Height of extrusion
extrusion = doc.addObject('PartDesign::Pad', 'Pad')
extrusion.Profile = sketch
extrusion.Length = extrusion_height

# Recompute the document to apply changes
doc.recompute()

# Export to a STEP file
output_file = "/path/to/your/rectangle.step"  # Change this to your desired path
#shape = body.Shape.exportStep(output_file)

print(f"STEP file exported to: {output_file}")

# to put the pad in  the active body
App.getDocument('RectangleExample3').getObject('Body').ViewObject.dropObject(App.getDocument('RectangleExample3').getObject('Pad'),None,'',[])

# To view in GUI, uncomment below lines
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
