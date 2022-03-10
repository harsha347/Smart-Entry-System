# opencv used for image reading and visualisation
import cv2

# Google's pretrained ocr model package to detect text in image
import pytesseract

# os library to ease the acceess of files from the system
import os

# regex to filter the usn from text 
import re

# Pillow library used to resize the image 
from PIL import Image

# pandas to read database and verify and extract info
import pandas as pd

im = Image.open(os.getcwd() + '\image.jpg')
#im.show()
im = im.resize((3000,4000))
im.save('image1.jpg')

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread(os.getcwd() + '\image1.jpg')

text_detected = pytesseract.image_to_string(img)
# print("OUTPUT:", text_detected)

# finding usn in the text using regex
# no usn in database ->x= ['1BM19ME007']
# graduated student ->x = ['1BM19ME000']
x = re.findall('1BM.*\d', text_detected)

if (len(x) > 0):
    print("USN found:", x)
    print("Checking database...\n")
else:
    print("USN not found! Please try again.\n")
    exit()

db = pd.read_excel('database.xlsx', sheet_name='Sheet1')

count = 0
flag = 0
for i in db.values:
    if x[0] in i:
        flag = 1
        print("USN Found in Database!\n")
        print("Details: ")
        print("Name -", db.iloc[count]['NAME'])
        print("Department -", db.iloc[count]['DEPT'])
        print("SEM -", db.iloc[count]['SEM'])
        if db.iloc[count]['GRADUATION YEAR'] > 2020:
            print("\nID Card is Valid!")
        else:
            print("\nID Card has expired!")
    count = count + 1

if (flag==0):
    print("USN not found in Database!")

 
