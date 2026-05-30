# Made by OlegQWERTY8364

import socket
import sys
from concurrent.futures import ThreadPoolExecutor

def scan(ip, port):
    try:
        with socket.socket() as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                print(f"{port}/tcp open")
    except Exception:
        pass

def parse(arg):
    for p in arg.split(','):
        if '-' in p:
            start, end = map(int, p.split('-'))
            yield from range(start, end + 1)
        else:
            yield int(p)

if __name__ == "__main__":
    ip = socket.gethostbyname(sys.argv[1])
    with ThreadPoolExecutor(200) as ex:
        for port in parse(sys.argv[2]):
            ex.submit(scan, ip, port)