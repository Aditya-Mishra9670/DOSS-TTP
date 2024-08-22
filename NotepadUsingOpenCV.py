import cv2
import numpy as np

# Initialize the drawing state
drawing = False
color = (0, 0, 0)  # Black color
thickness = 2

def draw_line(event, x, y, flags, param):
    global drawing, color, thickness

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(canvas, (x, y), thickness, color, -1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(canvas, (prev_x, prev_y), (x, y), color, thickness)
        prev_x, prev_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(canvas, (prev_x, prev_y), (x, y), color, thickness)

# Create a white canvas
canvas = np.ones((500, 700, 3), dtype=np.uint8) * 255

# Set up the OpenCV window
cv2.namedWindow('Virtual Notepad')
cv2.setMouseCallback('Virtual Notepad', draw_line)

while True:
    cv2.imshow('Virtual Notepad', canvas)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  # Press 'q' to quit
        break
    elif key == ord('c'):  # Press 'c' to clear the canvas
        canvas[:] = 255
    elif key == ord('r'):  # Press 'r' to change color to red
        color = (0, 0, 255)
    elif key == ord('b'):  # Press 'b' to change color to blue
        color = (255, 0, 0)
    elif key == ord('g'):  # Press 'g' to change color to green
        color = (0, 255, 0)

cv2.destroyAllWindows()
