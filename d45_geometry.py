import FreeCAD
import numpy as np
# ========================================================
# ======== Geometry parameterisation =====================
# ========================================================
# 1. number of profiles in the wing
n_profiles = 6

# 2. The distance of the profile from the centreline of the fuselage in the direction of the wing tip in mm
wing_section_y_cordinates = np.array([0.35,2.1774,4.5496,6.0039,6.948,7.5])*-1000.0     

# 3. The distance of the profile leading edge from the wing root in the direction of the tariling edge in mm
wing_section_x_cordinates = np.array([0.0,0.014025,0.10489,0.214318,0.3234744,0.430468])*1000.0   
'''
wing_section_x_cordinates = [0]
for count,value in enumerate (wing_section_x_cordinates_uf):
    if count == 0:
        pass
    else :
        differance = wing_section_x_cordinates_uf[0]-value
        #print(value,differance)
        wing_section_x_cordinates.append(differance)
'''
#3.1 The length of the chordline of the profile in mm
wing_section_chord_length = np.array([0.7319,0.7154,0.6085,0.4826,0.3568,0.2309])*1000.0

# 4. location to dat file for the airfoil profile for 0 degree flap position
profile_1 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing Profiles 20241207/D45-1-132-15-F0.csv',delimiter=',')
profile_2 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing Profiles 20241207/D45-2-132-15-F0.csv',delimiter=',')
profile_3 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing Profiles 20241207/D45-3-131-15-F0.csv',delimiter=',')
profile_4 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing Profiles 20241207/D45-4-129-155-F0.csv',delimiter=',')
profile_5 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing Profiles 20241207/D45-5-127-163-F0.csv',delimiter=',')
profile_6 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing Profiles 20241207/D45-6-125-17-F0.csv',delimiter=',')


'''
# 4. location to dat file for the airfoil profile for 20 degree flap position
profile_1 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing Profiles 20241207/D45-1-132-15-F20.csv',delimiter=',')
profile_2 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing Profiles 20241207/D45-2-132-15-F20.csv',delimiter=',')
profile_3 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing Profiles 20241207/D45-3-131-15-F20.csv',delimiter=',')
profile_4 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing Profiles 20241207/D45-4-129-155-F20.csv',delimiter=',')
profile_5 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing Profiles 20241207/D45-5-127-163-F20.csv',delimiter=',')
profile_6 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing Profiles 20241207/D45-6-125-17-F20.csv',delimiter=',')
'''





#------------------------------------------------------------------------------------
# Pre calculations for the preparation of the CAD Model

# check if the input data is correct
if len(wing_section_y_cordinates) != n_profiles :
    raise Exception('The number of profiles and the locations for it in the y-direction do not match, Please check the input data !')
elif len(wing_section_x_cordinates) != n_profiles:
    raise Exception('The number of profiles and the locations for it in the  x-direction do not match. Please check the input data !')

profile_1_x_cordinates = (profile_1[:,0]*wing_section_chord_length[0])+wing_section_x_cordinates[0]
profile_1_y_cordinates = profile_1[:,1]*wing_section_chord_length[0]

profile_2_x_cordinates = (profile_2[:,0]*wing_section_chord_length[1])+wing_section_x_cordinates[1]
profile_2_y_cordinates = profile_2[:,1]*wing_section_chord_length[1]
#profile_2_y_cordinates = (profile_2[:,1]*wing_section_chord_length[1])+0.2

profile_3_x_cordinates = (profile_3[:,0]*wing_section_chord_length[2])+wing_section_x_cordinates[2]
profile_3_y_cordinates = (profile_3[:,1]*wing_section_chord_length[2])
#profile_3_y_cordinates = (profile_3[:,1]*wing_section_chord_length[2])-0.2

profile_4_x_cordinates = (profile_4[:,0]*wing_section_chord_length[3])+wing_section_x_cordinates[3]
profile_4_y_cordinates = profile_4[:,1]*wing_section_chord_length[3]

profile_5_x_cordinates = (profile_5[:,0]*wing_section_chord_length[4])+wing_section_x_cordinates[4]
profile_5_y_cordinates = profile_5[:,1]*wing_section_chord_length[4]

profile_6_x_cordinates = (profile_6[:,0]*wing_section_chord_length[5])+wing_section_x_cordinates[5]
profile_6_y_cordinates = profile_6[:,1]*wing_section_chord_length[5]


# ========================================================
# ======== Geometry Creation in FreeCAD ==================
# ========================================================
import FreeCAD, Part, Draft

# Create a new document
doc = FreeCAD.newDocument('D45_Wing_Design')

# create the points for the profile 1
for count,value in enumerate (profile_1_x_cordinates):
    globals()[f'Profile_1_Point_{int(count+1)}'] = FreeCAD.Vector(profile_1_x_cordinates[count],profile_1_y_cordinates[count],wing_section_y_cordinates[0])

