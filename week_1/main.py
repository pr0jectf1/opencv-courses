#QR CODE DETECTOR
#Dects QR Code and creates a bounding box around it.
import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
img = cv2.imread("./images/qr.png")

qrDecoder = cv2.QRCodeDetector()
opencvData, bbox, rectifiedImage = qrDecoder.detectAndDecode(img)
n = len(bbox[0])

for x in range(n): 
    print(x)
    point2 = x +1
    if x == n-1:
        point2 = 0
    cv2.line(img, (int(bbox[0][x][0]),int(bbox[0][x][1])), (int(bbox[0][point2][0]),int(bbox[0][point2][1])), (0,255,0))
cv2.imwrite("./images/QRCode-Output.png", img)
