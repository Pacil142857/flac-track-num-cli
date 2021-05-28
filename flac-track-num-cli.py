import os
import sys
from mutagen import MutagenError
from mutagen.flac import FLAC


# The path to the FLAC files should be given as a command-line argument
if len(sys.argv) != 2:
    path = input('Path to FLAC files: ')
else:
    path = sys.argv[1]

FLAC_files = []

try:
    for filename in os.listdir(path):
        if filename.endswith('.flac'):
            FLAC_files.append(filename)
except:
    # TODO: Determine exceptions raised by this and print a proper error message instead of just continuing
    pass