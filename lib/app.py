from model import *
import argparse
from commands import *

def main():
    parser = argparse.ArgumentParser(description="Enter title and content of your note")
    parser.add_argument("-t", "--title", type=str, required=True, help="Title of your note")
    parser.add_argument("-c", "--content", type=str, required=True, help="Enter note content")
    args = parser.parse_args()
    title = args.title
    content = args.content
    
    create(title, content)


if __name__ == "__main__":
    main()