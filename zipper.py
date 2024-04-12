import zipfile
import pathlib


def make_archive(filepaths, dest):
    dest_folder = pathlib.Path(dest, "Compressed.zip")
    with zipfile.ZipFile(dest_folder, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
