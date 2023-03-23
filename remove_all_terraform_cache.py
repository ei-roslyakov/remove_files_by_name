import pathlib
import loguru
import os
import shutil
import argparse

logger = loguru.logger


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--path",
        required=True,
        type=str,
        default="default",
        action="store",
        help="Path to check files",
    )
    parser.add_argument(
        "--key-to-delete",
        required=True,
        type=str,
        nargs="+",
        action="store",
        help="folders\files to delete",
    )
    parser.add_argument(
        "--wildcard",
        required=False,
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
        help="Do I need to use wildcard for key?",
    )

    return parser.parse_args()


def delete_data():
    logger.info("Application started")
    args = parse_args()

    keys_to_delete = args.key_to_delete
    path_to_delete = args.path

    for key in keys_to_delete:
        if args.wildcard:
            key = f"{key}*"
        for item in pathlib.Path(path_to_delete).rglob(f"{key}"):
            if os.path.isfile(item):
                os.remove(item)
                logger.info(f"DELETED {item}")
            if os.path.isdir(item):
                shutil.rmtree(item)
                logger.info(f"DELETED {item}")

    logger.info("Application finished")


if __name__ == "__main__":
    delete_data()
