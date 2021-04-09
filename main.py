from python_imagesearch.imagesearch import *
import pyautogui as pag
 
#변수초기화
found_img = 0
 
#프로그램시작
print("Start seeking..")
process_list = {'obj1':'./obj1.png' , 'obj2':'./obj2.png', 'obj3':'./obj3.png', 'obj4':'./obj4.png'}
 
for key, value in process_list.items():
    found_img = 0
    while found_img == 0:
        print("searching {}..".format(key))
        find_img = imagesearch(process_list.get(key))
        if find_img[0] != -1: 
            pag.moveTo(find_img[0]+20, find_img[1]+20)
            pag.click() 
            found_img = -1 #반복문 탈출
            print("{} has been found!".format(key))
