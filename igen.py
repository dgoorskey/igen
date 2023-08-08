"""
This program generates html code with links to a list of files.
Typical usage: `python3 igen.py *.txt > index.html`.
"""

import sys

INDEX_HTML_PREFIX = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>index</title>
</head>
<body>
    <h1>My Webbed Site</h1>
    <ul>
"""

INDEX_HTML_SUFFIX = """    </ul>
</body>
</html>"""

def eprint(message: str) -> None:
    """
    Prints a message to stderr in the form `ssg: my message`.
    """
    print(f'ssg: {message}', file=sys.stderr)

def get_file_title(file_path: str) -> str:
    """
    Given the path to a file, gets the first line in that file and returns it.
    """
    title = ''
    try:
        with open(file_path, 'r') as file:
            title = file.readline() # title is first line

    except EnvironmentError as e:
        eprint(f'failed to open {file_path}: {e}')
        sys.exit(-1)

    # strip only newlines from end of title
    while title.endswith('\n'):
        title = title[:-1]

    return title

def get_index_html(file_paths: list[str]) -> str:
    """
    Generates html code with links to all the files in `file_paths`.
    The titles of the links are given by the `get_file_title` function.
    """
    index_html = INDEX_HTML_PREFIX

    # generate nav links
    for file_path in file_paths:
        file_title = get_file_title(file_path)

        # note the path starts with '/'
        index_html += f'        <li><a href="/{file_path}">{file_title}</a></li>\n'
    
    index_html += INDEX_HTML_SUFFIX

    return index_html

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: python ssg.py [FILE]...')
        sys.exit(0)
    
    file_paths = sys.argv[1:]
    file_paths = sorted(file_paths)

    index_html = get_index_html(file_paths)
    print(index_html)
