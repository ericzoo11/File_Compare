import tkinter 
from tkinter import filedialog, messagebox
import drive_compare



def center(app):
    # Call all pending idle tasks - carry out geometry management and redraw widgets.
    app.update_idletasks()
    # Get width and height of the screen
    width = app.winfo_width()
    height = app.winfo_height()
    # Calculate geometry
    x = (app.winfo_screenwidth() // 2) - (width // 2)
    y = (app.winfo_screenheight() // 2) - (height // 2)
    # Set geometry
    app.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def getDirPath():
    try:
        app.filename = filedialog.askdirectory(initialdir="/Users/ericzhu/")
        print("path 1: {}".format(app.filename))
    except:
        print("unable to open file")
    # use globally set counter variable
    global counter
    # count each button press
    counter = counter + 1
    # set label
    label.config(text=f"Button clicked: {counter} times")



counter = 0
#Window setup 
app = tkinter.Tk()
app.minsize(400, 400)
app.title("File Compare")
center(app)
label = tkinter.Label(app, text="Click the Button")
label.place(x=10, y=10)
button1 = tkinter.Button(app, text="Path 1", command=getDirPath)
button1.place(x=10, y=40)

app.mainloop()

