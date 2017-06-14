import subprocess


OUTPUT_FILE = './scripts/output.txt'


def run_command(command):
    subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def parse_output():
    with open(OUTPUT_FILE, 'rt') as f:
        data = f.read()
        print(data)


if __name__ == "__main__":
    run_command(f'echo 2 | python manage.py makemigrations > {OUTPUT_FILE}')
    parse_output()
