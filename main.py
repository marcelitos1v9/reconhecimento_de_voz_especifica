import tkinter as tk
from controllers.voice_controller import VoiceController
from views.main_view import MainView

def main():
    root = tk.Tk()
    controller = VoiceController()
    app = MainView(root, controller)
    root.mainloop()

if __name__ == "__main__":
    main()
