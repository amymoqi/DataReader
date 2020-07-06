import ntpath
import os
import pandas

# ----------------------------------------------------------------------------------------------------------------------
# Set up
# ----------------------------------------------------------------------------------------------------------------------
# TODO: Input
FILTER = []  # Input which column you want to filter, ex. [[column_name1, col_name2], [col_name3, col_name4]]
FILES = []  # If you want to manually chose what you want transfer
RENAME = '_sample'
columns = []
# ----------------------------------------------------------------------------------------------------------------------
# Procedure
# ----------------------------------------------------------------------------------------------------------------------
## get files
# Get all the XXX type files under a directory.
if FILES:
    extension = '.csv'  # CSV for example
    files = []
    for file in os.listdir(".\\Input"):  # may change the directory
        if file.endswith(extension):
            files.append(file)


## functions
def all_column_values(dataframe, column_name: str) -> list:
    """
    given a dataframe and a column name, return a list that contains all column elements
    hint: it should be very short, only one line using pandas
    :param dataframe:
    :return:
    """


# TODO: filter column.
def find_column_values(column: list):
    """
    this function reduces redundant element in columns, which means, after call this function, column still contains all
    elements but each element only appears once.
    you may call set() function (delete this line after you finish)
    """
    pass


def reduce_df(df, lst: list):
    """
    given a data frame and a list, reduce the data frame
    this web maybe helpful:
    https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values

   :param df: dataframe
   :param lst: a list that contains list of unique elements in the columns that want to be filtered.
    ex. [['a', 'b', 'c'], ['d', 'e', 'f']]
    """
    pass


# if the directory does not exist, then create it
if not os.path.exists('.\\Output'):
    os.mkdir('.\\Output')

# main
for index in range(len(FILES)):
    df = pandas.read_csv(FILES[index], low_memory=False) # read to pandas
    for column_name in FILTER[index]:
        columns.append(all_column_values(df, column_name))
        find_column_values(columns)
    reduce_df(df, columns)
    # write to file
    file_name = ntpath.basename(FILES[index])  # extract file name from a path
    df.to_csv(r'.//Output//sample_' + file_name, index=False, header=True)
    columns = []  # reset


# if __name__ == "__main__":
