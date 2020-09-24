import click

@click.group()
def first():
    print("hello world")

@click.command()
@click.option("--name", help="the name")
def second(name):
    print("this is second: {}".format(name))

@first.command()
def third():
    print("this is third")

def main():

    first.add_command(second)
    first.add_command(third)
    second()

if __name__ == '__main__':
    main()