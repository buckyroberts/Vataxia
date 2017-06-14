import subprocess


OUTPUT_FILE = './scripts/output.txt'


def run_command(command):
    subprocess.run(
        command,
        shell=True,
        stderr=subprocess.PIPE,
    )


def get_issue(data):
    if 'You are trying to add a non-nullable field' in data:
        return {
            'type': 'value_needed',
            'model': data[data.find("' to ") + 5:data.find(" without ")],
            'field': data[data.find("field '") + 7:data.find("' to ")]
        }
    return {}


def handle_value_needed(issue):
    items = [
        {'model': 'profile', 'field': 'age', 'answer': '26'},
        {'model': 'profile', 'field': 'city', 'answer': "\'Pasadena\'"}
    ]
    if issue.get('type') == 'value_needed':
        for item in items:
            if issue['model'] == item['model'] and issue['field'] == item['field']:
                answer = item['answer']
                run_command(f'expect ./scripts/handle_value_needed_prompt.sh "{answer}"')


def resolve_issues():
    with open(OUTPUT_FILE, 'rt') as f:
        data = f.read()
        issue = get_issue(data)
        handle_value_needed(issue)


if __name__ == "__main__":
    run_command(f'echo 2 | python manage.py makemigrations > {OUTPUT_FILE}')
    resolve_issues()
    run_command('python manage.py migrate')
