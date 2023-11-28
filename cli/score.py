import click
from scrapper.matches import Match
from rich.console import Console

console=Console()


@click.command()
def lscore():
    match_inform=Match().get_matchlink()
   
    print("\t\tLive Matches")
    for match_info in  match_inform:
        console.print(f'[green]Title: {match_info["title"]}[/green]')
        console.print(f'[blue]Team 1: {match_info["team1"]}, Score: {match_info["team1_score"]}[/blue]')
        console.print(f'Team 2: {match_info["team2"]}, Score: {match_info["team2_score"]}')
        console.print(f'Result: {match_info["result"]}')
        console.print(f'Status: {match_info["status"]}')
        console.print(f'Tournament: {match_info["tournament"]}')
        print(f'Link: {match_info["link"]}\n')
    
@click.group()
def cli():
    pass
cli.add_command(lscore)
if __name__ == '__main__':
    cli()