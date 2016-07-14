import re
import urllib.request
from tkinter import *


master = Tk()

e = Entry(master,width=80)
e.grid(row=0, column=1,padx=5,pady=5)

text = Text(master)
text.grid(row=1, column=1)


def so():
    sou = urllib.request.quote(e.get())

    url = "http://api-jp02.smartmiu.com:184/s.py/op_search?word="+sou

    r = urllib.request.urlopen(url)

    s = r.read().decode("UTF-8")

    if s.find('<title>') == -1:
        text.insert(INSERT,"对你不起客官没有找到您想要的资源")

    a = re.findall(r"(?<=<title>).+?(?=</title>)",s)

    b = re.findall(r"(?<=<url>).+?(?=</url>)",s)

    c = re.findall(r"(?<=<size>).+?(?=</size>)",s)
    length1 = len(a)*2
    length2 = len(a)*3

    r = 1
    k = 2
    for i in c:
        if r<length1:        
            a.insert(r,i)
            r+=2

    for i in b:
        if k<length2:        
            a.insert(k,i)
            k+=3
      

    for each in range(len(a)):
        if each%3 == 0:
            text.insert(INSERT, (a[each],a[each+1],"\n",a[each+2],"\n\n"))

         
            #print(a[each],a[each+1],"\n",a[each+2],"\n")

                 


Button(master, text="搜琐", width=5, command=so).grid(row=0, column=2, padx=5, pady=5)


mainloop()

##def show():
##    
##    print("作品")
##
##c1 = Checkbutton(master,text="成人模式",variable=show)
###c2 = Checkbutton(master, text="帅锅", variable=show)
##c1.grid(row=1,column=2)
###c2.grid(row=1)




