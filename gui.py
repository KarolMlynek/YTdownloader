import tkinter as tk
from tkinter import ttk
from downloader import Downloader
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
        link = ttk.Label(self, text="Link: ")
        link_entry = tk.Entry(self,width=35)
        listbox_label = ttk.Label(self, text="Choose audio quality")
        listbox = tk.Listbox(self, selectmode=tk.SINGLE, width=60)

        button_back = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button_submit = ttk.Button(self, text="Submit", command=lambda: controller.show_frame())
        link.place(relx=0.10, y=50, anchor="center")
        link_entry.place(relx=0.40, y=50, anchor="center")
        button_back.place(relx=0.3, y=450, anchor="center")
        button_submit.place(relx=0.6, y=450, anchor="center")
        listbox_label.place(relx=0.20, y=130, anchor="center")
        listbox.place(relx=0.50, y=300, anchor="center")

    def add_item(self):
        item = self.entry.get()
        if item:
            self.listbox.insert(tk.END, item)
            self.entry.delete(0, tk.END)

class Video(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        link = ttk.Label(self, text="Link: ")
        link_entry = tk.Entry(self, width=35)
        listbox_label = ttk.Label(self, text="Choose  video quality")
        listbox = tk.Listbox(self, selectmode=tk.SINGLE, width=60)

        button_back = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button_submit = ttk.Button(self, text="Submit", command=lambda: controller.show_frame())
        link.place(relx=0.10, y=50, anchor="center")
        link_entry.place(relx=0.40, y=50, anchor="center")
        button_back.place(relx=0.3, y=450, anchor="center")
        button_submit.place(relx=0.6, y=450, anchor="center")
        listbox_label.place(relx=0.20, y=130, anchor="center")
        listbox.place(relx=0.50, y=300, anchor="center")

class AV(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        link = ttk.Label(self, text="Link: ")
        link_entry = tk.Entry(self, width=35)
        listbox_label_audio = ttk.Label(self, text="Choose  audio quality")
        listbox_audio = tk.Listbox(self, selectmode=tk.SINGLE)
        listbox_label_video = ttk.Label(self, text="Choose video quality")
        listbox_video = tk.Listbox(self, selectmode=tk.SINGLE)

        button_back = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button_submit = ttk.Button(self, text="Submit", command=lambda: controller.show_frame())
        link.place(relx=0.10, y=50, anchor="center")
        link_entry.place(relx=0.40, y=50, anchor="center")
        button_back.place(relx=0.3, y=450, anchor="center")
        button_submit.place(relx=0.6, y=450, anchor="center")
        listbox_label_audio.place(relx=0.20, y=130, anchor="center")
        listbox_audio.place(relx=0.20, y=300, anchor="center")
        listbox_label_video.place(relx=0.80, y=130, anchor="center")
        listbox_video.place(relx=0.80, y=300, anchor="center")



'''app = TkinterApp()
app.geometry("615x500")
app.mainloop()'''