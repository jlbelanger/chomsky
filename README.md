# Chomsky

## Developing

``` bash
cp config.py.sample config.py
brew install pipenv
brew install portaudio
pipenv install
pipenv shell
python main.py
```

## Linting

``` bash
pylint *.py chomsky/*.py chomsky/commands/*.py
```

## Testing

``` bash
python -m unittest chomsky/test/*.py
```
