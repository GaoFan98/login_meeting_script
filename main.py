import subprocess
import pandas as pd
import pyautogui
import time
from datetime import datetime



def signIn(meetingid):
    subprocess.call("C:\Program Files (x86)\Tencent\WeMeet\wemeetapp.exe")
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

df = pd.read_excel('timings.xlsx')

while True:
    # To get current time
    now = datetime.now().strftime("%H:%M")
    if now in str(df['Timings']):
        mylist = df["Timings"]
        mylist = [i.strftime("%H:%M") for i in mylist]
        c = [i for i in range(len(mylist)) if mylist[i] == now]
        row = df.loc[c]
        meeting_id = str(row.iloc[0, 1])

        time.sleep(5)
        signIn(meeting_id)
        time.sleep(2)
        print('signed in')
        break


#signIn('448949037')
