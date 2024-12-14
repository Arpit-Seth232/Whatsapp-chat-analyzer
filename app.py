import streamlit as st
import Whatsapp_chat_analyzer as ws
import matplotlib.pyplot as plt
from collections import Counter
import helper as hp
import pandas as pd
import seaborn as sn

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')

    df = ws.preprocess(data)

    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'Overall')

    selected_user = st.sidebar.selectbox("Show analysis with respect to ",user_list)

   

    if( st.sidebar.button("Show Analysis")):
        
        ## top statistics

        st.title("Top Statistics")
        
        col1,col2,col3,col4 = st.columns(4)

        col1.header("Total Messages")
        col1.title(hp.fetch_stats(selected_user,df)[0])

        col2.header("Total Words")
        col2.title(hp.fetch_stats(selected_user,df)[1])

        col3.header("Total Media Files")
        col3.title(hp.fetch_stats(selected_user,df)[2])

        col4.header("Total Links")
        col4.title(hp.fetch_stats(selected_user,df)[3])


        ## monthly - timeline 

        st.title("Monthly Timeline")

        timeline = hp.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'],timeline['messages'],color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        ## daily - timeline

        st.title('Daily Timeline')

        daily = hp.daily_timeline(selected_user,df)
        fig,ax=plt.subplots()
        ax.bar(daily['only-date'],daily['messages'],color='purple')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)


        ## activity map

        st.title('Activity Map')

        col1,col2 = st.columns(2)

        col1.header("Most Busy Day")
        busy_day = hp.week_activity_map(selected_user,df)
        fig,ax = plt.subplots()
        ax.bar(busy_day.index,busy_day.values)
        col1.pyplot(fig)

        col2.header("Most Busy Month")
        busy_month = hp.monthly_acticity_map(selected_user,df)
        fig,ax = plt.subplots()
        ax.bar(busy_month.index,busy_month.values,color='orange')
        col2.pyplot(fig)


        ## weekly activity map

        st.title('Weekly Activity Map')

        user_heatmap = hp.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sn.heatmap(user_heatmap)
        st.pyplot(fig)





        if(selected_user == 'Overall'):
            st.header("Most Busy User")
            col1,col2 = st.columns(2)

            x,y=hp.most_busy_user(df)
           
            fig,ax = plt.subplots()

            ax.bar(x.index,x.values)
            plt.xticks(rotation='vertical')
            col1.pyplot(fig)

            col2.dataframe(y)

        df_wc = hp.create_wordcloud(selected_user,df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.title("Word Cloud")
        st.pyplot(fig)


        ## calculating top 20 words

        words = hp.most_common_words(selected_user,df)
        words = pd.DataFrame(Counter(words).most_common(20))

        fig,ax = plt.subplots()
        ax.barh(words[0],words[1])
        st.title('Most Common Words')
        st.pyplot(fig)
        
        st.table(words)


        ## finding the emojis used

        emojis = hp.emoji_analysis(selected_user,df)
        emojis = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))


        st.title("Emoji Analysis")

        col1,col2 = st.columns(2)
        col1.table(emojis)
        if(len(emojis)!=0):
            fig,ax = plt.subplots()
            ax.pie(emojis[1],labels=emojis[0],autopct='%0.2f')
            col2.pyplot(fig)






        

    
