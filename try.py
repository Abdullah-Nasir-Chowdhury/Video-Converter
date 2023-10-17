import os, sys, ffmpeg

stream = ffmpeg.input('C:/Users/HP/Desktop/PythonProjects/Video_Converter/Hackules-Recording.mkv')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'Hackules-Recording.mp4')
ffmpeg.run(stream)