import json
from pathlib import Path


# საწყისი მონაცემები
chess_players = [
    {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
    {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
    {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
    {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
    {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
    {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
    {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
    {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
    {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]


# 1.სრული გზის დაბრუნება context manager-ით
def get_full_path(filename):
    with open(filename, "a", encoding="utf-8") as file:
        return str(Path(file.name).resolve())


#საწყისი სიის ფაილში შენახვა
def save_players(filename, players):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(players, file, ensure_ascii=False, indent=4)


# 2.ფაილის კონტენტის წაკითხვა
def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


# 3.ერთი ლექსიკონის დამატება ფაილში
def add_player(filename, player):
    players = read_file(filename)

    if not isinstance(player, dict):
        raise TypeError("მონაცემი უნდა იყოს ლექსიკონი (dict).")

    players.append(player)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(players, file, ensure_ascii=False, indent=4)


# 4.მოთამაშის განახლება id-ის მიხედვით
def update_player(filename, player_id, new_data):
    players = read_file(filename)

    for player in players:
        if player["id"] == player_id:
            player.update(new_data)

            with open(filename, "w", encoding="utf-8") as file:
                json.dump(players, file, ensure_ascii=False, indent=4)

            return True

    return False


#პროგრამის გაშვება
filename = "chess_players.json"

#საწყისი მონაცემების ჩაწერა JSON ფაილში
save_players(filename, chess_players)

#სრული გზა
print("ფაილის სრული გზა:")
print(get_full_path(filename))

#ორი ახალი მოთამაშე — თითოეული ემატება როგორც ცალკე dict
add_player(filename, {
    "id": 568,
    "name": "Kasparov",
    "country": "Russia",
    "rating": 2705,
    "age": 56
})

add_player(filename, {
    "id": 189,
    "name": "Karpov",
    "country": "Russia",
    "rating": 2698,
    "age": 59
})

#Jobava-ს რეიტინგის განახლება
update_player(filename, 19, {
    "rating": 2600
})

#საბოლოო კონტენტის დაბეჭდვა
print("\nფაილის საბოლოო კონტენტი:")
print(read_file(filename))