# Assignment 5: Object Detection and Document Recognition

## Overview
This assignment involves recognizing text from small-sized documents, including supermarket receipts and utility bill cheques.



### Installation:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/ADA-GWU/a5-object-detection-tmehtiyev2019.git
   cd a5-object-detection-tmehtiyev2019
   ```
2. **Install the requirements:**
   ```bash
    pip install -r requirements.txt
   ```

3.**Run the code:**
  ```bash
  python main.py
   ```

## Usage Instructions

### Start the Application
- Run `python main.py` from the terminal. This will open a window displaying the loaded image (e.g., a receipt or bill).

### Selecting Points
- Click on the image to select the four corners of the document. Start with the top-left corner and proceed clockwise to select the top-right, bottom-right, and bottom-left corners. Each click will place a red circle at the selected point.
- After selecting all four corners, a message will appear in the console: "Four corners selected. Press 'w' to warp perspective, 't' to detect text, or 'r' to reset."

### Warp Perspective
- Press 'w' to apply a perspective transformation. This adjusts the image to show the document as if viewed directly from the front, making it rectangular and easier to read.
- The warped image will then be displayed in a new window titled "Warped Image".

### Detect Text
- With the warped image open, press 't' to detect text using the MSER algorithm. This will highlight detected text regions on the warped image.
- The detected text regions will be shown with green bounding boxes.

### Reset Selection
- If you need to reselect the corners, press 'r'. This will allow you to restart the corner selection process on the original image.

### Exit the Program
- Close the image window or press 'q' to quit the program.

## Features
- **Perspective Transformation:** Converts the trapezoidal shape of the document to a rectangular form using manually selected corners.
- **Text Detection:** Utilizes the MSER algorithm to detect regions likely to contain text.
- **Text Recognition:** Ready for integration with a pre-trained CNN to recognize the detected text (currently shows detected regions).
- **Visualization:** Shows the processed images and detected text regions.

