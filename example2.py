#import libraries
import pandas as pd
import os

########### Specify the filepath #################################################

filepath = ".\example2"

########## List all the files in the folder #######################################
files = os.listdir(filepath)

######### Filter the list of filenames so it only contains the files you want #####
filtered_files = [item for item in files if "ChunkyChips" in item]

###### Example 2: group by date, take latest version ###########################
df_files = pd.DataFrame(filtered_files, columns=['filename'])

#Filter for last number being a digit
df_files = df_files[df_files['filename'].str[-5:-4].str.isdigit()]

# Extract grouping key (first x characters) and sorting key (last x characters before extension)
df_files['Group'] = df_files['filename'].str[:8] #Group by date
df_files['SortKey'] = df_files['filename'].str[-5:-4]  # Extracting last x digit before ".txt"

# Convert SortKey to numeric for proper sorting
df_files['SortKey'] = pd.to_numeric(df_files['SortKey'])

# Assign row number within each group
df_files['RowNumber'] = df_files.sort_values(['Group', 'SortKey'], ascending=[True, False]).groupby('Group').cumcount() + 1

#select only the latest file
df_files=df_files[df_files['RowNumber'] == 1]

final_list = list(df_files['filename'])

################################################################################

# This is a more efficient way to loop over a list
combined_df = pd.concat(
    [pd.read_csv(f"{filepath}/{filename}") for filename in final_list],
    ignore_index=True
)

#######Can do some tests of the combined dataframe here##################

######## Optionally do things to the dataset here ##############################

#name the index column

#add columns
    
#solve dq issues

####### Save the combined data to a single file ################################
combined_df.to_pickle("output/example2.pkl")
combined_df.to_csv("output/example2.csv")