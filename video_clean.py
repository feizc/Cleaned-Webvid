import cv2 
import numpy as np

def opencv_inpainting(image, mask): 
    #cv2.imshow('mask', mask)
    #cv2.waitKey(0)

    dst = cv2.inpaint(image, mask, 5, cv2.INPAINT_TELEA) # cv2.INPAINT_NS
    cv2.imwrite('dst.jpg', dst)
    cv2.imwrite('image.jpg', image)


def video_remove_watermark(video_path, mask):
    video = cv2.VideoCapture(video_path)
    while (video.isOpened()):
        retval, image = video.read() 
        if retval == True: 
            opencv_inpainting(image, mask)
            break

mask_path = 'black_binary.jpg'
mask = cv2.imread(mask_path, 0)
mask = np.uint8(mask)
video_path = '2.mp4'
video_remove_watermark(video_path, mask)