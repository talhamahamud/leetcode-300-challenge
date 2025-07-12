import os
import re

# --- Configuration ---
FOLDERS = {
    "Easy": "Easy",
    "Medium": "Medium",
    "Hard": "Hard"
}
GOALS = {
    "Easy": 200,
    "Medium": 75,
    "Hard": 25
}
README_FILE = "README.md"

# Ensure script runs from its own directory
os.chdir(os.path.dirname(__file__))

def count_solutions(path):
    if not os.path.exists(path):
        return 0
    return len([
        f for f in os.listdir(path)
        if f.endswith(".py") or f.endswith(".cpp") or f.endswith(".js")
    ])

def calculate_completion(solved, goal):
    return round((solved / goal) * 100, 1) if goal else 0.0

def build_progress_table():
    total_solved = 0
    total_goal = 0
    lines = [
        "## 📊 Progress Tracker",
        "| Difficulty | Solved | Goal | Completion |",
        "|------------|--------|------|------------|"
    ]
    for level in FOLDERS:
        solved = count_solutions(FOLDERS[level])
        goal = GOALS[level]
        percent = calculate_completion(solved, goal)
        lines.append(f"| {level:<10} | {solved:<6} | {goal:<4} | {percent:.1f}%       |")
        total_solved += solved
        total_goal += goal

    total_percent = calculate_completion(total_solved, total_goal)
    lines.append(f"| **Total**  | {total_solved:<6} | {total_goal:<4} | {total_percent:.1f}%       |")
    return "\n".join(lines)

def update_readme():
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    new_table = build_progress_table()

    # Match everything from ## 📊 Progress Tracker to the next --- or ##
    pattern = r"## 📊 Progress Tracker\n(?:.*\n)*?\| \*\*Total\*\*.*?\|\n?(?:.*\n)*?(?=^---|\Z|^## )"
    replacement = new_table + "\n\n> 🧠 Target: Solve all 300 problems by [your target date here]\n> 🎯 Progress will be updated regularly as I solve new problems.\n\n---\n"

    updated_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("✅ README.md progress updated cleanly.")

    
    
if __name__ == "__main__":
    update_readme()
