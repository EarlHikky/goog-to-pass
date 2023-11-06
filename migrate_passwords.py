import argparse
import csv
import textwrap

import gnupg


def main():
    parser = argparse.ArgumentParser(description='migrate passwords from google to Pass')
    parser.add_argument('csvfile', help='csv with passwords')
    parser.add_argument('recipients', help='gpg key id')
    csvfile = parser.parse_args().csvfile
    recipients = parser.parse_args().recipients
    gpg = gnupg.GPG()
    with open(csvfile, 'r') as file:
        records = csv.reader(file)
        next(records)
        for row in records:
            pass_card = textwrap.dedent(f"""\
                                    {row[3]}
                                    login: {row[2]}
                                    url: {row[1]}
                                    """)

            gpg.encrypt(pass_card, recipients=recipients,
                        output=f'Chrome/{row[0]}.gpg', always_trust=True)


if __name__ == '__main__':
    main()
