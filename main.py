"""
Asks the user for input to generate a password
"""

from getpass import getpass
from argparse import ArgumentParser
from generate import Pass
from pyperclip import copy


def main(argsv):
    """Main function"""
    name = input("name: ")
    site = input("site: ")
    master = getpass("pass: ")

    length = argsv.length
    counter = argsv.counter
    rules = ["lowercase", "uppercase", "digits", "symbols"]
    if argsv.exclude_paypal:
        exclude = "`~-_=+[]\\{|};:'\",<.>/?"
    elif argsv.exclude_paypal:
        exclude = "`\\|'\"<>"
    else:
        exclude = argsv.exclude

    password = Pass(name, site, master, length,
                    counter, rules, exclude).password

    copy(password)


if __name__ == "__main__":
    parser = ArgumentParser(description="")
    parser.add_argument("-l", "--length", type=int, default=16,
                        help="Set the length of your password (default: 16)")
    parser.add_argument("-c", "--counter", type=int, default=0,
                        help="Set a counter for you generated password (default: 0)")
    parser.add_argument("-e", "--exclude", type=str, default="",
                        help="Select characters you wish to exclude")
    parser.add_argument("--exclude-paypal", dest="exclude_paypal", default=False,
                        action="store_true", help="Special exclude characters for paypal")
    parser.add_argument("--exclude-hetzner", dest="exclude_paypal", default=False,
                        action="store_true", help="Special exclude characters for hetzner")
    args = parser.parse_args()

    main(args)
