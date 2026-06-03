from classes import Ingredient, Recipe, ShoppingList, DietaryRecipe
# Ваш код здесь
import pytest

@pytest.mark.parametrize('name,quantity,unit',[('соль',20,'г'),('масло',100,'мл'),('мука',500,'г')])

def test_ingredient(name,quantity,unit):
    ing = Ingredient(name, quantity, unit)
    assert ing.name == name
    assert ing.quantity == quantity
    assert ing.unit == unit

@pytest.mark.parametrize('name,quantity,unit',[('соль',20,'г'),('масло',100,'мл'),('мука',500,'г')])
def test_str(name,quantity,unit):
    ing = Ingredient(name,quantity, unit)
    assert str(ing) == f'{ing.name}: {ing.quantity} {ing.unit}'

def test_eq():
    ing1=Ingredient('соль', 20, 'г')
    ing2=Ingredient('соль', 45, 'г')
    assert ing1==ing2

    ing1=Ingredient('соль', 20, 'г')
    ing2=Ingredient('сахар', 20, 'г')
    assert ing1!=ing2

    ing1=Ingredient('соль', 20, 'г')
    ing2=Ingredient('соль', 20, 'мл')
    assert ing1!=ing2

# Ваш код здесь
def test_recipe():
    recipe=Recipe('Цезарь', [Ingredient('капуста',100,'г'),Ingredient('помидоры',50,'г')])
    assert recipe.title =='Цезарь'
    assert recipe.ingredients==[Ingredient('капуста',100,'г'),Ingredient('помидоры',50,'г')]

def test_add_ingredient_new():
    recipe=Recipe('Цезарь', [Ingredient('капуста',100,'г'),Ingredient('помидоры',50,'г')])
    recipe.add_ingredients(Ingredient('курица',150,'г'))
    assert ('курица',150,'г') in [(ingredient.name,ingredient.quantity,ingredient.unit) for ingredient in recipe.ingredients]

def test_add_ingredient_old():
    recipe=Recipe('Цезарь', [Ingredient('капуста',100,'г'),Ingredient('помидоры',50,'г')])
    recipe.add_ingredients(Ingredient('помидоры',30,'г'))
    assert ('помидоры',80,'г') in [(ingredient.name,ingredient.quantity,ingredient.unit) for ingredient in recipe.ingredients]

def test_scale():
    recipe=Recipe('Цезарь', [Ingredient('капуста',100,'г'),Ingredient('помидоры',50,'г')])
    scaled=recipe.scale(3)

    assert scaled is not recipe

    assert scaled.ingredients[0].quantity == 300
    assert scaled.ingredients[1].quantity == 150

    assert recipe.ingredients[0].quantity == 100
    assert recipe.ingredients[1].quantity == 50

    with pytest.raises(ValueError):
        scaled=recipe.scale(-3)
    
# Ваш код здесь
def test_add_recipe():
    shopping_list=ShoppingList([(Ingredient('капуста',100,'г'), 'Цезарь'), (Ingredient('мука',500,'г'),'Блинчики')])
    shopping_list.add_recipe(Recipe('Жаркое',[Ingredient('говядина',200,'г'), Ingredient('морковь',100,'г')]),3)
    items = shopping_list.get_list()
    assert any(x.name=='говядина' for x in items)

    meat = [x for x in items if x.name=='говядина'][0]
    assert meat.quantity==600

    with pytest.raises(ValueError):
        shopping_list.add_recipe(Recipe('Жаркое',[Ingredient('говядина',200,'г'), Ingredient('морковь',100,'г')]),-3)

def test_remove_recipe():
    shopping_list = ShoppingList([(Ingredient('капуста',100,'г'), 'Цезарь'), (Ingredient('мука',500,'г'),'Блинчики')])
    shopping_list.remove_recipe('Цезарь')
    items = shopping_list.get_list()
    assert all(x.name!='капуста' for x in items)
    assert any(x.name=='мука' for x in items)

    shopping_list.remove_recipe('Роллы')
    items = shopping_list.get_list()
    assert any(x.name=='мука' for x in items)


def test_get_list():
    shopping_list = ShoppingList([(Ingredient('мука',500,'г'), 'Цезарь'), (Ingredient('мука',300,'г'),'Блинчики'), (Ingredient('капуста',100,'г'),'Цезарь')])
    items = shopping_list.get_list()

    flour=[x for x in items if x.name == 'мука'][0]
    assert flour.quantity==800
    assert len([x for x in items if x.name == 'мука'])==1

    names = [x.name for x in items]
    assert names==sorted(names)


def test_add():
    shopping_list = ShoppingList([(Ingredient('капуста',100,'г'), 'Цезарь')])
    other = ShoppingList([(Ingredient('мука',500,'г'), 'Блинчики')])

    len1 = len(shopping_list._items)
    len2 = len(other._items)

    combined=shopping_list+other
    names = [x.name for x in combined.get_list()]
    assert 'капуста' in names
    assert 'мука' in names

    assert len(shopping_list._items)==len1
    assert len(other._items)==len2
