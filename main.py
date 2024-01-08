#!/usr/bin/env python3
import argparse
import time
import pynput.keyboard as keyboard


def suppress_keypress(max_time):
    with keyboard.Listener(suppress=True) as listener:
        if max_time is None:
            listener.join()
        else:
            time.sleep(max_time)
            listener.stop()


def main():
    parser = argparse.ArgumentParser(
        description="CLI app to suppress key presses for a specified duration."
    )
    parser.add_argument(
        "--max-time",
        type=float,
        default=None,
        help="Maximum time to suppress key presses (in seconds)",
    )

    args = parser.parse_args()
    if args.max_time is None:
        print("Suppressing key presses indefinitely press cmd+. to interrupt")
    try:
        suppress_keypress(args.max_time)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
