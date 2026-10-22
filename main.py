import json
games = []

FILENAME = "games.json"

def save_games():
    with open(FILENAME, "w") as f:
        json.dump(games, f, indent=2)

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

def remove_game(title):
    title = title.strip().lower()
    for g in games:
        if g["title"].lower() == title:
            games.remove(g)
            return True
    return False

def show_results(results):
    if not results:
        print("No matches.")
        return
    for g in results:
        print(f"- {g['title']} ({g['platform']}) - {g['status']}")

def prompt_add_game():
    title = input("Title: ")
    platform = input("Platform: ")
    status = input("Status: ")
    if add_game(title, platform, status):
        print("Game added.")
        save_games()
    else:
        print("Title can't be blank.")

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


def main():
    while True:
        print("\n1) Add game  2) List games  3) Search  4) Remove Game 5) Quit")
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
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

main()

