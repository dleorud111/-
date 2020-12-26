#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "Malgun Gothic"


# In[4]:


data = pd.read_csv('./enrolleds_detail.csv')
data


# In[5]:


# 시간데이터 전처리하기
format = '%Y-%m-%dT%H:%M:%S.%f'
data['done_date_time'] = pd.to_datetime(data['done_date'], format=format)
data


# In[6]:


# 요일 구하기(dt.day_name함수)
data['done_date_time_weekday'] = data['done_date_time'].dt.day_name()
data


# In[7]:


# 요일별 사용자 수 계산
weekdata = data.groupby('done_date_time_weekday')['user_id'].count()
weeks = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

# 요일 순서대로 순서 정렬
weekdata = weekdata.agg(weeks)
weekdata


# In[8]:


plt.figure(figsize=(8,5))
plt.bar(weekdata.index, weekdata)
plt.title('요일별 수강 완료 수강생 수')
plt.xlabel('요일')
plt.ylabel('수강생(명)')
plt.xticks(rotation=90)
plt.show()


# In[9]:


# 시간 추출(dt.hour)
data['done_date_time_hour'] = data['done_date_time'].dt.hour
data


# In[11]:


# 시간별로 유저 개수
hourdata = data.groupby('done_date_time_hour')['user_id'].count()

# 정렬
hourdata = hourdata.sort_index()
hourdata


# In[14]:


plt.figure(figsize=(22,5))
# 선그래프
plt.plot(hourdata.index, hourdata)
plt.title('시간별 수강 완료 수강생 수')
plt.xlabel('시간')
plt.ylabel('수강생(명)')
plt.xticks(np.arange(24))
plt.show()


# In[15]:


# 요일별 시간별 그래프 그리기
data_pivot_table = pd.pivot_table(data, values='user_id', aggfunc='count', index=['done_date_time_weekday'],
              columns=['done_date_time_hour']).agg(weeks)
data_pivot_table


# In[22]:


# 히트맵그리기(높은 수치 확인 쉽게)
plt.figure(figsize=(14,5))
plt.pcolor(data_pivot_table)
plt.xticks(np.arange(0.5,len(data_pivot_table.columns),1), data_pivot_table.columns)
plt.yticks(np.arange(0.5,len(data_pivot_table.index),1), data_pivot_table.index)
plt.title('요일별 종료 시간 히트맵')
plt.xlabel('시간')
plt.ylabel('요일')
plt.colorbar()
plt.show()


# In[ ]:




