import emoji.unicode_codes
import pandas as pd
from urlextract import URLExtract
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import emoji

extractor = URLExtract()

def total_messages(df):
     return df.shape[0]




def total_words(df):
     
     words = []

     for msg in df['messages']:
          words.extend(msg.split())
     return(len(words)) 




def total_media(df):
    cnt =0 
    for msg in df['messages']:
         if(msg == '<Media omitted>\n'):
              cnt+=1
    return cnt  



def total_links(df):
     link = []
     for msg in df['messages']:
          link.extend(extractor.find_urls(msg))
     return len(link)







############################################# main #####################################################3


def fetch_stats(selected_user,df):
     words = []
     if(selected_user != 'Overall'):
        df = df[df['user']==selected_user]
          
     return total_messages(df),total_words(df),total_media(df),total_links(df)


def most_busy_user(df):
     x=df['user'].value_counts().head()
     df = round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'index':'name','user':'percent'})
     
     return x,df

def create_wordcloud(selected_user,df):
     if(selected_user != 'Overall'):
        df = df[df['user']==selected_user]
     wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
     df_wc=wc.generate(df['messages'].str.cat(sep=" "))
     return df_wc

     
def most_common_words(selected_user,df):
     if(selected_user != 'Overall'):
        df = df[df['user']==selected_user]

     temp = df[df['user']!='group_notification']
     temp = temp[temp['messages']!='<Media omitted>\n']

     fs = open('stop_hinglish.txt','r')
     stop_words = fs.read()
     fs.close()

     words = []
     for message in temp['messages']:
          for word in message.split():
               if word not in stop_words:
                    words.append(word)
   
     return words   


def emoji_analysis (selected_user,df):
      if(selected_user != 'Overall'):
        df = df[df['user']==selected_user]

      emojis=[]
      for message in df['messages']:
           emojis.extend([c for c in message if c in emoji.EMOJI_DATA])  

      return emojis   


def monthly_timeline(selected_user,df):
      if(selected_user != 'Overall'):
        df = df[df['user']==selected_user]

      timeline = df.groupby(['Year','Month_num','Month']).count()['messages'].reset_index()

      time = []
      for i in range(timeline.shape[0]):
          time.append(timeline['Month'][i]+'-'+str(timeline['Year'][i]))

      timeline['time'] = time 
      return timeline  


def daily_timeline (selected_user,df):
     if(selected_user != 'Overall'):
        df = df[df['user']==selected_user]

     timeline = df.groupby(['only-date']).count()['messages'].reset_index()  
     return timeline


def week_activity_map(selected_user,df):
    if(selected_user != 'Overall'):
        df = df[df['user']==selected_user]

    return df['day_name'].value_counts()   
    

def monthly_acticity_map(selected_user,df):
    if(selected_user != 'Overall'):
        df = df[df['user']==selected_user]

    return df['Month'].value_counts()  


def activity_heatmap(selected_user,df):
    if(selected_user != 'Overall'):
        df = df[df['user']==selected_user]
    
    act = df.pivot_table(index='day_name',columns='period',values='messages',aggfunc='count').fillna(0)
    return act
    

    




   
    
               


 