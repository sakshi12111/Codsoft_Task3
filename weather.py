import tkinter
from tkinter import *
from tkinter import ttk
import requests

root=tkinter.Tk()
root.title("WEATHER UPDATES")
root.geometry("500x500")
p1=PhotoImage(file="photo.png")

root.iconphoto(False,p1)
root.config(bg="darkblue")


def data_get():
    p2=PhotoImage(file="cloud.png")
    p3=PhotoImage(file="rain.png")
    p4=PhotoImage(file="snow.png")
    p5=PhotoImage(file="clear.png")
    city=city_name.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=693f98d117d1f775785a95ae0ae5c4a8").json()
    w_label1.config(text=data["weather"][0]["main"])
    w_des1.config(text=data["weather"][0]["description"])
    w_temp1.config(text=str(data["main"]["temp"]-273.15)+" C")
    w_press1.config(text=data["main"]["pressure"])

    if(data["weather"][0]["main"]=="Clouds"): 
        new=p2.subsample(2,2)
        label=tkinter.Label(root,image=new,width=100,height=100)
        label.photo = new
        label.grid(column=2,row=9)
        label.place(x=50,y=280)
    elif(data["weather"][0]["main"]=="Rain"):
         new1=p3.subsample(2,2)
         label=tkinter.Label(root,image=new1,width=100,height=100)
         label.photo = new1
         label.grid(column=2,row=9)
         label.place(x=50,y=280)
    elif(data["weather"][0]["main"]=="Snow"):
         new2=p4.subsample(2,2)
         label=tkinter.Label(root,image=new2,width=100,height=100)
         label.photo = new2
         label.grid(column=2,row=9)
         label.place(x=50,y=280)
    elif(data["weather"][0]["main"]=="Clear"):
         new3=p5.subsample(1,1)
         label=tkinter.Label(root,image=new3,width=100,height=100)
         label.photo = new3
         label.grid(column=2,row=9)
         label.place(x=50,y=280)



name_label=Label(root,text="CloudVue Weather",font=("Times New Roman",20,"bold"),bg="lightblue")
name_label.place(x=22,y=30,width=450)

enter_state=Label(root,text="Select the state:",font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
enter_state.place(x=50,y=120,width=200)

list_states=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh",
             "Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram",
             "Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand",
             "West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep",
             "National Capital Territory of Delhi","Puducherry"]
city_name=StringVar()
com=ttk.Combobox(root,values=list_states,font=("Times New Roman",13),textvariable=city_name)
com.place(x=220,y=120,width=200,height=30)

w_label=Label(root,text="Climate:",font=("Times New Roman",13,"bold"),fg="white",bg="darkblue")
w_label.place(x=200,y=285)
w_label1=Label(root,text="",font=("Times New Roman",13,"bold"),fg="white",bg="darkblue")
w_label1.place(x=280,y=285,width=200)

w_des=Label(root,text="Description:",font=("Times New Roman",13,"bold"),fg="white",bg="darkblue")
w_des.place(x=200,y=305)
w_des1=Label(root,text="",font=("Times New Roman",13,"bold"),fg="white",bg="darkblue")
w_des1.place(x=280,y=305,width=200)

w_temp=Label(root,text="Temperature:",font=("Times New Roman",13,"bold"),fg="white",bg="darkblue")
w_temp.place(x=200,y=325)
w_temp1=Label(root,text="",font=("Times New Roman",13,"bold"),fg="white",bg="darkblue")
w_temp1.place(x=280,y=325,width=200)

w_press=Label(root,text="Pressure:",font=("Times New Roman",13,"bold"),fg="white",bg="darkblue")
w_press.place(x=200,y=345)
w_press1=Label(root,text="",font=("Times New Roman",13,"bold"),fg="white",bg="darkblue")
w_press1.place(x=280,y=345,width=200)

done_btn=Button(root,text="Done",font=("Times New Roman",15,"bold"),command=data_get)
done_btn.place(x=220,y=190)
root.mainloop()