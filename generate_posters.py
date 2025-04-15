import os
import subprocess

# Paths
video_dir = ""
output_dir = ""

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Walk through the video directory and its subdirectories
for root, _, files in os.walk(video_dir):
    for file in files:
        if file.endswith(".mp4"):
            video_path = os.path.join(root, file)
            output_file = os.path.join(
                output_dir, os.path.splitext(file)[0] + ".png"
            )

            # Generate the poster image using ffmpeg
            try:
                subprocess.run(
                    [
                        "ffmpeg",
                        "-i",
                        video_path,
                        "-ss",
                        "00:00:01.000",
                        "-vframes",
                        "1",
                        output_file,
                    ],
                    check=True,
                )
                print(f"Generated poster: {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"Error generating poster for {video_path}: {e}")
