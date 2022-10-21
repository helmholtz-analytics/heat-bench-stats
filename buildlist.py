import sys
import json
from pathlib import Path

def main():
    benchmarkresults = []
    for path in Path('./data').glob('*/*.json'):
        benchmarkresults.append({
            'name':'{}'.format(*path.parts),
            'file':str(path)
        })
    json.dump(benchmarkresults, sys.stdout, indent=4)


if __name__ == "__main__":
    main()
