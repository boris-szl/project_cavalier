# library for manipulating rows and columns for pandas DataFrames

def setDateRows1(df):
    row_list = list(df.index)
    df2 = df.set_axis([x.strftime("%m/%d/%Y") for x in row_list], axis=0, inplace=False)
    return df2

def setDateRows2(df):
    row_list = list(df.index)
    df2 = df.set_axis([x.strftime("%Y") for x in row_list], axis=0, inplace=False)
    return df2

def renameCols(df):
    col_list = list(df.columns)
    df2 = df.set_axis([x.strftime("%m/%d/%Y") for x in col_list], axis=1, inplace=False)
    return df2

def ColsToInt(df):
    timestamps = df.columns
    col_list = list(timestamps.strftime("%Y"))
    df2 = df.set_axis([int(x) for x in col_list], axis=1, inplace=False)
    return df2

def removeWhitespaceInIndex(dataframe):
    # first we check if the index is a string or an integer or float
    if ( (dataframe.index.is_integer or dataframe.index.is_float) == True):
        raise Error("Index should contain string values")
    else:
        # iterate over dataframe
        # locate redundant whitespace in col "name"
        # remove whitespace with
        for i, row in dataframe.iterrows():
            " ".join(i.split())
    return dataframe