profile_1_all_lines = []
for count in range(1,len(profile_1_x_cordinates)):

    if count == len(profile_1_x_cordinates)-1:
        globals()[f'Profile_1_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_1_Point_{int(count)}'],globals()[f'Profile_1_Point_{int(count+1)}'])
        globals()[f'Profile_1_Line_{int(count+1)}'] = Part.LineSegment(globals()[f'Profile_1_Point_{int(count+1)}'],globals()[f'Profile_1_Point_{int(1)}'])
        profile_1_all_lines.append(globals()[f'Profile_1_Line_{int(count)}'].toShape())
        profile_1_all_lines.append(globals()[f'Profile_1_Line_{int(count+1)}'].toShape())
    else:
        globals()[f'Profile_1_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_1_Point_{int(count)}'],globals()[f'Profile_1_Point_{int(count+1)}'])
        #geompy.addToStudy(globals()[f'Line_{int(count)}'],'Line_'+str(count))
        profile_1_all_lines.append(globals()[f'Profile_1_Line_{int(count)}'].toShape())


profile_1_line = Part.Wire(profile_1_all_lines)
profile_1_face = Part.Face(profile_1_line)
Part.show(profile_1_face,'profile_1_face')

# create the points for the profile 2
for count,value in enumerate (profile_2_x_cordinates):
    globals()[f'Profile_2_Point_{int(count+1)}'] = FreeCAD.Vector(profile_2_x_cordinates[count],profile_2_y_cordinates[count],wing_section_y_cordinates[1])

profile_2_all_lines = []
for count in range(1,len(profile_2_x_cordinates)):

    if count == len(profile_2_x_cordinates)-1:
        globals()[f'Profile_2_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_2_Point_{int(count)}'],globals()[f'Profile_2_Point_{int(count+1)}'])
        globals()[f'Profile_2_Line_{int(count+1)}'] = Part.LineSegment(globals()[f'Profile_2_Point_{int(count+1)}'],globals()[f'Profile_2_Point_{int(1)}'])
        profile_2_all_lines.append(globals()[f'Profile_2_Line_{int(count)}'].toShape())
        profile_2_all_lines.append(globals()[f'Profile_2_Line_{int(count+1)}'].toShape())
    else:
        globals()[f'Profile_2_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_2_Point_{int(count)}'],globals()[f'Profile_2_Point_{int(count+1)}'])
        #geompy.addToStudy(globals()[f'Line_{int(count)}'],'Line_'+str(count))
        profile_2_all_lines.append(globals()[f'Profile_2_Line_{int(count)}'].toShape())


profile_2_line = Part.Wire(profile_2_all_lines)
profile_2_face = Part.Face(profile_2_line)
Part.show(profile_2_face,'profile_2_face')

# create the points for the profile 3
for count,value in enumerate (profile_3_x_cordinates):
    globals()[f'Profile_3_Point_{int(count+1)}'] = FreeCAD.Vector(profile_3_x_cordinates[count],profile_3_y_cordinates[count],wing_section_y_cordinates[2])

profile_3_all_lines = []
for count in range(1,len(profile_3_x_cordinates)):

    if count == len(profile_3_x_cordinates)-1:
        globals()[f'Profile_3_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_3_Point_{int(count)}'],globals()[f'Profile_3_Point_{int(count+1)}'])
        globals()[f'Profile_3_Line_{int(count+1)}'] = Part.LineSegment(globals()[f'Profile_3_Point_{int(count+1)}'],globals()[f'Profile_3_Point_{int(1)}'])
        profile_3_all_lines.append(globals()[f'Profile_3_Line_{int(count)}'].toShape())
        profile_3_all_lines.append(globals()[f'Profile_3_Line_{int(count+1)}'].toShape())
    else:
        globals()[f'Profile_3_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_3_Point_{int(count)}'],globals()[f'Profile_3_Point_{int(count+1)}'])
        #geompy.addToStudy(globals()[f'Line_{int(count)}'],'Line_'+str(count))
        profile_3_all_lines.append(globals()[f'Profile_3_Line_{int(count)}'].toShape())


profile_3_line = Part.Wire(profile_3_all_lines)
profile_3_face = Part.Face(profile_3_line)
Part.show(profile_3_face,'profile_3_face')





# create the points for the profile 4
for count,value in enumerate (profile_4_x_cordinates):
    globals()[f'Profile_4_Point_{int(count+1)}'] = FreeCAD.Vector(profile_4_x_cordinates[count],profile_4_y_cordinates[count],wing_section_y_cordinates[3])

