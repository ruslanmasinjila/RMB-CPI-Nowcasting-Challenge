############################################
# RMB-CPI-Nowcasting-Challenge
# AUTHOR: RUSLAN MASINJILA
############################################

import pandas as pd

targets =[
'headline CPI',                        
'food and non-alcoholic beverages',    
'alcoholic beverages and tobacco',     
'clothing and footwear',              
'housing and utilities',                
'household contents and services',      
'health',                              
'transport',                            
'communication',                        
'recreation and culture',               
'education',                           
'restaurants and hotels',               
'miscellaneous goods and services'     
]

months_dict = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

# File parameters
dataframe_filename   = 'input_cpi_values.csv'


algorithm    = ['mean','median']
target_month = ['September','October','November']


def predict(dataframe):

    dataframe_diff = dataframe.diff()
    dataframe_diff['Year']  = dataframe['Year']
    dataframe_diff['Month'] = dataframe['Month']

    for algo in algorithm:
        print("##########################################################")
        print(f"RESULTS USING {algo}")
        print("##########################################################")
        print()
        dataframe_submission = pd.DataFrame(columns = ['ID','Value'])
        for month in target_month:
            dataframe_diff_target_month = dataframe_diff[dataframe_diff['Month']==months_dict[month]].dropna()
            
            for target in targets:
                cental_measure = None
                if(algo=='mean'):
                    cental_measure = dataframe_diff_target_month[target].mean()
                elif(algo=='median'):
                    cental_measure = dataframe_diff_target_month[target].median()
                    
                previous_month = months_dict[month]-1
                y_pred = dataframe[dataframe['Month']==previous_month][target].iloc[-1] + cental_measure
                new_row = {'ID': month+'_'+target, 'Value': y_pred}
                dataframe_submission.loc[len(dataframe_submission)] = new_row
                    
            
        dataframe_submission.fillna(0, inplace=True)
        print(dataframe_submission)
        print()
        print()
        submission_file_name = f'results_using_{algo}.csv'
        dataframe_submission.to_csv(submission_file_name,index=False)
                    
  
def main():

    dataframe  = pd.read_csv(dataframe_filename)
    predict(dataframe)
    
main()