import json

import os
import argparse

def save_results(in_path: str, out_path: str, id: str):

    # Get new data
    with open(in_path, 'r') as in_file:
        new_data = json.load(in_file)
        del new_data["benchmarks"][0]["stats"]["data"]
        new_data["benchmarks"][0]["commit_info"] = new_data["commit_info"]
        new_data["benchmarks"][0]["heat_commit_id"] = id

    if os.path.isfile(out_path) and os.access(out_path, os.R_OK):
        # checks if file exists
        print("Path exists")
        with open(out_path, 'r+') as out_file:
            file_data =json.load(out_file)
            file_data.append(new_data["benchmarks"][0])
            out_file.seek(0)
            json.dump(file_data, out_file, indent=4)

    else:
        print ("aggregate file is missing or is not readable, creating file...")
        with open(out_path, 'w') as out_file:
            out_file.write(json.dumps([new_data["benchmarks"][0]], indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("in_path")
    parser.add_argument("out_path")
    parser.add_argument("id")

    args = parser.parse_args()
    save_results(args.in_path, args.out_path, args.id)

