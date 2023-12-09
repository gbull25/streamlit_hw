import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px

def gender_distribution(df):
    fig = px.histogram(df, x='GENDER', color ='GENDER', 
                    title='Принадлежность к полу')
    sex = ['Мужчина', 'Женщина']
    for idx, name in enumerate(sex):
        fig.data[idx].name = name
        fig.data[idx].hovertemplate = name
    
    return fig

def work_distribution(df):
    fig = px.histogram(df, x='SOCSTATUS_WORK_FL', color ='SOCSTATUS_WORK_FL', 
                    title='Статус работы')
    work = ['Работает', 'Безработный']
    for idx, name in enumerate(work):
        fig.data[idx].name = name
        fig.data[idx].hovertemplate = name
    
    return fig

def pens_distribution(df):
    fig = px.histogram(df, x='SOCSTATUS_PENS_FL', color ='SOCSTATUS_PENS_FL', 
                    title='Статус пенсионного возраста')
    pens = ['Не пенсионер', 'Пенсионер']
    for idx, name in enumerate(pens):
        fig.data[idx].name = name
        fig.data[idx].hovertemplate = name
    
    return fig

def ownership_distibution(df):
    fig = px.histogram(df, x='FL_PRESENCE_FL', color ='FL_PRESENCE_FL', 
                    title='Наличие собственной недвижимости')
    flat = ['Имеет недвижимость', 'Не имеет недвижимости']
    for idx, name in enumerate(flat):
        fig.data[idx].name = name
        fig.data[idx].hovertemplate = name
    
    return fig

def education_distribution(df):
    fig = px.histogram(df, x='EDUCATION', color ='EDUCATION', 
                    title='Образование')
    fig.update_layout(xaxis = {"categoryorder":"total ascending"})
    return fig

def marital_distribution(df):
    fig = px.histogram(df, x='MARITAL_STATUS', color ='MARITAL_STATUS', 
                    title='Статус брачных отношений')
    fig.update_layout(xaxis = {"categoryorder":"total ascending"})

    return fig


def family_income_distribution(df):
    fig = px.histogram(df, x='FAMILY_INCOME', color ='FAMILY_INCOME', 
                       title='Заработок семьи')
    fig.update_layout(xaxis = {"categoryorder":"total ascending"})
    
    return fig

def personal_income_distribution(df):
    fig = px.histogram(df, x='PERSONAL_INCOME', 
                       title='Индивидуальный заработок',
                       marginal="box", # or violin, rug
                       hover_data=df.columns)
    fig.update_layout(xaxis = {"categoryorder":"total ascending"})
    
    return fig


def top_regions_distribution(df):
    top_regions = df['REG_ADDRESS_PROVINCE'].value_counts().head(10).reset_index()
    fig = px.bar(top_regions, x='count', 
                color = 'REG_ADDRESS_PROVINCE',
                title='Самые популярные регионы проживания клиентов',
                labels = {'x':'Регион', 'y':'Номер'}
                )
    fig.update_layout(xaxis = {"categoryorder":"total ascending"})
    return fig

def correlation_heatmap(df):
    numerical_columns = ['AGE', 'CHILD_TOTAL', 'PERSONAL_INCOME', 'TARGET', 'LOAN_NUM_TOTAL', 'LOAN_NUM_CLOSED', 'OWN_AUTO']
    correlation_matrix_all = df[numerical_columns].corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix_all, annot=True, cmap='coolwarm', linewidths=.5, ax=ax)
    ax.set_title('Матрица корреляции численных столбцов')
    return fig, ax

def loans_scatter(df):
    fig  = px.scatter(df, x='LOAN_NUM_TOTAL', y='LOAN_NUM_CLOSED',
                      title = 'Количество взятых кредитов и количество возвращенных кредитов',
                      labels = dict(x = 'Взятые кредиты', y = 'Возвращенные кредиты'),
                      marginal_x="histogram", marginal_y="rug") 
    return fig

def family_work_distribution(df):
    fig = px.histogram(df, x='FAMILY_INCOME', color ='SOCSTATUS_WORK_FL', 
                       title='Заработок семьи')
    fig.update_layout(xaxis = {"categoryorder":"total ascending"})
    
    work = ['Работает', 'Безработный']
    for idx, name in enumerate(work):
        fig.data[idx].name = name
        fig.data[idx].hovertemplate = name
    
    return fig

def target_to_all(df):
    target = df['TARGET']
    columns = ['AGE', 'GENDER', 'EDUCATION', 'MARITAL_STATUS',
       'CHILD_TOTAL', 'DEPENDANTS', 'SOCSTATUS_WORK_FL', 'SOCSTATUS_PENS_FL',
       'REG_ADDRESS_PROVINCE', 'FL_PRESENCE_FL', 'OWN_AUTO',
       'FST_PAYMENT', 'LOAN_NUM_TOTAL', 
       'LOAN_NUM_CLOSED', 'FAMILY_INCOME', 'PERSONAL_INCOME']
    names = ['Возраст', 'Пол', 'Образование', 'Статус брака', 'Кол-во детей',
             'Кол-во подопечных', 'Статус работы', 'Статус пенсионера', 
             'Регистрационный адрес', 'Наличие недвижимости', 'Наличие автомобиля',
             'Первый платеж', 'Кол-во кредитов', 'Кол-во погашенных кредитов',
             'Заработок семьи', 'Индивидуальный заработок']
    fig_list = []
    for column, name in zip(columns,names):
            fig = px.histogram(df, x=column , color = target, 
                       title=f'График признака {name} в зависимости от целевой переменной')
            
            work = ['Отклик был', 'Отклика не было']
            for idx, name in enumerate(work):
                fig.data[idx].name = name
                fig.data[idx].hovertemplate = name

            fig.update_layout(xaxis = {"categoryorder":"total ascending"})
            fig_list.append(fig)
    return fig_list
