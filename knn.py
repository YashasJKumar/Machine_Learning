import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

dataset = pd.read_csv("Datasets/Social_Network_Ads.csv")

X = dataset.iloc[:, [1, 2, 3]].values
y = dataset.iloc[:, -1].values

encoder = LabelEncoder()

X[:, 0] = encoder.fit_transform(X[:, 0])
# print(X[0:5, 0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors=5, metric="minkowski", p=2)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

print("Confusion Matrix: \n", confusion_matrix(y_test, y_pred))
print("Accuracy: ", str(accuracy_score(y_test, y_pred) * 100) + " %")
