import pandas as pd

data={
    "services":[
        "api-gateway","notification", "user-service", "order-service"
    ],
    "cpu_usage":[90, 60, 85, 45],
    "memory_usage":[70, 65, 80, 50],
    "error_rate":[35, 10, 25, 5]
}

df=pd.DataFrame(data) #create dataframe
# print(df)
# print(df.info())

# print(df["services"])   #get column
# print(df[["services", "cpu_usage"]])  #get multiple columns
# print(df.iloc[0])   #select rows using .iloc
print(df.loc[df["cpu_usage"] > 80])