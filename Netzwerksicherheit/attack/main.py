import os
import tqdm
import click
import socket
import ipaddress

from icmplib import ping
from typing import List, Tuple


PORT_RANGE_MIN = 1
PORT_RANGE_MAX = 1024


def port_is_open(ip: str, port: int) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, port))   
        s.close()
        result = True
    except Exception:
        result = False

    return result


def get_open_ports(ip: str) -> List[int]:
    open_ports = []

    for port in range(PORT_RANGE_MIN, PORT_RANGE_MAX):
        if port_is_open(ip, port):
            open_ports.append(port)

    return open_ports

def get_active_ip_addresses(ip_range: str) -> List[str]:
    active_ip_addresses =[]

    for ip in ipaddress.IPv4Network(ip_range):
        if ping(format(ip), privileged=False):
            print(ip)
        else:
            print("no result")

    return active_ip_addresses


def has_ssh_banner(ip: str, port: int) -> bool:
    return False


@click.command()
@click.option("--range", default="192.168.68.0/25", help="Specify the ip range you want to scan for ssh servers.")
def main(range):
    get_active_ip_addresses(range)

if __name__ == "__main__":
    main()
