#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid lightseagreen 3px; padding: 20px">
# <div>    
# <p><font color="black" >
# Привет! Меня зовут Мария Четырева, и я буду делать ревью твоего проекта. Давай будем общаться на «ты». 
# По ходу твоего решения я буду оставлять комментарии, обрати внимание на их цвет.</font></p>
# </div>
# 
# <div class="alert alert-success">
# 
# <b>✔️</b> Зеленым цветом отмечены удачные и элегантные решения, на которые можно опираться в будущем.
# 
# </div>
# 
# <div class="alert alert-warning">
# 
# <b>⚠️</b> Жёлтым цветом выделено то, что в следующий раз можно сделать по-другому. Это не критичные ошибки, исправление которых остается на твое усмотрение. Однако постарайся, чтобы после твоих доработок их было не больше 3.
# 
# </div>
# 
# <div class="alert alert-danger">
# 
# <b>❌</b> Красным цветом отмечены критичные ошибки, без исправления которых проект не будет принят.
# 
# </div>
# 
# <p><font color="black" >Давай работать над проектом в диалоге: если ты что-то меняешь в проекте по моим рекомендациям — пиши об этом. Выбери для своих комментариев какой-то заметный цвет, так мне будет легче отследить изменения, например вот так:
# 
# <div class="alert alert-info">
# <b>Комментарий студента:</b> Ок
# <br>
# </div>
#     
# Пожалуйста, не перемещай, не изменяй и не удаляй мои комментарии. Всё это поможет выполнить повторную проверку твоего проекта оперативнее. </font></p>
# 
# </div>

# <div style="border:solid lightseagreen 3px; padding: 20px">
# <div>
# <b>Общий комментарий ревьюера: </b>
#    Хорошая работа! Однако есть некоторые критические ошибки и советы, как сделать твой проект еще лучше. Особенно обрати внимание на избыточное использование print() и display().
#    Исправь эти замечания и присылай на повторное ревью. Удачи!  
# 
# </div>
#     
#  <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера v2:</b> Молодец, все ошибки исправлены, работу принимаю!
# 
# </div>
#     

# # Яндекс.Музыка

# Сравнение Москвы и Петербурга окружено мифами. Например:
#  * Москва — мегаполис, подчинённый жёсткому ритму рабочей недели;
#  * Петербург — культурная столица, со своими вкусами.
# 
# На данных Яндекс.Музыки вы сравните поведение пользователей двух столиц.
# 
# **Цель исследования** — проверьте три гипотезы:
# 1. Активность пользователей зависит от дня недели. Причём в Москве и Петербурге это проявляется по-разному.
# 2. В понедельник утром в Москве преобладают одни жанры, а в Петербурге — другие. Так же и вечером пятницы преобладают разные жанры — в зависимости от города. 
# 3. Москва и Петербург предпочитают разные жанры музыки. В Москве чаще слушают поп-музыку, в Петербурге — русский рэп.
# 
# **Ход исследования**
# 
# Данные о поведении пользователей вы получите из файла `yandex_music_project.csv`. О качестве данных ничего не известно. Поэтому перед проверкой гипотез понадобится обзор данных. 
# 
# Вы проверите данные на ошибки и оцените их влияние на исследование. Затем, на этапе предобработки вы поищете возможность исправить самые критичные ошибки данных.
#  
# Таким образом, исследование пройдёт в три этапа:
#  1. Обзор данных.
#  2. Предобработка данных.
#  3. Проверка гипотез.
# 
# 

# ## Обзор данных
# 
# Составьте первое представление о данных Яндекс.Музыки.
# 
# 
# 

# Основной инструмент аналитика — `pandas`. Импортируйте эту библиотеку.

# In[1]:


# импорт библиотеки pandas
import pandas as pd


# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера:</b> Очень здорово, что ты используешь сокращение pd для Pandas, это общепринятое сокращение для этой библиотеки для удобной дальнейшей работы.
# 
# </div>

