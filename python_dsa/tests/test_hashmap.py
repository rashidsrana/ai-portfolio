from python_dsa.hashmap import HashMap


def test_put_get():
    hm = HashMap()
    hm.put("name", "Rashid")
    assert hm.get("name") == "Rashid"


def test_remove():
    hm = HashMap()
    hm.put("age", 35)
    hm.remove("age")
    assert hm.get("age") is None
