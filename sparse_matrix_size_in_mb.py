def sparse_df_size_in_mb(sparse_df):
    '''
    Size of a sparse matrix in Mbytes
    '''
    size_in_bytes = sparse_df.data.nbytes
    size_in_kb = size_in_bytes / 1024
    size_in_mb = size_in_kb / 1024
    return size_in_mb
