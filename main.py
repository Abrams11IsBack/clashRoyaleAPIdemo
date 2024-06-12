import requests
import json

print("Function 1: Chest tracker")
print("Function 2: Battle log (JSON)")
print("Function 3: Player info")
wybor = input("Selection: (1 - 3): ")
print(wybor)

if wybor == '1':
    headers = {
        'Authorization': 'Bearer YOUR_KEY',
    }

    response = requests.get('https://api.clashroyale.com/v1/players/%23PLAYER_ID/upcomingchests', headers=headers)

    print(response.content)

    data = response.content

    parsed_data = json.loads(data)

    for item in parsed_data['items']:
        print(f"Chest in: {item['index'] + 1} games.")
        print(f"Chest name: {item['name']}")
        print("="*25)
elif wybor == '2':
    headers = {
        'Authorization': 'Bearer YOUR_KEY',
    }

    response = requests.get('https://api.clashroyale.com/v1/players/%23PLAYER_ID/battlelog', headers=headers)

    print(response.content)
elif wybor == '3':
    headers = {
        'Authorization': 'Bearer YOUR_KEY',
    }

    response = requests.get('https://api.clashroyale.com/v1/players/%23PLAYER_ID', headers=headers)

    print(response.content)

    data = response.content

    parsed_data = json.loads(data.decode('utf-8'))

    def display_user_data(data):
        print(f"Tag: {data['tag']}")
        print(f"Name: {data['name']}")
        print(f"Experience Level: {data['expLevel']}")
        print(f"Trophies: {data['trophies']}")
        print(f"Best Trophies: {data['bestTrophies']}")
        print(f"Wins: {data['wins']}")
        print(f"Losses: {data['losses']}")
        print(f"Battle Count: {data['battleCount']}")
        print(f"Three Crown Wins: {data['threeCrownWins']}")
        print(f"Challenge Cards Won: {data['challengeCardsWon']}")
        print(f"Challenge Max Wins: {data['challengeMaxWins']}")
        print(f"Tournament Cards Won: {data['tournamentCardsWon']}")
        print(f"Tournament Battle Count: {data['tournamentBattleCount']}")
        print(f"Role: {data['role']}")
        print(f"Donations: {data['donations']}")
        print(f"Donations Received: {data['donationsReceived']}")
        print(f"Total Donations: {data['totalDonations']}")
        print(f"War Day Wins: {data['warDayWins']}")
        print(f"Clan Cards Collected: {data['clanCardsCollected']}")
        print(f"Clan Tag: {data['clan']['tag']}")
        print(f"Clan Name: {data['clan']['name']}")
        print(f"Clan Badge ID: {data['clan']['badgeId']}")
        print(f"Arena ID: {data['arena']['id']}")
        print(f"Arena Name: {data['arena']['name']}")
        print("League Statistics:")
        print(f"  Current Season Trophies: {data['leagueStatistics']['currentSeason']['trophies']}")
        print(f"  Previous Season Trophies: {data['leagueStatistics']['previousSeason']['trophies']}")
        print(f"  Best Season Trophies: {data['leagueStatistics']['bestSeason']['trophies']}")

    display_user_data(parsed_data)
else:
    print("Error")
