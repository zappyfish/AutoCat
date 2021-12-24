import argparse

from src.cat_gen.impls.cat_gen_factory import get_cat_generator
from src.winterland.winterland import Winterland

MAX_CATS = 8  # We're not having this discussion again!
WINTERLAND_IMAGE_PATH = "data/winterland_1.jpeg"


def parse_args():
    parser = argparse.ArgumentParser(description="Generate feline Winterland.")
    parser.add_argument("--num-cats", type=int, required=True, help="Number of cats to create in the Winterland")
    parser.add_argument("--out-path", type=str, required=True, help="File path to write the Winterland")
    parser.add_argument("--generator-type", type=str, default="constant", help="Type of cat generator to use.")
    return parser.parse_args()


def main(generator_type, num_cats, out_path):
    if num_cats > MAX_CATS:
        raise ValueError("That's too many cats, man!")
    elif num_cats < 0:
        raise ValueError("What's a negative cat?")

    winterland = Winterland(WINTERLAND_IMAGE_PATH)
    cat_generator = get_cat_generator(generator_type)

    for i in range(num_cats):
        cat = cat_generator.generate_cat()
        winterland.add_cat(cat)

    winterland.write_winterland_to_file(out_path)


if __name__ == "__main__":
    args = parse_args()
    main(args.generator_type, args.num_cats, args.out_path)
