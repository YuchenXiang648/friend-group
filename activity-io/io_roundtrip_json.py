from pathlib import Path
import json

group = {
    "members": [
        {"id": "alice", "age": 21, "hobbies": ["climbing", "reading"]},
        {"id": "bob",   "age": 22, "hobbies": ["music"]},
        {"id": "chris", "age": 20, "hobbies": []},
    ],
    "friendships": [["alice","bob"], ["bob","chris"]],
    "meta": {"created_by": "xiang-yin", "version": 1}
}

def save_json(obj, path):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

def load_json(path):
    with Path(path).open("r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    out = "activity-io/group.json"
    save_json(group, out)
    loaded = load_json(out)
    assert loaded == group, "Round-trip mismatch!"
    print("JSON round-trip OK")
