# Assuming video and corresponding srts are present in current directory
import os
import re
from typing import List

def is_type_of(filename: str, file_ext: List[str]=None) -> bool:
    if file_ext == None:
        file_ext = ['mkv', 'mp4']
    
    for ext in file_ext:
        if filename.lower().endswith(ext):
            return True
    
    return False


season_episode_re = re.compile(r'[sS]\d{2}[eE]\d{2}')

files = os.listdir()
videos = list(filter(lambda file: is_type_of(file, ['mkv']), files))
subs = list(filter(lambda file: is_type_of(file, ['srt']), files))

video_file_names = {}
for v in videos:
    m = season_episode_re.findall(v)
    # remove extension
    video_file_names[m[0].lower()] = os.path.splitext(v)[0]

sub_file_names = {}
for v in subs:
    m = season_episode_re.findall(v)
    sub_file_names[m[0].lower()] = v

for season_episode_number, curr_sub_filename in sub_file_names.items():
    # get the video file names and add `.srt`
    new_sub_name = video_file_names[season_episode_number.lower()] + '.srt'
    os.rename(curr_sub_filename, new_sub_name)
