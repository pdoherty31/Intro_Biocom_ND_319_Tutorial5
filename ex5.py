###Exercise 5-1###
import pandas as pd
wages=pd.read_table("wages.csv",",")
gen_years=wages.iloc[0:len(wages),0:2]
gen_years=gen_years.sort_values(by=['gender','yearsExperience'], ascending=[1,1])
gen_years.to_csv('ex5_1.txt', header=True, index=False, sep=" ")

###Exercise 5-2###
import pandas as pd
wages=pd.read_table("wages.csv",",")
wage_low=wages.iloc[0:len(wages),[0,1,3]]
wage_low=wage_low.sort_values(by=['wage'], ascending=[1])
print ("The lowest wage in both genders is:")
print (wage_low[:1])

wage_high=wages.iloc[0:len(wages),[0,1,3]]
wage_high=wage_high.sort_values(by=['wage'], ascending=[0])
print ("The highest wage in both genders is:")
print (wage_high[:1])

Ftot=wages_10.gender.eq('female').sum()
print ("Number of Females in the Top 10 Wages:")
print (Ftot)

###Exercise 5-3###
import pandas as pd
wages=pd.read_table("wages.csv",",")
no_college=min(wages.wage[wages.yearsSchool==12])
yes_college=min(wages.wage[wages.yearsSchool==16])

print("The minimum wage for non college grads is", no_college)
print("The minimum wage for college grads is", yes_college)
