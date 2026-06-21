import pyautogui, keyboard
from PIL import Image

def paint(image: Image, delay: float, upper_left: tuple, lower_right: tuple):
    pyautogui.PAUSE = delay
    final_img = image.resize((lower_right[0]-upper_left[0], lower_right[1]-upper_left[1])) #resizing image
    stop_flag = False
    for x in range(final_img.width):
        if stop_flag: break
        for y in range(final_img.height):
            if keyboard.is_pressed('esc'):
                stop_flag = True
                break
            if final_img.getpixel((x, y)) == 255:
                pyautogui.click(upper_left[0]+x, upper_left[1]+y)
    if stop_flag: print("stopped by user")
    else: print("completed")