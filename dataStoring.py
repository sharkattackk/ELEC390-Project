import pandas as pd
import numpy as np
import h5py as h5

# read CSV files into pandas dataframes
df1 = pd.read_csv('Lydia_Jump_right pocket - front pocket.csv')
df2 = pd.read_csv('Lydia_Walking_right pocket-front pocket.csv')
df3 = pd.read_csv('Cameron_jump_right_pocket_&_front_pocket.csv')
df4 = pd.read_csv('Cameron_walking_right_pocket_&_front_pocket.csv')

#combined 
framesJ = [df1, df2]
combinedJ = pd.concat(framesJ, keys=["x", "y"])
framesW = [df1, df2]
combinedW = pd.concat(framesW, keys=["x", "y"])

# create HDF5 files and store dataframes in them
with h5.File('./Project-data.h5', mode='w') as store:
    #adding Lydias data group
    G1 = store.create_group('/Lydia')
    G1.create_dataset('jumping', data = df1)
    G1.create_dataset('walking', data = df2)

    #adding camerons data group 
    G2 = store.create_group('/Cameron')
    G2.create_dataset('jumping', data = df3)
    G2.create_dataset('walking', data = df4)

    #adding Msendoos data group


    #need to shuffle these
    #adding train dataset
    G4 = store.create_group('/dataset/train')
        #jump
    G4.create_dataset('jumping', data=combinedJ)
        #walking
    G4.create_dataset('walking', data=combinedW)


    #add 10% of all data to one file and shuffle
    #adding test dataset

