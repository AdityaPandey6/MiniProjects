import cv2

# Changeing parameters
source = "image.jpg"
destination = 'newimage.png'
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED())
# cv2.imshow("title", src)

# percent by which image is resized

# calculating the percentage of the original image
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src,(new_width, new_height))
cv2.imwrite(destination, output)
cv2.waitKey(0)