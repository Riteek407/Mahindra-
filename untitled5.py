from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk


root = Tk()
root.title("Planet Encylopedia")
root.geometry("700x700")
root.configure(background="lightblue")

Thar = ImageTk.PhotoImage(Image.open("Thar.jpg"))
scorpio = ImageTk.PhotoImage(Image.open("scorpio.jpg"))
Bolero = ImageTk.PhotoImage(Image.open("bolero.jpg"))

label_img = Label(root, text="Planet :",bg="lightblue")
label_img_name = Label(root, font=("courier",18,"bold"),bg="lightblue")
label_img_image = Label(root, bg="gold2", highlightthickness=5, border=2,relief=SOLID)
label_img_details =Label(root,font=("castleer"), bg="lightblue")
label_img_info = Label(root,font=("courier",10,"bold"),bg='lightblue', wraplength=500)

img = ["Thar", "Scorpio", "Bolero"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values =img, textvariable=selectedval)

def ImgInfo():
    img = selectedval.get()
    if img == "Thar":
        label_img_name['text'] = "Thar"
        label_img_image['image'] = Thar
        label_img_details['text'] = " Made by Mahindra in INDIA"
        label_img_info['text'] = "Information The Mahindra Thar is a compact, four-wheel drive, off-road SUV manufactured by Indian automaker Mahindra and Mahindra Ltd."
 
    elif img == "Bolero":
       label_img_name['text'] = "Bolero"
       label_img_image['image'] = Bolero
       label_img_details['text'] = "Mahindra in INDIA"
       label_img_info['text'] = " Mileage and drive experience is good, good for off-roading. Rough and tough Car by Mahindra. Bolero is a dream car for everyone who wants to get a safe and secure journey. I did think about many cars I Chosen This One Because the car gives the best performance in driving and a safe experience on long tours also."

 
    elif img == "Scorpio":
       label_img_name['text'] = "Scorpio"
       label_img_image['image'] = scorpio
       label_img_details['text'] = "Mahindra in INDIA"
       label_img_info['text'] = " The Z8 offers a great overall package of all the nifty features and tech that is available in the top variant. As this variant offers all possible powertrain options, Z8 is the option you should consider."           
dropdown.place(relx=0.5, rely=0.1, anchor=CENTER)
            
btn = Button(root, text="Show Cars Info" , command=ImgInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

label_img.place(relx=0.2, rely=0.1 , anchor=CENTER)
label_img_name.place(relx=0.5,rely=0.2, anchor=CENTER)   
label_img_image.place(relx=0.5, rely=0.4, anchor =CENTER)
label_img_details.place(relx=0.5, rely=0.7, anchor=CENTER)
label_img_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()