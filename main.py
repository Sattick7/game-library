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


add_game("Witcher 3", "PC", "Playing")
print("____Your Games____")
list_games()
print(f"Total:{len(games)}")