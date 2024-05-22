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
    git clone https://github.com/yourusername/mrc-to-png-converter.git
    ```

2. Navigate to the repository directory:

    ```bash
    cd mrc-to-png-converter
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from the command line with the following command:

```bash
python mrc_converter.py <root_dir> [options]
