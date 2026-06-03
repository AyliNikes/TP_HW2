# Продукт

Это консольное приложение, которое позволяет создавать блюда, добавлять их в "рецепты", масштабировать порции и генерировать список покупок.

## Описание

Реализованы классы `Ingredient`, `Recipe`, `DietaryRecipe` и `ShoppingList`
с использованием принципов ООП.
'Ingredient' представляет собой класс, хранящий данные об одном конректном ингредиенте с его необходимым количеством.
'Recipe' - это класс рецепта некоторого блюда со списком всех нужных ингредиентов.
'DietaryRecipe' - класс, унаследованный от Recipe с возможностью уточнения категории блюда.
'ShoppingList' - класс, содержащий рецепты и их ингредиенты.

## Установка

```bash
git clone https://github.com/AyliNikes/TP_HW2.git
cd TP_HW2
```

Установка зависимостей:

```bash
# Linux / macOS
python3 -m pip install -r requirements.txt

# Windows
py -m pip install -r requirements.txt
```

## Использование

Код классов находится в `classes.py`. Запуск тестов:

```bash
# Linux / macOS
python3 -m pytest

# Windows
py -m pytest
```

Тесты расположены в `test_recipes.py`.

## Автор

Просекин Илья ТАДБ251
