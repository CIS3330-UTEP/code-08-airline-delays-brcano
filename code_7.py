import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm_api
import seaborn as sns
#If any of this libraries is missing from your computer. Please install them using pip.
filename = 'Flight_Delays_2018.csv'
df = pd.read_csv(filename)
df_bydelay = df.query("ARR_DELAY >= 45 and OP_CARRIER_NAME")
selected_columns_df = df_bydelay[['WHEELS_OFF', 'WHEELS_ON', 'DISTANCE', 'OP_CARRIER_NAME']]
model = sm_api.ols('ARR_DELAY  ~ WHEELS_OFF + WHEELS_ON + DISTANCE + C(OP_CARRIER_NAME)', data=df).fit()
print(model.summary())
anova_table = sm.stats.anova_lm(model,typ=2) #typ2 running anova and is a stat model with OLS
print(anova_table)
#ARR_DELAY is the column name that should be used as dependent variable (Y).
sns.boxplot(x='OP_CARRIER_NAME' , y='ARR_DELAY', data=df_bydelay) #this boxplot shows the delay time for each carrier and helps show how knowing which carrier can affect times for delays.
plt.title('Arrival Delay by Airline (Delays ≥ 45 min)') #the title of it 
plt.xticks(rotation=45) # makes graph look better 
plt.xlabel('Carrier Name') # You can change it with one of the selected columns and it will update the graph. can X in the box plot then update name here. 
plt.ylabel('Arrival Delay (minutes)') # This is ARR_Delay
plt.show() # Shows box plot
# I was able to get this from a mix of all the previous practices and powerpoints and I googled how to edit x and y axis lable names. 