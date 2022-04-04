from unicodedata import name
from crud import crud


if __name__== "__main__":
    crud.delete('pessoas', 'nome', 'Guilherme' )