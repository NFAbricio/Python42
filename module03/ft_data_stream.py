import random
import typing

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use", "release"]

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))

def consume_event(event_list: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        event = random.choice(event_list)
        event_list.remove(event)
        yield event

def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")
        
    ten_events = [next(stream) for _ in range(10)]
    print(f"\nBuilt list of 10 events: {ten_events}")
    
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")

if __name__ == "__main__":
    main()