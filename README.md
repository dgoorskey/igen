# igen

i(ndex)gen generates an html page with links to other files.
usually you would use it to generate an `index.html` page for a directory of
html, text, or media files.

## dependencies

python 3.6+

## installation

download `igen.py`.

## usage

- `igen.py` takes as arguments a list of files, and writes html to stdout.
  - for example: `python3 igen.py a.txt b.txt c.txt`.
- to generate an `index.html` for a bunch of text files in the current
  directory: `python3 igen.py *.txt > index.html`.
- to generate an `index.html` for a bunch of text files in a subdirectory:
  `python3 igen.py mydir/*.txt > index.html`
- to do both: `python3 igen.py *.txt mydir/*.txt > index.html`

## how links are generated

1. file paths passed in as arguments are sorted alphabetically.
   if you're making a blog, i recommend prefixing your filenames with iso-8601
   dates.
2. file paths are prepended with `/` to make them absolute paths.
   be mindful about where your working directory is.
3. the first line of each file is taken to be its title
4. a link of the form `<a href="/path/to/myfile.txt">my file's title</a>` is
   generated for each file.
