import os
import subprocess

if not os.path.exists("assets"):
    raise Exception("Please create and put all videos in assets folder!")

mkv_list = os.listdir("assets")

if not os.path.exists("results"):
    os.mkdir("results")

for mkv in mkv_list:
    name, ext = os.path.splitext(mkv)
    if ext != ".mkv":
        raise Exception("Please add MKV files only!")

    output_name = name + ".mp4"
    try:
        subprocess.run(
            ['ffmpeg', '-i', f"assets/{mkv}", "-codec", "copy",
             f"results/{output_name}"], check=True
        )
    except:
        raise Exception(
            "Please Download, Install and Add the path of FFMPEG to Environment Variable!"
        )

print(f"{len(mkv_list)} video(s) converted to MP4")
os.startfile("results")