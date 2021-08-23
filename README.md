# ColorDetection

Color Detection is the process of identifying colors, we humans can easily identify colors, but for a computer its not the case, When a computer process a image they just read the 
pixels values ranging from 0 - 255. Any color for them is just a rnumber between this range. In this ColorDetection project we get the name of the color by just clicking over the 
portion in the image. We will use a csv file which have colors with their names and their pixels value. Then we will calculate the distance of the pixels to each colors in the file 
and finally select the one which has the minimal distance.


## DATASET
The dataset contains 865 colors along with their names , HEX values, RGB values

## IMG.JPG
Sample image file for detection of colors

## REQUIREMENTS
The necessary modules required for the project is included in the requirements.txt. If you are building a separate environment for the project, just install the file using 
```
pip install -r requirements.txt
```

## colorapp.py
This file contains all the necessary codes of the project


# Steps for building the project

### 1 Accepting user image
We are using argparse library to create an argument parser. We can directly give an image path from the command prompt:
```
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
img = cv2.imread(img_path)
```

### 2 Reading the csv file
With the pandas module reading the csv file
```
import pandas as pd
name=['color','color_name','Hex','R','G','B']
color_file = pd.read_csv('colors.csv',names=name,header=None)
```
### 3 MouseClickEvent
Later we will create a cv2 window. In the cv2 window where our image will be displayed, we set a callback function which will be called when a mouse event happens.
It will gives us the pixel values at the position where the mouse was left doubled clicked.
```
def mouseclickfunction(event, x ,y, flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, mousex, mousey, clicked
        clicked= True
        mousex = x
        mousey = y
        b,g,r = img[y,x]
        b, g, r = int(b), int(g), int(r)
```

### 4 Extracting color name
We have the rgb values from the previous method, Now its time to determine which color it is. For this we will iterate through each row of the dataframe and find the 
difference between the rgb values we obtained and the RGB values of the color in the list, initially we set minimum = 10000 but after every iteration we check the difference
is either bigger or smaller, if it is smaller than initial , then the minimum is updated to  the new difference. Then finally we extract out the color name for which the minimum
was the smallest

```
def extract_color_name(R, G, B):
    minimum= 10000
    for i in range(len(color_file)):
        d = abs(R - int(color_file.loc[i,'R']))+abs(G-int())+abs(G-int(color_file.loc[i,'G']))+abs(B-int(color_file.loc[i,'B']))
        if d <= minimum:
            minimum = d
            colorname = color_file.loc[i,'color_name']
    return colorname

```

### 5 Creating a window and set a call back event on the window
We created a window and set a callback and bind the above mouseclickfunction

```
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image', mouseclickfunction)
```

### 6 Displaying the image on the window

```
while True:
    cv2.imshow('image', img)
    if clicked:
        #cv2.rectangle(image, startpoint, endpoint, color, thickness) -1 thickness fills rectangle entirely
        cv2.rectangle(img, (20,20), (1460,100), (b,g,r), -1)
  
        #Creating text string to display ( Color name and RGB values )
        text=extract_color_name(r, g,  b)+' R=' + str(r) + ' G='+ str(g) + ' B=' + str(b)

        #cv2.putText(img,text,start,font(0-7), fontScale, color, thickness, lineType, (optional bottomLeft bool) )
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        #For very light colours we will display text in black colour
        if (r+g+b>=600):
            cv2.putText(img, text, (50,50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked= False
        
    #Break the loop when user hits 'esc' key 
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
```

### 6 Running the Python File
Run the Python file from the command prompt. Make sure to give an image path using ‘-i’ argument. If the image is in another directory, then you need to give full 
path of the image:

```
#python colorapp.py -i <add your image path here>
python colorapp.py -i C:\Users\saiki\Desktop\Color_Detection_API\img.jpg
```






