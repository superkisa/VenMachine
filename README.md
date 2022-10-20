# HW CLasses

# Task

> **Var1. Vending machine.** Imagine, you are developing a vending machine. You need to keep your vending machine state: which items are presented on which shelves, how much money inside machine to give change, how much money user inserted in current time, which purchases users made etc. It is expected that your class has following methods:
> 
> - Display methods and properties to check which items are available, current balance etc.
> - Pick up/add cash to the vending machine.
> - Methods to purchase products.
> - Methods for operator to put items into a vending machine (think of the limits on the size of the machine), deposit/withdraw internal wallet.

# Plan

Класс товар:

- Атрибуты
    - Наименование
    - Цена
    - Расположение в автомате
- Методы:
    - Вывод стоимости товара

Класс автомат:

- Атрибуты
    - Количество строк
    - Количество столбцов
    - Вместимость ячейки
    - Наполненность каждой из ячеек(?)
- Методы
    - Выдача единицы товара из ячейки
    - Вывод заполненности определенной ячейки
    - Вывод заполененности всех ячеек
    - Заполнение оператором ячеек
    - Вывод сообщения о том, что ячейка опустела

Класс касса:

- Атрибуты
    - Количество денег в автомате (разбить по номиналу)
- Методы
    - Вывод остатка денег в автомате
    - Поступление денег
    - Расчет и вывод сдачи
    - Вывод сообщения о том, что деньги заканчиваются
    - Опустошить кассу