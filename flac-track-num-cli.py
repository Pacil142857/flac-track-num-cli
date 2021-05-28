import glob
import os
import sys
from mutagen import MutagenError
from mutagen.flac import FLAC


def select_file(file_list, track_num):
    '''From a list of files, have the user select one.'''
    
    while True:
    
        # Print files
        for i, file in enumerate(file_list):
            print(f'[{i + 1}]: {file}')
        
        # Ask user which file to pick
        selected_file = input(f'Track #{track_num}: ')
    
        try:         
            # The number is too big or below 1
            if int(selected_file) > len(file_list) or int(selected_file) < 1:
                print('Invalid input. Please type in the number of the track you want to choose.')
            else:
                # Valid input
                return file_list[int(selected_file) - 1]

        except ValueError:
            # The user didn't input a number
            print('Invalid input. Please type in the number of the track you want to choose.')


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


for i in range(len(FLAC_files)):
    
    # Get the file
    file = select_file(FLAC_files, i + 1)
    print(file)
    FLAC_files.remove(file)
    
    audio = FLAC(file)
    audio['TrackNumber'] = str(i + 1)
    audio.save()
    