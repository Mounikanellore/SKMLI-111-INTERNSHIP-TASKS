from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import plot_tree
import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('iris')
target=df['species']
df1 = df.copy()
df1=df1.drop('species',axis=1)
df1.shape
X=df1
le=LabelEncoder()
target=le.fit_transform(target)
Y=target
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
print("Training split input:",X_train.shape)
print("Testing split input:",X_test.shape)
dtree=DecisionTreeClassifier()
dtree.fit(X_train,Y_train)
print("Decision Tree Clasifier Created")
Y_pred=dtree.predict(X_test)
print("classification_report-\n",classification_report(Y_test,Y_pred))
plt.figure(figsize=(20,20))
dec_tree= plot_tree(decision_tree=dtree,feature_names=df1.columns,class_names=['setosa','versicolor','virginica'],filled=True,precision=1)