# <div class="alert alert-warning">
# <b>⚠️ Комментарий ревьюера:</b> Комментарии принято писать сверху. Если строка будет достаточно длинной, то их расположение справа неудобно. Учти это в своих будущих проектах  </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Привет, Мария! Большое спасибо, что с пониманием относишься к ошибкам и недочетам, и что даешь советы по улучшению взаимодействия с проектами в дальнейшем.
# Сразу здесь скажу, что все комментарии я переместил в соответствии с твоим замечанием.
# <br>
# </div>
# 

# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера v2:</b> Круто!
# 
# </div>

# Прочитайте файл `yandex_music_project.csv` из папки `/datasets` и сохраните его в переменной `df`:

# In[2]:


# чтение файла с данными и сохранение в df
df = pd.read_csv('/datasets/yandex_music_project.csv')


# Выведите на экран первые десять строк таблицы:

# In[3]:


# получение первых 10 строк таблицы df
df.head(10)


# <div class="alert alert-danger">
# 
# <b>❌ Комментарий ревьюера </b> Для вывода датафреймов действительно используется функция display(). Но в данном случае для вывода на экран не нужно использовать ни print(), ни display(): результат и так будет выведен, так как это последняя (и единственная) строчка ячейки.
# 
# </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Убрал вывод display()
# <br>
# </div>

# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера v2:</b> 👍
# 
# </div>

# Одной командой получить общую информацию о таблице:

# In[4]:


# получение общей информации о данных в таблице df
df.info()


# <div class="alert alert-danger">
# 
# <b>❌ Комментарий ревьюера </b> Мы хотели получить информацию о датафрейме, а получили сам датафрейм, причем с нарушением табличного вида
# 
# </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Исправил, убрал функцию display(), вывел информацию о датафрейме.
# <br>
# </div>

# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера v2:</b> Да,теперь все правильно
# 
# </div>

# Итак, в таблице семь столбцов. Тип данных во всех столбцах — `object`.
# 
# Согласно документации к данным:
# * `userID` — идентификатор пользователя;
# * `Track` — название трека;  
# * `artist` — имя исполнителя;
# * `genre` — название жанра;
# * `City` — город пользователя;
# * `time` — время начала прослушивания;
# * `Day` — день недели.
# 
# В названиях колонок видны три нарушения стиля:
# 1. Строчные буквы сочетаются с прописными.
# 2. Встречаются пробелы.
# 3. Найдите ещё одну проблему в названии колонок и опишите её в этом пункте.
# **Комментарий студента** - третье нарушение стиля заключается в присваивании не совсем правильного названия столбцу "время начала прослушивания". По названию столбца можно решить, что это общее время прослушивания. Или вообще не понять, что это за время. Считаю, что правильнее было бы назвать столбец "sl_time" - start listening time.
# 
# 
# 
# Количество значений в столбцах различается. Значит, в данных есть пропущенные значения.
# 

# <div class="alert alert-danger">
# 
# <b>❌ Комментарий ревьюера </b> Обрати внимание, что третье нарушение стиля ты должен обнаружить и вписать сам
# 
# </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Обнаружил, вписал в этот же пункт.
# <br>
# </div>

# <div class="alert alert-danger">
# 
# <b>❌ Комментарий ревьюера v2 </b> Ну к названиям да, можно придраться. Но мы имели ввиду еще одно нарушение. Подсказка: посмотри какие исправления в названия столбцов ты вносишь дальше
# 
# </div>

# **Выводы**
# 
# В каждой строке таблицы — данные о прослушанном треке. Часть колонок описывает саму композицию: название, исполнителя и жанр. Остальные данные рассказывают о пользователе: из какого он города, когда он слушал музыку. 
# 
# Предварительно можно утверждать, что, данных достаточно для проверки гипотез. Но встречаются пропуски в данных, а в названиях колонок — расхождения с хорошим стилем.
# 
# Чтобы двигаться дальше, нужно устранить проблемы в данных.

# ## Предобработка данных
# Исправьте стиль в заголовках столбцов, исключите пропуски. Затем проверьте данные на дубликаты.

# ### Стиль заголовков
# Выведите на экран названия столбцов:

# In[5]:


# перечень названий столбцов таблицы df
df.columns


