import numpy as np
# ========================================================
# ======== Geometry parameterisation =====================
# ========================================================
# 1. number of profiles in the wing
n_profiles = 5

# 2. The location of the profile from the wing root in mm
wing_section_y_cordinates = np.array([0.4005700570057006,4.435503550355036, 5.960356035603561, 6.907660766076608, 7.500220022002201])*1000.0     

# 3. The location of the profile from the wing root in mm
wing_section_x_cordinates_uf = np.array([0.7342962755033171, 0.6084542900928411, 0.48261230468236516, 0.3567703192718892, 0.23092833386141318])*1000.0   
wing_section_x_cordinates = [0]
for count,value in enumerate (wing_section_x_cordinates_uf):
    if count == 0:
        pass
    else :
        differance = wing_section_x_cordinates_uf[0]-value
        #print(value,differance)
        wing_section_x_cordinates.append(differance)
#3.1 
wing_section_chord_length = np.array([750,650,550,400,250])

# 4. location to dat file for the airfoil profile
profile_1 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing profiles 20240805/D45-1-132-15-F0-V6.csv',delimiter=',')
profile_2 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing profiles 20240805/D45-2-131-15-F0-V4.csv',delimiter=',')
profile_3 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing profiles 20240805/D45-3-129-155-F0-V2.csv',delimiter=',')
profile_4 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing profiles 20240805/D45-4-127-163-F0-V6.csv',delimiter=',')
profile_5 = np.loadtxt('/home/akram_metar/D_Drive/Akaflieg/D45 Wing Data/Wing profiles 20240805/D45-5-125-17-F0-V1.csv',delimiter=',')

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

profile_3_x_cordinates = (profile_3[:,0]*wing_section_chord_length[2])+wing_section_x_cordinates[2]
profile_3_y_cordinates = profile_3[:,1]*wing_section_chord_length[2]

profile_4_x_cordinates = (profile_4[:,0]*wing_section_chord_length[3])+wing_section_x_cordinates[3]
profile_4_y_cordinates = profile_4[:,1]*wing_section_chord_length[3]

profile_5_x_cordinates = (profile_5[:,0]*wing_section_chord_length[4])+wing_section_x_cordinates[4]
profile_5_y_cordinates = profile_5[:,1]*wing_section_chord_length[4]

# ========================================================
# ======== Geometry Creation in FreeCAD ==================
# ========================================================
import FreeCAD, Part, Draft

# Create a new document
doc = FreeCAD.newDocument()

# To change the name of the documents
doc.Label = "D45_Wing_Molds"




for count,value in enumerate (profile_1_x_cordinates):
    globals()[f'Profile_1_Point_{int(count+1)}'] = FreeCAD.Vector(profile_1_x_cordinates[count],profile_1_y_cordinates[count],wing_section_y_cordinates[0])
    #geompy.addToStudy(globals()[f'Profile_1_Point_{int(count+1)}'],'Profile_1_point_'+str(count+1))

profile_1_all_lines = []
for count in range(1,len(profile_1_x_cordinates)):

    if count == len(profile_1_x_cordinates)-1:
        globals()[f'Profile_1_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_1_Point_{int(count)}'],globals()[f'Profile_1_Point_{int(count+1)}'])
        globals()[f'Profile_1_Line_{int(count+1)}'] = Part.LineSegment(globals()[f'Profile_1_Point_{int(count+1)}'],globals()[f'Profile_1_Point_{int(1)}'])
        profile_1_all_lines.append(globals()[f'Profile_1_Line_{int(count)}'])
        profile_1_all_lines.append(globals()[f'Profile_1_Line_{int(count+1)}'])
    else:
        globals()[f'Profile_1_Line_{int(count)}'] = Part.LineSegment(globals()[f'Profile_1_Point_{int(count)}'],globals()[f'Profile_1_Point_{int(count+1)}'])
        #geompy.addToStudy(globals()[f'Line_{int(count)}'],'Line_'+str(count))
        profile_1_all_lines.append(globals()[f'Profile_1_Line_{int(count)}'])


profile_1_line = Part.Wire(profile_1_all_lines)
profile_1_face = Part.Face(profile_1_line)
extrude = profile_1_face.extrude(FreeCAD.Vector(0, 0, 5))


















