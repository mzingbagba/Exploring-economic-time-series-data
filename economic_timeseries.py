#==============================================================================
#1 IMPORTING RELEVANT PACKAGES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
import datetime
from datetime import datetime
import os
from scipy import stats

#2. SETTING WORKING DIRECTORY
os.chdir(r"C:\...")
print(os.getcwd())

data = pd.read_excel('data.xls')
print(data)

### Rearranging Year and Month columns into Period (Year-Month)
start = datetime(2000, 2, 1)
data['Date'] = pd.date_range(start, periods=194, freq='M')
#data['Period'] = pd.to_datetime(data['Date']).dt.to_period('M')
print(data)

#3. DATA VISUALISATION
#There are 32 variables with different values. I divide this into groups of 8 plots
fig = plt.figure(figsize =(20,10))
ax1 = fig.add_subplot(241)
ax2 = fig.add_subplot(242)
ax3 = fig.add_subplot(243)
ax4 = fig.add_subplot(244)
ax5 = fig.add_subplot(245)
ax6 = fig.add_subplot(246)
ax7 = fig.add_subplot(247)
ax8 = fig.add_subplot(248)
ax1.plot(data['Date'], data['BCROIL'], color='b')
ax1.set_title('BCROIL')
ax2.plot(data['Date'], data['IntBkWAve'], color='b')
ax2.set_title('IntBkWAve')
ax3.plot(data['Date'], data['M1'], color='b')
ax3.set_title('M1')
ax4.plot(data['Date'], data['M2'], color='b')
ax4.set_title('M2')
ax5.plot(data['Date'], data['M2+'], color='b')
ax5.set_title('M2+')
ax6.plot(data['Date'], data['MPR'], color='b')
ax6.set_title('MPR')
ax7.plot(data['Date'], data['RM'], color='b')
ax7.set_title('RM')
ax8.plot(data['Date'], data['TBR-91 day'], color='b')
ax8.set_title('TBR-91 day')
#ax.plot(data['Date'], data['MPR'], color='g')
plt.show()

fig = plt.figure(figsize =(20,10))
ax1 = fig.add_subplot(241)
ax2 = fig.add_subplot(242)
ax3 = fig.add_subplot(243)
ax4 = fig.add_subplot(244)
ax5 = fig.add_subplot(245)
ax6 = fig.add_subplot(246)
ax7 = fig.add_subplot(247)
ax8 = fig.add_subplot(248)
ax1.plot(data['Date'], data['BNCG'], color='b')
ax1.set_title('BNCG')
ax2.plot(data['Date'], data['CIC'], color='b')
ax2.set_title('CIC')
ax3.plot(data['Date'], data['COB'], color='b')
ax3.set_title('COB')
ax4.plot(data['Date'], data['CocoaP'], color='b')
ax4.set_title('CocoaP')
ax5.plot(data['Date'], data['DD'], color='b')
ax5.set_title('DD')
ax6.plot(data['Date'], data['FCD'], color='b')
ax6.set_title('FCD')
ax7.plot(data['Date'], data['GIR'], color='b')
ax7.set_title('GIR')
ax8.plot(data['Date'], data['GSE-ASI'], color='b')
ax8.set_title('GSE-ASI')
plt.show()

fig = plt.figure(figsize =(20,10))
ax1 = fig.add_subplot(241)
ax2 = fig.add_subplot(242)
ax3 = fig.add_subplot(243)
ax4 = fig.add_subplot(244)
ax5 = fig.add_subplot(245)
ax6 = fig.add_subplot(246)
ax7 = fig.add_subplot(247)
ax8 = fig.add_subplot(248)
ax1.plot(data['Date'], data['CIEANom'], color='b')
ax1.set_title('CIEANom')
ax2.plot(data['Date'], data['CIEAReal'], color='b')
ax2.set_title('CIEAReal')
ax3.plot(data['Date'], data['CPI-F'], color='b')
ax3.set_title('CPI-F')
ax4.plot(data['Date'], data['CPI-NF'], color='b')
ax4.set_title('CPI-NF')
ax5.plot(data['Date'], data['CPI-O'], color='b')
ax5.set_title('CPI-O')
ax6.plot(data['Date'], data['INF-F'], color='b')
ax6.set_title('INF-F')
ax7.plot(data['Date'], data['INF-NF'], color='b')
ax7.set_title('INF-NF')
ax8.plot(data['Date'], data['INF-YOY'], color='b')
ax8.set_title('INF-YOY')
plt.show()

fig = plt.figure(figsize =(20,10))
ax1 = fig.add_subplot(241)
ax2 = fig.add_subplot(242)
ax3 = fig.add_subplot(243)
ax4 = fig.add_subplot(244)
ax5 = fig.add_subplot(245)
ax6 = fig.add_subplot(246)
ax7 = fig.add_subplot(247)
ax8 = fig.add_subplot(248)
ax1.plot(data['Date'], data['CITOB'], color='b')
ax1.set_title('CITOB')
ax2.plot(data['Date'], data['IBKEXRENDMUSD'], color='b')
ax2.set_title('IBKEXRENDMUSD')
ax3.plot(data['Date'], data['IBKEXRMAVEUSD'], color='b')
ax3.set_title('IBKEXRMAVEUSD')
ax4.plot(data['Date'], data['IBKXEMAVEGBP'], color='b')
ax4.set_title('IBKXEMAVEGBP')
ax5.plot(data['Date'], data['IBKXRAVEEURO'], color='b')
ax5.set_title('IBKXRAVEEURO')
ax6.plot(data['Date'], data['IBKXRENDMEURO'], color='b')
ax6.set_title('IBKXRENDMEURO')
ax7.plot(data['Date'], data['IBKXRENDMGBP'], color='b')
ax7.set_title('IBKXRENDMGBP')
ax8.plot(data['Date'], data['TotDep'], color='b')
ax8.set_title('TotDep')
plt.show()

#4. SUMMARY STATISTICS
#leaving out ear, month, date and period (note interested in these now)
data_summary = data.drop(['Year','Month', 'Date', 'Period'], axis=1, inplace=True)
print(round(data.describe(), 3))
print(data.skew())
print(data.kurt())
print(stats.jarque_bera(data['BCROIL']))

#Taking natural log of series
data_log = np.log(data)
print(round(data_log.describe(), 3))
print(data_log.skew())
print(data_log.kurt())
print(stats.jarque_bera(data_log['BCROIL']))

#Taking first-difference (of original data)
data_diff = data.diff(axis = 0, periods = 1)
print(data_diff)
print(round(data_diff.describe(), 3))
print(data_diff.skew())
print(data_diff.kurt())
print(stats.jarque_bera(data_diff['BCROIL']))

#Taking first-difference (of log-transformed data)
data_log_diff = data_log.diff(axis = 0, periods = 1)
print(data_log_diff)
print(round(data_log_diff.describe(), 3))
print(data_log_diff.skew())
print(data_log_diff.kurt())
print(stats.jarque_bera(data_log_diff['BCROIL']))
 












