import tkinter as tk
from tkinter import filedialog
from controllers.voice_controller import VoiceController

class MainView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Reconhecimento de Voz")

        self.train_button = tk.Button(root, text="Treinar Modelo", command=self.train_model)
        self.train_button.pack()

        self.label = tk.Label(root, text="Selecione o arquivo de áudio:")
        self.label.pack()

        self.button = tk.Button(root, text="Carregar áudio", command=self.load_audio)
        self.button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def train_model(self):
        dataset_path = filedialog.askdirectory()
        if dataset_path:
            self.controller.train_model(dataset_path)
            self.result_label.config(text="Modelo treinado com sucesso!")

    def load_audio(self):
        audio_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
        if audio_path:
            result = self.controller.identify_voice(audio_path)
            self.result_label.config(text=result)
