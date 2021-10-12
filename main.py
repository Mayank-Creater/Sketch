import cv2  #importing module

def img():
    path = input("Enter path of Image : ") # Opting for the path of the image
    img = cv2.imread(path)

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invertImg = 255 - grayImg
    blurImg = cv2.GaussianBlur(invertImg, (21, 21), 0) 
    invertBlurImg = 255 - blurImg
    pencilSketch = cv2.divide(grayImg, invertBlurImg, scale=256.0) 

    cv2.imshow("Original Image", img) 
    cv2.imshow("Pencil Sketch", pencilSketch)
    cv2.waitKey(0)

def camera():
  cap = cv2.VideoCapture(0) #Accessing the Camera
  
    while True:
        _, img = cap.read() # reading the content of camera
        
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        invertImg = 255 - grayImg
        blurImg = cv2.GaussianBlur(invertImg, (21, 21), 0)
        invertBlurImg = 255 - blurImg
        pencilSketch = cv2.divide(grayImg, invertBlurImg, scale=256.0)

        cv2.imshow("Original Image", img)
        cv2.imshow("Pencil Sketch", pencilSketch)
        if cv2.waitKey(1) == ord("q"):
            break

mode = input("Enter mode of sketch - Image(I) or Camera(C) : ")

if mode.upper() == 'I':
    img()

elif mode.upper() == 'C':
    camera()

else: 
    print("Enter valid mode!!")
