#!/usr/bin/python

from moviepy.editor import *
from os.path import *
import getopt
import sys

extensions = ['mp4', 'mp3', 'wav']

command_arguments = sys.argv

argument_list = sys.argv[1:]
short_options = 'f:c:'
long_options = ['file=', 'convert=']

arguments, values = getopt.getopt(argument_list, short_options, long_options)

if len(command_arguments) <= 1:
    print('\nUsage script.py --file=file-path --convert=mp3/wav')
    exit()
else:
    file_name = arguments[0][1]
    convert_to = arguments[1][1]

source_file_name = file_name.split('.')[0]
source_file_extension = file_name.split('.')[1]

if source_file_extension == convert_to:
    print('Convert argument value should not be the same with the selected file extension!')
    exit()

# check if file found or not
file_path = os.getcwd() + '\\' + file_name
if not os.path.isfile(file_path):
    print('\nSelected file not found!')
    print('\nProgram stopped..')
    exit()

print(f'\nSelected file : {file_name}')
print(f'Converting to : {convert_to}\n\n')

video = VideoFileClip(file_name)

for extension in extensions:
    if convert_to == extension:
        video.audio.write_audiofile(source_file_name + '.' + convert_to)

        print(f"Successfully converting from {source_file_extension} to {convert_to}")
