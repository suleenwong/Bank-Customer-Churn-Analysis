import pandas as pd

def grouping(df, group, var, normalize=False):
    """
    Args:
        df (DataFrame): DataFrame
        group (string): variable to group
        var (string): variable of interest
    """
    grouped_df = (df
        .groupby(group)[var]
        .value_counts(normalize=normalize)
        .mul(100)
        .rename('percent')
        .reset_index())

    return grouped_df