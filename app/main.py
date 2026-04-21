import argparse
from app.reader import read_multiple
from app.reports.registry import get_report
from app.formatter import print_table


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files"
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report name"
    )

    args = parser.parse_args()

    videos = read_multiple(args.files)
    report = get_report(args.report)

    result = report.generate(videos)
    print_table(result)


if __name__ == "__main__":
    main()