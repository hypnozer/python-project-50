import argparse
import json


def read_json(path):
    with open(path) as file:
        return json.load(file)


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format", help="set format of output"
    )

    args = parser.parse_args()

    print("first:", args.first_file)
    print("second:", args.second_file)

    data1 = read_json(args.first_file)
    data2 = read_json(args.second_file)
    
    print("file1 content:", data1)
    print("file2 content:", data2)


if __name__ == "__main__":
    main()
