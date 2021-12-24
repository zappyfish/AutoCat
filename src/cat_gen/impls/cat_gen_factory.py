from src.cat_gen.impls.constant_cat_generator import ConstantCatGenerator


def get_cat_generator(generator_type):
    if generator_type == "constant":
        return ConstantCatGenerator()
    else:
        raise ValueError(f"Undefined cat generator type: {generator_type}")
