from tkinter import *
root = Tk()
def send():
    send = "You:"+ sp.get()
    text.insert(END,"\n" + send)
    if(sp.get()== 'hi' or sp.get()== 'Hi'):
        text.insert(END, "\n" + "Bot: hello")
    elif(sp.get()=='hello' or sp.get()=='Hello' or sp.get()=='hlw' or sp.get()=='Hlw'):
        text.insert(END, "\n" + "Bot: hi")
    elif (sp.get() == 'how are you?' or sp.get() == 'how are you' or sp.get() == 'How are you?' or sp.get() == 'how r u?' or sp.get() == 'how r u'):
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif (sp.get() == "i'm fine too" or sp.get() == "i'm fine" or sp.get() == "i'm f9" or sp.get() == "i am f9"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
text = Text(root,bg='blue', fg='white')
text.grid(row=0,column=0,columnspan=2)
sp = Entry(root,width=80)
send = Button(root,text='Send',bg='deeppink', fg='white', width=20,command=send).grid(row=1,column=1)
sp.grid(row=1,column=0)
root.title('Asp Prothes')
root.mainloop()
