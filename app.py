import subprocess
import os


def convert_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lane"
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Successfully converted!")
    except subprocess.CalledProcessError as e:
        print("Conversion failed!")


convert_to_mp3('Hackules-Recording.mkv', 'audio.mp3')