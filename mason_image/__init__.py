import argparse
from mason_image.converter import mess_up


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", help="path of image to mess up", dest="in_image")
    parser.add_argument("--out", help="path of output image", dest="out_image")
    args = parser.parse_args()

    if args.in_image is None:
        parser.error("please specify --in")

    out = args.out_image if args.out_image is not None else "out.jpg"
    mess_up(args.in_image, out)
