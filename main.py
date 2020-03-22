import sys
from chomsky.app import App
from chomsky.listener import Listener
from chomsky.trainer import Trainer

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        App().start()
    elif sys.argv[1] == 'record':
        i = 1
        while True:
            print('Recording...')
            Listener(False, i).listen()
            print('Saved ' + str(i) + '.wav')
            i += 1
    elif sys.argv[1] == 'train':
        Trainer.train()
