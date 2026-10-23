import json
games = []

FILENAME = "games.json"
VALID_STATUSES = ["playing", "finished", "wishlist", "abandoned"]

def save_games():
    with open(FILENAME, "w") as f:
        json.dump(games, f, indent=2)


def load_games():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: games.json is damaged. Starting with an empty library.")
        return []
    if not isinstance(data, list):
        print("Warning: games.json has the wrong format. Starting empty.")
        return []
    return data

def add_game(title, platform, status):
    title = title.strip()
    platform = platform.strip()
    status = status.strip().lower()

    if not title:
        return False, "Title can't be blank."
    if not platform:
        return False, "Platform can't be blank."
    if status not in VALID_STATUSES:
        return False, "Status must be one of: " + ", ".join(VALID_STATUSES)
    for g in games:
        if g["title"].lower() == title.lower():
            return False, "That game is already in your library."

    games.append({"title": title, "platform": platform, "status": status})
    return True, "Game added."

def list_games():
    if not games:
        print("No Games yet. ")
        return
    for i, g in enumerate(games, 1):
        print(f"{i}. {g['title']} ({g['platform']}) - {g['status']}")

def search_games(term):
    term = term.strip().lower()
    if not term:
        return []
    return[g for g in games if term in g["title"].lower()]

def remove_game(title):
    title = title.strip().lower()
    for g in games:
        if g["title"].lower() == title:
            games.remove(g)
            return True
    return False

def update_status(title, new_status):
    title = title.strip().lower()
    new_status = new_status.strip().lower()

    if new_status not in VALID_STATUSES:
        return False, "Status must be one of: " + ", ".join(VALID_STATUSES)
    for g in games:
        if g["title"].lower() == title:
            g["status"] = new_status
            return True, "Status updated."
    return False, "Game not found."

def show_results(results):
    if not results:
        print("No matches.")
        return
    for g in results:
        print(f"- {g['title']} ({g['platform']}) - {g['status']}")

def prompt_add_game():
    title = input("Title: ")
    platform = input("Platform: ")
    status = input(f"Status ({', '.join(VALID_STATUSES)}): ")
    ok, message = add_game(title, platform, status)
    print(message)
    if ok:
        save_games()

def prompt_search():
    term = input("Search for: ")
    show_results(search_games(term))


def prompt_remove_game():
    title = input("Title to remove: ")
    if remove_game(title):
        print("Game removed.")
        save_games()
    else:
        print("Game not found.")

def prompt_update_status():
    title = input("Title of game to update: ")
    status = input(f"New status ({', '.join(VALID_STATUSES)}): ")
    ok, message = update_status(title, status)
    print(message)
    if ok:
        save_games()


def main():
    games.extend(load_games())
    while True:
        print("\n1) Add game  2) List games  3) Search  4) Remove Game 5) Update 6) Quit")
        choice = input("> ").strip()

        if choice == "1":
            prompt_add_game()
        elif choice == "2":
            list_games()
        elif choice == "3":
            prompt_search()
        elif choice == "4":
            prompt_remove_game()
        elif choice == "5":
            prompt_update_status()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

