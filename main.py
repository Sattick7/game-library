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

def prompt_add_game():
    title = input("Title: ")
    platform = input("Platform: ")
    status = input("Status: ")
    if add_game(title, platform, status):
        print("Game added.")
    else:
        print("Title can't be blank.")

def prompt_search():
    term = input("Search for: ")
    show_results(search_games(term))


def main():
    while True:
        print("\n1) Add game  2) List games  3) Search  4) Quit")
        choice = input("> ").strip()

        if choice == "1":
            prompt_add_game()
        elif choice == "2":
            list_games()
        elif choice == "3":
            prompt_search()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

main()

