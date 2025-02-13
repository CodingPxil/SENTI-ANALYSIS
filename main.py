from tkinter import*


root= Tk()
root.geometry("500x500")

label = Label(root, text="Get the Sentiment:")
label.pack()

textA = Entry(root, width=30)
textA.pack()

get_senti_b = Button(root, text="GetSentiment", fg="white", bg="green")
get_senti_b.pack()


root.mainloop()