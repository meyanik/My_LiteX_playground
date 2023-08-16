import os
import subprocess
from tkinter import filedialog
from tkinter import Tk, Button, Label

class DockerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Docker GUI')
        self.path = ""

        self.label = Label(master, text="No directory selected")
        self.label.pack()

        self.open_button = Button(master, text="Browse Directory", command=self.browse_dir)
        self.open_button.pack()

        self.docker_button = Button(master, text="Run Docker", command=self.run_docker, state='disabled')
        self.docker_button.pack()

    def browse_dir(self):
        self.path = filedialog.askdirectory()
        self.label.configure(text=self.path)
        if self.path:  # Enable the Docker button only if a path is selected
            self.docker_button['state'] = 'normal'

    def run_docker(self):
        if not self.path:
            return
        command = f"docker run --rm -v {self.path}:/root/docker_shared -w /root/docker_shared meyanik/litex:0.01 python3 base.py"
        subprocess.run(command, shell=True)

root = Tk()
my_gui = DockerGUI(root)
root.mainloop()
