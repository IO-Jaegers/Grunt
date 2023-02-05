default_value_x = 224
default_value_y = 224
depth = 3

epoch = 10
size_of_categories = 3
batch_size = 32


def get_epoch() -> int:
    global epoch
    return epoch


def set_epoch(
        v: int
) -> None:
    global epoch
    epoch = v


def get_batch_size() -> int:
    global batch_size
    return batch_size


def set_batch_size(
        v: int
):
    global batch_size
    batch_size = v


def get_size_of_categories() -> int:
    global size_of_categories
    return size_of_categories


def set_size_of_categories(
        val: int
) -> None:
    global size_of_categories
    size_of_categories = val


def get_image_size_x() -> int:
    global default_value_x
    return default_value_x


def get_image_size_y() -> int:
    global default_value_y
    return default_value_y


def get_image_size_depth() -> int:
    global depth
    return depth


def set_image_size_x(
        v: int
) -> None:
    global default_value_x
    default_value_x = v


def set_image_size_y(
        v: int
) -> None:
    global default_value_y
    default_value_y = v


def set_image_size_depth(
        v: int
) -> None:
    global depth
    depth = v
