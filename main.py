import cv2
import numpy as np

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            orig_x, orig_y = int(x / scale_factor), int(y / scale_factor)
            points.append((orig_x, orig_y))
            cv2.circle(img_display, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow("Image", img_display)
            if len(points) == 4:
                print("Four corners selected. Press 'w' to warp perspective, 't' to detect text, or 'r' to reset.")

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def warp_perspective():
    global warped_image  # Declare global to modify it inside the function
    ordered_points = order_points(np.array(points))
    (tl, tr, br, bl) = ordered_points

    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    max_width = max(int(widthA), int(widthB))
    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    max_height = max(int(heightA), int(heightB))
    dst = np.array([[0, 0], [max_width - 1, 0], [max_width - 1, max_height - 1], [0, max_height - 1]], dtype="float32")
    matrix = cv2.getPerspectiveTransform(ordered_points, dst)
    warped_image = cv2.warpPerspective(orig, matrix, (max_width, max_height))
    cv2.imshow("Warped Image", warped_image)

def detect_text_mser():
    if 'warped_image' in globals():
        gray = cv2.cvtColor(warped_image, cv2.COLOR_BGR2GRAY)
        mser = cv2.MSER_create()
        mser.setMinArea(100)
        mser.setMaxArea(3000)
        regions, _ = mser.detectRegions(gray)
        for region in regions:
            hull = cv2.convexHull(region.reshape(-1, 1, 2))
            cv2.polylines(warped_image, [hull], True, (0, 255, 0), 1)
            x, y, w, h = cv2.boundingRect(hull)
            cv2.rectangle(warped_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Detected Text", warped_image)
    else:
        print("Please warp the image first before detecting text.")

img = cv2.imread('Receipts/input_receipt.jpeg')
if img is None:
    print("Error: Image not loaded. Check the path.")
    exit()

orig = img.copy()
max_height = 600
max_width = 800
scale_factor = min(max_width / img.shape[1], max_height / img.shape[0])
img_display = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
cv2.imshow("Image", img_display)
points = []
warped_image = None  # Initialize warped_image variable

cv2.setMouseCallback("Image", mouse_click)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('w'):
        if len(points) == 4:
            warp_perspective()
    elif key == ord('t'):
        detect_text_mser()
    elif key == ord('r'):
        img_display = cv