# <div class="alert alert-danger">
# 
# <b>❌ Комментарий ревьюера </b> Избыточный вызов print() — исправь здесь и далее
# 
# </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Исправил, убрал функцию print(), вывел информацию о названиях столбцов.
# <br>
# </div>

# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера v2:</b> 👍
# 
# </div>

# Приведите названия в соответствие с хорошим стилем:
# * несколько слов в названии запишите в «змеином_регистре»,
# * все символы сделайте строчными,
# * устраните пробелы.
# 
# Для этого переименуйте колонки так:
# * `'  userID'` → `'user_id'`;
# * `'Track'` → `'track'`;
# * `'  City  '` → `'city'`;
# * `'Day'` → `'day'`.

# In[6]:


# переименование столбцов
df = df.rename(columns={'  userID': 'user_id', 'Track': 'track', '  City  ': 'city', 'Day' : 'day'})


# Проверьте результат. Для этого ещё раз выведите на экран названия столбцов:

# In[7]:


# проверка результатов - перечень названий столбцов
print(df.columns)


# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера:</b> Вот теперь с названиями столбцов все в порядке!
# 
# </div>

# ### Пропуски значений
# Сначала посчитайте, сколько в таблице пропущенных значений. Для этого достаточно двух методов `pandas`:

# In[8]:


# подсчёт пропусков
print(df.isna().sum())


# <div class="alert alert-success">
# <b>✔️ Комментарий ревьюера:</b> Ты использовал метод isna() для нахождения пропущенных значений, это отлично! На самом деле, isnull() и isna() делают одно и то же, но использование isna() предпочтительнее.  </div>

# Не все пропущенные значения влияют на исследование. Так в `track` и `artist` пропуски не важны для вашей работы. Достаточно заменить их явными обозначениями.
# 
# Но пропуски в `genre` могут помешать сравнению музыкальных вкусов в Москве и Санкт-Петербурге. На практике было бы правильно установить причину пропусков и восстановить данные. Такой возможности нет в учебном проекте. Придётся:
# * заполнить и эти пропуски явными обозначениями,
# * оценить, насколько они повредят расчётам. 

# Замените пропущенные значения в столбцах `track`, `artist` и `genre` на строку `'unknown'`. Для этого создайте список `columns_to_replace`, переберите его элементы циклом `for` и для каждого столбца выполните замену пропущенных значений:

# In[9]:


# перебор названий столбцов в цикле и замена пропущенных значений на 'unknown'    
columns_to_replace = df.loc[:, 'track' : 'genre']
for i in columns_to_replace:
    columns_to_replace[i] = columns_to_replace[i].fillna('unknown')
print(columns_to_replace)


# <div class="alert alert-danger">
# 
# <b>❌ Комментарий ревьюера </b> Список columns_to_replace должен содержать названия столбцов, в которых мы хотим произвести замену пропущенных значений
# 
# </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Исправил. Теперь цикл for перебирает значения columns_to_replace и заменяет пустые на 'unknown'
# <br>
# </div>

# Убедитесь, что в таблице не осталось пропусков. Для этого ещё раз посчитайте пропущенные значения.

# In[10]:


# подсчёт пропусков
print(df.isna().sum())


# ### Дубликаты
# Посчитайте явные дубликаты в таблице одной командой:

# In[11]:


# подсчёт явных дубликатов
print(df.duplicated().sum())


# <div class="alert alert-success">
# <b>✔️ Комментарий ревьюера:</b> В дальнейшем советую подписывать выводимые результаты. Это позволит быстрее разобраться в выводимых данных и не запутаться. В этом помогут f-строки. Примеры использования можешь посмотреть тут: 
#     
#    https://shultais.education/blog/python-f-strings
#  </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Я попробовал сделать так: print(f'Число явных дубликатов:', df.duplicated().sum()), выдало 0. Позже разберусь, как это должно работать.
# <br>
# </div>

# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера v2:</b> Все потому, что ты не перезапустил проект и сейчас в памяти находится обновленный датафрейм, в котором убраны дубликаты. Если нажать Cell → Run all, то все будет ок
# 
# </div>

