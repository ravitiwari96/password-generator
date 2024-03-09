from tkinter import*
import string
import random
import pyperclip

def generator():
    small_alphabet = string.ascii_lowercase
    capital_alphabet = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation
    
    all = small_alphabet + capital_alphabet + numbers + special_characters
    password_length = int(length_Box.get())


# condition for password generate

    if choice.get()==1:
            passwordField.insert(0,random.sample(small_alphabet,password_length))
            
            
    if choice.get()==2:
            passwordField.insert(0,random.sample(small_alphabet+capital_alphabet+numbers,password_length))
    
    if choice.get()==3:
            passwordField.insert(0,random.sample(all,password_length))


#function of copy

def copy():
    random_password = passwordField.get()    
    pyperclip.copy(random_password)     
            
    

root = Tk()

root.config(bg='White')
choice = IntVar()
Font=('times new roman',13,'bold')
passwordLabel = Label(root,text='Password Generator',font=('times new roman',20,"bold"),bg='Black',fg='white')
passwordLabel.grid()

root.geometry("300x350")

# weak button
weakradioButton = Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=3)

# medium button
mediumradioButton = Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=3)

# strong button
strongradioButton = Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=3)

#Password Heading
lengthLabel = Label(root,text='Password Length',font=Font,bg='black',fg='white')
lengthLabel.grid(pady=3)

# given the length of the password
length_Box = Spinbox(root,from_=5,to_=18,width=8,font=Font)
length_Box.grid(pady=3)

# password generate button
generateButton = Button(root,text='Generate',font=Font,command=generator)
generateButton.grid(pady=3)

# password display box
passwordField = Entry(root,width=25,bd=2,font=Font)
passwordField.grid(pady=3)

#pass copy button 
copyButton = Button(root,text='Copy',font=Font,command=copy)
copyButton.grid(pady=3)

root.mainloop()