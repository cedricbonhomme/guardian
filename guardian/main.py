#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
from datetime import datetime
from yaml import load, CLoader
from jinja2 import Template

from . import conf
from . import notification


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
    """Main function responsible to trigger the tests."""
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
        help="Send notification of failed test(s) via email.",
    )
    parser.add_argument(
        "--irc",
        dest="irc_notification",
        action="store_true",
        help="Send notification of failed test(s) via IRC.",
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
            "nb_test": len(services[service]["tests"]),
        }
        print("+ " + service)
        for test in services[service]["tests"]:
            print(" - " + test)
            if services[service]["tests"][test].get("disabled", False):
                # test disabled in the configuration file, skip it
                print("     Test disabled in the configuration file.")
                continue
            cmd = services[service]["tests"][test]["probe"]
            expected = services[service]["tests"][test]["expected"]
            # print("   - " + cmd)
            # print("   - " + expected)
            result = exec_cmd(cmd)
            if result == expected:
                results.append(True)
                print("     ✅")
            else:
                results.append(False)
                all_errors.append((service, test))
                report["is_ok"] = False
                report["errors"].append(test)
                print("     ❌")

        reports.append(report)

    end_date = datetime.now()
    print("Execution time: {} seconds.".format((end_date - start_date).total_seconds()))

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

        if arguments.irc_notification:
            print("Sending IRC notification...")
            for error in all_errors:
                notification.irker(
                    "Error for service '{}'. Test: {}".format(error[0], error[1])
                )

    if arguments.html_report:
        print("Generating HTML status page...")
        template = Template(open("guardian/templates/report.html").read())
        outputHTML = template.render(
            reports=reports, end_date=end_date, time=end_date - start_date
        )
        with open("reports/index.html", "w") as f:
            f.write(outputHTML)


if __name__ == "__main__":
    # Point of entry in execution mode.
    run()
