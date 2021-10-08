from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class text_editor:

    current_opened_file = "untitled"

    def new_file(self):
        ans = messagebox.askquestion("myNotepad","Do you want to save the file?")
        if ans == "no":
            self.text_area.delete(1.0,END)
            self.current_opened_file = "untitled"
        if ans =="yes":
            self.save_file()
            self.current_opened_file = "untitled"

    def open_file(self):

        open_file = filedialog.askopenfile(initialdir="/" , title="Open file" , filetypes=(("text files","*.txt"),("all files","*.*")))
        if(open_file != None):
            self.text_area.delete(1.0,END)
            for line in open_file:
                self.text_area.insert(END,line)
            self.current_opened_file = open_file.name
            open_file.close()



    def save_file(self):

        if self.current_opened_file == "untitled":
            self.save_as_file()
        else:
            saveas_file = open(self.current_opened_file,"w+")
            saveas_file.write(self.text_area.get(1.0,END))
            saveas_file.close()



    def save_as_file(self):
        saveas_file = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if saveas_file is None:
            return
        save_text = self.text_area.get(1.0,END)
        self.current_opened_file = saveas_file.name
        saveas_file.write(save_text)
        saveas_file.close()

    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first","sel.last")

    def paste_text(self):
        self.text_area.insert(INSERT,self.text_area.clipboard_get())

    def __init__(self,master):
        self.master = master
        master.title("myNotepad")
        self.text_area = Text(self.master,undo=True)
        self.text_area.pack(fill=BOTH,expand=1)

        #creating nav bar
        self.main_menu = Menu()
        self.master.config(menu=self.main_menu)

        #creating file menu
        self.file_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="File",menu=self.file_menu)

        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open",command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save ", command=self.save_file)
        self.file_menu.add_command(label="Save as", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save as", command=master.quit)

        #creating edit menu
        self.edit_menu = Menu(self.main_menu,tearoff =False)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)

        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)

root = Tk()
te = text_editor(root)
root.mainloop()
