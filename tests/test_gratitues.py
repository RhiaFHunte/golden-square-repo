from lib.gratitues import Gratitudes

def test_initial_state_is_empty():
    g = Gratitudes()
    assert g.gratitudes == []
    assert g.format() == "Be grateful for: "

def test_add_single_gratitude():
    g = Gratitudes()
    g.add("family")
    assert g.gratitudes == ["family"]
    assert g.format() == "Be grateful for: family"

def test_add_multiple_gratitudes():
    g = Gratitudes()
    g.add("family")
    g.add("friends")
    g.add("health")
    assert g.gratitudes == ["family", "friends", "health"]
    assert g.format() == "Be grateful for: family, friends, health"