import click

from apps.api.context import Context
from apps.api.domain import commands, exceptions, models
from apps.api.service_layer import handlers

context = Context()


@click.group()
def cli():
    pass


@click.command()
@click.argument("id")
def get(id):
    click.echo(f"Get Person by id {id!r}")
    command = commands.GetPerson(id=id)
    try:
        click.echo(context.messagebus.handle(command).json())
    except exceptions.EntityNotFound as e:
        click.echo(f"Person not found by id {id!r}")


@click.command()
@click.argument("name")
@click.argument("age")
def add(name, age):
    click.echo(f"Add Person named {name!r} age {age!r}")
    person = models.PersonModel(name=name, age=age)
    command = commands.AddPerson(person=person)
    click.echo(context.messagebus.handle(command).json())


cli.add_command(get)
cli.add_command(add)


if __name__ == "__main__":
    cli()