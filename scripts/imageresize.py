import argparse
import cv2
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input')
parser.add_argument('-o', '--output')
args = parser.parse_args()

inputFiles = glob.glob(args.input + '/*.png')
for p in inputFiles:
    filename = os.path.basename(p)
    print filename
    inputImage = cv2.imread(p)
    '''
    croppedHeight = 900
    croppedWidth = int(float(croppedHeight) * 1280 / 800)
    xOffset = (inputImage.shape[1] - croppedWidth) / 2
    cropped = inputImage[:croppedHeight, xOffset:xOffset+croppedWidth]
    resized = cv2.resize(cropped, (700, int(float(700) * 800 / 1280)))
    '''
    resized = cv2.resize(inputImage, (700, int(float(700) * 800 / 1280)))
    cv2.imwrite(args.output + "/" + filename, resized)
    