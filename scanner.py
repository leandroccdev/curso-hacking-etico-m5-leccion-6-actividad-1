from argparse import ArgumentParser
from colorama import Fore, Style
from datetime import datetime
from ipaddress import ip_network, IPv4Network
from nmap.nmap import PortScanner
from sys import argv, exit
from typing import NoReturn, Tuple
import re

def error(msg: str, terminate=True) -> NoReturn:
    '''Prints a message an terminate program.'''
#<
    print(f"{Style.BRIGHT}{Fore.RED}[Error]{Style.RESET_ALL} {msg}")
    exit(1)
#>

def info(msg: str) -> None:
    '''Prints an info message.'''
#<
    print(f"{Style.BRIGHT}{Fore.YELLOW}[Info]{Style.RESET_ALL} {msg}")
#>

def get_date_time() -> Tuple[str, str]:
    '''Retrieve current date and time as (DD-MM-YYYY, HH:MM:SS).'''
#<
    now: datetime.datetime = datetime.now()
    return (now.strftime("%d-%m-Y"), now.strftime("%H:%M:%S"))
#>

def scan(network: str, ports: str='-') -> None:
    '''Scans a network and prints a resume.

    Arguments:
        - network (str): X.X.X.X/YY
        - ports (str): [PORT|START-END|A,B,C]
    '''
#<
    info("Scanning...")
    ps: PortScanner = PortScanner()
    r: dict = ps.scan(network, arguments='-sV', ports=ports)
    output: str = f"Command executed: {r['nmap']['command_line']}\n\n"

    # Analizes scan results
    active_hosts: dict = r["nmap"]["scanstats"]["uphosts"]
    for host,hscan in r["scan"].items():
        output += f"{Style.BRIGHT}Host:{Style.RESET_ALL} {host}\n"

        # Analizes port scans results
        #<
        for port,pscan in hscan["tcp"].items():
            product:str = pscan["product"]
            version:str = pscan["version"]
            extra:str = pscan["extrainfo"]
            port_details:str = f"{product} {version} {extra}"
            state:str = pscan["state"]

            # Sets status color
            #<
            match state:
                case "closed":
                    state = f"{Fore.RED}{state}{Style.RESET_ALL}"
                case "open":
                    state= f"{Fore.GREEN}{state}{Style.RESET_ALL}"
                case "filtered" | "unfiltered" | "closed|filtered" | "open|filtered":
                    state = f"{Fore.WHITE}{state}{Style.RESET_ALL}"
            #>

            output += f"- {Style.BRIGHT}Port:{Style.RESET_ALL} {port} -> {state}\n"

            # Adds empty details
            #<
            if port_details.replace(" ", ""):
                port_details = f"{Fore.YELLOW}{port_details}{Style.RESET_ALL}"
                output += f"   {port_details}\n"
            #>
        #>

    # Adds final info to report
    _date, _time = get_date_time()
    output += f"\n\n"
    output += f"Date: {_date}\n"
    output += f"Time: {_time}\n"
    output += f"\nActive Hosts: {active_hosts}"
    print(output)

#>

def main():
    #<
    # CLI Parameters
    #<
    ap = ArgumentParser(
            add_help = True,
            description="Modulo 5 - Lección 6 - Actividad 1: escaneo automatizado con nmap."
        )
    ap.add_argument(
            "-n",
            "--network",
            action="store",
            dest="network",
            help="Red IPV4 a analizar en formato XXX.XXX.XXX.XXX/YY"
        )
    ap.add_argument(
            "-p",
            "--ports",
            action="store",
            default="-",
            dest="ports",
            help="Puerto/s a analizar en formato [PORT|START-END|A,B,C]"
        )
    args = ap.parse_args()
    #>

    if not args.network:
        error("Network not given!")

    # Validate network
    try:
        network: IPv4Network = ip_network(args.network)
    except ValueError as e:
        error(str(e))

    # Validate port
    port_match = re.match(
            r"^(?:[0-9]{1,5}|[0-9]{1,5}-[0-9]{1,5}|(?:[0-9]{1,5},?)+)$",
            args.ports
        )
    if not port_match:
        error("Wrong port format!")

    # Start scan
    scan(args.network, args.ports)
    #>

if __name__ == '__main__':
    #<
    try:
        main()
    except KeyboardInterrupt:
        error("Aborted...")
    #>
