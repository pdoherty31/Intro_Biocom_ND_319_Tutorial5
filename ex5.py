###Exercise 5-1###
import pandas as pd
wages=pd.read_table("wages.csv",",")
gen_years=wages.iloc[0:len(wages),0:2]
gen_years=gen_years.sort_values(by=['gender','yearsExperience'], ascending=[1,1])
gen_years.to_csv('ex5_1.txt', header=True, index=False, sep=" ")