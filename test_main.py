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

def test_add_blank_title_rejected():
    ok, message = main.add_game("", "PC", "playing")
    assert ok is False
    assert main.games == []


def test_add_spaces_only_title_rejected():
    ok, message = main.add_game("   ", "PC", "playing")
    assert ok is False
    assert main.games == []


def test_add_blank_platform_rejected():
    ok, message = main.add_game("Hades", "", "playing")
    assert ok is False
    assert main.games == []


def test_add_invalid_status_rejected():
    ok, message = main.add_game("Hades", "PC", "banana")
    assert ok is False
    assert main.games == []


def test_add_duplicate_rejected_ignoring_capitals():
    main.add_game("Hades", "PC", "playing")
    ok, message = main.add_game("hades", "Switch", "finished")
    assert ok is False
    assert len(main.games) == 1


def test_remove_missing_game():
    assert main.remove_game("Nope") is False


def test_remove_needs_exact_title():
    main.add_game("Hades", "PC", "playing")
    assert main.remove_game("Had") is False
    assert len(main.games) == 1


def test_update_missing_game():
    ok, message = main.update_status("Nope", "finished")
    assert ok is False


def test_update_invalid_status_changes_nothing():
    main.add_game("Hades", "PC", "playing")
    ok, message = main.update_status("Hades", "banana")
    assert ok is False
    assert main.games[0]["status"] == "playing"


def test_search_no_match_returns_empty_list():
    main.add_game("Hades", "PC", "playing")
    assert main.search_games("zelda") == []

def test_blank_search_returns_nothing():
    main.add_game("Hades", "PC", "playing")
    assert main.search_games("") == []
    assert main.search_games("   ") == []

def test_load_missing_file_returns_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "FILENAME", str(tmp_path / "nope.json"))
    assert main.load_games() == []


def test_load_broken_json_returns_empty(tmp_path, monkeypatch):
    bad = tmp_path / "games.json"
    bad.write_text("[{broken")
    monkeypatch.setattr(main, "FILENAME", str(bad))
    assert main.load_games() == []


def test_save_then_load_round_trip(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "FILENAME", str(tmp_path / "games.json"))
    main.add_game("Hades", "PC", "playing")
    main.save_games()
    assert main.load_games() == main.games