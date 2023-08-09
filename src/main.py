"""Sum integers, possibly squared first."""
import argparse
import sys
from collections.abc import Iterator, Sequence

import sample

_PARSER = argparse.ArgumentParser(
    description='Sum a list of integers',
)

_PARSER.add_argument(
    '-s',
    '--square',
    action='store_true',
    help='square the integers before summing',
)

_PARSER.add_argument(
    'integers',
    nargs='*',
    help='integers possibly squared to sum',
    type=int,
)


class Args:
    """Parsed command line arguments."""

    square: bool
    integers: Iterator[int]

    def __init__(self, args: Sequence[str] | None = None) -> None:
        """
        Create an Arg object from args.

        Args:
            args (Sequence[str] | None): if None, use sys.arv
        """
        _PARSER.parse_args(args, namespace=self)


def run(args: Args | None = None) -> None:
    """
    Produce the sum or sum of squares given Args.

    Args:
        args (Args | None): The square flag and integer list.

    Returns:
        int: The sum.
    """
    if args is None:
        args = Args()

    result = (sample.total_squares if args.square else sample.total)(
        args.integers,
    )
    print(f'Total is {result}')
    sys.exit(0)

if __name__ == '__main__':
    run()
