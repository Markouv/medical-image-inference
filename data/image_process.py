import os
import glob
import random
from PIL import Image

image_path = "./raw_image"
train_data_path = "./train_data"
test_data_path = "./test_data"
image_list = os.listdir(image_path)[1:]
cropped_image_list = []
crop_len = 128

# 打开TIF图片
for image_name in image_list:
    image = Image.open(os.path.join(image_path, image_name))
    
    crop_h_num = int(image.size[0] / crop_len)
    crop_v_num = int(image.size[1] / crop_len)

    for i in range(crop_h_num):
        for j in range(crop_v_num):
            cropped_image = image.crop((i*crop_len, j*crop_len, (i+1)*crop_len, (j+1)*crop_len))
            cropped_image_list.append(cropped_image)
    # print("图片格式:", image.format)
    # print("图片模式:", image.mode)
    
random.shuffle(cropped_image_list)
train_image_list = cropped_image_list[:int(0.8*len(cropped_image_list))]
test_image_list = cropped_image_list[int(0.8*len(cropped_image_list)):]

for i, train_image in enumerate(train_image_list):
    train_image.save(os.path.join(train_data_path, f"{i}.tif"))
    
for i, test_image in enumerate(test_image_list):
    test_image.save(os.path.join(test_data_path, f"{i}.tif"))



