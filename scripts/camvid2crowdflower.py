def rgbToBgr(rgb):
    return (rgb[2], rgb[1], rgb[0])


labelMap = {"Animal" : "Obstacle",
            "Archway" : "Obstacle",
            "Bicyclist" : "Bike",
            "Bike" : "Bike",
            "Bridge" : "Background",
            "Building" : "Background",
            "Car" : "Vehicle",
            "CartLuggagePram" : "Obstacle",
            "Child" : "Pedestrian",
            "Column_Pole" : "Obstacle",
            "Fence" : "Obstacle",
            "LaneMkgsDriv" : "Road Marking",
            "LaneMkgsNonDriv" : "Road Marking",
            "Misc_Text" : "Background",
            "MotorcycleScooter" : "Vehicle",
            "OtherMoving" : "Obstacle",
            "ParkingBlock" : "Road",
            "Pedestrian" : "Pedestrian",
            "Road" : "Road",
            "RoadShoulder" : "Background",
            "Sidewalk" : "Background",
            "SignSymbol" : "Obstacle",
            "Sky" : "Background",
            "SUVPickupTruck" : "Vehicle",
            "TrafficCone" : "Obstacle",
            "TrafficLight" : "Obstacle",
            "Train" : "Vehicle",
            "Tree" : "Background",
            "Truck_Bus" : "Vehicle",
            "Tunnel" : "Road",
            "VegetationMisc" : "Background",
            "Void" : "Background",
            "Wall" : "Background",
            }

camvidColorMap = dict()

with open('/home/jpu/hackweek/camvid-labels.txt') as f:
     for line in f:
        line = line.strip()
        tokens = line.split()
        color = tuple(int(x) for x in tokens[:3])
        camvidColorMap[tokens[3]] = color

import json
with open('/home/jpu/hackweek/crowdflower.txt') as f:
    data = json.load(f)

crowdflowerColorMap = dict()
for k, v in data.iteritems():
    hexValue = v["color"].lstrip('#')
    rgb = tuple(int(hexValue[i:i+2], 16) for i in (0, 2 ,4))
    crowdflowerColorMap[k] = rgb
print crowdflowerColorMap

c2cMap = dict()
for k in camvidColorMap:
    c2cMap[rgbToBgr(camvidColorMap[k])] = rgbToBgr(crowdflowerColorMap[labelMap[k]])

print c2cMap

import cv2
import glob
import numpy as np 
import os

inputFiles = glob.glob('/home/jpu/hackweek/gta-data/02_camvid_labels/*.png')
for p in inputFiles:
    filename = os.path.basename(p)
    print filename
    inputImage = cv2.imread(p)
    unique_colors = set(tuple(v) for m2d in inputImage for v in m2d)

    outputImage = np.zeros(inputImage.shape, dtype="uint8")
    for color in unique_colors:
        if not color in c2cMap:
            print color
        else:
            outputImage[np.where((inputImage==color).all(axis=2))] = c2cMap[color]
    cv2.imwrite('/home/jpu/hackweek/gta-data/02_cf_labels/' + filename, outputImage)

