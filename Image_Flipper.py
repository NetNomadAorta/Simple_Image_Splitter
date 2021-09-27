import time
import os
import shutil
import cv2
import glob



# User Parameters/Constants to Set
ORIG_IMG_DIR = "Images/To_Flip_Images/"
FLIPPED_IMG_DIR = "Images/Flipped_Images/"

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}h:{1}m:{2}s".format(int(hours) ,int(mins), round(sec)))


def deleteDirContents(dir):
    # Deletes photos in path "dir"
    # # Used for deleting previous cropped photos from last run
    for f in os.listdir(dir):
        fullName = os.path.join(dir, f)
        shutil.rmtree(fullName)


# Deletes unnecessary string in file name
def replaceFileName(dir):
    # os.chdir(dir)
    for filename in glob.glob(slotDir + "/*"):
        os.rename(filename, filename.replace("Stitcher-Snaps_for_8in_Wafer_Pave.", ""))
    for filename in glob.glob(slotDir + "/*"):
        os.rename(filename, filename.replace(".p0", ""))


def makeDir(lenSlot):
    lenMain = (len(FLIPPED_IMG_DIR)-1)
    os.makedirs("./" + FLIPPED_IMG_DIR + mainOrigImgDir[0][lenMain:] \
        + "/" + slotDir[-lenSlot:], exist_ok=True)
    splitSlotDir = "./" + FLIPPED_IMG_DIR + mainOrigImgDir[0][lenMain:] \
        + "/" + slotDir[-lenSlot:]
    return splitSlotDir

# Reads image and splits it into sections and saves it
def imageFlipper(imagePath, splitSlotDir, lenName):
    image = cv2.imread(imagePath)
    flipImageX = cv2.flip(image, 1)
    flipImageY = cv2.flip(image, 0)
    flipImageXY = cv2.flip(image, -1)
    cv2.imwrite(splitSlotDir + "/" +  imagePath[-(lenName+1):], image)
    cv2.imwrite(splitSlotDir + "/" +  imagePath[-(lenName+1):-4] \
        + "-Flipped_X.jpg", flipImageX)
    cv2.imwrite(splitSlotDir + "/" +  imagePath[-(lenName+1):-4] \
        + "-Flipped_Y.jpg", flipImageY)
    cv2.imwrite(splitSlotDir + "/" +  imagePath[-(lenName+1):-4] \
        + "-Flipped_XY.jpg", flipImageXY)



# MAIN():
# =============================================================================
# Starting stopwatch to see how long process takes
start_time = time.time()

# Clears some of the screen for asthetics
print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Deletes contents in cropped- and split-image folders
deleteDirContents("./" + FLIPPED_IMG_DIR)

# Load Stitched-Image Path
# Main Stitched-Image directory
mainOrigImgDir = glob.glob(ORIG_IMG_DIR + "*")

i = 0
# Runs through each slot file within the main file within stitched-image folder
for slotDir in glob.glob(mainOrigImgDir[0] + "/*"): 
    print("Starting", slotDir, "\n")
    replaceFileName(slotDir)
    
    lenSlot = len(os.listdir(mainOrigImgDir[0])[i])
    splitSlotDir = makeDir(lenSlot)
    lenName = len(os.listdir(slotDir)[0])
    for imagePath in glob.glob(slotDir + "/*"):
        imageFlipper(imagePath, splitSlotDir, lenName)
    i += 1
        

print("Done!")

# Starting stopwatch to see how long process takes
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