profile_4_all_lines = []
for count in range(1,len(profile_4_x_cordinates)):

    if count == len(profile_4_x_cordinates)-1:
        globals()[f'Profile_4_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_4_Point_{int(count)}'],globals()[f'Profile_4_Point_{int(count+1)}'])
        globals()[f'Profile_4_Line_{int(count+1)}'] = Part.LineSegment(globals()[f'Profile_4_Point_{int(count+1)}'],globals()[f'Profile_4_Point_{int(1)}'])
        profile_4_all_lines.append(globals()[f'Profile_4_Line_{int(count)}'].toShape())
        profile_4_all_lines.append(globals()[f'Profile_4_Line_{int(count+1)}'].toShape())
    else:
        globals()[f'Profile_4_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_4_Point_{int(count)}'],globals()[f'Profile_4_Point_{int(count+1)}'])
        #geompy.addToStudy(globals()[f'Line_{int(count)}'],'Line_'+str(count))
        profile_4_all_lines.append(globals()[f'Profile_4_Line_{int(count)}'].toShape())


profile_4_line = Part.Wire(profile_4_all_lines)
profile_4_face = Part.Face(profile_4_line)
Part.show(profile_4_face,'profile_4_face')



# create the points for the profile 5
for count,value in enumerate (profile_5_x_cordinates):
    globals()[f'Profile_5_Point_{int(count+1)}'] = FreeCAD.Vector(profile_5_x_cordinates[count],profile_5_y_cordinates[count],wing_section_y_cordinates[4])

profile_5_all_lines = []
for count in range(1,len(profile_5_x_cordinates)):

    if count == len(profile_5_x_cordinates)-1:
        globals()[f'Profile_5_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_5_Point_{int(count)}'],globals()[f'Profile_5_Point_{int(count+1)}'])
        globals()[f'Profile_5_Line_{int(count+1)}'] = Part.LineSegment(globals()[f'Profile_5_Point_{int(count+1)}'],globals()[f'Profile_5_Point_{int(1)}'])
        profile_5_all_lines.append(globals()[f'Profile_5_Line_{int(count)}'].toShape())
        profile_5_all_lines.append(globals()[f'Profile_5_Line_{int(count+1)}'].toShape())
    else:
        globals()[f'Profile_5_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_5_Point_{int(count)}'],globals()[f'Profile_5_Point_{int(count+1)}'])
        #geompy.addToStudy(globals()[f'Line_{int(count)}'],'Line_'+str(count))
        profile_5_all_lines.append(globals()[f'Profile_5_Line_{int(count)}'].toShape())


profile_5_line = Part.Wire(profile_5_all_lines)
profile_5_face = Part.Face(profile_5_line)
Part.show(profile_5_face,'profile_5_face')

# create the points for the profile 6
for count,value in enumerate (profile_6_x_cordinates):
    globals()[f'Profile_6_Point_{int(count+1)}'] = FreeCAD.Vector(profile_6_x_cordinates[count],profile_6_y_cordinates[count],wing_section_y_cordinates[5])

profile_6_all_lines = []
for count in range(1,len(profile_6_x_cordinates)):

    if count == len(profile_6_x_cordinates)-1:
        globals()[f'Profile_6_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_6_Point_{int(count)}'],globals()[f'Profile_6_Point_{int(count+1)}'])
        globals()[f'Profile_6_Line_{int(count+1)}'] = Part.LineSegment(globals()[f'Profile_6_Point_{int(count+1)}'],globals()[f'Profile_6_Point_{int(1)}'])
        profile_6_all_lines.append(globals()[f'Profile_6_Line_{int(count)}'].toShape())
        profile_6_all_lines.append(globals()[f'Profile_6_Line_{int(count+1)}'].toShape())
    else:
        globals()[f'Profile_6_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_6_Point_{int(count)}'],globals()[f'Profile_6_Point_{int(count+1)}'])
        #geompy.addToStudy(globals()[f'Line_{int(count)}'],'Line_'+str(count))
        profile_6_all_lines.append(globals()[f'Profile_6_Line_{int(count)}'].toShape())


profile_6_line = Part.Wire(profile_6_all_lines)
profile_6_face = Part.Face(profile_6_line)
Part.show(profile_6_face,'profile_6_face')





wing1 = Part.makeLoft([profile_1_face,profile_2_face],solid=True)
Part.show(wing1,'wing1')

wing2 = Part.makeLoft([profile_2_face,profile_3_face],solid=True)
Part.show(wing2,'wing2')

wing3 = Part.makeLoft([profile_3_face,profile_4_face],solid=True)
Part.show(wing3,'wing3')


wing4 = Part.makeLoft([profile_4_face,profile_5_face],solid=True)
Part.show(wing4,'wing4')


wing5 = Part.makeLoft([profile_5_face,profile_6_face],solid=True)
Part.show(wing5,'wing5')

















Gui.ActiveDocument.ActiveView.setAxisCross(True)
Gui.SendMsgToActiveView("ViewFit")