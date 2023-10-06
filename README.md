# RMB-CPI-Nowcasting-Challenge
Prediction of South Africa's CPI for the months of September, October, and November 2023.

## Authors
- [Ruslan Masinjila](https://github.com/ruslanmasinjila)

## Packages Used
Pandas version 2.1.1

## Runtime
Local Machine: Less than 5 seconds.

Google Colab:  Less than 10 seconds due to automatic installation of latest Pandas Library.

## Files Included
* cpi_predictor_google_colab.ipynb
* cpi_predictor_local_machine.py
* input_cpi_values.csv
* README.md
* requirements.txt

## Files Generated (Output)
* results_using_mean.csv
* results_using_median.csv

## Setup and Usage Instructions
* Install required packages by running the following command in a terminal: 
    
    pip install -r requirements.txt

* Run script on local machine as follows: 
    * Open a terminal and navigate to "RMB-CPI-Nowcasting-Challenge" directory.
    * Run the command: python cpi_predictor_local_machine.py

* Alternativelly, run the script in Google Colab as follows:  
    * File -> Upload notebook.
    * Click on "Browse" and select the notebook "cpi_predictor_google_colab.ipynb" or simply drag-and-drop the notebook.
    * Click on the folder icon in the left pane.
    * Click on upload icon and select "input_cpi_values.csv" or simply drag-and-drop the file into the left pane.
    * Click on OK to close the Warning dialog box.
    * To run the script, click on Runtime - > Run all.
    * Right-click on the files area and select refresh to view the output files.
	
## Input Data
The input data is stored in "input_cpi_values.csv" and contains all CPI values for South Africa from January 2009 obtained from [Statistics South Africa](https://www.statssa.gov.za/). The data was copied from the PDF publications to .csv file (input_cpi_values.csv) with the help of [tabula-py](https://pypi.org/project/tabula-py/).

## Output Data
The predicted cpi values are saved in "results_using_mean.csv" and "results_using_median.csv" files. In addition, the results are also printed on the terminal. Rember to refresh the files section of Google Colab after running the script to view these files (i.e right-click on the files area and select refresh).


## Approach Used
For each of the cpi categories, the cpi value of the next month is estimated by adding the cpi value of the current month to the mean, or the median, of the difference between historical cpi values of next month and the current month. For example, if the next month is Y, the current month is X, and the current year is j, then cpi for the month Y of the year j is found as follows:

Yj = Xj + mean(Yi-Xi)   for all 2009 <= i < j

OR 

Yj = Xj + median(Yi-Xi)   for all 2009 <= i < j

The results for mean and median are saved in the "results_using_mean.csv" and "results_using_median.csv" files respectivelly in addition to being printed on the screen.