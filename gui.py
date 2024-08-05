import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)


class TkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Audio, Video, AV):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        check_var = tk.IntVar()
        check_var1 = tk.IntVar()
        label = ttk.Label(self, text="Welcome to YTDownloader", font=LARGEFONT)
        button1 = ttk.Button(self, text="Begin", command=lambda: self.retrieve_state(check_var, check_var1))
        description = tk.Label(self,
                               text="The YT Downloader app is a user-friendly tool designed to effortlessly"
                                    " download videos and audio from YouTube. With a simple interface, it allows users"
                                    " to save their favorite content in various formats and resolutions directly to "
                                    "their devices. Key features include high-speed downloads, support for multiple "
                                    "file formats (MP4, MP3, AVI, etc.), batch downloading, and the ability to extract "
                                    "audio from videos. Whether for offline viewing or converting videos into audio "
                                    "files, YT Downloader provides a seamless experience for users looking to access "
                                    "their preferred YouTube content anytime, anywhere.",
                               font=("Helvetica", 10), wraplength=550, justify="left")
        checkboxes_question = ttk.Label(self, text="Choose what you prefer")
        checkbutton = tk.Checkbutton(self, text="Audio", variable=check_var,
                                     command=lambda: self.on_checkbutton_toggle(check_var))
        checkbutton2 = tk.Checkbutton(self, text="Video", variable=check_var1,
                                     command=lambda: StartPage.on_checkbutton_toggle(self, check_var1))
        label.place(relx=0.5, y=50, anchor="center")
        description.place(relx=0.5, y=200, anchor="center")
        checkboxes_question.place(relx=0.20, y=280, anchor="center")
        button1.place(relx=0.5, y=350, anchor="center")
        checkbutton.place(relx=0.14, y=300, anchor="center")
        checkbutton2.place(relx=0.14, y=320, anchor="center")

    def on_checkbutton_toggle(self, check_var):
        if check_var.get() == 1:
            print("Checkbox is checked")
        else:
            print("Checkbox is unchecked")

    def retrieve_state(self, check_var, check_var1):
        if check_var.get() == 1 and check_var1.get() == 0:
            self.controller.show_frame(Audio)
        if check_var.get() == 1 and check_var1.get() == 1:
            self.controller.show_frame(AV)
        if check_var.get() == 0 and check_var1.get() == 1:
            self.controller.show_frame(Video)

class Audio(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1", font = LARGEFONT)
        label.place(relx=0.5, y=50, anchor="center")
        button1 = ttk.Button(self, text="StartPage", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1, padx=10, pady=10)



class Video(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button2 = ttk.Button(self, text ="Back", command= lambda: controller.show_frame(StartPage))
        button2.grid(row=2, column=1, padx=10, pady=10)

class AV(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        pass



app = TkinterApp()
app.geometry("615x500")
app.mainloop()