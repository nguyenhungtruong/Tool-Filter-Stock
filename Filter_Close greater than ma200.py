# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:32:36 2023

@author: Nguyen_Hung_Truong
"""
import pandas as pd
import numpy as np
import vnstock as vn
import statistics

vn30 = ['HPG ',	'NVL ',	'SSI ',	'PDR ',	'VPB ',	'POW ',	'STB ',	'MBB ',	'HDB ',	'VRE ',	'TCB ',	'TCH ',	'CTG ',	'TPB ',	'VHM ',	'SBT ',	'VIC ',	'MWG ',	'MSN ',	'VNM ',	'VCB ',	'KDH ',	'FPT ',	'PLX ',	'BID ',	'VJC ',	'GAS ',	'BVH ',	'PNJ ',	'REE ',]
vnmid = ['AAA',	'AGG',	'ANV',	'ASM',	'BCG',	'BMP',	'BWE',	'CII',	'CMG',	'CRE',	'CTD',	'CTR',	'DBC',	'DCM',	'DGC',	'DGW',	'DHC',	'DIG',	'DPM',	'DXG',	'DXS',	'EIB',	'FRT',	'GEG',	'GEX',	'GMD',	'HBC',	'HCM',	'HDG',	'HNG',	'HPX',	'HSG',	'HT1',	'IMP',	'KBC',	'KDC',	'KDH',	'KOS',	'LPB',	'MSB',	'NKG',	'NLG',	'NT2',	'OCB',	'PAN',	'PC1',	'PHR',	'PNJ',	'PPC',	'PTB',	'PVD',	'PVT',	'REE',	'SAM',	'SBT',	'SCR',	'SCS',	'SHB',	'SJS',	'SSB',	'SZC',	'TCH',	'TMS',	'VCG',	'VCI',	'VGC',	'VHC',	'VND',	'VPI',	'VSH',]
vn100 = vn30 + vnmid
list_ma200 = []
list_close = []
for i in vn100:
    ma200 = statistics.mean(vn.stock_historical_data(i, "2022-03-07", "2023-03-07").sort_values(by='TradingDate',ascending = False ).iloc[0:200,3].tolist()) # Stock whose price is greater than the moving average (Close,200)
    list_ma200.append(ma200)
    close = vn.stock_historical_data(i, "2022-03-07", "2023-03-07").sort_values(by='TradingDate',ascending = False ).iloc[0:200,3].tolist()[0]
    list_close.append(close)
data = {"Stock":vn100,
        "MA200":list_ma200,
        "Close":list_close
        }   
data_frame = pd.DataFrame(data)
compare = []
for i in range(len(vn100)):
    if data_frame.iloc[i,2] > data_frame.iloc[i,1]: # if close > ma200 then 1 else 0 
       compare.append(1)
    else:
        compare.append(0)
data_frame['Compare'] = compare
print(data_frame.query('Compare == 1'))       
    
    



   