import pandas as pd 

pd.set_option('display.max_columns',100,'display.width',1000)

version = '20190917'
data = f'd:/run_record_{version}.xlsx'

display_col = ['date','total_min','total_dist_in_meters', 'meter_per_min', 'proj_meter_12_min', 'vo2max_meter','multiplier','form']


df = pd.read_excel(data, sheet_name='data').dropna()[display_col]
df.set_index('date', inplace=True)

print(df.tail(20))

'''
filter_criteria
'''

now_vo2max_meter = round(df['vo2max_meter'][-1],2)
now_form = round(df['form'][-1],2)
meter_per_min = round(df['meter_per_min'][-1],2)


import datetime as dt 
today = dt.datetime.today()

period_start = pd.to_datetime(df.index[0]).strftime('%Y-%m-%d')
period_end = pd.to_datetime(today.strftime('%Y-%m-%d'))

import matplotlib.pyplot as plt 

'''testing plotting with Chinese'''
import matplotlib.font_manager as mfm

# font_path = r'c:\\Windows\fonts\kaiu.ttf'
font_path=r'c:\\WINDOWS\FONTS\DENG.TTF'
prop = mfm.FontProperties(fname=font_path)
# end

plt.style.use('seaborn')
plt.figure()

#HSIF N_value plotting details
plt.subplot(311)
# plt.xlabel('')
plt.xlabel('日期',FontProperties=prop)
plt.ylabel('狀態% (Form in %)', rotation =0, FontProperties=prop)
plt.title(f"狀態百分比 (Form %): {period_start} 至 {period_end}\n Form: {now_form} % ", FontProperties=prop) 
form_graph = df.loc[:,'form'].plot()

plt.subplot(312)
# plt.xlabel('')
plt.xlabel('日期',FontProperties=prop)
plt.ylabel('米(meter)', rotation =0, FontProperties=prop)
plt.title(f"速度(Pace)\n 每分鐘跑 (Distance Per Min): {period_start} 至 {period_end} \n Speed: {meter_per_min} m/min", FontProperties=prop) 
meter_per_min_graph = df.loc[:,'meter_per_min'].plot()

plt.subplot(313)
# plt.xlabel('')
plt.xlabel('日期',FontProperties=prop)
plt.ylabel('ml / kg / min/ \n vo2max', rotation =0, FontProperties=prop)
plt.title(f"最大含氧 \n vo2max) \n ml/kg/min : {period_start} 至 {period_end}\n VO2Max Today: {now_vo2max_meter} ml/kg/min", FontProperties=prop) 
meter_per_min_graph = df.loc[:,'vo2max_meter'].plot()


plt.tight_layout()
plt.show()

