from pathlib import Path
import argparse

def calc_dir_size(dir):
    total_size = sum(f.stat().st_size for f in Path(dir).rglob('*') if f.is_file())
    return total_size


def main(args):
    root_path = Path(args.path)
    for item in root_path.iterdir():
        if item.is_file():
            item_size = item.stat().st_size
        else:
            item_size = calc_dir_size(item)

        print(f"{item_size}b  {item.name}")


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("path", type=str, help="Start path")
    main(arg_parser.parse_args())
