games = []
def add_game( title, platform, status):
    title = title.strip()
    platform = platform.strip()
    status = status.strip()

    if not title:
        return False
    
    games.append({"title": title, "platform": platform, "status": status})
    return True

def list_games():
    if not games:
        print("No Games yet. ")
        return
    for i, g in enumerate(games, 1):
        print(f"{i}. {g['title']} ({g['platform']}) - {g['status']}")

def search_games(term):
    term = term.strip().lower()
    return[g for g in games if term in g["title"].lower()]

def show_results(results):
    if not results:
        print("No matches.")
        return
    for g in results:
        print(f"- {g['title']} ({g['platform']}) - {g['status']}")


add_game("Witcher 3", "PC", "Playing")
add_game("GTA V", "PC", "Finished")
add_game("Hollow Knight", "PC", "Abandoned")
show_results(search_games("GTA"))

