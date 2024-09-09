import tensorflow as tf
import numpy as np
import os
import librosa

class VoiceRecognitionModel:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Input(shape=(13,)),  # 13 MFCCs
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')  # Saída binária
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def preprocess_audio(self, audio_path):
        audio, sr = librosa.load(audio_path, sr=16000)
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
        return np.mean(mfccs.T, axis=0)

    def load_dataset(self, dataset_path):
        features = []
        labels = []
        for folder in os.listdir(dataset_path):
            folder_path = os.path.join(dataset_path, folder)
            label = 1 if folder == "target_voice" else 0  # Supondo que a pasta "target_voice" tenha a voz desejada
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                features.append(self.preprocess_audio(file_path))
                labels.append(label)
        return np.array(features), np.array(labels)

    def train(self, dataset_path, epochs=10):
        X, y = self.load_dataset(dataset_path)
        self.model.fit(X, y, epochs=epochs)
        self.model.save('trained_voice_model.h5')

    def predict(self, audio_path):
        features = self.preprocess_audio(audio_path)
        features = np.expand_dims(features, axis=0)
        prediction = self.model.predict(features)
        return prediction
