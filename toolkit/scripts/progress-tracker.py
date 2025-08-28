#!/usr/bin/env python3
"""
CTF Progress Tracker
A simple script to track and visualize CTF learning progress
"""

import json
import os
from datetime import datetime
from pathlib import Path
import argparse

class CTFTracker:
    def __init__(self, data_file="toolkit/data/progress.json"):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """Load existing progress data or create new structure"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        else:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            return {
                "challenges": [],
                "stats": {
                    "total_solved": 0,
                    "categories": {
                        "web": 0,
                        "crypto": 0,
                        "forensics": 0,
                        "pwn": 0,
                        "rev": 0,
                        "misc": 0
                    },
                    "difficulties": {
                        "easy": 0,
                        "medium": 0,
                        "hard": 0
                    }
                },
                "sessions": []
            }

    def save_data(self):
        """Save progress data to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def add_challenge(self, name, category, difficulty, points, platform, date_solved=None):
        """Add a solved challenge to the tracker"""
        if date_solved is None:
            date_solved = datetime.now().strftime("%Y-%m-%d")
        
        challenge = {
            "name": name,
            "category": category.lower(),
            "difficulty": difficulty.lower(),
            "points": int(points),
            "platform": platform,
            "date_solved": date_solved,
            "timestamp": datetime.now().isoformat()
        }
        
        self.data["challenges"].append(challenge)
        self.update_stats()
        self.save_data()
        print(f"✅ Added challenge: {name} ({category}, {difficulty})")

    def update_stats(self):
        """Update statistics based on solved challenges"""
        self.data["stats"]["total_solved"] = len(self.data["challenges"])
        
        # Reset counters
        for cat in self.data["stats"]["categories"]:
            self.data["stats"]["categories"][cat] = 0
        for diff in self.data["stats"]["difficulties"]:
            self.data["stats"]["difficulties"][diff] = 0
        
        # Count challenges
        for challenge in self.data["challenges"]:
            cat = challenge["category"]
            diff = challenge["difficulty"]
            if cat in self.data["stats"]["categories"]:
                self.data["stats"]["categories"][cat] += 1
            if diff in self.data["stats"]["difficulties"]:
                self.data["stats"]["difficulties"][diff] += 1

    def start_session(self, focus_area="general"):
        """Start a new learning session"""
        session = {
            "start_time": datetime.now().isoformat(),
            "focus_area": focus_area,
            "challenges_attempted": [],
            "notes": ""
        }
        
        self.data["sessions"].append(session)
        self.save_data()
        print(f"🚀 Started new session focusing on: {focus_area}")
        return len(self.data["sessions"]) - 1

    def end_session(self, session_id, notes=""):
        """End a learning session"""
        if session_id < len(self.data["sessions"]):
            self.data["sessions"][session_id]["end_time"] = datetime.now().isoformat()
            self.data["sessions"][session_id]["notes"] = notes
            self.save_data()
            print("⏹️ Session ended and saved")
        else:
            print("❌ Invalid session ID")

    def show_progress(self):
        """Display current progress statistics"""
        stats = self.data["stats"]
        
        print("\n📊 CTF Learning Progress")
        print("=" * 40)
        print(f"Total Challenges Solved: {stats['total_solved']}")
        
        print("\n📂 By Category:")
        for category, count in stats["categories"].items():
            if count > 0:
                print(f"  {category.capitalize()}: {count}")
        
        print("\n🎯 By Difficulty:")
        for difficulty, count in stats["difficulties"].items():
            if count > 0:
                print(f"  {difficulty.capitalize()}: {count}")
        
        print(f"\n📚 Total Learning Sessions: {len(self.data['sessions'])}")
        
        if self.data["challenges"]:
            recent = sorted(self.data["challenges"], key=lambda x: x["timestamp"])[-5:]
            print("\n🏆 Recent Challenges:")
            for challenge in recent:
                print(f"  • {challenge['name']} ({challenge['category']}, {challenge['date_solved']})")

    def list_challenges(self, category=None, difficulty=None):
        """List challenges with optional filtering"""
        challenges = self.data["challenges"]
        
        if category:
            challenges = [c for c in challenges if c["category"] == category.lower()]
        if difficulty:
            challenges = [c for c in challenges if c["difficulty"] == difficulty.lower()]
        
        if not challenges:
            print("No challenges found matching criteria")
            return
        
        print(f"\n📋 Challenges ({len(challenges)} found):")
        print("-" * 60)
        for challenge in sorted(challenges, key=lambda x: x["date_solved"], reverse=True):
            print(f"• {challenge['name']}")
            print(f"  Category: {challenge['category']} | Difficulty: {challenge['difficulty']} | Points: {challenge['points']}")
            print(f"  Platform: {challenge['platform']} | Solved: {challenge['date_solved']}")
            print()

def main():
    parser = argparse.ArgumentParser(description="CTF Progress Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add challenge command
    add_parser = subparsers.add_parser("add", help="Add a solved challenge")
    add_parser.add_argument("name", help="Challenge name")
    add_parser.add_argument("category", help="Challenge category")
    add_parser.add_argument("difficulty", help="Challenge difficulty")
    add_parser.add_argument("points", help="Points value")
    add_parser.add_argument("platform", help="CTF platform")
    add_parser.add_argument("--date", help="Date solved (YYYY-MM-DD)")
    
    # Progress command
    subparsers.add_parser("progress", help="Show progress statistics")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List challenges")
    list_parser.add_argument("--category", help="Filter by category")
    list_parser.add_argument("--difficulty", help="Filter by difficulty")
    
    # Session commands
    session_parser = subparsers.add_parser("session", help="Manage learning sessions")
    session_parser.add_argument("action", choices=["start", "end"], help="Session action")
    session_parser.add_argument("--focus", help="Focus area for session start")
    session_parser.add_argument("--id", type=int, help="Session ID for end")
    session_parser.add_argument("--notes", help="Notes for session end")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    tracker = CTFTracker()
    
    if args.command == "add":
        tracker.add_challenge(args.name, args.category, args.difficulty, 
                            args.points, args.platform, args.date)
    
    elif args.command == "progress":
        tracker.show_progress()
    
    elif args.command == "list":
        tracker.list_challenges(args.category, args.difficulty)
    
    elif args.command == "session":
        if args.action == "start":
            focus = args.focus or "general"
            tracker.start_session(focus)
        elif args.action == "end":
            if args.id is not None:
                notes = args.notes or ""
                tracker.end_session(args.id, notes)
            else:
                print("❌ Session ID required for end action")

if __name__ == "__main__":
    main()