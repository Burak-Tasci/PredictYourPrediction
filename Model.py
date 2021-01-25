import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def getData():
    with open("numbers.data","r") as f:
        DATA = f.read().split()
        np.random.shuffle(DATA)
        TRAIN_DATA, TEST_DATA = DATA[:100],DATA[101:]
        TRAIN_DATA = pd.DataFrame(data=TRAIN_DATA,index=range(100),columns=['8-Digit Number'])
        TRAIN_DATA['Answer'] = -1
        return TRAIN_DATA, TEST_DATA

TrainData, TestData = getData()

def PrepareNumber(number):
    temp = list(number)
    if (len(temp) != 8):
        for i in range(8-len(temp)):
            temp.insert(0,'0')
            
    return temp

# with open("training_numbers.data","w") as w:
#     w.write("8-Digit Number,Answer\n")
#     for i in range(100):
#         print("Tahmininiz nedir?")
#         print(TrainData['8-Digit Number'][i]+": ",end="")
#         temp = input()
#         w.write(TrainData['8-Digit Number'][i]+","+ temp+"\n")

for i in range(100):
    print("Tahmin:")
    print(TrainData['8-Digit Number'][i]+":",end="")
    TrainData['Answer'][i] = int(input())


veriler = TrainData
Ones = []
for i in range(len(veriler.iloc[:,0])):
    temp = str(veriler.iloc[:,0][i]).count('1')
    Ones.append(temp)

veriler = pd.concat([veriler.iloc[:,:-1],pd.DataFrame(data=Ones,columns = ['OneCount']),veriler.iloc[:,-1:]],axis = 1)

Digits = veriler.iloc[:,:1]
Digits['8-Digit Number'] = Digits['8-Digit Number'].map(str)
Digits_list = list()

for i in range(len(Digits['8-Digit Number'])):
    temp = PrepareNumber(Digits['8-Digit Number'][i])
    Digits_list.append(temp)
    
Digits_df = pd.DataFrame(data = Digits_list,columns = ['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eight'])

Digits_df['First'] = Digits_df['First'].map(int)
Digits_df['Second'] = Digits_df['Second'].map(int)
Digits_df['Third'] = Digits_df['Third'].map(int)
Digits_df['Fourth'] = Digits_df['Fourth'].map(int)
Digits_df['Fifth'] = Digits_df['Fifth'].map(int)
Digits_df['Fifth'] = Digits_df['Fifth'].map(int)
Digits_df['Sixth'] = Digits_df['Sixth'].map(int)
Digits_df['Seventh'] = Digits_df['Seventh'].map(int)
Digits_df['Eight'] = Digits_df['Eight'].map(int)
veriler = pd.concat([Digits_df,veriler.iloc[:,1:]],axis = 1) 

X = veriler.iloc[:,:-1].values
Y = veriler.iloc[:,-1:].values

from sklearn.tree import DecisionTreeRegressor

r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X,Y)

numbers_pred = np.array(PrepareNumber(TestData[1])).reshape(-1,8).astype('int64')
Ones_pred =  np.count_nonzero(numbers_pred)
Ones_pred = pd.DataFrame(data = Ones_pred,index=range(1),columns = ['OneCount'])
numbers_pred = pd.DataFrame(data = numbers_pred,columns = ['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eight'])
Prediction_X = pd.concat([numbers_pred,Ones_pred],axis = 1)

Prediction_Y = r_dt.predict(Prediction_X)























