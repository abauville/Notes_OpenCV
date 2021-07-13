import ipywidgets as widgets
import threading
from IPython.display import display, Image
import cv2


# A button to stop the camera
stopButton = widgets.ToggleButton(
    value=False,
    description='Stop',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Description',
    icon='square' # (FontAwesome names without the `fa-` prefix)
)


# view the camera
def view(button, fn=None):
    # button is a Ipywdiget button to stop the camera
    # fn is function to apply some treatment on the image. It should return an image
    cap = cv2.VideoCapture(0)
    display_handle=display(None, display_id=True)
    i = 0
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1) # if your camera reverses your image
        if fn:
            frame = fn(frame)
        _, frame = cv2.imencode('.jpeg', frame)
        display_handle.update(Image(data=frame.tobytes()))
        if stopButton.value==True:
            cap.release()
            display_handle.update(None)


# Example:
"""
stopButton.value=False
display(stopButton)            
thread = threading.Thread(target=view, args=(stopButton,))
thread.start()
"""