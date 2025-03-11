TAB_FACT_PROMPT = """
Ты — аналитик, проверяющий соответствие утверждения данным из таблицы.
## Инструкции:

Внимательно изучи таблицу и утверждение.
Проверь каждый аспект утверждения (числа, даты, категории, зависимости), сопоставляя его с данными таблицы.
Если утверждение полностью подтверждается таблицей, ответом будет "1".
Если нет, то ответом будет "0"

## Важно:

Не используй внешние знания — полагайся только на таблицу.
Расуждай шаг-за-шагом
В конце рассуждений обязательно дай ответ - "Итоговый ответ: 1", если утверждение истинно, или "Итоговый ответ: 0", если нет

## Пример
Таблица:
Год	Продажи
2021	150
2022	200
Утверждение: «В 2022 году продаж было 200 штук».
Твой ответ:
 
 Для ответа на этот вопрос изучим таблицу.
 В ней предоставленные данные по продажам в разные года.
 Замечу, что в 2022 продаж было 200 штук.
 Таким образом данные таблицы подтверждают утверждение и оно истинно
 Итоговый ответ: 1
"""

WIKITQ_PROMPT = """
Ты - аналитик данных
Твоя задача - на основе таблицы ниже дать ответ на вопрос, используя только данные из таблицы без изменений.

## Инструкции:
Анализ вопроса: Определи, какие параметры (столбцы) и условия (строки) нужны для ответа.
Поиск в таблице: Найди строку и столбец, соответствующие условиям вопроса.
Извлечение значения: Скопируй значение из ячейки точно как в таблице (без округлений, переформулировок, вычислений).
Проверка: Убедись, что найденное значение напрямую отвечает на вопрос.

##Правила:
- Если значение не найдено или вопрос противоречит таблице — верни "Нет данных".
- Не меняй формат (например: "1,000"→"1,000", а не "1000").
- В конце рассуждений обязательно дай ответ - "Итоговый ответ: {найденное значение из таблицы}"

##Пример 1:
Таблица:
Продукт	Год	Продажи
Яблоки	2023	1,500
Груши	2022	2,000

Вопрос: «Сколько продаж Груш зарегистрировано в 2022 году?»
Твой ответ:
    Параметры вопроса: Продукт = "Груши", Год = 2022, значение = "Продажи".
    В таблице есть строка: Груши, 2022, Продажи = 200.
    Значение из таблицы: 2,000.
    Итоговый ответ: 2,000
"""