from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    macarrao = Dish('macarrão', 18.00)
    lasanha = Dish('Lasanha', 12.00)
    lasanha2 = Dish('Lasanha', 12.00)
    salmao = Dish('Salmão', 90.00)
    farinha = Ingredient('farinha')
    ovo = Ingredient('ovo')

    assert macarrao.name == 'macarrão'
    assert macarrao.price == 18.00
    assert hash(lasanha) == hash(lasanha2)
    assert hash(lasanha) != hash(salmao)
    assert lasanha == lasanha2
    assert lasanha != macarrao
    assert repr(macarrao) == "Dish('macarrão', R$18.00)"
    with pytest.raises(TypeError):
        Dish(2, "15")
    with pytest.raises(ValueError):
        Dish(2, 0)
    lasanha.add_ingredient_dependency(farinha, 2)
    lasanha.add_ingredient_dependency(ovo, 4)
    ingredients = lasanha.get_ingredients()
    assert farinha in ingredients
    assert ovo in ingredients
    assert lasanha.recipe[farinha] == 2
    assert lasanha.recipe[ovo] == 4
    assert lasanha.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.GLUTEN,
    }
