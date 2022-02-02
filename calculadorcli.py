from typer import Typer
from colorama import Fore, Style

app = Typer()

@app.command()
def sum(n1: float, n2: float):
    """
    => add number
    """
    print(f'{Fore.GREEN}sum: {n1 + n2}{Style.RESET_ALL}')

@app.command()
def sub(n1: float, n2: float):
    """
    => subtract number
    """
    print(f'{Fore.GREEN}sub: {n1 - n2}{Style.RESET_ALL}')

@app.command()
def mul(n1: float, n2: float):
    """
    => multiply number
    """
    print(f'{Fore.GREEN}mul: {n1 * n2}{Style.RESET_ALL}')

@app.command()
def div(n1: float, n2: float):
    """
    => divide number
    """
    print(f'{Fore.GREEN}div: {n1 / n2}{Style.RESET_ALL}')

if __name__ == '__main__':
    app()
