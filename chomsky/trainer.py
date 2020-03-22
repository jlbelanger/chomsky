import glob
import os
from pyAudioAnalysis import audioTrainTest
import config

class Trainer():
    @staticmethod
    def should_train():
        return not os.path.isfile(config.MODEL_NAME)

    @staticmethod
    def train():
        paths = glob.glob('sounds/commands/*')
        mid_window = 1.0
        mid_step = 1.0
        audioTrainTest.featureAndTrain(paths, mid_window, mid_step, audioTrainTest.shortTermWindow, audioTrainTest.shortTermStep, config.CLASSIFIER_TYPE, config.MODEL_NAME)

