import glob
import os
import sys
from mutagen import MutagenError
from mutagen.flac import FLAC


# The path to the FLAC files should be given as a command-line argument
if len(sys.argv) != 2:
    path = input('Path to FLAC files: ')
else:
    path = sys.argv[1]

# Go to the path where the FLAC files are
try:
    os.chdir(path)
except FileNotFoundError:
    print('That directory can\'t be found. The program is terminating.')
    sys.exit()
    
FLAC_files = []

# Get the FLAC files
for file in glob.glob('*.flac'):
    FLAC_files.append(file)
        
if not FLAC_files:
    # No FLAC files found, so terminating program
    print('No FLAC files were found. The program is terminating.')
    sys.exit()
