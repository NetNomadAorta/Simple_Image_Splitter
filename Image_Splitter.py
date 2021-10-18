import time
import os
import shutil
import cv2
import glob



# User Parameters/Constants to Set
ORIG_IMG_DIR = "Images/Original_Images/"
SPLIT_IMG_DIR = "Images/Splitted_Images/"
SPLIT_COUNT = 10 # Number of rows and columns each image gets split into

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
        os.rename(filename, filename.replace("Window_Die1_Pave.", ""))
    for filename in glob.glob(slotDir + "/*"):
        os.rename(filename, filename.replace(".p0", ""))

def makeDir(lenSlot):
    lenMain = (len(SPLIT_IMG_DIR)-1)
    os.makedirs("./" + SPLIT_IMG_DIR + mainOrigImgDir[0][lenMain:] \
        + "/" + slotDir[-lenSlot:], exist_ok=True)
    splitSlotDir = "./" + SPLIT_IMG_DIR + mainOrigImgDir[0][lenMain:] \
        + "/" + slotDir[-lenSlot:]
    return splitSlotDir

# Reads image and splits it into sections and saves it
def imageSplitter(imagePath, splitSlotDir, lenName):
    image = cv2.imread(imagePath)
    lenY = image.shape[0]
    lenX = image.shape[1]
    lenRow = int(lenY/SPLIT_COUNT)
    lenCol = int(lenX/SPLIT_COUNT)
    for row in range(SPLIT_COUNT):
        for col in range(SPLIT_COUNT):
            if (row + 1) < 10 and (col + 1) < 10:
                cv2.imwrite(splitSlotDir + "/" +  imagePath[-(lenName+1):-4] + "-0" + \
                    str(row+1) + "0" + str(col+1) + ".jpg", image[(row * lenRow): \
                    ((row+1) * lenRow), (col * lenCol): ((col+1) * lenCol)])
            elif (row + 1) < 10:
                cv2.imwrite(splitSlotDir + "/" +  imagePath[-(lenName+1):-4] + "-0" + \
                    str(row+1) + str(col+1) + ".jpg", image[(row * lenRow): \
                    ((row+1) * lenRow), (col * lenCol): ((col+1) * lenCol)])
            elif (col + 1) < 10:
                cv2.imwrite(splitSlotDir + "/" +  imagePath[-(lenName+1):-4] + "-" + \
                    str(row+1) + "0" + str(col+1) + ".jpg", image[(row * lenRow): \
                    ((row+1) * lenRow), (col * lenCol): ((col+1) * lenCol)])
            else:
                cv2.imwrite(splitSlotDir + "/" +  imagePath[-(lenName+1):-4] + "-" + \
                    str(row+1) + str(col+1) + ".jpg", image[(row * lenRow): \
                    ((row+1) * lenRow), (col * lenCol): ((col+1) * lenCol)])



# MAIN():
# =============================================================================
# Starting stopwatch to see how long process takes
start_time = time.time()

# Clears some of the screen for asthetics
print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Deletes contents in cropped- and split-image folders
deleteDirContents("./" + SPLIT_IMG_DIR)

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
        imageSplitter(imagePath, splitSlotDir, lenName)
    i += 1
        

print("Done!")

# Starting stopwatch to see how long process takes
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
