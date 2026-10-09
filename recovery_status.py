"""Display the practice archive's recovery status using the installed Cowsay."""

from pathlib import Path
import subprocess


def main():
    """Report whether the saved recovery result is ready to inspect."""
    result = Path('whitehouse_secrets/whitehouse_secrets.txt')
    if result.is_file() and result.stat().st_size:
        message = 'Saved file found. Open it to verify recovery: ' + str(result)
    else:
        message = 'No recovery output yet. Try the candidate passwords.'
    try:
        subprocess.run(['cowsay', message], check=True)
    except (OSError, subprocess.CalledProcessError):
        print(message)


if __name__ == '__main__':
    main()
