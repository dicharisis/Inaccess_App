
import click 
from datetime import datetime
from src.application import APP
import sys

now = datetime.utcnow()
Ending_period = now.strftime("%Y%m%dT%H%M%SZ")    


@click.group()
def cli():
    pass

@cli.command()
@click.option('--period', 
               type=str,                         
               help='Period should be 1h 1d 1mo 1y', 
               default='1h')

@click.option('--tz', 
               type=str,                         
               help='TimeZone should be one of pytz.all_timezones()', 
               default='Europe/Athens')


@click.option('--t1', 
               type=str,                         
               help='Starting period in format YYYYmmddTHHMMSSZ', 
               default='20000101T000000')

@click.option('--t2', 
               type=str,                         
               help='Ending period in format YYYYmmddTHHMMSSZ', 
               default=Ending_period)

                                             
def main(period,tz,t1,t2):
    try:
        thread = APP(period,tz,t1,t2)
        thread.run()
        sys.exit(0)
    except:
        sys.exit(10)
        