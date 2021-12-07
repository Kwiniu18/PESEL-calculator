import click
from calculating import *
from peseldecoder import *


@click.group()
def cli():
    pass


@cli.command()
@click.argument("day", type=int)
@click.argument("month", type=int)
@click.argument("year", type=int)
@click.argument("gender", type=str)
def generate(day, month, year, gender):
    pesel_gen(day, month, year, gender)


@cli.command()
@click.argument("pesel", type=str)
def decode(pesel):
    pesel_decoder(pesel)


if __name__ == "__main__":
    cli()
