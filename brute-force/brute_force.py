import numpy as np
import cv2
from matplotlib import pyplot as plt

for x in range(0,999,1)
    if (x % 100) ==0
        path= "/image.orig" + x +"jpg"
        img = cv2.imread(path,0)


img1 = cv2.imread('full.jpg',0)          # queryImage
img2 = cv2.imread('full_img.jpg',0) # trainImage

# Initiate SIFT detector
surf = cv2.xfeatures2d.SURF_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = surf.detectAndCompute(img1,None)
kp2, des2 = surf.detectAndCompute(img2,None)
np.savetxt('kp1.txt', kp1, delimiter=" ", fmt="%s")
np.savetxt('des1.txt', des1, delimiter=" ", fmt="%s")
np.savetxt('kp2.txt', kp2, delimiter=" ", fmt="%s")
np.savetxt('des2.txt', des2, delimiter=" ", fmt="%s")
# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des1,des2,k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in range(len(matches))]

# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i]=[1,0]

draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)

img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)

plt.imshow(img3,),plt.show()