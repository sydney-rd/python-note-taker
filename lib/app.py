from model import *
import argparse
from commands import *


def main():
    parser = argparse.ArgumentParser(description="Enter title and content of your note")
    parser.add_argument("-t", "--title", type=str, help="Title of your note")
    parser.add_argument("-c", "--content", type=str, help="Enter note content")
    parser.add_argument("-v", "--view", action="store_true", help="View all notes")
    args = parser.parse_args()

    if args.view:
        view()
    elif args.title and args.content:
        create(args.title, args.content)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()