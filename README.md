# YouTube Video Downloader

![GitHub Logo](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)

## Purpose
The purpose of this project is to enhance my Python programming skills, particularly focusing on the use of the Tkinter library. This YouTube Video Downloader is built entirely with Python and provides a simple yet efficient way to download videos from YouTube.

## Features
- User-friendly interface powered by Tkinter
- Ability to download videos from YouTube with ease
- Supports various video formats and resolutions

## How to Use (Using the App)
1. Download the repository and extract it to a folder.
2. Run `YouTubeVidDownloader.exe` to launch the application.
3. Enter the URL of the YouTube video you want to download and select the desired format/resolution.
4. Click the download button to save the video to your local storage.

## How to Use (Using the Source Code)
1. Clone or download the repository to your local machine.

2. Ensure you have Python installed.
   - If you don't have Python installed, download it from the [official Python website](https://www.python.org/downloads/) and follow the installation instructions.

3. Install the necessary dependencies by running the following commands in your terminal or command prompt:

   - `time`: This library is part of Python's standard library and doesn't require separate installation.

   - `tkinter` (imported as `tk`) and `ttk` from `tkinter`: These libraries are used for creating graphical user interfaces (GUI) and are included with Python, but in some cases, you might need to install the Tcl/Tk libraries separately.
     - On Linux:
       ```bash
       sudo apt-get install python3-tk
       ```
     - On macOS:
       ```bash
       brew install python-tk
       ```
     - On Windows, the libraries should be included with the Python installation.

   - `pytube` (imported as `YouTube`): This library is used for downloading YouTube videos.
     ```bash
     pip install pytube
     ```

   - `threading`: This library is part of Python's standard library and doesn't require separate installation.

   - `os`: This library is part of Python's standard library and doesn't require separate installation.

   - `PIL` (imported as `Image` and `ImageTk`): This library is used for working with images.
     ```bash
     pip install Pillow
     ```

   - `filedialog` from `tkinter`: This library is part of `tkinter` and doesn't require separate installation.

4. Run the application using the following command in your terminal or command prompt:

   ```bash
   python main.py


## Known Bugs
Some resolutions may not work due to codec issues. This will be resolved soon.

## Source Code
The source code for this project is available in the [source branch](https://github.com/NanoTom/YouTubeVidDownloader-Python/tree/source).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
