## Python Video Compressor.

This Python script compresses videos in a specified folder, adjusting the resolution to 720p HD, the frame rate to 30 fps, and applying specific encoding to optimize file size without significantly compromising quality. Videos longer than 60 seconds are moved to a review folder without being compressed. The script uses `ffmpeg` for compression and `moviepy` for video manipulation and analysis.

### Prerequisites

To run this script, you need Python installed on your system, along with the following dependencies:

- `ffmpeg`: A command-line tool for processing multimedia.
- `moviepy`: A Python library for video editing.

You can install `moviepy` using pip:

```bash
pip install moviepy
```

`ffmpeg` must be installed and accessible from your system's PATH. See the [official ffmpeg documentation](https://ffmpeg.org/download.html) for installation instructions specific to your operating system.

### Usage

1. **Configure the Script**: Open the script in a text editor and ensure the folder paths (`ruta_carpeta` and `carpeta_revision`) are accessible and correct for your file system.

2. **Run the Script**: Open a terminal or command line, navigate to the directory where the script is located, and execute it with Python:

    ```bash
    python video_compressor.py
    ```

3. **Enter Folder Paths**: The script will prompt you to enter the path of the folder where the videos to be compressed are located and the review folder for videos that exceed the maximum allowed duration.

### How It Works

The script performs the following operations:

- Searches for all `.mp4` files in the specified folder and its subfolders.
- Checks the duration of each video using `moviepy`. If the duration exceeds 60 seconds, the video is moved to the review folder.
- Videos that do not exceed the duration limit are compressed using `ffmpeg`, adjusting the resolution, frame rate, video codec, video bitrate, preset, video profile, audio codec, and audio bitrate as specified in the `ffmpeg` command.
- Attempts to delete the original file after compression, retrying up to 5 times in case of permission errors.

### Important Notes

- Ensure you have enough disk space for the compressed videos, as the script does not delete the original files until after compression is successful.
- Deletion of original files may fail if they are being used by another process or if there are permission issues.

### Contributions

If you wish to contribute to the improvement of this script, consider cloning the repository and submitting your changes via pull requests. Make sure to follow best coding practices and include clear comments in your modifications.