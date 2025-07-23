
import pandas as pd
readf = pd.read_excel("ONT_POS_Weeks.xlsx")
readf.to_csv("ONT_POS_Weeks.csv",index = None,header = True)



