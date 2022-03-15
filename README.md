# Chomsky

## Development

### Setup

``` bash
cp config.py.example config.py
brew install pipenv
brew install portaudio
pipenv install
```

### Run

``` bash
pipenv shell
python main.py
```

### Record

``` bash
pipenv shell
python main.py record
```

### Train

``` bash
pipenv shell
python main.py train
```

## Lint

``` bash
pylint *.py chomsky/*.py chomsky/commands/*.py
```

## Test

``` bash
python -m unittest chomsky/test/*.py
```

## Add a command

Create a new file at `chomsky/commands/_wakeup/x.py` (where `x` is the name of the command).

Run `record` to record trigger files. Place the files in `sounds/commands/x`.
