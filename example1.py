#import libraries
import pandas as pd
import os

########### Specify the filepath #################################################
filepath = ".\example1"

########## List all the files in the folder #######################################
files = os.listdir(filepath)

######### Filter the list of filenames so it only contains the files you want #####
filtered_files = [item for item in files if "ChunkyChips" in item]

######### Loop over the list, adding each file to a dataframe as you go ##########
combined_df = pd.DataFrame()

for i in range(len(filtered_files)):
    print(i)
    filenamei = filtered_files[i]
    print(filenamei)
    filei = pd.read_csv(f"{filepath}/{filenamei}")
    combined_df = pd.concat([combined_df, filei], ignore_index = True)

# This is a more efficient way to do the same thing
# combined_df = pd.concat(
#     [pd.read_csv(f"{filepath}/{filename}") for filename in final_list],
#     ignore_index=True
# )

#######Can do some tests of the combined dataframe here##################

######## Optionally do things to the dataset here ##############################

#name the index column

#add columns
    
#solve dq issues

####### Save the combined data to a single file ################################
combined_df.to_pickle("output/example1.pkl")
combined_df.to_csv("output/example1.csv")