# 📊 WhatsApp Chat Analyzer

A web-based application to analyze WhatsApp group or personal chats and gain insights like message statistics, activity trends, sentiment analysis, and more. Built using Python and Streamlit.

## 🚀 Demo

🔗 [Live App](https://whatsapp-chat-analyzer-crdqgmnegvfeq2r667cwif.streamlit.app/)

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Libraries:** Pandas, Matplotlib, NumPy, Seaborn, WordCloud, Emojify

## 📂 Features

- 📈 **Message Stats**: Total messages, words, media, and links shared.
- 🕒 **Timeline Analysis**: Monthly and daily activity trends.
- 🧑‍🤝‍🧑 **User Activity**: Most active users in the group.
- 🔥 **Busiest Time**: Heatmap of active hours.
- 💬 **Common Words**: Frequently used words in the chat.
- 😂 **Emoji Stats**: Emoji usage breakdown.
- 😊 **Sentiment Analysis**: Understand the emotional tone of conversations.
- 🌥️ **WordCloud**: Visualize word frequency in a cloud format.

## 📁 How to Use

1. Export your WhatsApp chat from the app:
   - Open WhatsApp → Chat → More → Export Chat → Without Media
2. Save the `.txt` file.
3. Upload it to this app and explore the insights!

## 💻 Local Setup

```bash
git clone https://github.com/Arpit-Seth232/Whatsapp-chat-analyzer.git
cd Whatsapp-chat-analyzer
pip install -r requirements.txt
streamlit run app.py
