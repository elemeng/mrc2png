import os
import argparse
import numpy as np
import mrcfile
import tifffile as tiff
from PIL import Image
import glob


class MRCConverterCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Convert MRC files to PNG format."
        )
        self.parser.add_argument(
            "root_dir", type=str, help="Root directory containing MRC files."
        )
        self.parser.add_argument(
            "--reverse", action="store_true", help="Reverse the order of frames."
        )
        self.parser.add_argument(
            "--resolution",
            type=str,
            choices=["Full", "1920x1080", "1280x720", "640x480"],
            default="Full",
            help="Resolution of the output PNG.",
        )
        self.parser.add_argument(
            "--pattern",
            type=str,
            default="*.mrc",
            help="Wildcard pattern for MRC file's name. eg:--pattern *preview.mrc will only process mrc files endswith preview.mrc",
        )
        self.args = self.parser.parse_args()

    def run(self):
        converter = MRCConverter(
            self.args.root_dir,
            self.args.reverse,
            self.args.resolution,
            self.args.pattern,
        )
        converter.mrc_to_png()


class MRCConverter:
    def __init__(self, root_dir, reverse_order, resolution, pattern):
        self.root_dir = root_dir
        self.reverse_order = reverse_order
        self.resolution = {
            "Full": None,
            "1920x1080": (1920, 1080),
            "1280x720": (1280, 720),
            "640x480": (640, 480),
        }.get(resolution)
        self.pattern = pattern
        self.output_dir = os.path.join(root_dir, "output")

    def mrc_to_png(self):
        os.makedirs(self.output_dir, exist_ok=True)
        mrc_files = glob.glob(
            os.path.join(self.root_dir, "**", self.pattern), recursive=True
        )
        for mrc_filename in mrc_files:
            rel_path = os.path.relpath(mrc_filename, self.root_dir)
            self.convert_single_mrc_to_png(mrc_filename, rel_path)

    def convert_single_mrc_to_png(self, mrc_filename, rel_path):
        tiff_filename = os.path.join(self.output_dir, rel_path.replace(".mrc", ".tiff"))
        png_filename = os.path.join(self.output_dir, rel_path.replace(".mrc", ".png"))

        try:
            with mrcfile.open(mrc_filename, mode="r") as mrc:
                data = np.array(mrc.data, dtype=np.float32)
                if self.reverse_order:
                    data = data[::-1]

                if self.resolution:
                    data = np.array(
                        [
                            np.array(
                                Image.fromarray(frame).resize(
                                    self.resolution, resample=Image.LANCZOS
                                )
                            )
                            for frame in data
                        ]
                    )
                tiff.imwrite(tiff_filename, data, photometric="minisblack")

            # Convert TIFF to PNG
            with Image.open(tiff_filename) as img:
                img = img.convert("L")
                img.save(png_filename)

            print(f"Converted {mrc_filename} to PNG.")
        except Exception as e:
            print(f"Error converting {mrc_filename}: {e}")
        finally:
            if os.path.exists(tiff_filename):
                os.remove(tiff_filename)


if __name__ == "__main__":
    cli = MRCConverterCLI()
    cli.run()
