#!/usr/bin/env python3

import argparse
import ipaddress
import sys


def get_addresses(path, excluded):
    scope = []

    with open(path) as file:
        lines = [line.strip() for line in file]

    for line in lines:
        try:
            ip = ipaddress.IPv4Address(line)
            if str(ip) not in excluded:
                scope.append(str(ip))
        except:
            try:
                cidr = ipaddress.IPv4Network(line)
                for ip in cidr:
                    if str(ip) not in excluded:
                        scope.append(str(ip))
            except:
                print('[-] Line "' + line + '" is not a valid CIDR or IPv4 address', file=sys.stderr)
                exit(1)
    return scope


def cli(args):
    excluded = []

    if args.exclude:
        excluded = get_addresses(args.exclude, [])

    for ip in get_addresses(args.include, excluded):
        print(ip)


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(add_help=True, description='Computes a list of IP addresses from inclusion and exclusion lists')
        parser.add_argument('include', help='File with IP address or range per line to include')
        parser.add_argument('-exclude', help='File with IP address or range per line to exclude')
        args = parser.parse_args()
        cli(args)
    except KeyboardInterrupt:
        exit(1)