# Вызовите специальный метод `pandas`, чтобы удалить явные дубликаты:

# In[12]:


# удаление явных дубликатов (с удалением старых индексов и формированием новых)
df = df.drop_duplicates().reset_index(drop=True)


# Ещё раз посчитайте явные дубликаты в таблице — убедитесь, что полностью от них избавились:

# In[13]:


# проверка на отсутствие дубликатов
print(df.duplicated().sum())


# <div class="alert alert-success">
# <b>✔️ Комментарий ревьюера:</b> Отлично, избавились от дубликатов
# </div>

# Теперь избавьтесь от неявных дубликатов в колонке `genre`. Например, название одного и того же жанра может быть записано немного по-разному. Такие ошибки тоже повлияют на результат исследования.

# Выведите на экран список уникальных названий жанров, отсортированный в алфавитном порядке. Для этого:
# * извлеките нужный столбец датафрейма, 
# * примените к нему метод сортировки,
# * для отсортированного столбца вызовите метод, который вернёт уникальные значения из столбца.

# In[14]:


# Просмотр уникальных названий жанров
df['genre'].sort_values().unique()


# <div class="alert alert-danger">
# 
# <b>❌ Комментарий ревьюера </b> Требовалось отсортировать список жанров, тогда ведь намного легче ориентироваться в нем 
# 
# </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Отсортировал методом sort_values(), действительно, так намного проще.
# <br>
# </div>

# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера v2:</b> 👍
# 
# </div>

# Просмотрите список и найдите неявные дубликаты названия `hiphop`. Это могут быть названия с ошибками или альтернативные названия того же жанра.
# 
# Вы увидите следующие неявные дубликаты:
# * *hip*,
# * *hop*,
# * *hip-hop*.
# 
# Чтобы очистить от них таблицу, напишите функцию `replace_wrong_genres()` с двумя параметрами: 
# * `wrong_genres` — список дубликатов,
# * `correct_genre` — строка с правильным значением.
# 
# Функция должна исправить колонку `genre` в таблице `df`: заменить каждое значение из списка `wrong_genres` на значение из `correct_genre`.

# In[15]:


# Функция для замены неявных дубликатов
def replace_wrong_genres(wrong_genres, correct_genres):
    for i in wrong_genres:
        df['genre'] = df['genre'].replace(wrong_genres, correct_genres)


# <div class="alert alert-danger">
# 
# <b>❌ Комментарий ревьюера </b> Странно написан цикл. Ты перебираешь значения wrong_genres из самого wrong_genres? Обозначь значение из списка wrong_genres другой переменной, например genre_to_replace
# 
# </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Исправил. Обычно так не делаю. Теперь переменная i.
# <br>
# </div>

# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера v2:</b> Да, теперь все хорошо)
# 
# </div>

# Вызовите `replace_wrong_genres()` и передайте ей такие аргументы, чтобы она устранила неявные дубликаты: вместо `hip`, `hop` и `hip-hop` в таблице должно быть значение `hiphop`:

# In[16]:


# Устранение неявных дубликатов
duplicates = ['hip', 'hop', 'hip-hop']
name = 'hiphop'
replace_wrong_genres(duplicates, name)


# Проверьте, что заменили неправильные названия:
# 
# *   hip
# *   hop
# *   hip-hop
# 
# Выведите отсортированный список уникальных значений столбца `genre`:

# In[17]:


# Проверка на неявные дубликаты
print(df['genre'].sort_values().unique())


# <div class="alert alert-danger">
# 
# <b>❌ Комментарий ревьюера </b> Так же добавь сортировку
# </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Добавил сортировку по тому же принципу, что и ранее, через метод sort_values().
# <br>
# </div>

# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера v2:</b> 👍
# 
# </div>

# **Выводы**
# 
# Предобработка обнаружила три проблемы в данных:
# 
# - нарушения в стиле заголовков,
# - пропущенные значения,
# - дубликаты — явные и неявные.
# 
# Вы исправили заголовки, чтобы упростить работу с таблицей. Без дубликатов исследование станет более точным.
# 
# Пропущенные значения вы заменили на `'unknown'`. Ещё предстоит увидеть, не повредят ли исследованию пропуски в колонке `genre`.
# 
# Теперь можно перейти к проверке гипотез. 

