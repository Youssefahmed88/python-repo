import tkinter
class MyGUI:
    def __init__(self):

        ##create the main window widget
        self.main_window=tkinter.Tk()

        ##display title
        self.main_window.title('My First GUI') 

        ##create label main window
        self.label=tkinter.Label(self.main_window, text='Hello, World')

        ##call the window widget pack method
        self.label.pack()

        ##enter the tkinter main loop
        tkinter.mainloop()

def main():
    my_gui=MyGUI()