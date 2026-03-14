import os
import argparse

def get_directory_size(path):
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
            except:
                pass
    return total_size


def human_readable(size):
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024


def analyze_directory(path):
    results = []

    for entry in os.scandir(path):
        if entry.is_dir():
            size = get_directory_size(entry.path)
            results.append((entry.name, size))

    results.sort(key=lambda x: x[1], reverse=True)
    return results


def main():
    parser = argparse.ArgumentParser(description="Disk Usage Analyzer")
    parser.add_argument("path", nargs="?", default=".", help="Directory to scan")

    args = parser.parse_args()
    path = os.path.abspath(args.path)

    print(f"\nScanning: {path}\n")

    data = analyze_directory(path)

    print("Top directories by size:\n")

    for i, (name, size) in enumerate(data[:10], 1):
        print(f"{i:2}. {human_readable(size):>10}   {name}")


if __name__ == "__main__":
    main()
