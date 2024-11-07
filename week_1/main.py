#QR CODE DETECTOR
import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
img = cv2.imread("../images/qr.png")

qrDecoder = cv2.QRCodeDetector()
opencvData, bbox, rectifiedImage = qrDecoder.detectAndDecode(img)
print(rectifiedImage)

if opencvData != None:
    print("QR Code Detected")
else:
    print("QR Code NOT Detected")

n = len(bbox)

resultImagePath = "../images/QRCode-Output.png"
cv2.imwrite(resultImagePath,img)
plt.imshow(img)