import os
import pandas

# ----------------------------------------------------------------------------------------------------------------------
# Set up
# ----------------------------------------------------------------------------------------------------------------------
# TODO: Input
FILTER = []  # Input which column you want to filter
FILES = []  # If you want to manually chose what you want transfer
RENAME = '_sample'

# ----------------------------------------------------------------------------------------------------------------------
# Procedure
# ----------------------------------------------------------------------------------------------------------------------

# Get all the XXX type files under a directory.
if FILES:
    extension = '.csv'  # CSV for example
    files = []
    for file in os.listdir(".\\Input"):
        if file.endswith(extension):
            files.append(file)

# TODO: filter column.
def xxx() -> None:
    """

    :return:
    """
    yyy()
    pass

def yyy() -> str:
    pass

OUTPUTS = []  # Any name that I want, e.x, file2 = XXX_sample/csv saved in Output directory

if __name__ == "__main__":
    xxx()
