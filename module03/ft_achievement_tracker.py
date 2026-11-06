import random

ACHIEVEMENTS = [
    'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme', 
    'Untouchable', 'Boss Slayer', 'Strategist', 'Speed Runner', 'Survivor', 
    'Treasure Hunter', 'First Steps', 'Hidden Path Finder', 'Unstoppable', 'Sharp Mind'
]

def gen_player_achievements() -> set[str]:
    num_achievements = random.randint(3, 8)
    return set(random.sample(ACHIEVEMENTS, num_achievements))

def main() -> None:
    print("=== Achievement Tracker System ===")
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }
    
    all_achievements = set()
    common_achievements = None
    
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
        all_achievements = all_achievements.union(achievements)
        if common_achievements is None:
            common_achievements = set(achievements)
        else:
            common_achievements = common_achievements.intersection(achievements)
            
    print(f"\nAll distinct achievements: {all_achievements}")
    print(f"Common achievements: {common_achievements}")
    
    for name, achievements in players.items():
        other_achievements = set()
        for other_name, other_achievs in players.items():
            if name != other_name:
                other_achievements = other_achievements.union(other_achievs)
        only_player = achievements.difference(other_achievements)
        print(f"Only {name} has: {only_player}")
        
    for name, achievements in players.items():
        missing = set(ACHIEVEMENTS).difference(achievements)
        print(f"{name} is missing: {missing}")

if __name__ == "__main__":
    main()