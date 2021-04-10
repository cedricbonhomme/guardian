#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from yaml import load, CLoader


def run():
    parser = argparse.ArgumentParser(prog='guardian')

    parser.add_argument("-c", "--config", dest="config_file",
                    required=True, help="Configuration file (YAML).")

    arguments = parser.parse_args()


    with open(arguments.config_file, "r") as f:
        stream = f.read()
        data = load(stream, Loader=CLoader)

    services = data["services"]
    for service in services:
        print("+ " + service)
        for check in services[service]["checks"]:
            print(" - " + check)


if __name__ == "__main__":
    # Point of entry in execution mode.
    run()