# ## Проверка гипотез

# ### Сравнение поведения пользователей двух столиц

# Первая гипотеза утверждает, что пользователи по-разному слушают музыку в Москве и Санкт-Петербурге. Проверьте это предположение по данным о трёх днях недели — понедельнике, среде и пятнице. Для этого:
# 
# * Разделите пользователей Москвы и Санкт-Петербурга
# * Сравните, сколько треков послушала каждая группа пользователей в понедельник, среду и пятницу.
# 

# Для тренировки сначала выполните каждый из расчётов по отдельности. 
# 
# Оцените активность пользователей в каждом городе. Сгруппируйте данные по городу и посчитайте прослушивания в каждой группе.
# 
# 

# In[18]:


# Подсчёт прослушиваний в каждом городе
city_count = df.groupby('city')['city'].count()


# <div class="alert alert-danger">
# 
# <b>❌ Комментарий ревьюера </b> Это можно сделать намного проще и даже одной строкой. Рассмотри для этого метод groupby
# 
# </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Да, действительно. Можно было догадаться по заданию "Сгруппируйте" :)
# <br>
# </div>

# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера v2:</b> Да)
# 
# </div>

# В Москве прослушиваний больше, чем в Петербурге. Из этого не следует, что московские пользователи чаще слушают музыку. Просто самих пользователей в Москве больше.
# 
# Теперь сгруппируйте данные по дню недели и подсчитайте прослушивания в понедельник, среду и пятницу. Учтите, что в данных есть информация только о прослушиваниях только за эти дни.
# 

# In[19]:


# Подсчёт прослушиваний в каждый из трёх дней
days_count = df.groupby('day')['day'].count()
print(days_count)


# <div class="alert alert-danger">
# 
# <b>❌ Комментарий ревьюера </b> Аналогично
# 
# </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Аналогично исправил.
# <br>
# </div>

# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера v2:</b> 👍
# 
# </div>

# В среднем пользователи из двух городов менее активны по средам. Но картина может измениться, если рассмотреть каждый город в отдельности.

# Вы видели, как работает группировка по городу и по дням недели. Теперь напишите функцию, которая объединит два эти расчёта.
# 
# Создайте функцию `number_tracks()`, которая посчитает прослушивания для заданного дня и города. Ей понадобятся два параметра:
# * день недели,
# * название города.
# 
# В функции сохраните в переменную строки исходной таблицы, у которых значение:
#   * в колонке `day` равно параметру `day`,
#   * в колонке `city` равно параметру `city`.
# 
# Для этого примените последовательную фильтрацию с логической индексацией.
# 
# Затем посчитайте значения в столбце `user_id` получившейся таблицы. Результат сохраните в новую переменную. Верните эту переменную из функции.

# In[20]:


# <создание функции number_tracks()>
# Объявляется функция с двумя параметрами: day, city.
# В переменной track_list сохраняются те строки таблицы df, для которых 
# значение в столбце 'day' равно параметру day и одновременно значение
# в столбце 'city' равно параметру city (используйте последовательную фильтрацию
# с помощью логической индексации).
# В переменной track_list_count сохраняется число значений столбца 'user_id',
# рассчитанное методом count() для таблицы track_list.
# Функция возвращает число - значение track_list_count.

def number_tracks(day, city):
    track_list = df[(df['day'] == day) & (df['city'] == city)]
    track_list_count = track_list['user_id'].count()
    return track_list_count

# Функция для подсчёта прослушиваний для конкретного города и дня.
# С помощью последовательной фильтрации с логической индексацией она 
# сначала получит из исходной таблицы строки с нужным днём,
# затем из результата отфильтрует строки с нужным городом,
# методом count() посчитает количество значений в колонке user_id. 
# Это количество функция вернёт в качестве результата


# <div class="alert alert-success">
# <b>✔️ Комментарий ревьюера:</b> Круто, что ты используешь логические операции для фильтрации строк датафрейма! О более продвинутых методах фильтрации мы расскажем подробнее в следующих курсах. </div>

