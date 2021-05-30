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
        selected_file = input(f'Track #{track_num} (type nothing to quit): ')
        
        # Quit, if the user wants to
        if not selected_file:
            sys.exit()
    
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


custom_track_nums = False
# The path to the FLAC files should be given as a command-line argument
if len(sys.argv) < 2:
    path = input('Path to FLAC files: ')
else:
    if sys.argv[1] in ('-c', '--custom'):
        custom_track_nums = True
        
        if len(sys.argv) != 3:
            path = input('Path to FLAC files: ')
        else:
            path = sys.argv[2]
    
    else:
        
        # The path will only be taken as a command-line argument if there's nothing else provided as a command-line argument
        # This is done so that users who paste a path with spaces in it don't accidentally put in an incomplete path
        if len(sys.argv) == 2:
            path = sys.argv[1]
        else:
            path = input('Path to FLAC files: ')

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
    
    # Get track number
    if custom_track_nums:
        while True:
            track_num = input('Track # (type nothing to quit): ')
            
            # Quit if the input is empty
            if not track_num:
                sys.exit()
            
            # Validate input
            try:
                
                # Ensure that the track number is a non-negative integer
                if int(track_num) >= 0 and int(track_num) == float(track_num):
                    track_num = int(track_num)
                    break
                else:
                    print('Track number must be a non-negative integer.')

            except ValueError:
                # The user didn't input a number
                print('Track number must be a non-negative integer.')
    
    else:
        track_num = i + 1
    
    # Get the file
    file = select_file(FLAC_files, track_num)
    print(file)
    FLAC_files.remove(file)
    
    # Edit the track number
    audio = FLAC(file)
    audio['TrackNumber'] = str(track_num)
    audio.save()
    