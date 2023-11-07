import argparse
import csv
import textwrap
import os
import shutil
from pathlib import Path

import gnupg


def main():
    parser = argparse.ArgumentParser(description='migrate passwords from google to Pass')
    parser.add_argument('csvfile', help='csv with passwords')
    parser.add_argument('recipients', help='gpg key id')
    parser.add_argument('--path', help='path to save passes', default='Migrate')
    csvfile = parser.parse_args().csvfile
    recipients = parser.parse_args().recipients
    path = parser.parse_args().path
    Path(path).mkdir(parents=True, exist_ok=True)
    gpg = gnupg.GPG()
    with open(csvfile, 'r') as file:
        records = csv.reader(file)
        next(records)
        for row in records:
            try:
                pass_name = f'{path}/{row[0]}.gpg'
                pass_card = textwrap.dedent(f"""\
                                    {row[3]}  # password
                                    login: {row[2]}
                                    url: {row[1]}
                                    """)
                if os.path.isfile(pass_name):
                    pass_name = f'{path}/{row[0]}-{row[2]}.gpg'

                gpg.encrypt(pass_card.encode('UTF-8'), recipients=recipients,
                            output=pass_name, always_trust=True)

            except Exception as e:
                print(e, row, sep='\n')
                shutil.rmtree(path)
                break


if __name__ == '__main__':
    main()
