import cv2 
import os 
from PIL import Image 
import csv 
from tqdm import tqdm 



def video_black_find(video_path, total_num): 
    video = cv2.VideoCapture(video_path)
    while (video.isOpened()):
        retval, image = video.read() 
        if retval == True: 
            gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            r, c = gray_img.shape[:2] 
            pixes_sum = r * c
            dark_points = (gray_img < 20) 
            target_array = gray_img[dark_points] 
            dark_sum = target_array.size 
            dark_prop = dark_sum / pixes_sum 
            if dark_prop > 0.65: 
                print('current black image number: ', total_num)
                image = Image.fromarray(image) 
                image.save(str(total_num) + '.jpg') 
                total_num += 1 
        break 
    return total_num


def search_pattern(csv_path, folder, total_num): 
    with open(csv_path, 'r') as csvfile:
        dataset = list(csv.DictReader(csvfile))

    for video_dict in tqdm(dataset): 
        videoid, name, page_dir = video_dict['videoid'], video_dict['name'], video_dict['page_dir'] 
        video_dir = os.path.join(folder, page_dir)
        video_dir = os.path.join(video_dir, page_dir)
        video_dir    = os.path.join(video_dir, f"{videoid}.mp4")
        if os.path.exists(video_dir): 
            total_num = video_black_find(video_dir, total_num) 
        if total_num > 100:
            break 


import numpy as np 
def image_binary(image_path): 
    image = cv2.imread(image_path, 0) 
    ret, thresh = cv2.threshold(image, 10, 255, cv2.THRESH_BINARY) 
    kernel = np.ones((5, 5), dtype=np.uint8)
    dilate = cv2.dilate(thresh, kernel, 5)
    cv2.imwrite('black_binary.jpg', dilate)



csv_path = 'results_10M_train.csv'
folder = 'webvid'
total_num = 1 
black_image_path = 'black.jpg'
image_binary(black_image_path)
# search_pattern(csv_path, folder, total_num) 
