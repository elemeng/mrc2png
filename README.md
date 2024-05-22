# MRC to PNG Converter

This script converts MRC (Microscopy Data) files to PNG format. MRC files are commonly used in electron microscopy to store 3D volume data. Converting them to PNG format makes it easier to view and share the images.

## Features

- Converts MRC files to PNG format.
- Supports specifying root directory and wildcard patterns for MRC files.
- Allows reversing the order of frames and setting the resolution of the output PNG.

## Usage

1. Download the compiled executable file: `dist/mrc2png`.

2. In a terminal, navigate to where you downloaded `mrc2png`, then run:

    ```bash
    ./mrc2png <root_dir> [options]
    ```

    Replace `<root_dir>` with the path to the root directory containing the MRC files.

    ### Options:

    - `-r, --reverse`: Reverse the order of frames.
    - `-s, --resolution <resolution>`: Set the resolution of the output PNG. Available options: "Full", "1920x1080", "1280x720", "640x480". Default: "Full".
    - `-p, --pattern <pattern>`: Specify a wildcard pattern for MRC files. Default: `"*.mrc"`. For example, `-p *preview.mrc` will only convert MRC files whose names end with `preview.mrc`.

3. For convenience, you can also add the executable file PATH to the end of your `~/.bashrc`:

    ```bash
    export PATH="path_to_your_executable_file":$PATH
    ```

    Then restart the terminal and just use as:

    ```bash
    mrc2png <root_dir> [options]
    ```

## For Customizing and Developing

### Requirements

- Python 3.6+
- Required Python packages: `numpy`, `mrcfile`, `tifffile`, `Pillow`

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/elemeng/mrc2png.git
    ```

2. Navigate to the repository directory:

    ```bash
    cd mrc2png
    ```

3. Install the Rye package manager:

    #### Linux and macOS:

    ```bash
    curl -sSf https://rye-up.com/get | bash
    ```

    #### Windows:

    Download and run the installer from [Rye Releases](https://github.com/astral-sh/rye/releases/latest/download/rye-x86_64-windows.exe).

4. Install dependencies:

    ```bash
    rye sync
    ```

5. Start coding!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
