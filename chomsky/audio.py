import wave
from pyaudio import PyAudio

class Audio():
    CHUNK = 1024

    @staticmethod
    def play(filename):
        wf = wave.open(filename, 'rb')

        p = PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(Audio.CHUNK)

        while data != b'':
            stream.write(data)
            data = wf.readframes(Audio.CHUNK)

        stream.stop_stream()
        stream.close()

        p.terminate()
