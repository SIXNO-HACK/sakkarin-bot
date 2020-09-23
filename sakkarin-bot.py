import string
import pyautogui
import time
import os
try:
 import config
 from config import epicwords
except:
    pass

def thegodpart():
    print("""

                  dP       dP                         oo          
                  88       88                                     
.d8888b. .d8888b. 88  .dP  88  .dP  .d8888b. 88d888b. dP 88d888b. 
Y8ooooo. 88'  `88 88888"   88888"   88'  `88 88'  `88 88 88'  `88 
      88 88.  .88 88  `8b. 88  `8b. 88.  .88 88       88 88    88 
`88888P' `88888P8 dP   `YP dP   `YP `88888P8 dP       dP dP    dP                                                    
                                                                  
    Created by : Sakkarin Su........

    Created by : sixno team
    """)
    print("---------------------------")
    print("[1] For  Single Phrase!")
    print("[2] For Multiple Phrase!")
    print("---------------------------")
    a = int(input("[ enter ] > "))
    if a == 1:
        k = input(" Enter The Word You Want To Spam: ") #ป้อนคำที่คุณต้องการส่งสแปม
        count = int(input("How Many Times Do You  Want To Spam:")) #คุณต้องการส่งสแปมกี่ครั้ง
        print (" You Have 5 Seconds, Place The Mouse Cursor On The Chat Box Where You Type!") #คุณมีเวลา 5 วินาทีวางเคอร์เซอร์ของเมาส์บนกล่องแชทที่คุณพิมพ์!
        time.sleep(5) #ทำให้โปรแกรมไม่ต้องทำอะไรเลยเป็นเวลา 5 วินาที
        for i in range(count):
            pyautogui.typewrite(k)
            pyautogui.press("enter")
            time.sleep(0.1)
        print("Spammed " + k + " " + str(count) + " times!")
        thegodpart()

    elif a == 2:
        k = int(input("How Many Words Do You Have That  You Want To Spam! > ")) #คุณต้องการสแปมกี่คำ!
        for i in range(k):
            print("Update The Config File, And Then Continue!") #อัปเดตไฟล์กำหนดค่าแล้วดำเนินการต่อ!
            print("Press Enter Once Done!") #กด Enter เมื่อเสร็จสิ้น!
            input("")
            l = int(input("How Many Times Do You Want To Spam The Message? > ")) #คุณต้องการส่งสแปมข้อความกี่ครั้ง
            for a in range(l):
                for i in epicwords:
                    pyautogui.typewrite(i)
                    pyautogui.press("enter")
                    time.sleep(0.1)
            print("Spammed Everything In Config File " + str(l) + " times!") #สแปมทุกอย่างในไฟล์กำหนดค่า
            thegodpart()
    else:
        print("Invalid Choice! The Again!") #ตัวเลือกไม่ถูกต้อง! อีกครั้ง!
        thegodpart()
thegodpart()
