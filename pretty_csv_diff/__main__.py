import argparse
import signal
import subprocess
import sys

from pretty_csv_diff.pretty_csv_diff import PrettyCsvDiff


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs=2, help='paths to the two csv files to be compared')
    parser.add_argument('pk', nargs='+', help='name or index of primary key column. multiple columns are allowed')
    parser.add_argument('--less', default=False, action='store_true', help='use less to view output')
    args = parser.parse_args()

    lines = []
    for formatted_row in PrettyCsvDiff(path=args.path, pk=args.pk).do():
        line = '  '.join(formatted_row)
        if args.less:
            lines.append(line)
            continue
        try:
            print(line)
        except BrokenPipeError:
            pass
    if args.less:
        write_to_less('\n'.join(lines), True)


def write_to_less(text, line_numbers):
    # https://unix.stackexchange.com/a/117882/366776
    less_cmd = ["less", "-SRX"]
    if line_numbers:
        less_cmd.append("-N")
    p = subprocess.Popen(less_cmd, stdin=subprocess.PIPE)
    try:
        p.stdin.write(text.encode("utf-8"))
    except BrokenPipeError:
        sys.exit(1)
    p.communicate()


if __name__ == '__main__':
    # Don't turn these signal into exceptions, just die.
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

    main()
