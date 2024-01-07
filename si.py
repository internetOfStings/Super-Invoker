#!/usr/bin/env python3
import argparse
import os
import subprocess

open_file = True # Used to determine if the file can be opened with si, used in the final line of code
audio_formats = ['.mp3', '.wav', '.acc', '.falc', '.ogg', '.wma', '.aiff', '.m4a', '.ape']
video_formats = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.3gp', '.3g2', '.mpeg', '.ogv']
image_formats = ['.jpeg', '.jpg', '.png', '.ico', '.JPEG', '.JPG', '.PNG', '.ICO']
office_formats = ['.doc', '.docx', '.docm', '.xls', '.xlsx', '.xlsm', '.ppt', '.pptx', '.pps', '.ppsx', '.pptm', '.ppsm', '.odt', '.ods', '.odp']


# Set program to be used
audio_player = 'mpv'
video_player = 'mpv'
image_viewer = 'sxiv'
office_suite = 'libreoffice'
pdf_viewer = 'evince'
web_browser = 'firefox'

# Set flags
audio_perameters = ['-no-video']
video_perameters = ['-fullscreen']
image_perameters = ['-f']
office_perameters = ['']
pdf_perameters = ['--fullscreen']
browser_perameters = ['']


# Passes arguments to the CLI program. IDEA: parser.add_argument('-a', '-auto'), Set document to auto compile.
parser = argparse.ArgumentParser()
parser.add_argument('file_to_open')
args = parser.parse_args()

# Splits the file name into a tuple containing the file name and extension
file_tuple = os.path.splitext(args.file_to_open)


if file_tuple[1] in image_formats:
	program = image_viewer
	perameters = image_perameters
elif file_tuple[1] in video_formats:
	program = video_player
	perameters = video_perameters
elif file_tuple[1] in audio_formats:
	program = audio_player
	perameters = audio_perameters
elif file_tuple[1] == '.pdf':
	program = pdf_viewer
	perameters = pdf_perameters
elif file_tuple[1] in ['.html', '.htm']:
	program = web_browser
	perameters = browser_perameters
elif file_tuple[1] in office_formats:
	program = office_suite
	perameters = office_perameters
else:
	print('This file cannot be opened with si')
	open_file = False

# Opens file with the program associated with the extension
if open_file: subprocess.call([program, args.file_to_open] + perameters)
