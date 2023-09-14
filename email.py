import platform #for windows,linux or macos
#from win10toast import ToastNotifier
import math
import pyautogui
import psutil
import time
import webbrowser
from gi.repository import Notify

email="https://google.com"

#open the gmail
webbrowser.open_new_tab(email)
time.sleep(30)
#click on the first mail
pyautogui.click(375,305)
time.sleep(8)
#mark as read
pyautogui.click(377,207)
time.sleep(5)

#to detect battery %
def get_battery_percentage():
    battery= psutil.sensors_battery()
    return battery.percent #ubuntu has no battery (attribute error)


#send notification
def send_notification(title,message):
    #send the wanted message
     Notify.init("battery percentage notification")
     notification= Notify.Notification.new(title,message)
     notification.show()

battery_per= get_battery_percentage()
send_notification("Battery notication",f"the battery is {battery_per}%")
#or using pynotifier







