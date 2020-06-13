from sklearn.datasets import load_breast_cancer
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
# data, target = load_breast_cancer(return_x_y = True)
# print(data)
cancer = load_breast_cancer()
# print(cancer.DESCR)
cols = cancer.feature_names
data = cancer.data
output_feature_name=cancer.target
# print('out\n',output_feature_name)
# print('data\n',data)
# print('cols\n',cols)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(data, output_feature_name, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Using DecisionTreeClassifier of tree class to use Decision Tree Algorithm

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)
# print(X_test)

plt.plot(X_test,Y_test)
plt.plot(X_test,Y_pred)
plt.ylabel('Accuracy')
plt.xlabel('Number of Neighbors')
# plt.legend()
plt.show()


# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)













































# df = pd.DataFrame(data, index= cols,columns=cols)
# print(df)
# lists= list(out.columns)
# print(lists)

# out = pd.DataFrame(data)

# print(type(out))


# out.columns=list
# print(out)
# print(df.rename(columns={'A': 'a', 'C': 'c'}))
# print(cols.isnull().sum())

# list=[]
# for i in cancer.target:
#     print(i)
#     if i == 0:
#         list.append(out[0])
#     else:
#         list.append(out[1])

# print(list)

# # dat= pd.DataFrame(data)
# # print(type(cols))
# # for i in range(len(cols)):
# #     dat = dat.rename(columns={i:cols[i]})
# # print(dat)
# # print(df.rename(columns={'A': 'a', 'C': 'c'}))
# df = {}
# for i in range(len(cols)):
#     df[cols[i]] = data[i] 
# # print(df)cd
# dfs=pd.DataFrame(df.items())
# print(dfs['mean radius'])

# # exploratory data analysis
# sns.heatmap(dfs.isnull(),yticklabels=False)

# plt.show()

# print(data.isnull().sum())
# print(dfs.isna().sum())