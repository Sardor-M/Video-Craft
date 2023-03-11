import numpy as np
import cv2 as cv

# Prepare a canvas
canvas = np.full((480, 640, 3), 255, dtype=np.uint8)

# Draw lines with its label
cv.line(canvas, (10, 10), (640-10, 480-10), color=(200, 200, 200), thickness=2)
cv.line(canvas, (640-10, 10), (10, 480-10), color=(200, 200, 200), thickness=2)
cv.line(canvas, (320, 10), (320, 480-10), color=(200, 200, 200), thickness=2)
cv.line(canvas, (10, 240), (640-10, 240), color=(200, 200, 200), thickness=2)
cv.putText(canvas, 'Line', (10, 20), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0))

# Draw a circle with its label
center = (100, 240)
cv.circle(canvas, center, radius=60, color=(0, 0, 255), thickness=5)
cv.putText(canvas, 'Circle', center, cv.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 0))

# Draw a rectangle with its label
pt1, pt2 = (320-60, 240-50), (320+60, 240+50)
cv.rectangle(canvas, pt1, pt2, color=(0, 255, 0), thickness=-1)
cv.putText(canvas, 'Rectangle', pt1, cv.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 255))

# Draw a polygon (triangle) with its label
pts = np.array([(540, 240-50), (540-55, 240+50), (540+55, 240+50)])
cv.polylines(canvas, [pts], True, color=(255, 0, 0), thickness=5)
cv.putText(canvas, 'Polylines', pts[0].flatten(), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 200, 200))

# Show the canvas
cv.imshow('Shape Drawing', canvas)
cv.waitKey()  # waits until the you press ESC 

def mouse_event_handler(event, x, y, flags, param):
    # Change 'mouse_state' (given as 'param') according to the mouse 'event'
    if event == cv.EVENT_LBUTTONDOWN:
        param[0] = True
        param[1] = (x, y)
    elif event == cv.EVENT_LBUTTONUP:
        param[0] = False
    elif event == cv.EVENT_MOUSEMOVE and param[0]:
        param[1] = (x, y)

def free_drawing(canvas_width=640, canvas_height=480, init_brush_radius=3):
    # Prepare a canvas and palette
    canvas = np.full((canvas_height, canvas_width, 3), 255, dtype=np.uint8)
    palette = [(0, 0, 0), (255, 255, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

    # Initialize drawing states
    mouse_state = [False, (-1, -1)] # Note) [mouse_left_button_click, mouse_xy]
    brush_color = 0
    brush_radius = init_brush_radius

    # Instantiate a window and register the mouse callback function
    cv.namedWindow('Free Drawing')
    cv.setMouseCallback('Free Drawing', mouse_event_handler, mouse_state)

    while True:
        # Draw a point if necessary
        mouse_left_button_click, mouse_xy = mouse_state
        if mouse_left_button_click:
           cv.circle(canvas, mouse_xy, brush_radius, palette[brush_color], -1)

        # Show the canvas
        canvas_copy = canvas.copy()
        info = f'Brush Radius: {brush_radius}'
        cv.putText(canvas_copy, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (127, 127, 127), thickness=2)
        cv.putText(canvas_copy, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, palette[brush_color])
        cv.imshow('Free Drawing', canvas_copy)

        # Process the key event
        key = cv.waitKey(1)
        if key == 27: # ESC
            break
        elif key == ord('\t'):
            brush_color = (brush_color + 1) % len(palette)
        elif key == ord('+') or key == ord('='):
            brush_radius += 1
        elif key == ord('-') or key == ord('_'):
            brush_radius = max(brush_radius - 1, 1)

    cv.destroyAllWindows()

if __name__ == '__main__':
    free_drawing()

cv.waitKey()