# Вызовите `number_tracks()` шесть раз, меняя значение параметров — так, чтобы получить данные для каждого города в каждый из трёх дней.

# In[21]:


# количество прослушиваний в Москве по понедельникам
print(number_tracks('Monday', 'Moscow'))


# In[22]:


# количество прослушиваний в Санкт-Петербурге по понедельникам
print(number_tracks('Monday', 'Saint-Petersburg'))


# In[23]:


# количество прослушиваний в Москве по средам
print(number_tracks('Wednesday', 'Moscow'))


# In[24]:


# количество прослушиваний в Санкт-Петербурге по средам
print(number_tracks('Wednesday', 'Saint-Petersburg'))


# In[25]:


# количество прослушиваний в Москве по пятницам
print(number_tracks('Friday', 'Moscow'))


# In[26]:


# количество прослушиваний в Санкт-Петербурге по пятницам
print(number_tracks('Friday', 'Saint-Petersburg'))


# Создайте c помощью конструктора `pd.DataFrame` таблицу, где
# * названия колонок — `['city', 'monday', 'wednesday', 'friday']`;
# * данные — результаты, которые вы получили с помощью `number_tracks`.

# In[27]:


# Таблица с результатами
data = [
    ['Moscow', number_tracks('Monday', 'Moscow'), 
     number_tracks('Wednesday', 'Moscow'), 
     number_tracks('Friday', 'Moscow')],
    ['Saint-Petersburg', number_tracks('Monday', 'Saint-Petersburg'), 
     number_tracks('Wednesday', 'Saint-Petersburg'), 
     number_tracks('Friday', 'Saint-Petersburg')]
    
    
]
columns = ['city', 'monday', 'wednesday', 'friday']
table = pd.DataFrame(data=data, columns=columns)
print(table)


# <div class="alert alert-success">
# <b>✔️ Комментарий ревьюера:</b> Отличная таблица получилась. Хорошо, что ты не заполнял ее вручную </div>

# **Выводы**
# 
# Данные показывают разницу поведения пользователей:
# 
# - В Москве пик прослушиваний приходится на понедельник и пятницу, а в среду заметен спад.
# - В Петербурге, наоборот, больше слушают музыку по средам. Активность в понедельник и пятницу здесь почти в равной мере уступает среде.
# 
# Значит, данные говорят в пользу первой гипотезы.

# ### Музыка в начале и в конце недели

# Согласно второй гипотезе, утром в понедельник в Москве преобладают одни жанры, а в Петербурге — другие. Так же и вечером пятницы преобладают разные жанры — в зависимости от города.

# Сохраните таблицы с данными в две переменные:
# * по Москве — в `moscow_general`;
# * по Санкт-Петербургу — в `spb_general`.

# In[28]:


# получение таблицы moscow_general из тех строк таблицы df, 
# для которых значение в столбце 'city' равно 'Moscow'

moscow_general = df[df['city'] == 'Moscow']
display(moscow_general)


# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера:</b> Фильтрация — очень полезный инструмент. Теперь мы умеем извлекать нужные части данных, это здорово
# 
# </div>

# 

# In[29]:


# получение таблицы spb_general из тех строк таблицы df,
# для которых значение в столбце 'city' равно 'Saint-Petersburg'

spb_general = df[df['city'] == 'Saint-Petersburg']
display(spb_general)


# Создайте функцию `genre_weekday()` с четырьмя параметрами:
# * таблица (датафрейм) с данными,
# * день недели,
# * начальная временная метка в формате 'hh:mm', 
# * последняя временная метка в формате 'hh:mm'.
# 
# Функция должна вернуть информацию о топ-10 жанров тех треков, которые прослушивали в указанный день, в промежутке между двумя отметками времени.

# In[30]:


