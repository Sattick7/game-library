import pytest
import main


@pytest.fixture(autouse=True)
def clean_library():
    main.games.clear()
    yield
    main.games.clear()


def test_add_game_success():
    ok, message = main.add_game("Hades", "PC", "playing")
    assert ok is True
    assert len(main.games) == 1
    assert main.games[0]["title"] == "Hades"


def test_add_game_cleans_input():
    main.add_game("  Hades  ", " PC ", " PLAYING ")
    game = main.games[0]
    assert game["title"] == "Hades"
    assert game["platform"] == "PC"
    assert game["status"] == "playing"


def test_search_finds_partial_match():
    main.add_game("Hades", "PC", "playing")
    main.add_game("Hollow Knight", "PC", "finished")
    main.add_game("Celeste", "Switch", "finished")
    results = main.search_games("h")
    assert len(results) == 2


def test_search_ignores_capitals():
    main.add_game("Hades", "PC", "playing")
    assert len(main.search_games("HADES")) == 1


def test_remove_game_success():
    main.add_game("Hades", "PC", "playing")
    assert main.remove_game("hades") is True
    assert main.games == []


def test_update_status_success():
    main.add_game("Hades", "PC", "playing")
    ok, message = main.update_status("Hades", "finished")
    assert ok is True
    assert main.games[0]["status"] == "finished"