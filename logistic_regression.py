import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score


dataset = pd.read_csv("Datasets/User_Data.csv")

# input
x = dataset.iloc[:, [2, 3]].values  # dataframe.iloc[:,start_col:end_col]

# output
y = dataset.iloc[:, 4].values

xtrain, xtest, ytrain, ytest = train_test_split(
    x, y, test_size=0.25, random_state=0
)


sc_x = StandardScaler()  # z = (x - u) / s where u is mean & s is std deviation  s=sqrt(x-mu)/N
xtrain = sc_x.fit_transform(xtrain)
xtest = sc_x.transform(xtest)

print(xtrain[0:10, :])


classifier = LogisticRegression(random_state=0)
classifier.fit(xtrain, ytrain)

y_pred = classifier.predict(xtest)


cm = confusion_matrix(ytest, y_pred)
print("Confusion Matrix : \n", cm)

print("Accuracy : ", accuracy_score(ytest, y_pred))
