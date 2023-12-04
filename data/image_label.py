import os
import fire
import time
from PIL import Image

train_data_path = "./train_data"
test_data_path = "./test_data"
train_output_path = "./train_data_label"
test_output_path = "./test_data_label"

train_file_list = os.listdir(train_data_path)
test_file_list = os.listdir(test_data_path)

train_data = [Image.open(os.path.join(train_data_path, filename)) for filename in train_file_list]
test_data = [Image.open(os.path.join(test_data_path, filename)) for filename in test_file_list]


def main(flag: str, start: int = 0):
    
    if flag == "train":
        for i, train_image in enumerate(train_data[start:]):
            print(f"now the working image id is {start+i}")
            train_image.show()
            label = input()
            
            if label != "1" and label != "0":
                raise ValueError("Label: you should input 1 or 0!")
            
            train_image.save(os.path.join(train_output_path, f"{label}_{start+i}.tif"))
            
    elif flag == "test":
        for i, test_image in enumerate(test_data[start:]):
            print(f"now the working image id is {start+i}")
            test_image.show()
            label = input()

            if label != "1" and label != "0":
                raise ValueError("Label: you should input 1 or 0!")
            
            test_image.save(os.path.join(test_output_path, f"{label}_{start+i}.tif"))
            
if __name__ == "__main__":
    fire.Fire(main)