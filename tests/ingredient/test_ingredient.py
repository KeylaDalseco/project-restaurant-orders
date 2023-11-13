from src.models.ingredient import (
    Ingredient,
    Restriction
)  # noqa: F401, E261, E501


# Req 1.
def test_ingredient():
    manteiga = Ingredient('manteiga')
    manteiga2 = Ingredient('manteiga')
    bacon = Ingredient('bacon')
    farinha = Ingredient('farinha')
    restriction1 = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    restriction2 = {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}

    assert hash(manteiga) == hash(manteiga2)
    assert hash(bacon) != hash(manteiga)
    assert manteiga == manteiga2
    assert manteiga != bacon
    assert bacon != farinha
    assert bacon.name == 'bacon'
    assert hash(bacon) != hash(farinha)
    assert repr(bacon) == "Ingredient('bacon')"
    assert repr(manteiga) == "Ingredient('manteiga')"
    assert manteiga.restrictions == restriction1
    assert bacon.restrictions == restriction2
    assert farinha.restrictions == {Restriction.GLUTEN}
