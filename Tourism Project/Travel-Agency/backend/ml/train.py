#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# In[36]:


df=pd.read_csv("tourism_price_dataset_1000.csv")


# In[37]:


df


# In[38]:


df = df.drop("ID", axis=1)


# In[39]:


df.info()


# In[40]:


df.describe()


# In[41]:


X = df.drop("Total_Cost", axis=1)
y = df["Total_Cost"]


# In[42]:


categorical_cols = [
    "Location",
    "Food_Level",
    "Guide_Support",
    "Transport_Type",
    "Season"
]


# In[43]:


numerical_cols = [
    "Num_Days",
    "Num_People",
    "Hotel_Rating",
    "Distance_km",
    "Activities_Count"
]


# In[44]:


preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ]
)


# In[45]:


model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=200))
])


# In[46]:


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# In[47]:


model.fit(X_train, y_train)


# In[48]:


y_pred = model.predict(X_test)


# In[49]:


print("\nModel Evaluation:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))


# In[50]:


joblib.dump(model, "tourism_price_model.pkl")


# In[51]:


model = joblib.load("tourism_price_model.pkl")


# In[52]:


new_data = pd.DataFrame([{
    "Location": "Goa",
    "Num_Days": 4,
    "Num_People": 2,
    "Food_Level": "Premium",
    "Hotel_Rating": 4,
    "Guide_Support": "Yes",
    "Transport_Type": "Flight",
    "Season": "Peak",
    "Distance_km": 5,
    "Activities_Count": 6
}])


# In[53]:


prediction = model.predict(new_data)


# In[54]:


print("Predicted Price:", prediction[0])


# In[ ]:




