import pandas as pd
import numpy as np
import h5py

# read CSV files into pandas dataframes
df1 = pd.read_csv('Lydia_Jump_right pocket - front pocket.csv')
df2 = pd.read_csv('Lydia_Walking_right pocket-front pocket.csv')

# create HDF5 files and store dataframes in them
with pd.HDFStore('Lydia_Jump_right pocket - front pocket.h5', mode='w') as store:
    store.put('df1', df1)

with pd.HDFStore('Lydia_Walking_right pocket-front pocket.h5', mode='w') as store:
    store.put('df2', df2)

matrix_1 = np.random.random(size = (1000,1000))
matrix_2 = np.random.random(size = (1000,1000))
matrix_3 = np.random.random(size = (1000,1000))
matrix_4 = np.random.random(size = (1000,1000))
matrix_5 = np.random.random(size = (1000,1000))
matrix_6 = np.random.random(size = (1000,1000))

#store hdf5 data into martix1
with h5py.File('./Lydia_Jump_right pocket - front pocket.h5', 'r') as hdf:
    matrix_1 = hdf['df1'][()]

with h5py.File('./Lydia_Walking_right pocket-front pocket.h5', 'r') as hdf:
    matrix_2 = hdf['df2'][()]

#
with h5py.File('./Lydia_member1.h5','w') as hdf:
    member1 = hdf.create_group('/Member1')
    member1.create_dataset('dataset1_Lydia_Jump', data = matrix_1)
    member1.create_dataset('dataset2_Lydia_walk', data = matrix_2)

    #hdf.create_dataset('dataset1_Lydia_Jump', data = matrix_1)s