# linkizator

## What

Python script that Converts user-provided link and text into HTML `<a>` tag hyperlink.

The repository includes the code, 2 sample files and the .exe + .exe required materials in `\dist`.

## How to run

If you have Python, just run the .py standalone file.

If you don't, run the `linkizator.exe` file inside `\dist`, making sure that the rest of `\dist` is there to support it. It should open inside the command line for Windows.

*Caveat: you won't be able to copy-paste input with more than 1 line into the command line.*

## Why

*Ulterior motive: it was just really good practice for basic Python. Feedback welcome.*

To quickly generate HTML links.

Basically, it joins 2 lists or listy strings (and/or listy files) into 1 listy string + some more pre-defined string (aforementioned HTML `<a>` tag.).

It's also filled with humorous user prompts.

## How

### Input

Prompts user to submit 1 or more links, and 1 or more texts.

* Links can be a varying part of an URL (e.g.: `a-page-name` in `www.website.com/a-page-name`).
* Because each link will be joined with its text twin, the user has to make sure link #1 matches text #1, #2 matches #2 and so on and so forth.

#### Accepted forms of input

1. Comma-separated string
1. New-line-separated string
1. .txt file (same folder or path from current directory)
1. .csv file with one or more "columns" (same folder or path from current directory)

### What it actually does

1. Turns input into Python list;
1. Gives user feedback and exits execution when input can't be worked with;
1. Asks user if there's anything to be added to the links (e.g.: fixed part of URL, such as the base website);
1. Asks user the preferred form of output;
1. Spits the output.

### Output

1 or more hyperlinks:

1. Printed in the command-line;
1. In a .txt file in current directory.

## FAQ

*Not that anyone asked anyway.*

**How to make a Windows executable from a Python script?**

TL;DR: using [py2exe](https://github.com/py2exe/py2exe).

**Are any modules used?**

Yes, [CSV](https://docs.python.org/3/library/csv.html).

**Why not pandas?**

My dog ate the link between Anaconda, VS Code and pandas.

**That's terrible code?!1**

Sorry, thanks for the feedback, feel free to share some tips if you have any.
