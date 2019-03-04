Processing Life Expectancy Tables
=================================

The Office for National Statistics (ONS) produces [life expectancy at birth
tables](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/lifeexpectancies)
for various geographies for England and Wales. However, because they are
statisticians they produce nasty broken Excel sheets instead of nice simple (and
easy to use) CSV files. 

In this exercise we will be taking a pair of raw data files
(`counties-m-birth.csv` and `counties-f-birth.csv`) that have been saved out
from Excel as CSV. They contain male and female life expectancies at birth for
English counties. You will need to edit the file `life_expectancy.py` and add in
some code to extract the lines we want (a header row and the ones with figures on), 
and then output them for each file. 

If you finish that task then you can think on how you might add the ability to
sort the rows based on a column the user specifies, or how you could combine the
male and female figures to allow them to be compared more easily.
