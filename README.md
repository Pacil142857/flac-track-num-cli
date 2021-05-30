# FLAC-Track-Num-CLI

This is a quick-and-dirty CLI tool written in Python to quickly edit the track number of multiple FLAC files at once.

## Usage

Run the program from CLI, like this: `py flac-track-num-cli.py`. If you want to use custom track numbers (i.e. the program won't start from 1 and go up), then add `-c` or `--custom` as a command-line argument right after the filename. You can also specify the path to the FLAC files as a command-line argument (make sure to encapsulate it with quotes if there are spaces in the path). Examples of using this might look like: `py flac-track-num-cli.py -c /path/to/FLAC/files`, `py flac-track-num-cli.py /path/to/FLAC/files`.

Once you run the program, simply go through the prompts.
