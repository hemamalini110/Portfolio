import streamlit as sl
import pandas as pandas

sl.set_page_config(layout="wide")

col1 , col2 =sl.columns(2)

with col1:
    sl.image("images/photo.png")

with col2:
    sl.title("Ahaan ")
    content ="""
    "Hi, I am Ahaan ,I am from Bengaluru. I completed my B. Com (Honors) from Christ College, Bengaluru in 2018.

My father is a doctor, and my mother is a social worker. I have a younger brother who is pursuing his B.Tech.

I love playing basketball and have represented my school in many competitions. My active participation in sports has taught me many skills. I am also an active member of my school alumni club and take initiative in organizing alumni meets.

I have a fascination for languages, so I am learning the Japanese language."""

    sl.info(content)

col3 , empty_cols ,col4 = sl.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        sl.title(row["title"])
        sl.write(row["description"])
        sl.image("images/"+row["image"])
        sl.write(f"[source code]({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        sl.title(row["title"])
        sl.write(row["description"])
        sl.image("images/"+row["image"])
        sl.write(f"[source code]({row['url']})")