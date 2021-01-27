from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from UI_python import Ui_MainWindow
import numpy as np
import pandas as pd

def getData():
    with open("numbers.data","r") as f:
        DATA = f.read().split()
        np.random.shuffle(DATA)
        TRAIN_DATA, TEST_DATA = DATA[:100],DATA[101:]
        TRAIN_DATA = pd.DataFrame(data=TRAIN_DATA,index=range(100),columns=['8-Digit Number'])
        TRAIN_DATA['Answer'] = -1
        return TRAIN_DATA, TEST_DATA
    
def PrepareNumber(number):
    temp = list(number)
    if (len(temp) != 8):
        for i in range(8-len(temp)):
            temp.insert(0,'0')
            
    return temp


def Prediction(TrainData,TestData):
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
    
    numbers_pred = np.array(PrepareNumber(TestData)).reshape(-1,8).astype('int64')
    Ones_pred =  np.count_nonzero(numbers_pred)
    Ones_pred = pd.DataFrame(data = Ones_pred,index=range(1),columns = ['OneCount'])
    numbers_pred = pd.DataFrame(data = numbers_pred,columns = ['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eight'])
    Prediction_X = pd.concat([numbers_pred,Ones_pred],axis = 1)
    
    Prediction_Y = int(r_dt.predict(Prediction_X))
    return Prediction_Y


class Window(QMainWindow):
    def __init__(self):
        self.Train_Data, self.Test_Data = getData()
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.help.setIcon(QtGui.QIcon("help.png"))
        self.train_count = 0
        self.test_count = 0
        self.ui.DataInput.setText(self.Train_Data['8-Digit Number'][self.train_count])
        self.ui.Predict0Btn.setEnabled(False)
        self.ui.Predict1Btn.setEnabled(False)
        

    def data_input_0btn(self):
        Answer = 0
        self.Train_Data['Answer'][self.train_count] = Answer
        self.train_count +=1
        if self.train_count != 100:
            self.ui.DataInput.setText(self.Train_Data['8-Digit Number'][self.train_count])
        else:
            self.ui.DataInput1Btn.setEnabled(False)
            self.ui.DataInput1Btn.setEnabled(False)
            QMessageBox.information(self, "Succeed!",
                                        "You've completed data input sequence, you can pass prediction sequence.")
            self.ui.DataInput.setText("Completed!")
            self.ui.Predict.setText(self.Test_Data[self.test_count])
            self.ui.Predict0Btn.setEnabled(True)
            self.ui.Predict1Btn.setEnabled(True)

    def data_input_1btn(self):
        Answer = 1
        self.Train_Data['Answer'][self.train_count] = Answer
        self.train_count +=1
        if self.train_count != 100:
            self.ui.DataInput.setText(self.Train_Data['8-Digit Number'][self.train_count])
        else:
            self.ui.DataInput1Btn.setEnabled(False)
            self.ui.DataInput0Btn.setEnabled(False)
            QMessageBox.information(self, "Succeed!",
                                        "You've completed data input sequence, you can pass prediction sequence.")
            self.ui.DataInput.setText("Completed!")
            self.ui.Predict.setText(self.Test_Data[self.test_count])
            self.ui.Predict0Btn.setEnabled(True)
            self.ui.Predict1Btn.setEnabled(True)


    def predict_0btn(self):
        Answer = 0
        Pred = Prediction(self.Train_Data,self.Test_Data[self.test_count])
        self.test_count +=1
        if Answer == Pred:
            response = "Your answer: {answer} \nMachine's prediction: {pred} ".format(answer = Answer,pred = Pred)
            QMessageBox.information(self,"Succeed!!!",response)
        else:
            response = "Your answer: {answer} \nMachine's prediction: {pred} ".format(answer = Answer,pred = Pred)
            QMessageBox.warning(self,"Unsuccessful :(",response)
            

    def predict_1btn(self):
        Answer = 1
        Pred = Prediction(self.Train_Data,self.Test_Data[self.test_count])
        self.test_count +=1
        if Answer == Pred:
            response = "Your answer: {answer} \nMachine's prediction: {pred} ".format(answer = Answer,pred = Pred)
            QMessageBox.information(self,"Succeed!!!",response)
        else:
            response = "Your answer: {answer} \nMachine's prediction: {pred} ".format(answer = Answer,pred = Pred)
            QMessageBox.warning(self,"Unsuccessful :(",response)

    def help(self):
                    QMessageBox.information(self, "Help!",
                                        "You need to")


app = QApplication([])
window = Window()
window.show()
app.exec()
