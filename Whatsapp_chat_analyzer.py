import re
import pandas as pd

def preprocess(data):

    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern,data)[1:]

    # print(messages)

    dates = re.findall(pattern,data)
    # print(dates)

    df = pd.DataFrame({'message_date':dates,'user_message':messages})

    df['message_date'] = pd.to_datetime(df['message_date'],format='%d/%m/%Y, %H:%M - ')

    # print(df)

    user = []
    message = []

    for msg in df['user_message']:
        entry = re.split('([\w\W]+?):\s',msg)
        # print(entry)
        if(entry[0]!=''):
            user.append('group_notification')
            message.append(entry[0])
        else:
            user.append(entry[1])
            message.append(entry[2])    

    df['user'] = user
    df['messages'] = message 

    df.drop(columns=['user_message'],inplace=True)
    df.rename(columns={'message_date':'date'},inplace=True)

    df['Year'] = df['date'].dt.year
    df['Month'] = df['date'].dt.month_name()
    df['Day'] = df['date'].dt.day
    df['Hour'] = df['date'].dt.hour
    df['Minute'] = df['date'].dt.minute
    df['Month_num'] = df['date'].dt.month
    df['only-date'] = df['date'].dt.date
    df['day_name'] = df['date'].dt.day_name()

    period = []

    for hour in df[['day_name','Hour']]['Hour']:
        if hour == 23:
            period.append(str(hour)+"-"+str('00'))
        elif hour == 0:
            period.append(str('00')+"-"+str(hour+1))
        else:
            period.append(str(hour)+"-"+str(hour+1))

    df['period']=period            




    print(df)
    return df


file = open('WhatsApp Chat with 3B (2024-25) CSE-AIML OFFICIAL GROUP .txt',encoding='utf-8')

data = file.read()

print(preprocess(data))



# print(data)


