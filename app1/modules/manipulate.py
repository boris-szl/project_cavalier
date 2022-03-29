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

# removing redundant whitespace
