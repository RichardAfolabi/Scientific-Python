"""
Dow CSV
-------

The table in the file 'dow2008.csv' has records holding the daily performance of the Dow Jones Industrial 
Average from the beginning of 2008.  The table has the following columns (separated by commas).

DATE        OPEN      HIGH      LOW       CLOSE     VOLUME      ADJ_CLOSE
2008-01-02  13261.82  13338.23  12969.42  13043.96  3452650000  13043.96
2008-01-03  13044.12  13197.43  12968.44  13056.72  3429500000  13056.72
2008-01-04  13046.56  13049.65  12740.51  12800.18  4166000000  12800.18
2008-01-07  12801.15  12984.95  12640.44  12827.49  4221260000  12827.49
2008-01-08  12820.9   12998.11  12511.03  12589.07  4705390000  12589.07
2008-01-09  12590.21  12814.97  12431.53  12735.31  5351030000  12735.31

1. Read the data from the file, converting the fields to appropriate data types.

"""
#%%
import pandas

try:
	pf_data = pandas.read_csv("dow2008.csv", index_col=0)
	print(pf_data)
except Exception as excpt:
	print("Error! %s " %excpt)
	

