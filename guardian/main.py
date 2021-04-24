#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
from datetime import datetime
from yaml import load, CLoader
from jinja2 import Template


def exec_cmd(cmd):
    """Execute a command in a sub process."""
    bash_string = r"""#!/bin/bash
    set -e
    {}
    """.format(
        cmd
    )
    result = subprocess.check_output(
        bash_string, shell=True, executable="/bin/bash", text=True
    )
    return result.strip()


def run():
    """Main function responsible to trigger the tests.
    """
    # Creates the command line parser.
    parser = argparse.ArgumentParser(prog="guardian")

    parser.add_argument(
        "-c",
        "--config",
        dest="config_file",
        required=True,
        help="Configuration file (YAML).",
    )
    parser.add_argument(
        "--email",
        dest="email_notification",
        action="store_true",
        help="Send an email in case of failed test(s).",
    )
    parser.add_argument(
        "--html",
        dest="html_report",
        action="store_true",
        help="Generate a HTML status page.",
    )

    parser.set_defaults(email_notification=False, html_report=False)

    arguments = parser.parse_args()


    # Read the configuration file
    with open(arguments.config_file, "r") as f:
        stream = f.read()
        data = load(stream, Loader=CLoader)


    # Pass through all the tests.
    results = []
    all_errors = []
    reports = []
    services = data["services"]
    start_date = datetime.now()
    for service in services:
        report = {
            "service_name": service,
            "is_ok": True,
            "errors": [],
        }
        print("+ " + service)
        for check in services[service]["checks"]:
            print(" - " + check)
            if  services[service]["checks"][check].get("disabled", False):
                # check disabled in the configuration file, skip it
                print("     Test disabled in the configuration file.")
                continue
            cmd = services[service]["checks"][check]["probe"]
            expected = services[service]["checks"][check]["expected"]
            # print("   - " + cmd)
            # print("   - " + expected)
            result = exec_cmd(cmd)
            if result == expected:
                results.append(True)
                print("     ✅")
            else:
                results.append(False)
                all_errors.append((service, check))
                report["is_ok"] = False
                report["errors"].append(check)
                print("     ❌")

        reports.append(report)
    print(reports)
    end_date = datetime.now()
    print("Execution time: {}".format(end_date - start_date))

    if all(results):
        print("✨ 🌟 ✨ All {} tests are successful.".format(len(results)))
    else:
        print(
            "{number} error{plural} occurred.".format(
                number=len(all_errors), plural="s" if len(all_errors) > 1 else ""
            )
        )
        if arguments.email_notification:
            print("Sending email notification...")
            # TODO

    if arguments.html_report:
        template = Template(open('guardian/templates/report.html').read())
        outputHTML = template.render(reports=reports, end_date=end_date)
        print()
        print(outputHTML)
        with open("reports/report.html", "w") as f:
            f.write(outputHTML)


if __name__ == "__main__":
    # Point of entry in execution mode.
    run()
