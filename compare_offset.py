import csv
import sys
from pathlib import Path
from tkinter import Tk, filedialog

def get_files():
    Tk().withdraw()  # Hide tkinter window
    files = filedialog.askopenfilenames(
        title="Select Two CSV Files",
        filetypes=[("CSV files", "*.csv")],
        multiple=True
    )
    return list(files)

def read_csv(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for idx, row in enumerate(reader) if idx > 1]  # Skip first 2 lines
    return rows

def parse_timecode(time_str):
    hours, minutes, seconds = map(float, time_str.split(":"))
    return hours * 3600 + minutes * 60 + seconds

def find_sync_point(file1_data, file2_data):
    sync_points = []
    for i, row1 in enumerate(file1_data):
        time1 = parse_timecode(row1[2])
        for j, row2 in enumerate(file2_data):
            time2 = parse_timecode(row2[2])
            offset = round(time1 - time2, 3)  # Round offset to 3 decimal places
            sync_points.append((i, j, offset))

    # Find the most common offsets
    offset_counts = {}
    for _, _, offset in sync_points:
        offset_counts[offset] = offset_counts.get(offset, 0) + 1

    # Sort offsets by frequency (descending)
    sorted_offsets = sorted(offset_counts.items(), key=lambda x: x[1], reverse=True)
    best_offset, best_count = sorted_offsets[0]
    matches = [(i, j) for i, j, offset in sync_points if offset == best_offset]

    return best_offset, matches, best_count, len(file1_data), sorted_offsets

def main():
    # If files are dropped onto the script, use them; otherwise prompt for files
    files = sys.argv[1:] if len(sys.argv) > 1 else get_files()

    # Prompt for missing files
    if len(files) < 2:
        print("Please select two files.")
        files = get_files()
    if len(files) < 2:
        print("Error: Two files are required.")
        sys.exit(1)

    file1, file2 = files[0], files[1]
    print(f"Comparing files:\n1. {file1}\n2. {file2}")

    file1_data = read_csv(file1)
    file2_data = read_csv(file2)

    # Find synchronization point
    best_offset, matches, match_count, total_scenes, sorted_offsets = find_sync_point(file1_data, file2_data)

    # Determine which file is ahead
    if best_offset > 0:
        file_ahead = file2
    else:
        file_ahead = file1

    # Calculate confidence percentage
    confidence_percentage = (match_count / total_scenes * 100) if total_scenes > 0 else 0

    # Display results for the best sync offset
    print(" ")
    print(f"Best sync offset (in seconds):            {best_offset:+.3f}")
    print(f"Number of matching scenes at this offset:       ({match_count})")
    print(f"Confidence percentage:                     {confidence_percentage:.1f}%")
    print(" ")
    print(f"File Ahead:  {file_ahead}")

    # Display other possible offsets (next 3 most frequent)
    print("Other Possible Offsets:")
    for offset, count in sorted_offsets[1:4]:
        percentage = (count / total_scenes * 100) if total_scenes > 0 else 0
        print(f"                    {offset:+.3f}    ({count})  -  {percentage:.1f}%")

    # Additional report line
    print("------ (Sub) Ahead = (Audio -) | Dub Ahead = (Audio +) ------")

    # Pause before closing
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
