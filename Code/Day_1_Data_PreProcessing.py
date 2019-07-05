"""
error to fix:
/usr/local/lib/python3.7/site-packages/sklearn/utils/deprecation.py:66: DeprecationWarning: Class Imputer is deprecated; Imputer was deprecated in version 0.20 and will be removed in 0.22. Import impute.SimpleImputer from sklearn instead.
  warnings.warn(msg, category=DeprecationWarning)
/usr/local/lib/python3.7/site-packages/sklearn/preprocessing/_encoders.py:415: FutureWarning: The handling of integer data will change in version 0.22. Currently, the categories are determined based on the range [0, max(values)], while in the future they will be determined based on the unique values.
If you want the future behaviour and silence this warning, you can specify "categories='auto'".
In case you used a LabelEncoder before this OneHotEncoder to convert the categories to integers, then you can now use the OneHotEncoder directly.
  warnings.warn(msg, FutureWarning)
/usr/local/lib/python3.7/site-packages/sklearn/preprocessing/_encoders.py:451: DeprecationWarning: The 'categorical_features' keyword is deprecated in version 0.20 and will be removed in 0.22. You can use the ColumnTransformer instead.
  "use the ColumnTransformer instead.", DeprecationWarning)
"""


## Step 1: Importing the libraries
import numpy as np
import pandas as pd
 
## Step 2: Importing dataset
dataset = pd.read_csv('../datasets/Data.csv')
# iloc[ : , :-1] 取除最后一列的所有列
X = dataset.iloc[ : , :-1].values
#print(f"X:{X}")
# iloc[ : , 3] 取最后一列
Y = dataset.iloc[ : , 3].values
#print(f"Y:{Y}")
 
## Step 3: Handling the missing data
#from sklearn.preprocessing import Imputer
#from sklearn import impute.SimpleImputer
from sklearn.impute import SimpleImputer
#imputer = SimpleImputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = SimpleImputer(missing_values = "NaN", strategy = "mean")
# error Input contains NaN, infinity or a value too large for dtype('float64')'')
print(f"X[ : , 1:3]:{X[ : , 1:3]}")
imputer = imputer.fit(X[ : , 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])
 
## Step 4: Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
### Creating a dummy variable
#onehotencoder = OneHotEncoder(categorical_features = [0])
onehotencoder = OneHotEncoder(ColumnTransformer = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y =  labelencoder_Y.fit_transform(Y)
 
## Step 5: Splitting the datasets into training sets and Test sets 
# old name is cross_validation, new name is mode_selection
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size = 0.2, random_state = 0)

## Step 6: Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)
### Done :smile:


