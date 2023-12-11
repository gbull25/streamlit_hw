import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import plot_func

df = pd.read_csv('full_table.csv')

st.title('Исследование склонности к отклику у клиентов банка')
st.image('data/bank3.jpg', caption='Великолепные клиенты нашего чудесного банка')

st.sidebar.title("Информация")
st.sidebar.info(
    """
    Эта дэшборда -- часть домашки по 
    замечательному курсу Прикладной Python
    программы магистратуры МОВС ВШЭ.
    """
)
st.sidebar.info("Пожалуйста, поделитесь впечатлениями о данной борде. \
                Ссылку на мой гитхаб вы можете найти \
                [здесь](https://github.com/gbull25/streamlit_hw).")

with st.expander('Описание задачи', expanded=True):
    st.markdown('''Нам дан датасет реальных банковских данных,
                содержащий нефильтрованную информацию о клиентах, 
                а также целевуюпеременную - откликнулся ли клиент 
                на некую маркетинговую кампанию.''')
    st.markdown('''Само же задание состоит за двух частей.  
                 - Первая заключается в сборе и фильтрации информации
                 о клиентах из нескольких файлов в формате csv
                 в одну таблицу, где каждая строчка соответствует
                 полной информации об одном клиенте. Эта часть
                 задания может быть найдена в моем репозитории,
                 ссылку на который вы можете найти в левой части 
                 страницы.  
                 - Вторая цель состоит в том, чтобы 
                 при помощи инструмента Streamlit провести 
                 :rainbow[разведочный анализ данных], 
                 чем мы с вами здесь и займемся!''')

csv = plot_func.convert_df(df)

st.download_button(
    label="Скачать итоговый датафрейм в формате CSV",
    data=csv,
    file_name='full_table.csv',
    mime='text/csv',
)
st.divider()

st.header('Разведочный анализ -- EDA')
st.subheader('Информация о клиентах')
st.divider()
st.subheader('Ниже представлены графики распределения признаков клиентуры Банка.')
with st.expander('Какого пола клиент?', expanded=True):
    st.plotly_chart(plot_func.gender_distribution(df), use_container_width=True)
    st.write('Количество мужчин в нашей выборке примерно вдвое больше, чем женщин.')
st.divider()

with st.expander('Работает ли клиент?', expanded=True):
    st.plotly_chart(plot_func.work_distribution(df), use_container_width=True)
    st.write('Почти все клиенты работают.')
st.divider()

with st.expander('Клиент -- пенсионер?', expanded=True):
    st.plotly_chart(plot_func.pens_distribution(df), use_container_width=True)
    st.write('Большинство клиентов не достигли пенсионного \
            возраста или не имеют пенсии по иным причинам.')
st.divider()

with st.expander('Есть ли квартира у клиента?', expanded=True):
    st.plotly_chart(plot_func.ownership_distibution(df), use_container_width=True)
    st.write('Клиентов без квартиры в собственности примерно \
            в два раза больше, чем клиентов с квартирой.')
st.divider()

with st.expander('Какое образование у клиента?', expanded=True):
    st.plotly_chart(plot_func.education_distribution(df), use_container_width=True)
    st.write('Больше всего людей со средне-специальным образованием. \
            На втором месте - среднее, на третьем - одно высшее образование.')
st.divider()

with st.expander('Женат ли клиент?', expanded=True):
    st.plotly_chart(plot_func.marital_distribution(df), use_container_width=True)
    st.write('Большинство клиентов состоит в зарегестрированном браке.')
st.divider()

with st.expander('Сколько зарабатывает семья клиента?', expanded=True):
    st.plotly_chart(plot_func.family_income_distribution(df), use_container_width=True)
    st.write('Семейный бюджет большинства клиентов \
             составляет от 10 до 50 тысяч рублей.')
st.divider()

with st.expander('Есть ли завсимость между заработком\
                  семьи клиента и его рабочим статусом?', expanded=True):
    st.plotly_chart(plot_func.family_work_distribution(df), use_container_width=True)
    st.write('В группе с доходом выше 50 тысяч рублей нет безработных клиентов.\
            В основных группах почти нет неработающих.\
            В группах с низким доходом около трети безработные')
st.divider()

with st.expander('Сколько зарабатывает сам клиент?', expanded=True):
    st.plotly_chart(plot_func.personal_income_distribution(df), use_container_width=True)
    st.write('Индвидуальный бюджет представлен на графике выше.\
            Вот некоторые характеристики этой величины: \
            Медиана - 12 тысяч рублей\
            Среднее значение - около 14 тысяч рублей')
st.divider()

with st.expander('Где проживает клиент?', expanded=True):
    st.plotly_chart(plot_func.top_regions_distribution(df), use_container_width=True)
    st.write('Чаще всего встречаются клиенты, проживающие в Краснодарском крае.')
st.divider()

st.subheader('Матрица корреляций признаков')
st.divider()

fig, ax = plot_func.correlation_heatmap(df)
st.pyplot(fig, use_container_width=True)
st.write('На графике видно сильную положительную корреляцию\
          количества взятых кредитов и закрытых. Можно\
          подсветить зависимость между количеством\
          детей и возрастом клиента, а также между индвидуальным заработком\
          и фактом наличия машины. Между остальными признаками\
          ярко выраженной зависимости не видно.')
st.divider()

st.plotly_chart(plot_func.loans_scatter(df), use_container_width=True)
st.write('Видно высокую взаимосвязь между количеством взятых кредитов и закрытых.\
          Как таковых выбросов нет.')
st.divider()

st.subheader('Графики распределения признаков клиентуры Банка\
              в зависимости от целевой переменной.')
with st.expander('Графиков много. Нажмите, если готовы.', expanded=False):
    figs = plot_func.target_to_all(df)
    for figure in figs:
        st.plotly_chart(figure, use_container_width=True)
    