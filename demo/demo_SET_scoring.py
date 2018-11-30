# -*- coding: utf-8 -*-


u'''
Created on Nov 2018

Samle comparing different models

@author: guillaume
'''

import pandas as pd
import matplotlib.pyplot as plt
from agmodeling.scoring.set_method import get_IPI_score


file = u'sample_data.xlsx'
print (u'Read excel data file : %s'%file)
df = pd.read_excel(file)
print (u'containing %d data ' % df.size)
#print df.head()
df25=df.filter(regex=u'.*25.*')
df25.plot()
df10=df.filter(regex=u'.*10.*')
df10.plot()

results = dict()

listModelNames = list()
for col in df10.columns :
    modelName = col.split(u'_',1)[1]
    if modelName != u'REF':
        listModelNames.append(modelName)


PM25=u'PM25'
PM10=u'PM10'
    
results25=list()
datas=dict()
datas[PM25] = list()
for col in df25.columns :
    if col != u'PM25_REF' :
        print u'\nScore IPI for %s' % col
        ipi = get_IPI_score(df[u'PM25_REF'], df[col])
        datas[PM25].append(ipi)
        
datas[PM10] = list()
for col in df10.columns :
    if col != u'PM10_REF' :
        print u'\nScore IPI for %s' % col
        ipi = get_IPI_score(df[u'PM10_REF'], df[col])
        datas[PM10].append(ipi)
    
res = pd.DataFrame.from_dict(datas, orient=u'index')
res.columns = listModelNames

print u'\n========================================'
print u'Results :'
print res



print u'\nFin du programme'
plt.show()
