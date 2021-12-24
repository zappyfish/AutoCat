import argparse

from src.cat_gen.cat_generator import CatGenerator
from src.winterland.winterland import Winterland

MAX_CATS = 8  # We're not having this discussion again!
WINTERLAND_IMAGE_PATH = ""


def parse_args():
    parser = argparse.ArgumentParser(description="Generate feline Winterland.")
    parser.add_argument("num-cats", type=int, help="Number of cats to create in the Winterland")
    parser.add_argument("out-path", type=str, help="File path to write the Winterland")
    return parser.parse_args()


def main(num_cats, out_path):
    if num_cats > MAX_CATS:
        raise ValueError("That's too many cats, man!")
    elif num_cats < 0:
        raise ValueError("What's a negative cat?")

    winterland = Winterland(WINTERLAND_IMAGE_PATH)
    cat_generator = CatGenerator()

    for i in range(num_cats):
        cat = cat_generator.generate_cat()
        winterland.add_cat(cat)

    winterland.write_winterland_to_file(out_path)


if __name__ == "__main__":
    args = parse_args()
    main(args.num_cats, args.out_path)
