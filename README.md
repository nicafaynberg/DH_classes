Я решила попробовать совместить результаты поиска самых частотных слов (униграмм) и биграмм. Попробовала я на тексте из Медузы, обнаружила, что в самых частотных биграммах есть слова, которых нет в простом частотном списке того же текста. 
Мысль такая, что мб стоит объединять результаты, чтобы были более полные результаты. 


Частотный список обычный
[('зулейх', 14), ('роман', 12), ('сериал', 12), ('яхина', 6), ('серия', 5), ('становиться', 5), ('самый', 5), ('книга', 5), ('показывать', 4), ('ссылка', 4), ('татарский', 4), ('муж', 4), ('муртаза', 4), ('лес', 4), ('персонаж', 4), ('сезон', 4), ('ничто', 4), ('россия', 3), ('открывать', 3), ('глаз', 3)]

Частотный список биграмм 
[(('зулейх', 'открывать'), 3), (('открывать', 'глаз'), 3), (('кулацкий', 'ссылка'), 2), (('ссылка', 'х'), 2), (('роман', 'гузель'), 2), (('гузель', 'яхина'), 2), (('татарский', 'крестьянка'), 2), (('крестьянка', 'зулейх'), 2), (('книга', 'яхина'), 2), (('создатель', 'сериал'), 2)]

Не совпадают слова: серия, самый, муж, Муртаза, лес, персонаж, сезон, ничто, Россия (эти есть в первом списке, но нет во втором); кулацкий, крестьянка, создатель (эти есть во втором, но их нет в первом). 

Не получилось: 
- разделить список биграмм на униграммы, следовательно, сравнить эти списки автоматически
- прогнать это же самое на файле из репозитория с файлами RT. не знаю почему, вроде из json достала тексты
- и много чего еще... 
