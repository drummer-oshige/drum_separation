import librosa
import soundfile


def drum_separation(path):
    y, sr = librosa.load(path)
    y_harmonic, y_percussive = librosa.effects.hpss(y, margin=1.5)
    return y_harmonic, y_percussive, sr


def write(path, y, sr):
    soundfile.write(path, y, sr, format='wav', subtype='PCM_16')
