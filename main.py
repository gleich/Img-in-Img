import cv2


full = cv2.imread("./sample_images/sammy.jpg")
face = cv2.imread("./sample_images/sammy_face.jpg")

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for method in methods:
    full_copy = full.copy()
    method = eval(method)
    res = cv2.matchTemplate(full_copy, face, method)