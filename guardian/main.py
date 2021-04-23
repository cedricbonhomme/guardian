#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
from yaml import load, CLoader


def exec_cmd(cmd):
    """Execute a command."""
    bash_string = r"""#!/bin/bash
    {}
    """.format(
        cmd
    )
    result = subprocess.check_output(
        bash_string, shell=True, executable="/bin/bash", text=True
    )
    return result.strip()


def run():
    parser = argparse.ArgumentParser(prog="guardian")

    parser.add_argument(
        "-c",
        "--config",
        dest="config_file",
        required=True,
        help="Configuration file (YAML).",
    )

    arguments = parser.parse_args()

    with open(arguments.config_file, "r") as f:
        stream = f.read()
        data = load(stream, Loader=CLoader)

    # Go through all checks
    services = data["services"]
    for service in services:
        print("+ " + service)
        for check in services[service]["checks"]:
            print(" - " + check)
            cmd = services[service]["checks"][check]["probe"]
            expected = services[service]["checks"][check]["expected"]
            # print("   - " + cmd)
            # print("   - " + expected)
            result = exec_cmd(cmd)
            if result == expected:
                print("     -> " + "OK")
            else:
                print("     -> " + "KO")


if __name__ == "__main__":
    # Point of entry in execution mode.
    run()
