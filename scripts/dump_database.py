import os


def main():
    for root, dirs, files in os.walk('v1'):
        if root[-10:] == 'migrations':
            for f in [file for file in files if file[:2] == '00']:
                os.remove(os.path.normpath(os.path.join(root, f)))
            create_init_file(root)


def create_init_file(root):
    init_file = os.path.normpath(os.path.join(root, '__init__.py'))
    if not os.path.exists(init_file):
        with open(init_file, 'wt') as f:
            f.write('')


def remove_database():
    if os.path.exists('db.sqlite3'):
        os.remove('db.sqlite3')
        print('Database removed')
    else:
        print('No database to remove')


if __name__ == "__main__":
    main()
    remove_database()
