import pyautogui
import time
import datetime

def open_onenote():
    pyautogui.press('win')
    time.sleep(2)
    pyautogui.write('OneNote')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3) # Wait for OneNote to open

def create_new_page(date_str):
    pyautogui.hotkey('ctrl', 'n') # Shortcut for creating a new page
    time.sleep(0.5)
    pyautogui.write(date_str) # 7 (Write the date string as the page title
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v') # Paste from clipboard

# Open OneNote
open_onenote()

# Start date
start_date = datetime.date(2025, 1, 1)

# Repeat 14 times
for i in range(300):
    current_date = start_date + datetime.timedelta(days=i)
    date_str = current_date.strftime("%Y-%m-%d (%A)")
    # if current_date.weekday() < 5:  # Weekday (0-4 are Monday to Friday)
    create_new_page(date_str)
    time.sleep(0.5) # A short delay to ensure the page is created before the next iteration

print("Pages created successfully.")
