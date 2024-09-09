from models.voice_model import VoiceRecognitionModel

class VoiceController:
    def __init__(self):
        self.model = VoiceRecognitionModel()

    def train_model(self, dataset_path):
        self.model.train(dataset_path)

    def identify_voice(self, audio_path):
        prediction = self.model.predict(audio_path)
        if prediction[0] > 0.5:
            return "Voz identificada!"
        else:
            return "Voz não identificada."
