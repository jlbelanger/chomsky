import glob
from pyAudioAnalysis import audioTrainTest
import config

class Trainer():
    @staticmethod
    def train():
        paths = Trainer.paths()
        mid_window = 1.0
        mid_step = 1.0
        audioTrainTest.featureAndTrain(paths, mid_window, mid_step, audioTrainTest.shortTermWindow, audioTrainTest.shortTermStep, config.CLASSIFIER_TYPE, config.MODEL_NAME)

    @staticmethod
    def paths():
        return glob.glob('sounds/commands/*')
