"""
organize.py - Helper script to manage algorithm-training repository
Usage: python scripts/organize.py
"""

import os
from pathlib import Path

class ProblemOrganizer:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent
        self.problems = []
        
    def add_problem(self, number, title, difficulty, topics, category="arrays"):
        """Add a problem to the tracking list"""
        problem = {
            "number": number,
            "title": title,
            "difficulty": difficulty,
            "topics": topics,
            "category": category,
            "file_name": self.generate_filename(number, title, difficulty)
        }
        self.problems.append(problem)
        return problem
    
    def generate_filename(self, number, title, difficulty):
        """Generate standardized filename"""
        folder = difficulty.lower()
        clean_title = title.lower().replace(" ", "-").replace("'", "")
        return f"{folder}/{number:03d}-{clean_title}"
    
    def generate_table_row(self, problem):
        """Generate markdown table row for README"""
        emoji_map = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
        emoji = emoji_map.get(problem["difficulty"], "⚪")
        
        return (
            f"| {problem['number']} | "
            f"[{problem['title']}](./{problem['file_name']}.md) | "
            f"{emoji} {problem['difficulty']} | "
            f"[Python](./{problem['file_name']}.py) | "
            f"{', '.join(problem['topics'])} |"
        )
    
    def organize_by_category(self):
        """Organize problems into categories"""
        categories = {}
        for problem in self.problems:
            cat = problem["category"]
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(problem)
        return categories
    
    def count_by_difficulty(self):
        """Count problems by difficulty"""
        counts = {"Easy": 0, "Medium": 0, "Hard": 0}
        for problem in self.problems:
            counts[problem["difficulty"]] += 1
        return counts
    
    def print_readme_section(self, category_name, problems):
        """Print formatted README section"""
        print(f"\n### {category_name}")
        print("| # | Title | Difficulty | Solution | Topics |")
        print("|---|-------|-----------|----------|--------|")
        for problem in sorted(problems, key=lambda x: x["number"]):
            print(self.generate_table_row(problem))
    
    def generate_full_readme(self):
        """Generate complete README content"""
        categories = self.organize_by_category()
        counts = self.count_by_difficulty()
        
        print("=== COPY THIS INTO YOUR README.md ===\n")
        
        # Stats table
        print("## 📊 Progress\n")
        print("| Difficulty | Solved |")
        print("|-----------|--------|")
        print(f"| Easy      | {counts['Easy']}     |")
        print(f"| Medium    | {counts['Medium']}     |")
        print(f"| Hard      | {counts['Hard']}     |")
        print(f"| **Total** | **{sum(counts.values())}** |\n")
        
        # Problem tables by category
        print("## 📚 Problems\n")
        
        category_names = {
            "arrays": "Arrays & Hashing",
            "two-pointers": "Two Pointers",
            "sliding-window": "Sliding Window",
            "stack": "Stack & Queue",
            "trees": "Binary Trees",
            "graphs": "Graphs",
            "dynamic-programming": "Dynamic Programming",
            "backtracking": "Backtracking",
            "binary-search": "Binary Search",
            "linked-lists": "Linked Lists",
            "heap": "Heap / Priority Queue",
            "strings": "Strings",
            "math": "Math & Geometry"
        }
        
        for category, problems in sorted(categories.items()):
            display_name = category_names.get(category, category.title())
            self.print_readme_section(display_name, problems)


# ============================================
# ADD YOUR PROBLEMS HERE
# ============================================

def main():
    org = ProblemOrganizer()
    
    # Example problems - ADD YOUR SOLVED PROBLEMS HERE
    org.add_problem(1, "Two Sum", "Easy", ["Array", "Hash Table"], "arrays")
    org.add_problem(20, "Valid Parentheses", "Easy", ["String", "Stack"], "stack")
    org.add_problem(54, "Spiral Matrix", "Medium", ["Array", "Matrix"], "arrays")
    org.add_problem(125, "Valid Palindrome", "Easy", ["Two Pointers", "String"], "two-pointers")
    org.add_problem(128, "Longest Consecutive Sequence", "Medium", ["Array", "Hash Table"], "arrays")
    org.add_problem(167, "Two Sum II", "Medium", ["Array", "Two Pointers"], "two-pointers")
    org.add_problem(200, "Number of Islands", "Medium", ["Array", "BFS", "DFS"], "graphs")
    
    # ADD MORE PROBLEMS HERE:
    # org.add_problem(number, "Problem Name", "Difficulty", ["Topic1", "Topic2"], "category")
    
    # Generate README content
    org.generate_full_readme()
    
    print("\n\n=== INSTRUCTIONS ===")
    print("1. Copy the output above")
    print("2. Paste it into your README.md (replace the Progress and Problems sections)")
    print("3. Update badges at the top with your current counts")
    print(f"4. Total problems: {len(org.problems)}")


if __name__ == "__main__":
    main()