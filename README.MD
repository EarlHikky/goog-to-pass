# Password Migration Tool

A Python script for migrating passwords from Google Chrome to Pass, a command-line password manager. This tool uses GPG
encryption to secure your passwords during the migration process.

## Requirements

- Python 3
- [GnuPG](https://gnupg.org/) (GPG) installed and configured

## Installation

1. Clone this repository to your local machine.

2. Install the required Python libraries using pip.

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the following command:

```bash
python migrate_passwords.py csvfile recipients
```

- `csvfile` - Path to the CSV file containing your passwords.
- `recipients` - GPG key ID for encryption.

The script will read the CSV file and encrypt each password entry using GPG, saving the encrypted files in the 'Chrome'
directory. The format of each password entry in the CSV file should be as follows:

```plaintext
URL, LOGIN, PASSWORD
```

- `URL`: The URL or website associated with the password.
- `LOGIN`: The username or email used for the login.
- `PASSWORD`: The corresponding password.

## Example

Here's an example of how to use the script:

```bash
python migrate_passwords.py passwords.csv yourgpgkeyid
```

## Acknowledgments

- This script uses the [gnupg](https://pypi.org/project/python-gnupg/) Python library for GPG encryption.

