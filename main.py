games = []
def add_game( title, platform, status):
    title = title.strip()
    platform = platform.strip()
    status = status.strip()

    if not title:
        return False
    
    games.append({"title": title, "platform": platform, "status": status})
    return True

add_game("Witcher 3", "PC", "Playing")
add_game("", "PC", "Finished")
print(games)