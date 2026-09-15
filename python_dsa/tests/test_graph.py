from python_dsa.graph import Graph


def test_bfs(capsys):
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    g.bfs(1)
    captured = capsys.readouterr()
    assert captured.out.strip() == "1 2 3 4"


def test_dfs(capsys):
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    g.dfs(1)
    captured = capsys.readouterr()
    assert captured.out.strip() == "1 2 3"
