from tkinter import*
import random
from PIL import ImageTk, Image

root = Tk()

root.title("People who are in my family")
root.geometry("600x400")
root.configure(background="pink")

img = ImageTk.PhotoImage(Image.open("button_image.jpg"))

button_label = Label(root, bg = "chocolate1", fg = "white")
button_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

family_name_list = ["Sophia", "Mama", "Daddy", "Bhai", "Guddi Anni", "Alykhan Uncle", "Kiara", "Blue Anni", "Enu Nani", "Yasu Nani", "Hami Nani", "Nanu", "Nani"]

def family_name() :
    random_no = random.randint(1, 13)
    random_family_name = family_name_list[random_no]
    button_label["text"] = "The people in my family are: " + random_family_name
    
btn = Button(root, image = img, command = family_name)
btn.place(relx = 0.5, rely = 0.2, anchor = CENTER)
root.mainloop()