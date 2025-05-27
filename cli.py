import argparse
import os
from src.converter import convert

def main():
    parser = argparse.ArgumentParser(description="Convert SARIF to GitLab SAST")
    parser.add_argument("input", help="SARIF input file")
    parser.add_argument("output", help="Output GitLab SAST file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"File not found: {args.input}")
        return

    convert(args.input, args.output)
    print(f"\n✅ GitLab SAST report saved to: {args.output}")

if __name__ == "__main__":
    main()
