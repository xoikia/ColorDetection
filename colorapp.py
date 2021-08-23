import argparse
import cv2
import pandas as pd


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
img = cv2.imread(img_path)
img = cv2.resize(img, (1500,1000), interpolation= cv2.INTER_LINEAR)


clicked = False
r = g = b = mousex = mousey = 0


name=['color','color_name','Hex','R','G','B']
color_file = pd.read_csv('colors.csv',names=name,header=None)


def extract_color_name(R, G, B):
    minimum= 10000
    for i in range(len(color_file)):
        d = abs(R - int(color_file.loc[i,'R']))+abs(G-int())+abs(G-int(color_file.loc[i,'G']))+abs(B-int(color_file.loc[i,'B']))
        if d <= minimum:
            minimum = d
            colorname = color_file.loc[i,'color_name']
    return colorname


def mouseclickfunction(event, x ,y, flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, mousex, mousey, clicked
        clicked= True
        mousex = x
        mousey = y
        b,g,r = img[y,x]
        b, g, r = int(b), int(g), int(r)

        
'''bind the above function to a window that will capture the mouse click'''        
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#cv2.resizeWindow('image', window_width, window_height)

cv2.setMouseCallback('image', mouseclickfunction)

while True:
    cv2.imshow('image', img)
    if clicked:

        cv2.rectangle(img, (20,20), (1460,100), (b,g,r), -1)

        text=extract_color_name(r, g,  b)+' R=' + str(r) + ' G='+ str(g) + ' B=' + str(b)

        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        if (r+g+b>=600):
            cv2.putText(img, text, (50,50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked= False

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()






