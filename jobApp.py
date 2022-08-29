from http.client import PAYMENT_REQUIRED
import pyautogui
import time
import os
import keyboard
# from PIL import ImageGrab
# from functools import partial
# ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
os.chdir(r"C:\\Users\\Tyler\\Documents\\repos\\jobApplications\\imgs")

def searchClickLoop(img):
    try:
        print(f"Searching for {img}")
        x, y = pyautogui.locateCenterOnScreen(img)
        pyautogui.click(x, y)
    except:
        print("Cannot be found")
        searchClick(img)
    else:
        print("Found!")

def searchClick(img):
    try:
        print(f"Searching for {img}")
        x, y = pyautogui.locateCenterOnScreen(img)
        pyautogui.click(x, y)
    except:
        print("Cannot be found")
        return False
    else:
        print("Found!")
        return True

def search(img):
    try:
        print(f"Searching for {img}")
        x, y = pyautogui.locateCenterOnScreen(img)
    except:
        print("Cannot be found")
        return False
    else:
        print("Found")
        return True

def prepareWindow():
    if search("windowOptionsSelected.png") == True:
        pyautogui.hotkey("ctrl", "t")
        return 1
    # Maximize any window that's open
    if searchClick("fullscreenButtonSelected.png") == True:
        return 1
    # Open new tab on browser
    if searchClick("newTabButtonUnselected.png") == True:
        return 1
    # Open a new browser window
    print("Opening new browser")
    pyautogui.click(218, 1061)    # Click windows search bar 
    time.sleep(.25)
    pyautogui.typewrite("Google Chrome")
    pyautogui.click(214, 512)    # Click Google Chrome result
    time.sleep(3)
    # Recursion
    prepareWindow()

pyautogui.alert("Input position and company in terminal.")
print("Input position and company name")
companyInput = input()
pyautogui.alert(f"Press OK to run program for {companyInput}.")
prepareWindow()

# Select the address bar and input link to Google Drive Cover Letter folder
pyautogui.hotkey("ctrl", "l")
time.sleep(.25)
pyautogui.typewrite("https://drive.google.com/drive/folders/1URJAlVcc5mSXqHxANXQro2TFLAPvymgx")
time.sleep(.25)
pyautogui.press("enter")
time.sleep(1)
# Allow user to select cover letter
pyautogui.alert("Select a cover letter and click OK to continue")
# Click on file tab and select make a copy
pyautogui.click(80, 152)
time.sleep(.25)
# Click on make a copy
pyautogui.click(233, 255)
time.sleep(.25)
# Rename file with the appropriate label
pyautogui.press("delete")
pyautogui.typewrite(f"Cover Letter 2022 - {companyInput}")
pyautogui.click(1046, 736)    # click make copy
time.sleep(.25)
# Go to previous tab and close; use only keyboard shortcuts
pyautogui.hotkey("ctrl", "pageup")
pyautogui.hotkey("ctrl", "w")
# Go to previous tab using keyboard shortcut (back to Google Drive)
pyautogui.hotkey("ctrl", "pageup")

# Open Resume
pyautogui.hotkey("ctrl", "l")
time.sleep(.25)
pyautogui.typewrite("https://drive.google.com/drive/folders/1b5LaAaenWG4LIc7dWgDacwDB2raUrJf6")
time.sleep(.25)
pyautogui.press("enter")
time.sleep(1)
# Allow user to select resume
pyautogui.alert("Select a resume and click OK to continue")
# Click on file tab and select make a copy
pyautogui.click(80, 152)
time.sleep(.25)
# Click on make a copy
pyautogui.click(233, 255)
time.sleep(.25)
# Rename file with the appropriate label
pyautogui.press("delete")
pyautogui.typewrite(f"Resume 2022 - {companyInput}")
pyautogui.click(1046, 736)    # click make copy
time.sleep(.25)
# Go to previous tab and close; use only keyboard shortcuts
pyautogui.hotkey("ctrl", "pageup")
pyautogui.hotkey("ctrl", "w")

# Allow user to review and make changes to both documents
pyautogui.alert("Input anything in terminal when edits are complete. Be sure to remain in the cover letter tab.")
print("Enter anything to save resume and cover letter to computer.")
# Once user has indicated that they are done, save each document on the PC
userInput = input()
# Saving cover letter
pyautogui.click(80, 152)    # Click file
time.sleep(.25)
pyautogui.click(223, 366)    # Download
time.sleep(.25)
pyautogui.click(494, 370)    # Microsoft doc conversion
time.sleep(2)
pyautogui.hotkey("ctrl", "l")
time.sleep(.25)
pyautogui.typewrite("C:\\Users\\Tyler\\Documents\\Job Hunt\\Cover Letters")
time.sleep(.25)
pyautogui.press("enter")
time.sleep(.25)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
time.sleep(.25)
pyautogui.press("enter")
time.sleep(.25)

# Saving resume
pyautogui.hotkey("ctrl", "pageup")
pyautogui.click(80, 152)    # Click file
time.sleep(.25)
pyautogui.click(223, 366)    # Download
time.sleep(.25)
pyautogui.click(494, 370)    # Microsoft doc conversion
time.sleep(2)
pyautogui.hotkey("ctrl", "l")
time.sleep(.25)
pyautogui.typewrite("C:\\Users\\Tyler\\Documents\\Job Hunt\\Resume")
time.sleep(.25)
pyautogui.press("enter")
time.sleep(.25)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
time.sleep(.25)
pyautogui.press("enter")
time.sleep(.25)