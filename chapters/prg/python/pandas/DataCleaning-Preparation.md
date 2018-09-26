
# Data Cleaning and Preparation
### Resources: 
Chapter 7 in 'Python for Data Analysis' by Wes McKinney (2017, O'Reilly)
* https://github.com/wesm/pydata-book

Chapter 3 in 'Python Data Science Handbook' by Jake VanderPlas (2016, O'Reilly)
* https://jakevdp.github.io/PythonDataScienceHandbook/

## Dataset: 2015 NSDUH
* National Survey on Drug Abuse and Health (NSDUH) 2015 
* Substance Abuse and Mental Health Services Administration 
* Center for Behavioral Health Statistics and Quality, October 27, 2016
* http://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2015-nid16893


## Step1: Load the data
* Import python modules
* load data file and save as DataFrame object
* Subset dataframe by column


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
file = pd.read_table('NSDUH-2015.tsv', low_memory=False)
data = pd.DataFrame(file)
```


```python
data.shape
```




    (57146, 2666)




```python
df = pd.DataFrame(data, columns=['QUESTID2', 'CATAG6', 'IRSEX','IRMARITSTAT',
        'EDUHIGHCAT', 'IRWRKSTAT18', 'COUTYP2', 'HEALTH2','STDANYYR1',
        'HEPBCEVER1','HIVAIDSEV1','CANCEREVR1','INHOSPYR','AMDELT',
        'AMDEYR','ADDPR2WK1','ADWRDST1','DSTWORST1','IMPGOUTM1',
        'IMPSOCM1','IMPRESPM1','SUICTHNK1','SUICPLAN1','SUICTRY1',
        'PNRNMLIF','PNRNM30D','PNRWYGAMT','PNRNMFLAG','PNRNMYR',
        'PNRNMMON','OXYCNNMYR','DEPNDPYPNR','ABUSEPYPNR','PNRRSHIGH',
        'HYDCPDAPYU','OXYCPDAPYU','OXCNANYYR2','TRAMPDAPYU','MORPPDAPYU',
        'FENTPDAPYU','BUPRPDAPYU','OXYMPDAPYU','DEMEPDAPYU','HYDMPDAPYU',
        'HERFLAG','HERYR','HERMON','ABODHER', 'MTDNPDAPYU',
        'IRHERFY','TRBENZAPYU','ALPRPDAPYU','LORAPDAPYU','CLONPDAPYU',
        'DIAZPDAPYU','SVBENZAPYU','TRIAPDAPYU','TEMAPDAPYU','BARBITAPYU',
        'SEDOTANYR2','COCFLAG','COCYR','COCMON','CRKFLAG',
        'CRKYR','AMMEPDAPYU','METHAMFLAG','METHAMYR','METHAMMON',
        'HALLUCFLAG','LSDFLAG','ECSTMOFLAG','DAMTFXFLAG','KETMINFLAG',
        'TXYRRESOV1','TXYROUTPT1','TXYRMHCOP1','TXYREMRGN1','TXCURRENT1',
        'TXLTYPNRL1','TXYRNOSPIL','AUOPTYR1','MHLMNT3','MHLTHER3',
        'MHLDOC3','MHLCLNC3','MHLDTMT3','AUINPYR1','AUALTYR1'])
df.shape
```




    (57146, 89)




```python
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>QUESTID2</th>
      <th>CATAG6</th>
      <th>IRSEX</th>
      <th>IRMARITSTAT</th>
      <th>EDUHIGHCAT</th>
      <th>IRWRKSTAT18</th>
      <th>COUTYP2</th>
      <th>HEALTH2</th>
      <th>STDANYYR1</th>
      <th>HEPBCEVER1</th>
      <th>...</th>
      <th>TXLTYPNRL1</th>
      <th>TXYRNOSPIL</th>
      <th>AUOPTYR1</th>
      <th>MHLMNT3</th>
      <th>MHLTHER3</th>
      <th>MHLDOC3</th>
      <th>MHLCLNC3</th>
      <th>MHLDTMT3</th>
      <th>AUINPYR1</th>
      <th>AUALTYR1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25095143</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>5</td>
      <td>99</td>
      <td>3</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>13005143</td>
      <td>4</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>67415143</td>
      <td>3</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70925143</td>
      <td>1</td>
      <td>2</td>
      <td>99</td>
      <td>5</td>
      <td>99</td>
      <td>2</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>75235143</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>3</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 89 columns</p>
</div>




```python
df.tail()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>QUESTID2</th>
      <th>CATAG6</th>
      <th>IRSEX</th>
      <th>IRMARITSTAT</th>
      <th>EDUHIGHCAT</th>
      <th>IRWRKSTAT18</th>
      <th>COUTYP2</th>
      <th>HEALTH2</th>
      <th>STDANYYR1</th>
      <th>HEPBCEVER1</th>
      <th>...</th>
      <th>TXLTYPNRL1</th>
      <th>TXYRNOSPIL</th>
      <th>AUOPTYR1</th>
      <th>MHLMNT3</th>
      <th>MHLTHER3</th>
      <th>MHLDOC3</th>
      <th>MHLCLNC3</th>
      <th>MHLDTMT3</th>
      <th>AUINPYR1</th>
      <th>AUALTYR1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>57141</th>
      <td>57863730</td>
      <td>5</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>2</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>57142</th>
      <td>97294730</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>57143</th>
      <td>31894730</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>57144</th>
      <td>98524730</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>5</td>
      <td>99</td>
      <td>2</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>57145</th>
      <td>80134730</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>99</td>
      <td>2</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 89 columns</p>
</div>



## Step 2: Recode null and missing values `NaN` 
* Replace values for `Bad Data`, `Don't know`, `Refused`, `Blank`, `Skip` with `NaN`
* Replace `NaN` with `0`


```python
df.replace([83, 85, 91, 93, 94, 97, 98, 99, 991, 993], np.nan, inplace=True)
df.fillna(0, inplace=True)
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>QUESTID2</th>
      <th>CATAG6</th>
      <th>IRSEX</th>
      <th>IRMARITSTAT</th>
      <th>EDUHIGHCAT</th>
      <th>IRWRKSTAT18</th>
      <th>COUTYP2</th>
      <th>HEALTH2</th>
      <th>STDANYYR1</th>
      <th>HEPBCEVER1</th>
      <th>...</th>
      <th>TXLTYPNRL1</th>
      <th>TXYRNOSPIL</th>
      <th>AUOPTYR1</th>
      <th>MHLMNT3</th>
      <th>MHLTHER3</th>
      <th>MHLDOC3</th>
      <th>MHLCLNC3</th>
      <th>MHLDTMT3</th>
      <th>AUINPYR1</th>
      <th>AUALTYR1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25095143</td>
      <td>1</td>
      <td>1</td>
      <td>4.0</td>
      <td>5</td>
      <td>0.0</td>
      <td>3</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>13005143</td>
      <td>4</td>
      <td>1</td>
      <td>3.0</td>
      <td>2</td>
      <td>1.0</td>
      <td>2</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>67415143</td>
      <td>3</td>
      <td>2</td>
      <td>4.0</td>
      <td>4</td>
      <td>4.0</td>
      <td>3</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70925143</td>
      <td>1</td>
      <td>2</td>
      <td>0.0</td>
      <td>5</td>
      <td>0.0</td>
      <td>2</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>75235143</td>
      <td>2</td>
      <td>2</td>
      <td>1.0</td>
      <td>3</td>
      <td>4.0</td>
      <td>3</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 89 columns</p>
</div>



## Step 3: Recode values for selected features:
Order matters here, because some features were saved as new variables
* Recode `2=0`: 
`['STDANYYR1','HEPBCEVER1', 'HIVAIDSEV1', 'CANCEREVR1', 'INHOSPYR ',
  'AMDELT','AMDEYR','ADDPR2WK1','DSTWORST1', 'IMPGOUTM1',
  'IMPSOCM1','IMPRESPM1','SUICTHNK1','SUICPLAN1','SUICTRY1',
  'PNRNMLIF','PNRNM30D','PNRWYGAMT','PNRWYGAMT','PNRRSHIGH'
  'TXYRRESOV1','TXYROUTPT1','TXYRMHCOP1','TXYREMRGN1', 'TXCURRENT1', 
  'TXLTYPNRL1','AUOPTYR1','AUINPYR1','AUALTYR1']`  
* Recode `3=1`: `['PNRRSHIGH', 'TXLTYPNRL1','TXYREMRGN1', 'AUOPTYR1','AUALTYR1']`
* Recode `5=1`: `['TXYRRESOV1', 'TXYROUTPT1','TXYRMHCOP1']`
* Recode `6=0`: `TXLTYPNRL`
* Recode `male=0`, `female=1`: `IRSEX` 
* Recode `1=4`, `2=3`, `3=2`, `4=1`: `IRMARITSTAT` 
* Recode `5=0`: `EDUHIGHCAT`
* Recode `1=2`, `2=1`, `3=0`, `4=0`: `IRWRKSTAT18` 
* Recode `1=3`, `3=1`: `COUTYP2`: 
* Recode `1=0`, `2=1`, `3=2`, `4=3`: `ADWRDST1` 


```python
columns = ['STDANYYR1','HEPBCEVER1', 'HIVAIDSEV1', 'CANCEREVR1', 'INHOSPYR ',
  'AMDELT','AMDEYR','ADDPR2WK1','DSTWORST1', 'IMPGOUTM1',
  'IMPSOCM1','IMPRESPM1','SUICTHNK1','SUICPLAN1','SUICTRY1',
  'PNRNMLIF','PNRNM30D','PNRWYGAMT','PNRWYGAMT','PNRRSHIGH'
  'TXYRRESOV1','TXYROUTPT1','TXYRMHCOP1','TXYREMRGN1', 'TXCURRENT1', 
  'TXLTYPNRL1','AUOPTYR1','AUINPYR1','AUALTYR1']
 
for col in df:
    df[col].replace(2,0,inplace=True)

df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>QUESTID2</th>
      <th>CATAG6</th>
      <th>IRSEX</th>
      <th>IRMARITSTAT</th>
      <th>EDUHIGHCAT</th>
      <th>IRWRKSTAT18</th>
      <th>COUTYP2</th>
      <th>HEALTH2</th>
      <th>STDANYYR1</th>
      <th>HEPBCEVER1</th>
      <th>...</th>
      <th>TXLTYPNRL1</th>
      <th>TXYRNOSPIL</th>
      <th>AUOPTYR1</th>
      <th>MHLMNT3</th>
      <th>MHLTHER3</th>
      <th>MHLDOC3</th>
      <th>MHLCLNC3</th>
      <th>MHLDTMT3</th>
      <th>AUINPYR1</th>
      <th>AUALTYR1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25095143</td>
      <td>1</td>
      <td>1</td>
      <td>4.0</td>
      <td>5</td>
      <td>0.0</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>13005143</td>
      <td>4</td>
      <td>1</td>
      <td>3.0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>67415143</td>
      <td>3</td>
      <td>0</td>
      <td>4.0</td>
      <td>4</td>
      <td>4.0</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70925143</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>5</td>
      <td>0.0</td>
      <td>0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>75235143</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>3</td>
      <td>4.0</td>
      <td>3</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 89 columns</p>
</div>




```python
col = ['PNRRSHIGH', 'TXLTYPNRL1', 'TXYREMRGN1', 'AUOPTYR1','AUALTYR1']

for col in df:
    df[col].replace(3,1,inplace=True)

df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>QUESTID2</th>
      <th>CATAG6</th>
      <th>IRSEX</th>
      <th>IRMARITSTAT</th>
      <th>EDUHIGHCAT</th>
      <th>IRWRKSTAT18</th>
      <th>COUTYP2</th>
      <th>HEALTH2</th>
      <th>STDANYYR1</th>
      <th>HEPBCEVER1</th>
      <th>...</th>
      <th>TXLTYPNRL1</th>
      <th>TXYRNOSPIL</th>
      <th>AUOPTYR1</th>
      <th>MHLMNT3</th>
      <th>MHLTHER3</th>
      <th>MHLDOC3</th>
      <th>MHLCLNC3</th>
      <th>MHLDTMT3</th>
      <th>AUINPYR1</th>
      <th>AUALTYR1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25095143</td>
      <td>1</td>
      <td>1</td>
      <td>4.0</td>
      <td>5</td>
      <td>0.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>13005143</td>
      <td>4</td>
      <td>1</td>
      <td>1.0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>67415143</td>
      <td>1</td>
      <td>0</td>
      <td>4.0</td>
      <td>4</td>
      <td>4.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70925143</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>5</td>
      <td>0.0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>75235143</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>1</td>
      <td>4.0</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 89 columns</p>
</div>




```python
df['SEX'] = df['IRSEX'].replace([1,2], [0,1])
df['MARRIED'] = df['IRMARITSTAT'].replace([1,2,3,4], [4,3,2,1])
df['EDUCAT'] = df['EDUHIGHCAT'].replace([1,2,3,4,5], [2,3,4,5,1])
df['EMPLOY18'] = df['IRWRKSTAT18'].replace([1,2,3,4], [2,1,0,0])
df['CTYMETRO'] = df['COUTYP2'].replace([1,2,3],[3,2,1])

df['EMODSWKS'] = df['ADWRDST1'].replace([1,2,3,4], [0,1,2,3])
df['TXLTPNRL'] = df['TXLTYPNRL1'].replace(6,0)

df['TXYRRESOV'] = df['TXYRRESOV1'].replace(5,1)
df['TXYROUTPT'] = df['TXYROUTPT1'].replace(5,1)
df['TXYRMHCOP'] = df['TXYRMHCOP1'].replace(5,1)

df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>QUESTID2</th>
      <th>CATAG6</th>
      <th>IRSEX</th>
      <th>IRMARITSTAT</th>
      <th>EDUHIGHCAT</th>
      <th>IRWRKSTAT18</th>
      <th>COUTYP2</th>
      <th>HEALTH2</th>
      <th>STDANYYR1</th>
      <th>HEPBCEVER1</th>
      <th>...</th>
      <th>SEX</th>
      <th>MARRIED</th>
      <th>EDUCAT</th>
      <th>EMPLOY18</th>
      <th>CTYMETRO</th>
      <th>EMODSWKS</th>
      <th>TXLTPNRL</th>
      <th>TXYRRESOV</th>
      <th>TXYROUTPT</th>
      <th>TXYRMHCOP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25095143</td>
      <td>1</td>
      <td>1</td>
      <td>4.0</td>
      <td>5</td>
      <td>0.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>1.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>13005143</td>
      <td>4</td>
      <td>1</td>
      <td>1.0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>4.0</td>
      <td>0</td>
      <td>2.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>67415143</td>
      <td>1</td>
      <td>0</td>
      <td>4.0</td>
      <td>4</td>
      <td>4.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>1.0</td>
      <td>5</td>
      <td>0.0</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70925143</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>5</td>
      <td>0.0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>75235143</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>1</td>
      <td>4.0</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>4.0</td>
      <td>2</td>
      <td>0.0</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 99 columns</p>
</div>




```python
df.shape
```




    (57146, 99)



### Examine column names


```python
df.columns
```




    Index(['QUESTID2', 'CATAG6', 'IRSEX', 'IRMARITSTAT', 'EDUHIGHCAT',
           'IRWRKSTAT18', 'COUTYP2', 'HEALTH2', 'STDANYYR1', 'HEPBCEVER1',
           'HIVAIDSEV1', 'CANCEREVR1', 'INHOSPYR', 'AMDELT', 'AMDEYR', 'ADDPR2WK1',
           'ADWRDST1', 'DSTWORST1', 'IMPGOUTM1', 'IMPSOCM1', 'IMPRESPM1',
           'SUICTHNK1', 'SUICPLAN1', 'SUICTRY1', 'PNRNMLIF', 'PNRNM30D',
           'PNRWYGAMT', 'PNRNMFLAG', 'PNRNMYR', 'PNRNMMON', 'OXYCNNMYR',
           'DEPNDPYPNR', 'ABUSEPYPNR', 'PNRRSHIGH', 'HYDCPDAPYU', 'OXYCPDAPYU',
           'OXCNANYYR2', 'TRAMPDAPYU', 'MORPPDAPYU', 'FENTPDAPYU', 'BUPRPDAPYU',
           'OXYMPDAPYU', 'DEMEPDAPYU', 'HYDMPDAPYU', 'HERFLAG', 'HERYR', 'HERMON',
           'ABODHER', 'MTDNPDAPYU', 'IRHERFY', 'TRBENZAPYU', 'ALPRPDAPYU',
           'LORAPDAPYU', 'CLONPDAPYU', 'DIAZPDAPYU', 'SVBENZAPYU', 'TRIAPDAPYU',
           'TEMAPDAPYU', 'BARBITAPYU', 'SEDOTANYR2', 'COCFLAG', 'COCYR', 'COCMON',
           'CRKFLAG', 'CRKYR', 'AMMEPDAPYU', 'METHAMFLAG', 'METHAMYR', 'METHAMMON',
           'HALLUCFLAG', 'LSDFLAG', 'ECSTMOFLAG', 'DAMTFXFLAG', 'KETMINFLAG',
           'TXYRRESOV1', 'TXYROUTPT1', 'TXYRMHCOP1', 'TXYREMRGN1', 'TXCURRENT1',
           'TXLTYPNRL1', 'TXYRNOSPIL', 'AUOPTYR1', 'MHLMNT3', 'MHLTHER3',
           'MHLDOC3', 'MHLCLNC3', 'MHLDTMT3', 'AUINPYR1', 'AUALTYR1', 'SEX',
           'MARRIED', 'EDUCAT', 'EMPLOY18', 'CTYMETRO', 'EMODSWKS', 'TXLTPNRL',
           'TXYRRESOV', 'TXYROUTPT', 'TXYRMHCOP'],
          dtype='object')



## Step 4: Rename Select Features for Description


```python
df =  df.rename(columns={'QUESTID2':'QID','CATAG6':'AGECAT',
     'STDANYYR1':'STDPYR','HEPBCEVER1':'HEPEVR','CANCEREVR1':'CANCEVR','INHOSPYR':'HOSPYR', 
     'AMDELT':'DEPMELT','AMDEYR':'DEPMEYR','ADDPR2WK1':'DEPMWKS','DSTWORST1':'DEPWMOS',
     'IMPGOUTM1':'EMOPGOUT','IMPSOCM1':'EMOPSOC','IMPRESPM1':'EMOPWRK',
     'SUICTHNK1':'SUICTHT','SUICPLAN1':'SUICPLN','SUICTRY1':'SUICATT',
     'PNRNMLIF':'PRLUNDR','PNRNM30D':'PRLUNDR30','PNRWYGAMT':'PRLGRTYR',
     'PNRNMFLAG':'PRLMISEVR','PNRNMYR':'PRLMISYR','PNRNMMON':'PRLMISMO',
     'OXYCNNMYR':'PRLOXYMSYR','DEPNDPYPNR':'PRLDEPYR','ABUSEPYPNR':'PRLABSRY',     
     'PNRRSHIGH':'PRLHIGH','HYDCPDAPYU':'HYDRCDYR','OXYCPDAPYU':'OXYCDPRYR', 
     'OXCNANYYR2':'OXYCTNYR','TRAMPDAPYU':'TRMADLYR','MORPPDAPYU':'MORPHPRYR',
     'FENTPDAPYU':'FENTNYLYR','BUPRPDAPYU':'BUPRNRPHN','OXYMPDAPYU':'OXYMORPHN',
     'DEMEPDAPYU':'DEMEROL','HYDMPDAPYU':'HYDRMRPHN','HERFLAG':'HEROINEVR',
     'HERYR':'HEROINYR', 'HERMON':'HEROINMO','ABODHER':'HEROINAB',
     'MTDNPDAPYU':'METHADONE','IRHERFY':'HEROINFQY',
     'TRBENZAPYU':'TRQBENZODZ','ALPRPDAPYU':'TRQALPRZM','LORAPDAPYU':'TRQLRZPM',
     'CLONPDAPYU':'TRQCLNZPM','DIAZPDAPYU':'TRQDIAZPM','SVBENZAPYU':'SDBENZDPN',
     'TRIAPDAPYU':'SDTRZLM','TEMAPDAPYU':'SDTMZPM','BARBITAPYU':'SDBARBTS', 
     'SEDOTANYR2':'SDOTHYR','COCFLAG':'COCNEVR','COCYR':'COCNYR','COCMON':'COCNMO',
     'CRKFLAG':'CRACKEVR','CRKYR':'CRACKYR','AMMEPDAPYU':'AMPHTMNYR', 
     'METHAMFLAG':'METHEVR','METHAMYR':'METHYR','METHAMMON':'METHMO',
     'HALLUCFLAG':'HLCNEVR','LSDFLAG':'LSDEVR','ECSTMOFLAG':'MDMAEVR',
     'DAMTFXFLAG':'DMTEVR','KETMINFLAG':'KETMNEVR', 
     'TXYRRESOV':'TRTRHBOVN','TXYROUTPT':'TRTRHBOUT','TXYRMHCOP':'TRTMHCTR',
     'TXYREMRGN1':'TRTERYR','TXCURRENT1':'TRTCURRCV','TXLTPNRL':'TRTCURPRL',
     'TXYRNOSPIL':'TRTGAPYR','AUOPTYR1':'MHTRTOYR','MHLMNT3':'MHTRTCLYR',
     'MHLTHER3':'MHTRTTHPY','MHLDOC3':'MHTRTDRYR', 'MHLCLNC3':'MHTRTMDOUT',
     'MHLDTMT3':'MHTRTHPPGM','AUINPYR1':'MHTRTHSPON','AUALTYR1':'MHTRTALT'})
     
df.shape
```




    (57146, 99)



## Step 5: Subset Data Frame with updated features


```python
df1 = df[['QID','AGECAT','SEX', 'MARRIED', 'EDUCAT', 
     'EMPLOY18','CTYMETRO','HEALTH2','STDPYR','HEPEVR','CANCEVR','HOSPYR', 
     'DEPMELT','DEPMEYR','DEPMWKS','DEPWMOS','EMODSWKS','EMOPGOUT',
     'EMOPSOC','EMOPWRK','SUICTHT','SUICPLN','SUICATT',
     'PRLUNDR','PRLUNDR30','PRLGRTYR','PRLMISEVR','PRLMISYR',
     'PRLMISMO','PRLOXYMSYR','PRLDEPYR','PRLABSRY','PRLHIGH',
     'HYDRCDYR','OXYCDPRYR','OXYCTNYR','TRMADLYR','MORPHPRYR',
     'FENTNYLYR','BUPRNRPHN','OXYMORPHN','DEMEROL','HYDRMRPHN',
     'HEROINEVR','HEROINYR','HEROINMO','HEROINAB','METHADONE','HEROINFQY',
     'TRQBENZODZ','TRQALPRZM','TRQLRZPM','TRQCLNZPM','TRQDIAZPM',
     'SDBENZDPN','SDTRZLM','SDTMZPM','SDBARBTS','SDOTHYR',
     'COCNEVR','COCNYR','COCNMO','CRACKEVR','CRACKYR',
     'AMPHTMNYR','METHEVR','METHYR','METHMO',
     'HLCNEVR','LSDEVR','MDMAEVR','DMTEVR','KETMNEVR', 
     'TRTRHBOVN','TRTRHBOUT','TRTMHCTR','TRTERYR','TRTCURRCV',
     'TRTCURPRL','TRTGAPYR','MHTRTOYR','MHTRTCLYR','MHTRTTHPY',
     'MHTRTDRYR','MHTRTMDOUT','MHTRTHPPGM','MHTRTHSPON','MHTRTALT']]
df1.shape
```




    (57146, 88)




```python
df1.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>QID</th>
      <th>AGECAT</th>
      <th>SEX</th>
      <th>MARRIED</th>
      <th>EDUCAT</th>
      <th>EMPLOY18</th>
      <th>CTYMETRO</th>
      <th>HEALTH2</th>
      <th>STDPYR</th>
      <th>HEPEVR</th>
      <th>...</th>
      <th>TRTCURPRL</th>
      <th>TRTGAPYR</th>
      <th>MHTRTOYR</th>
      <th>MHTRTCLYR</th>
      <th>MHTRTTHPY</th>
      <th>MHTRTDRYR</th>
      <th>MHTRTMDOUT</th>
      <th>MHTRTHPPGM</th>
      <th>MHTRTHSPON</th>
      <th>MHTRTALT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25095143</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>13005143</td>
      <td>4</td>
      <td>0</td>
      <td>4.0</td>
      <td>0</td>
      <td>2.0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>67415143</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>5</td>
      <td>0.0</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70925143</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>75235143</td>
      <td>0</td>
      <td>0</td>
      <td>4.0</td>
      <td>2</td>
      <td>0.0</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 88 columns</p>
</div>



## Step 6: Export data frame to CSV file


```python
df1.to_csv('nsduh-dataset.csv', sep=',', encoding='utf-8')
```
