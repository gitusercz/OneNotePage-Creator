# OneNotePage-Creator
A simple demonstration of how handy pyautogui could be. 

# OneNotePage Creator

I decided to keep a diary of what I eat. I have tried multiple methods (paper, some app etc.) none of them worked because of habit friction. The most sustainable method proved to be filling a precreated table in OneNote. To automate the process of creating the blank templates I wrote a simple script using pyautogui.

![DemoRun](/resources/flow.gif)

## How it works:

- Simulates Windows keypress
- Types OneNote, hits enter, wait for OneNote to start.
- Creates a new tab
- Gives a title (which is a date and the name of the day)
- Pastes whatever is on the clipboard (you have to copy it for yourself beforehand!)
- Creates another tab for as many times as you previously entered.

You have to wait the process to finish and do not use the machine in the meantime.

---

Attila Czibere  
2024-02
