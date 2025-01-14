import re
import urllib.request
from tkinter import *;
#**lets check if this works
def fun():
    url = "http://www.spoj.com/users/"
    str = ent.get();
    url += str;
    url += "/";
    data = urllib.request.urlopen(url);
    data = data.read();
    data1 = data.decode("utf-8");
    #*****solved***
    m = re.search("Problems solved</dt>", data1);
    pos = m.end() + 13;
    ans="";
    while (data1[pos] != '<'):
        ans+=data1[pos];
        pos += 1;
    tex.insert(END,ans);
    #*****solution submitted***
    m = re.search("Solutions submitted</dt>", data1);
    pos = m.end() + 13;
    ans="";
    while (data1[pos] != '<'):
        ans += data1[pos];
        pos += 1;
    tex2.insert(END,ans);
    #*****belongs to*******
    m = re.search("fa fa-map-marker", data1);
    pos = m.end() + 7;
    ans = "";
    while (data1[pos] != '<'):
        ans += data1[pos];
        pos += 1;
    tex3.insert(END, ans);
    #*****Rank*********
    m = re.search("World Rank: #", data1);
    pos = m.end();
    ans = "";
    while (data1[pos] != ' '):
        ans += data1[pos];
        pos += 1;
    tex4.insert(END, ans);
    #*****Last Seen****
    url = "http://www.spoj.com/status/";
    url += str;
    url += "/";
    data = urllib.request.urlopen(url);
    data = data.read();
    data1 = data.decode("utf-8");
    m = re.search("span title=", data1);
    pos = m.end() + 1;
    ans = "";
    while (data1[pos] != ' '):
        ans += data1[pos];
        pos += 1;
    tex5.insert(END, ans);

def fun2():
    screen.quit();

def fun3():
    tex.delete(1.0,END);
    ent.delete(0,END);
    tex2.delete(1.0, END);
    tex3.delete(1.0, END);
    tex4.delete(1.0, END);
    tex5.delete(1.0, END);

#******Frame************
screen=Tk();
screen.title("Spoj Teller");
screen.resizable(width=False,height=False);
frame=Frame(screen,width=1000,height=500,bg="khaki3");
frame.grid(row=0,column=0);

#*******Spoj Teller******
lab0=Label(frame,text="The Spoj Teller",bg="khaki3",fg="gray23");
lab0.grid(row=0,column=1,columnspan=1,sticky="W");
lab0.config(font=("Times New Roman",45,"bold"));


#*******Enter The Handle*********
ent=Entry(frame,bg="ivory2",relief=SUNKEN,bd=5);
lab1=Label(frame,text="Handle",fg="gray23",bg="khaki3",bd=2);
lab1.grid(row=1,column=0,columnspan=2,sticky="W");
lab1.config(font=("Times New Roman",25));
ent.grid(row=1,column=2,sticky="W");
ent.config(font=("Comic sans",20,"italic"));


#*******Solved Questions*********
lab2=Label(frame,text="Solved questions",fg="gray23",bg="khaki3",bd=2);
lab2.grid(row=2,column=0,columnspan=1,sticky="W");
lab2.config(font=("Times New Roman",25));
tex=Text(frame,width=15,height=1,bg="ivory2",relief=SUNKEN,bd=5);
tex.grid(row=2,column=2,sticky="W",columnspan=2);
tex.config(font=("Comic sans",20,"italic"));

#********Solution Submitted******
lab3=Label(frame,text="Solution Submitted",fg="gray23",bg="khaki3",bd=2);
lab3.grid(row=3,column=0,columnspan=1,sticky="W");
lab3.config(font=("Times New Roman",25));
tex2=Text(frame,width=15,height=1,bg="ivory2",relief=SUNKEN,bd=5);
tex2.grid(row=3,column=2,sticky="W",columnspan=2);
tex2.config(font=("Comic sans",20,"italic"));

#********Belongs To*************
lab4=Label(frame,text="Belongs To",fg="gray23",bg="khaki3",bd=2);
lab4.grid(row=4,column=0,columnspan=1,sticky="W");
lab4.config(font=("Times New Roman",25));
tex3=Text(frame,width=15,height=1,bg="ivory2",relief=SUNKEN,bd=5);
tex3.grid(row=4,column=2,sticky="W",columnspan=2);
tex3.config(font=("Comic sans",20,"italic"));


#*********Rank***************
lab5=Label(frame,text="Rank",fg="gray23",bg="khaki3",bd=2);
lab5.grid(row=5,column=0,columnspan=1,sticky="W");
lab5.config(font=("Times New Roman",25));
tex4=Text(frame,width=15,height=1,bg="ivory2",relief=SUNKEN,bd=5);
tex4.grid(row=5,column=2,sticky="W",columnspan=2);
tex4.config(font=("Comic sans",20,"italic"));

#*********Last Seen***************
lab6=Label(frame,text="Last Seen",fg="gray23",bg="khaki3",bd=2);
lab6.grid(row=6,column=0,columnspan=1,sticky="W");
lab6.config(font=("Times New Roman",25));
tex5=Text(frame,width=15,height=1,bg="ivory2",relief=SUNKEN,bd=5);
tex5.grid(row=6,column=2,sticky="W",columnspan=2);
tex5.config(font=("Comic sans",20,"italic"));

#*******Buttons*********
submit=Button(frame,text="Find",fg="black",bg="ivory4",command=fun);
submit.grid(row=8,column=1,sticky="N");
submit.config(font=("Comic sans",20));

clearing=Button(frame,text="Clear",bg="ivory4",command=fun3);
clearing.grid(row=8,column=0,sticky="W");
clearing.config(font=("Comic sans",20));

exi=Button(frame,text="Exit",fg="black",bg="ivory4",command=fun2);
exi.grid(row=8,column=2,sticky="E");
exi.config(font=("Comic sans",20));


