{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7c69a03b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import streamlit as st\n",
    "import altair as alt\n",
    "from wordcloud import WordCloud\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ccfcd7d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.set_page_config(page_title=\"Day 5\", layout=\"wide\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "89c23259",
   "metadata": {},
   "outputs": [],
   "source": [
    "def loadData():\n",
    "    #query = \"select * from tweetinformation\"\n",
    "    #df = db_execute_fetch(query, dbName=\"tweets\", rdf=True)\n",
    "    df=pd.read_csv('processed_tweet_data.csv')\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f55b43b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def selectHashTag():\n",
    "    df = loadData()\n",
    "    hashTags = st.multiselect(\"choose combaniation of hashtags\", list(df['hashtags'].unique()))\n",
    "    if hashTags:\n",
    "        df = df[np.isin(df, hashTags).any(axis=1)]\n",
    "        st.write(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e033f67e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def selectLocAndAuth():\n",
    "    df = loadData()\n",
    "    location = st.multiselect(\"choose Location of tweets\", list(df['place'].unique()))\n",
    "    lang = st.multiselect(\"choose Language of tweets\", list(df['lang'].unique()))\n",
    "\n",
    "    if location and not lang:\n",
    "        df = df[np.isin(df, location).any(axis=1)]\n",
    "        st.write(df)\n",
    "    elif lang and not location:\n",
    "        df = df[np.isin(df, lang).any(axis=1)]\n",
    "        st.write(df)\n",
    "    elif lang and location:\n",
    "        location.extend(lang)\n",
    "        df = df[np.isin(df, location).any(axis=1)]\n",
    "        st.write(df)\n",
    "    else:\n",
    "        st.write(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8e4718ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "def barChart(data, title, X, Y):\n",
    "    title = title.title()\n",
    "    st.title(f'{title} Chart')\n",
    "    msgChart = (alt.Chart(data).mark_bar().encode(alt.X(f\"{X}:N\", sort=alt.EncodingSortField(field=f\"{Y}\", op=\"values\",\n",
    "                order='ascending')), y=f\"{Y}:Q\"))\n",
    "    st.altair_chart(msgChart, use_container_width=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ad6fd8f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def wordCloud():\n",
    "    df = loadData()\n",
    "    cleanText = ''\n",
    "    for text in df['original_text']:\n",
    "        tokens = str(text).lower().split()\n",
    "\n",
    "        cleanText += \" \".join(tokens) + \" \"\n",
    "\n",
    "    wc = WordCloud(width=650, height=450, background_color='white', min_font_size=5).generate(cleanText)\n",
    "    st.title(\"Tweet Text Word Cloud\")\n",
    "    st.image(wc.to_array())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f08ce712",
   "metadata": {},
   "outputs": [],
   "source": [
    "def stBarChart():\n",
    "    df = loadData()\n",
    "    dfCount = pd.DataFrame({'Tweet_count': df.groupby(['original_author'])['original_text'].count()}).reset_index()\n",
    "    dfCount[\"original_author\"] = dfCount[\"original_author\"].astype(str)\n",
    "    dfCount = dfCount.sort_values(\"Tweet_count\", ascending=False)\n",
    "\n",
    "    num = st.slider(\"Select number of Rankings\", 0, 50, 5)\n",
    "    title = f\"Top {num} Ranking By Number of tweets\"\n",
    "    barChart(dfCount.head(num), title, \"original_author\", \"Tweet_count\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "9c577e4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def langPie():\n",
    "    df = loadData()\n",
    "    dfLangCount = pd.DataFrame({'Tweet_count': df.groupby(['lang'])['original_text'].count()}).reset_index()\n",
    "    dfLangCount[\"lang\"] = dfLangCount[\"lang\"].astype(str)\n",
    "    dfLangCount = dfLangCount.sort_values(\"Tweet_count\", ascending=False)\n",
    "    dfLangCount.loc[dfLangCount['Tweet_count'] < 10, 'lang'] = 'Other languages'\n",
    "    st.title(\" Tweets Language pie chart\")\n",
    "    fig = px.pie(dfLangCount, values='Tweet_count', names='lang', width=500, height=350)\n",
    "    fig.update_traces(textposition='inside', textinfo='percent+label')\n",
    "\n",
    "    colB1, colB2 = st.beta_columns([2.5, 1])\n",
    "\n",
    "    with colB1:\n",
    "        st.plotly_chart(fig)\n",
    "    with colB2:\n",
    "        st.write(dfLangCount)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "2d0b3be7",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.title(\"Data Display\")\n",
    "selectHashTag()\n",
    "st.markdown(\"<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>\", unsafe_allow_html=True)\n",
    "selectLocAndAuth()\n",
    "st.title(\"Data Visualizations\")\n",
    "wordCloud()\n",
    "with st.beta_expander(\"Show More Graphs\"):\n",
    "    stBarChart()\n",
    "    langPie()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a73f0de",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
