import subprocess
import os
import time
import pyautogui

def signIn(meetingid):
    current_dir = r"C:\Program Files (x86)\Tencent\VooVMeeting"
    subprocess.Popen(os.path.join(current_dir,"voovmeetingapp.exe"))
    time.sleep(3)
    
    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(1)

    meeting_id_btn = pyautogui.locateCenterOnScreen('meeting_id.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meetingid)
    time.sleep(3)

    media_btn = pyautogui.locateAllOnScreen('Media_button.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(1)

    join_btn = pyautogui.locateCenterOnScreen('enter_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(5)

    close_button = pyautogui.locateCenterOnScreen('close_button.png')
    pyautogui.moveTo(close_button)
    pyautogui.click()
    time.sleep(3)

    close_button2 = pyautogui.locateCenterOnScreen('close_button2.png')
    pyautogui.moveTo(close_button2)
    pyautogui.click()
    time.sleep(3)

signIn(21323123)
