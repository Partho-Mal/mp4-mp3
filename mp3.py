import os
import subprocess

# Path to the folder containing MP4 files
input_folder = r"C:\Users\night\Videos\Video-1"
output_folder = r"C:\Users\night\Videos\mp3"  # Optional, for saving MP3 files separately

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through every file in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mkv"):
        # Define the input MP4 file path
        input_file = os.path.join(input_folder, filename)
        
        # Define the output MP3 file path
        output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.mp3")
        
        # Convert MP4 to MP3 using ffmpeg
        command = ["ffmpeg", "-i", input_file, "-q:a", "0", "-map", "a", output_file]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Print out ffmpeg output for debugging
        print(result.stdout)
        print(result.stderr)

print("Conversion complete!")






