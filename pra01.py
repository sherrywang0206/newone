# 載入pandas 模組
import pandas as pd
#建立Series
data=pd.Series([55,20,33])
#基本Series
#print("找最大",data.max())
#print("中位數",data.median())
#print("資料放大",data*2)

#data=data==55 #逐一比較每一個值，輸出boolean
#print(data)

#建立dataframe{"key":[value,value]}
data=pd.DataFrame({
  "name":["John","Python","Mary"],
  "salary":[1000,555,666]

})
#print(data)
#取得特定欄位(直行)
#print(data["salary"])
#取得特定列
print(data.iloc[0])


