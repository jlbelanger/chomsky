# Inspired by https://github.com/jeysonmc/python-google-speech-scripts/blob/master/stt_google.py
import audioop
import math
import wave
import pyaudio
from pyAudioAnalysis import audioTrainTest
import config

class Listener():
    CHUNK = 1024
    RATE = 44100
    CHANNELS = 1
    FORMAT = pyaudio.paInt16
    OUTPUT_FILENAME = 'output.wav'
    NUM_PRE_FRAMES = 10
    NUM_POST_FRAMES = 20

    def __init__(self, should_classify=True, i=None):
        self.p = None
        self.should_classify = should_classify
        self.i = i

    def listen(self):
        # return input('> ')
        self.p = pyaudio.PyAudio()
        stream = self.p.open(format=Listener.FORMAT, channels=Listener.CHANNELS, rate=Listener.RATE, input=True, frames_per_buffer=Listener.CHUNK)

        self.loop(stream)

        stream.close()
        self.p.terminate()

        if self.should_classify:
            return Listener.classify()

        return None

    def loop(self, stream):
        is_speaking = False
        num_silent_frames = 0
        word_start_index = None
        word_end_index = None
        frames = []
        i = 0
        threshold = 700

        while True:
            frame = stream.read(Listener.CHUNK)
            frames.append(frame)
            number = math.sqrt(abs(audioop.avg(frame, 4)))

            if is_speaking:
                if number < threshold:
                    # Speech is quiet.
                    num_silent_frames += 1

                    if num_silent_frames >= Listener.NUM_POST_FRAMES:
                        # Speech has stopped.
                        is_speaking = False
                        word_end_index = i
                        break
                else:
                    # Speech is continuing.
                    num_silent_frames = 0
            elif number >= threshold:
                # Speech has started.
                is_speaking = True
                word_start_index = i

            i += 1

        self.isolate(frames, word_start_index, word_end_index)

    def isolate(self, frames, word_start_index, word_end_index):
        min_frame = max(0, word_start_index - Listener.NUM_PRE_FRAMES)
        frames = frames[min_frame:word_end_index]

        if self.should_classify:
            filename = Listener.OUTPUT_FILENAME
        else:
            filename = str(self.i) + '.wav'

        wf = wave.open(filename, 'wb')
        wf.setnchannels(Listener.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(Listener.FORMAT))
        wf.setframerate(Listener.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    @staticmethod
    def classify():
        output = audioTrainTest.fileClassification(Listener.OUTPUT_FILENAME, config.MODEL_NAME, config.CLASSIFIER_TYPE)
        print(output)
        i = output[0]
        models = output[2]
        i = int(i)
        if i < 0:
            return None
        result = models[int(i)]
        print(result)
        return result
