import argparse

MAX_CATS = 8  # We're not having this discussion again!


def parse_args():
    parser = argparse.ArgumentParser(description="Generate feline Winterland.")
    parser.add_argument("num_cats", type=int, help="Number of cats to create in the Winterland")
    return parser.parse_args()


def main(num_cats):
    if num_cats > MAX_CATS:
        raise ValueError("That's too many cats, man!")
    pass


if __name__ == "__main__":
    args = parse_args()
    main(args.num_cats)