# Объявление функции genre_weekday() с параметрами table, day, time1, time2,
# которая возвращает информацию о самых популярных жанрах в указанный день в
# заданное время:
# 1) в переменную genre_df сохраняются те строки переданного датафрейма table, для
#    которых одновременно:
#    - значение в столбце day равно значению аргумента day
#    - значение в столбце time больше значения аргумента time1
#    - значение в столбце time меньше значения аргумента time2
#    Используйте последовательную фильтрацию с помощью логической индексации.
# 2) сгруппировать датафрейм genre_df по столбцу genre, взять один из его
#    столбцов и посчитать методом count() количество записей для каждого из
#    присутствующих жанров, получившийся Series записать в переменную
#    genre_df_count
# 3) отсортировать genre_df_count по убыванию встречаемости и сохранить
#    в переменную genre_df_sorted
# 4) вернуть Series из 10 первых значений genre_df_sorted, это будут топ-10
#    популярных жанров (в указанный день, в заданное время)

def genre_weekday(table, day, time1, time2):
    genre_df = table[
        (table['day'] == day) & 
        (table['time'] > time1) & 
        (table['time'] < time2)
    ]
    genre_df_count = genre_df.groupby('genre')['genre'].count()
    genre_df_sorted = genre_df_count.sort_values(ascending=False)
    return genre_df_sorted.head(10)


# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера:</b> Все верно
# 
# </div>

# Cравните результаты функции `genre_weekday()` для Москвы и Санкт-Петербурга в понедельник утром (с 7:00 до 11:00) и в пятницу вечером (с 17:00 до 23:00):

# In[31]:


# вызов функции для утра понедельника в Москве (вместо df — таблица moscow_general)
# объекты, хранящие время, являются строками и сравниваются как строки
# пример вызова: genre_weekday(moscow_general, 'Monday', '07:00', '11:00')

genre_weekday(moscow_general, 'Monday', '07:00', '11:00')


# In[32]:


# вызов функции для утра понедельника в Петербурге (вместо df — таблица spb_general)
display(genre_weekday(spb_general, 'Monday', '07:00', '11:00'))


# In[33]:


# вызов функции для вечера пятницы в Москве
display(genre_weekday(moscow_general, 'Monday', '18:00', '23:00'))


# In[34]:


# вызов функции для вечера пятницы в Петербурге
display(genre_weekday(spb_general, 'Monday', '18:00', '23:00'))


# **Выводы**
# 
# Если сравнить топ-10 жанров в понедельник утром, можно сделать такие выводы:
# 
# 1. В Москве и Петербурге слушают похожую музыку. Единственное отличие — в московский рейтинг вошёл жанр “world”, а в петербургский — джаз и классика.
# 
# 2. В Москве пропущенных значений оказалось так много, что значение `'unknown'` заняло десятое место среди самых популярных жанров. Значит, пропущенные значения занимают существенную долю в данных и угрожают достоверности исследования.
# 
# Вечер пятницы не меняет эту картину. Некоторые жанры поднимаются немного выше, другие спускаются, но в целом топ-10 остаётся тем же самым.
# 
# Таким образом, вторая гипотеза подтвердилась лишь частично:
# * Пользователи слушают похожую музыку в начале недели и в конце.
# * Разница между Москвой и Петербургом не слишком выражена. В Москве чаще слушают русскую популярную музыку, в Петербурге — джаз.
# 
# Однако пропуски в данных ставят под сомнение этот результат. В Москве их так много, что рейтинг топ-10 мог бы выглядеть иначе, если бы не утерянные  данные о жанрах.

# ### Жанровые предпочтения в Москве и Петербурге
# 
# Гипотеза: Петербург — столица рэпа, музыку этого жанра там слушают чаще, чем в Москве.  А Москва — город контрастов, в котором, тем не менее, преобладает поп-музыка.

# Сгруппируйте таблицу `moscow_general` по жанру и посчитайте прослушивания треков каждого жанра методом `count()`. Затем отсортируйте результат в порядке убывания и сохраните его в таблице `moscow_genres`.

# In[35]:


# одной строкой: группировка таблицы moscow_general по столбцу 'genre', 
moscow_genres = moscow_general.groupby('genre')['genre'].count().sort_values(ascending=False)
# подсчёт числа значений 'genre' в этой группировке методом count(), 
# сортировка получившегося Series в порядке убывания и сохранение в moscow_genres


