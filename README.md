# mrc2png

# MRC to PNG Converter

This script converts MRC (Microscopy Data) files to PNG format. MRC files are commonly used in electron microscopy to store 3D volume data. Converting them to PNG format makes it easier to view and share the images.

## Features

- Converts MRC files to PNG format.
- Supports specifying root directory and wildcard patterns for MRC files.
- Allows reversing the order of frames and setting the resolution of the output PNG.

## Requirements

- Python 3.6+
- Required Python packages: `numpy`, `mrcfile`, `tifffile`, `Pillow`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/elemeng/mrc2png.git
    ```

2. Navigate to the repository directory:

    ```bash
    cd mrc2png
    ```

3. Install the rye package manager:

    Linux and macOS:

    curl -sSf https://rye-up.com/get | bash
    
    Windows:

    Download and run the installer (64bit Intel/AMD: https://github.com/astral-sh/rye/releases/latest/download/rye-x86_64-windows.exe).
4. Install dependencies

    ```bash
    rye sync
    ```
## Usage

Run the script from the command line with the following command:

```bash
python mrc_converter.py <root_dir> [options]
```

Replace <root_dir> with the path to the root directory containing the MRC files.

Options:
### -r, --reverse: Reverse the order of frames.

### -s, --resolution <resolution>: Set the resolution of the output PNG. Available options: "Full", "1920x1080", "1280x720", "640x480". Default: "Full".

### -p, --pattern <pattern>: Specify a wildcard pattern for MRC files. Default: "*.mrc". eg: -p *preview.mrc will only convert mrc file whose name endswith preview.mrc.
