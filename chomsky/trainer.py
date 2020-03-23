import glob
import os
import time
from pyAudioAnalysis import audioTrainTest
import config

class Trainer():
    @staticmethod
    def should_train():
        if not os.path.isfile(config.MODEL_NAME + '-timestamp'):
            return True

        latest_time = Trainer.get_time()
        if not latest_time:
            return True

        files = glob.glob('sounds/commands/**/*.wav')
        for file in files:
            t = os.path.getmtime(file)
            if t > latest_time:
                return True

        return False

    @staticmethod
    def train():
        paths = glob.glob('sounds/commands/*')
        mid_window = 1.0
        mid_step = 1.0
        audioTrainTest.featureAndTrain(paths, mid_window, mid_step, audioTrainTest.shortTermWindow, audioTrainTest.shortTermStep, config.CLASSIFIER_TYPE, config.MODEL_NAME)

        Trainer.set_time()

    @staticmethod
    def get_time():
        with open(config.MODEL_NAME + '-timestamp', 'r') as f:
            lines = float(f.read())
            f.close()
            return lines
        return ''

    @staticmethod
    def set_time():
        with open(config.MODEL_NAME + '-timestamp', 'w') as f:
            f.write(str(time.time()))
            f.close()
