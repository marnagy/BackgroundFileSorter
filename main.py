import os
import sys
from pathlib import Path
from tqdm import tqdm

FOLDER_PATH = os.path.join(Path.home(), 'downloads')

def sort_file(file) -> None:
    _, ext = os.path.splitext(file)
    ext = ext[1:] if ext is not None else '_EMPTY'
    #print(file, ext)
    ext = ext.upper()
    os.makedirs(ext, exist_ok=True)
    try:
        os.rename(file, os.path.join(ext, file))
    except Exception as e:
        print(e, file=sys.stderr)

def main() -> None:
    os.chdir(FOLDER_PATH)
    #print(f'Current working directory:', os.getcwd())

    # initial sorting
    files = list(filter(lambda f: os.path.isfile(f), os.listdir()))
    for file in tqdm(files, ascii=True):
        sort_file(file)

if __name__ == '__main__':
    main()
