from mylib.wiki import search_wiki

def test_search_wiki():
    assert "History of the Los Angeles Lakers" in search_wiki()