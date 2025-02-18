import json

def load_data(filename):
    with open(f'static/data/{filename}', 'r', encoding='utf-8') as f:
        data = json.load(f)  
    return data


def load_template(temp):
    with open(f'static/templates/{temp}', 'r') as f:
        return (f.read())


def add_note(new_note):
    notes_file = "static/data/notes.json"
    
    try:
        with open(notes_file, "r", encoding="utf-8") as file:
            notes = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        notes = []
    
    notes.append(new_note)
    
    with open(notes_file, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)