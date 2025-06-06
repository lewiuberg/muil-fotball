import os
import subprocess

# Paths
video_dir = "./docs/assets/videos/"
output_dir = "./docs/assets/img/"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Walk through the video directory and its subdirectories
for root, _, files in os.walk(video_dir):
    for file in files:
        if file.endswith(".mp4"):
            video_path = os.path.join(root, file)

            # Skip files in the root of video_dir
            if os.path.abspath(root) == os.path.abspath(video_dir):
                print(f"Skipping file in root directory: {file}")
                continue

            # Extract subfolder name from the file name (e.g., "forsvar" from "forsvar-2.mp4")
            subfolder_name = file.split("-")[0]
            subfolder_path = os.path.join(output_dir, subfolder_name)

            # Ensure the subfolder exists
            os.makedirs(subfolder_path, exist_ok=True)

            # Define the output file path in the correct subfolder
            output_file = os.path.join(
                subfolder_path, os.path.splitext(file)[0] + ".png"
            )

            # Check if the poster already exists
            if not os.path.exists(output_file):
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
            else:
                print(f"Poster already exists: {output_file}")
