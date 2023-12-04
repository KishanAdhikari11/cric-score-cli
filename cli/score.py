import click
from scrapper.matches import Match
from rich.console import Console
from rich.table import Table

console=Console()


@click.command()
def lmatches():
    match_info=Match().get_matchlink()
    console.print("\t\tLive Matches")
    for match in match_info:
        console.print(f'🏏[bold cyan]{match["tournament"]}[/bold cyan]')
        console.print(f'{match["team1"]} vs {match["team2"]}\n\n')
    

@click.command()
def lscore():
    match_inform=Match().get_matchlink()
    for match_info in  match_inform:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Title", style="cyan", no_wrap=True)
        table.add_column(match_info['title'], justify="right", style="green")
        table.add_row(match_info['team1'],match_info['team1_score'])
        table.add_row(match_info['team2'],match_info['team2_score'])
        table.add_row('Result',match_info['result'])
        console.print(table)



@click.group()
def cli():
    pass
cli.add_command(lscore)
cli.add_command(lmatches)
if __name__ == '__main__':
    cli()