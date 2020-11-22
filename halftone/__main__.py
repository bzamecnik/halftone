import argparse

import PIL.Image
import halftone as ht


def parse_args():
    parser = argparse.ArgumentParser(description="Image halftoning.")
    parser.add_argument("input", help="input image path")
    parser.add_argument("output", help="output image path")
    parser.add_argument(
        "-f",
        "--spot-function",
        choices=ht.spot_functions.keys(),
        default='eulcid',
        help="Spot function (shape of the dot)",
    )
    parser.add_argument(
        "-s",
        "--spacing",
        type=int,
        defalt=10,
        help="Grid spacing (in px)",
    )
    parser.add_argument(
        "-a",
        "--angle",
        type=int,
        defalt=0,
        help="Grid angle (in degrees CCW)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    input_img = PIL.Image.open(args.input)
    fn = ht.spot_functions[args.spot_function]
    halftoned_img = ht.halftone(input_img, fn(args.angle, args.spacing))
    halftoned_img.save(args.output)
