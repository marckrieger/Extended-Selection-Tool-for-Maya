import pymel.core as pm
import maya.cmds as cmds
import math

def addSelection(self):
    directionX = cmds.floatFieldGrp(inputDirection, query=True, value1=True)
    directionY = cmds.floatFieldGrp(inputDirection, query=True, value2=True)
    directionZ = cmds.floatFieldGrp(inputDirection, query=True, value3=True)
    direction = [directionX, directionY, directionZ]
    spreadAngle = cmds.floatSliderGrp(inputAngle, query=True, value=True)

    selectedObject = pm.ls(sl=True)[0]

    faceNormalsInfo = pm.polyInfo(fn=True)

    faceNormalsStr = str(faceNormalsInfo).replace('FACE_NORMAL', '').replace(': ', "':'").replace('[', '').replace(']', '').replace('\\n', '')        
    faceNormalsDic = eval('{' + faceNormalsStr + '}')

    faceNormalsDicKeys = list(faceNormalsDic.keys())
    faceNormalsDicValues = list(faceNormalsDic.values())

    def find_indices():
        indices = []
        for idx, value in enumerate(faceNormalsDicValues):

            valueList = [float(x) for x in value.split()]
            
            # Calculate the dot product
            dotProduct = sum([direction[i] * valueList[i] for i in range(len(direction))])

            # Calculate the magnitude of the vectors
            directionLength = math.sqrt(sum([direction[i]**2 for i in range(len(direction))]))
            valueListLength = math.sqrt(sum([valueList[i]**2 for i in range(len(valueList))]))

            # Calculate the angle in radians
            angleVariationRad = math.acos(dotProduct / (directionLength * valueListLength))

            # Convert the angle to degrees
            angleVariation = math.degrees(angleVariationRad)

            if(angleVariation <= spreadAngle):
                indices.append(idx)
        return indices

    matchingFaces = find_indices()

    for x in matchingFaces:
        pm.select(selectedObject + '.f[' + str(x) + ']', add=True)        

window = "estWindow"
title = "Extended Selection Tool"
size = (400, 200)
        
# close old window is open
if cmds.window(window, exists = True):
    cmds.deleteUI(window, window=True)
    
# create new window
window = cmds.window(window, title=title, widthHeight=size)

cmds.columnLayout(adjustableColumn = True)
cmds.separator(height=20)
cmds.text('Select by normals')
cmds.separator(height=20)
inputDirection = cmds.floatFieldGrp(label='Direction', numberOfFields=3, value2=1.0)
inputAngle = cmds.floatSliderGrp(field=True, label='Spread Angle', minValue=0, maxValue=180, value=90)
cmds.separator(height=20)
# cmds.button(label='Select', command=select)
cmds.button(label='Add Selection', command=addSelection)

# display new window
cmds.showWindow()