#welcom to m.parsa store!!
#here we have some product:yogurt,chips,milk,Sausage,gum.
#i want to  start my project with random
import random

product=["yogurt","chips","milk","Sausage","gum"]

day_1={
    "yogurt":"nothing",
    "chips":"nothing",
    "milk":"nothing",
    "Sausage":"nothing",
    "gum":"nothing"
}
day_2={
    "yogurt":"nothing",
    "chips":"nothing",
    "milk":"nothing",
    "Sausage":"nothing",
    "gum":"nothing"
}
day_3={
    "yogurt":"nothing",
    "chips":"nothing",
    "milk":"nothing",
    "Sausage":"nothing",
    "gum":"nothing"
}

#this item sold in first day
y_1=random.randint(0,200)
day_1["yogurt"]=y_1
ch_1=random.randint(0,200)
day_1["chips"]=ch_1
m_1=random.randint(0,200)
day_1["milk"]=m_1
s_1=random.randint(0,200)
day_1["Sausage"]=s_1
g_1=random.randint(0,200)
day_1["gum"]=g_1

day_1_value=day_1.items()
print(f"the product that sold in first day ={day_1_value}")

#this item sold in second day
y_2=random.randint(0,200)
day_2["yogurt"]=y_2
ch_2=random.randint(0,200)
day_2["chips"]=ch_2
m_2=random.randint(0,200)
day_2["milk"]=m_2
s_2=random.randint(0,200)
day_2["Sausage"]=s_2
g_2=random.randint(0,200)
day_2["gum"]=g_2

day_2_value=day_2.items()
print(f"the product that sold in second day ={day_2_value}")

#this item sold in third day
y_3=random.randint(0,200)
day_3["yogurt"]=y_3
ch_3=random.randint(0,200)
day_3["chips"]=ch_3
m_3=random.randint(0,200)
day_3["milk"]=m_3
s_3=random.randint(0,200)
day_3["Sausage"]=s_3
g_3=random.randint(0,200)
day_3["gum"]=g_3

day_3_value=day_3.items()
print(f"the product that sold in third day={day_3_value}")

#the goals:
#first goal
y_m=0
most_y="nothing"
y_day1=int(day_1["yogurt"])
y_day2=int(day_2["yogurt"])
y_day3=int(day_3["yogurt"])

if y_day1>y_day2 and y_day1>y_day3:
    most_y="day_1"
    y_m=y_1
elif y_day2>y_day1 and y_day2>y_day3:
    most_y="day_2"
    y_m=y_2
elif y_day3>y_day1 and y_day3>y_day2:
    most_y="day_3"
    y_m=y_3
print(f"at {most_y} we sold the most yogurt={y_m}")

ch_m=0
most_ch="nothing"
ch_day1=int(day_1["chips"])
ch_day2=int(day_2["chips"])
ch_day3=int(day_3["chips"])

if ch_day1>ch_day2 and ch_day1>ch_day3:
    most_ch="day_1"
    ch_m=ch_1
elif ch_day2>ch_day1 and ch_day2>ch_day3:
    most_ch="day_2"
    ch_m=ch_2
elif ch_day3>ch_day1 and ch_day3>ch_day2:
    most_ch="day_3"
    ch_m=ch_3
print(f"at {most_ch} we sold the most chips={ch_m}")

m_m=0
most_m="nothing"
m_day1=int(day_1["milk"])
m_day2=int(day_2["milk"])
m_day3=int(day_3["milk"])

if m_day1>m_day2 and m_day1>m_day3:
    most_m="day_1"
    m_m=m_1
elif m_day2>m_day1 and m_day2>m_day3:
    most_m="day_2"
    m_m=m_2
elif m_day3>m_day1 and m_day3>m_day2:
    most_m="day_3"
    m_m=m_3
print(f"at {most_m} we sold the most milk={m_m}")

s_m=0
most_s="nothing"
s_day1=int(day_1["Sausage"])
s_day2=int(day_2["Sausage"])
s_day3=int(day_3["Sausage"])

if s_day1>s_day2 and s_day1>s_day3:
    most_s="day_1"
    s_m=s_1
elif s_day2>s_day1 and s_day2>s_day3:
    most_s="day_2"
    s_m=s_2
elif s_day3>s_day1 and s_day3>s_day2:
    most_s="day_3"
    s_m=s_3
print(f"at {most_s} we sold the most Sausage={s_m}")

g_m=0
most_g="nothing"
g_day1=int(day_1["gum"])
g_day2=int(day_2["gum"])
g_day3=int(day_3["gum"])

if g_day1>g_day2 and g_day1>g_day3:
    most_g="day_1"
    g_m=g_1
elif g_day2>g_day1 and g_day2>g_day3:
    most_s="day_2"
    s_m=s_2
elif g_day3>g_day1 and g_day3>g_day2:
    most_g="day_3"
    g_m=g_3
print(f"at {most_g} we sold the most gum={g_m}")
print("----------------------------------------------------------------")
#goal_2

more="nothing"

d_1_p=y_1+ch_1+m_1+s_1+g_1
d_2_p=y_2+ch_2+m_2+s_2+g_2
d_3_p=y_3+ch_3+m_3+s_3+g_3

if d_1_p>d_2_p and d_1_p>d_3_p:
    more="day_1"
    print(f"we sold the most item in {more} = {d_1_p}")
elif d_2_p>d_1_p and d_2_p>d_3_p:
    more="day_2"
    print(f"we sold the most item in {more} = {d_2_p}")
if d_3_p>d_2_p and d_3_p>d_1_p:
    more="day_3"
    print(f"we sold the most item in {more} = {d_3_p}")
