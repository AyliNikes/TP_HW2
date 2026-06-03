# Ваш код здесь
class Ingredient:
    def __init__(self,name,quantity,unit):
        self.name=name
        self.quantity=quantity
        self.unit=unit
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self,value):
        if value <=0:
            raise ValueError('Количество должно быть положительным')
        self._quantity=float(value)
    
    def __str__(self):
        return f'{self.name}: {self.quantity} {self.unit}'
    
    def __repr__(self):
        return f'Ingredient({self.name}, {self.quantity}, {self.unit})'
    
    def __eq__(self,other):
        return self.name==other.name and self.unit==other.unit
    
# Ваш код здесь
class Recipe:
    def __init__(self, title, ingredients: list):
        self.title=title
        self.ingredients=ingredients

    def add_ingredients(self,ingredient: Ingredient):
        flag=0
        for x in self.ingredients:
            if x.name==ingredient.name and x.unit==ingredient.unit:
                x.quantity+=ingredient.quantity
                flag=1
                break
        if flag==0:
            self.ingredients.append(ingredient)
    
    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio,(int,float)) and ratio>0
    
    def scale(self, ratio: float):
        new_ingredients = [Ingredient(x.name, x.quantity*ratio, x.unit) for x in self.ingredients]
        return Recipe(self.title, new_ingredients)
    
    def __len__(self):
        return len(set([x.name for x in self.ingredients]))
    
    def __str__(self):
        return f'Блюдо: {self.title}\nНеобходимые ингредиенты:\n' + '\n'.join(f'\t{x}' for x in self.ingredients)
    


class ShoppingList:
    def __init__(self,items):
        self._items=items
    
    def add_recipe(self,recipe: Recipe, portions: float):
        if portions<=0:
            raise ValueError('Количество порций должно быть положительным')
        scaled = recipe.scale(portions)
        for x in scaled.ingredients:
            self._items.append((x, recipe.title))

    def remove_recipe(self, title: str):
        self._items = [x for x in self._items if x[1] != title]
    
    def get_list(self):
        _dict=dict()
        for x in self._items:
            name,unit=x[0].name,x[0].unit
            cor=(name,unit)
            if cor in _dict:
                _dict[cor]+=x[0].quantity
            else:
                _dict[cor]=x[0].quantity
        sp=[]
        for i, quantity in _dict.items():
            name,unit=i
            sp.append(Ingredient(name,quantity,unit))
        sp.sort(key=lambda x: x.name)        
        return sp
    
    def __add__(self, other):
        new=ShoppingList([])
        new._items = self._items + other._items
        return new
    
# Ваш код здесь
class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        if ingredients is None:
            ingredients = []
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        new_recipe = super().scale(ratio)
        return DietaryRecipe(self.title, self.diet_type, new_recipe.ingredients)
    
    def __str__(self):
        return f'[{self.diet_type}] {super().__str__()}'