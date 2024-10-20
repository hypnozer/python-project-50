import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
        usage="%(prog)s [-h] first_file second_file"
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    parser.print_help()


if __name__ == "__main__":
    main()