# <div class="alert alert-danger">
# 
# <b>❌ Комментарий ревьюера </b> Отсортированный Series необходимо сохранить в переменную moscow_genres. Сейчас там хранится просто число прослушиваний каждого жанра
# 
# </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Сделал по-человечески. Теперь moscow_genres отсортирован. Не стыдно показывать.
# <br>
# </div>

# <div class="alert alert-warning">
# <b>⚠️ Комментарий ревьюера:</b> Методы удобно вызывать «цепочкой», это позволит не заводить промежуточных переменных. В нашем случае так:
#      
# .count().sort_values(ascending=False)
# </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Да, теперь, поняв на практике, как это работает, постараюсь всегда следовать этому правилу.
# <br>
# </div>

# <div class="alert alert-success">
# 
# <b>✔️ Комментарий ревьюера v2:</b> Молодец!
# 
# </div>

# Выведите на экран первые десять строк `moscow_genres`:

# In[36]:


display(moscow_genres.sort_values(ascending=False).head(10))# просмотр первых 10 строк moscow_genres


# Теперь повторите то же и для Петербурга.
# 
# Сгруппируйте таблицу `spb_general` по жанру. Посчитайте прослушивания треков каждого жанра. Результат отсортируйте в порядке убывания и сохраните в таблице `spb_genres`:
# 

# In[37]:


# одной строкой: группировка таблицы spb_general по столбцу 'genre', 
spb_genres = spb_general.groupby('genre')['genre'].count()
# подсчёт числа значений 'genre' в этой группировке методом count(), 
spb_genres.sort_values(ascending=False)
# сортировка получившегося Series в порядке убывания и сохранение в spb_genres


# Выведите на экран первые десять строк `spb_genres`:

# In[38]:


# просмотр п# просмотр первых 10 строк spb_genres
display(spb_genres.sort_values(ascending=False).head(10))


# **Выводы**

# Гипотеза частично подтвердилась:
# * Поп-музыка — самый популярный жанр в Москве, как и предполагала гипотеза. Более того, в топ-10 жанров встречается близкий жанр — русская популярная музыка.
# * Вопреки ожиданиям, рэп одинаково популярен в Москве и Петербурге. 
# 

# <div class="alert alert-success">
# <b>✔️ Комментарий ревьюера:</b> Выводы — это очень важная часть. Как раз ради них и делается исследование. Не забывай в своих будущих проектах делать промежуточные выводы после каждого раздела и общий вывод в конце  </div>

# ## Итоги исследования

# Вы проверили три гипотезы и установили:
# 
# 1. День недели по-разному влияет на активность пользователей в Москве и Петербурге. 
# 
# Первая гипотеза полностью подтвердилась.
# 
# 2. Музыкальные предпочтения не сильно меняются в течение недели — будь то Москва или Петербург. Небольшие различия заметны в начале недели, по понедельникам:
# * в Москве слушают музыку жанра “world”,
# * в Петербурге — джаз и классику.
# 
# Таким образом, вторая гипотеза подтвердилась лишь отчасти. Этот результат мог оказаться иным, если бы не пропуски в данных.
# 
# 3. Во вкусах пользователей Москвы и Петербурга больше общего чем различий. Вопреки ожиданиям, предпочтения жанров в Петербурге напоминают московские.
# 
# Третья гипотеза не подтвердилась. Если различия в предпочтениях и существуют, на основной массе пользователей они незаметны.
# 
# **На практике исследования содержат проверки статистических гипотез.**
# Из данных одного сервиса не всегда можно сделать вывод о всех жителях города.
# Проверки статистических гипотез покажут, насколько они достоверны, исходя из имеющихся данных. 
# С методами проверок гипотез вы ещё познакомитесь в следующих темах.

# <div class="alert alert-success">
# <b>✔️ Комментарий ревьюера:</b> Вот и готов твой первый проект в портфолио! Осталось лишь немного доработать </div>

# <div class="alert alert-info">
# <b>Ответ на комментарий ревьюера:</b> Спасибо тебе большое. Надеюсь, сейчас я все исправил.
# <br>
# </div>
