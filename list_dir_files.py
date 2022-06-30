import os

path_orinent = r"C:\Users\10196\MVS\Data"

list_offsetIMG = [i for i in os.listdir(path_orinent) if i[-4:] == '.bmp']
print(list_offsetIMG)
