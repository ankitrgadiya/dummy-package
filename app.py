#!/usr/bin/env python3

from sys import argv
from publisher.publisher import Publisher
from listener.listener import Listener


def main():
    if len(argv) != 2:
        print("Invalid arguments.")
        exit(1)
    elif argv[1] == "publish":
        pub = Publisher()
        pub.start()
    elif argv[1] == "listen":
        lis = Listener()
        lis.start()
    else:
        print("Invalid argument.")


if __name__ == "__main__":
    main()
