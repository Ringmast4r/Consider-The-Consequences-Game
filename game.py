#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONSIDER THE CONSEQUENCES (1930)
Interactive Fiction Game - CMD Terminal Edition

Based on the 1930 choose-your-own-adventure book by Doris Webster and Mary Alden Hopkins
The first interactive fiction book in history (predating "Choose Your Own Adventure" by 49 years)
"""

import os
import sys
import time
import random
from story_data import STORY_DATA

# Set UTF-8 encoding for Windows console
if os.name == 'nt':
    os.system('chcp 65001 >nul 2>&1')  # Set console to UTF-8
    os.system('')  # Enable ANSI escape codes in Windows 10+

# ANSI Color Codes - Work natively in Windows 10+ CMD
class Color:
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'

# ASCII Art
ASCII_TITLE = r"""
 ██████╗ ██████╗ ███╗   ██╗███████╗██╗██████╗ ███████╗██████╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔══██╗██╔════╝██╔══██╗
██║     ██║   ██║██╔██╗ ██║███████╗██║██║  ██║█████╗  ██████╔╝
██║     ██║   ██║██║╚██╗██║╚════██║██║██║  ██║██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██║ ╚████║███████║██║██████╔╝███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

████████╗██╗  ██╗███████╗
╚══██╔══╝██║  ██║██╔════╝
   ██║   ███████║█████╗
   ██║   ██╔══██║██╔══╝
   ██║   ██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝

 ██████╗ ██████╗ ███╗   ██╗███████╗███████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗ ██████╗███████╗███████╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝██╔════╝██╔═══██╗██║   ██║██╔════╝████╗  ██║██╔════╝██╔════╝██╔════╝
██║     ██║   ██║██╔██╗ ██║███████╗█████╗  ██║   ██║██║   ██║█████╗  ██╔██╗ ██║██║     █████╗  ███████╗
██║     ██║   ██║██║╚██╗██║╚════██║██╔══╝  ██║▄▄ ██║██║   ██║██╔══╝  ██║╚██╗██║██║     ██╔══╝  ╚════██║
╚██████╗╚██████╔╝██║ ╚████║███████║███████╗╚██████╔╝╚██████╔╝███████╗██║ ╚████║╚██████╗███████╗███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝
"""

ASCII_BOOK = r"""
    ___________________
   /                  /|
  /   1930 EDITION  / |
 /                 /  |
/__________________/   |
|                  |   |
|   CONSIDER THE   |   |
|   CONSEQUENCES   |   /
|                  |  /
|__________________|_/
"""

ASCII_HELEN = r"""
    @@@@@@@
   @  o o  @
   @   <   @    HELEN
   @  \_/  @    The Romantic
    @@@@@@@
"""

ASCII_JED = r"""
    #######
   #  O O  #
   #   ^   #    JED
   #  \_/  #    The Heir
    #######
"""

ASCII_SAUNDERS = r"""
    $$$$$$$
   $  - -  $
   $   .   $    SAUNDERS
   $  \_/  $    The Dutiful Son
    $$$$$$$
"""

ASCII_HEART = "<3"
ASCII_DIAMOND = "<>"
ASCII_STAR = "*"
ASCII_BOOK_ICON = "[BOOK]"
ASCII_CHOICE = ">"

# Scene transition visuals
ASCII_TRANSITION = r"""
        *    .    *    .    *    .    *
    .    *    .    *    .    *    .    *
*    .    *    .    *    .    *    .
"""

ASCII_CHAPTER_DIVIDER = r"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                          ~ Chapter Transition ~                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

ASCII_THINKING = r"""
        . o O ( ? )
       /
      /
   [You]
"""

ASCII_LOVE = r"""
    ♥♥♥     ♥♥♥
  ♥♥   ♥♥ ♥♥   ♥♥
 ♥♥           ♥♥
  ♥♥         ♥♥
    ♥♥     ♥♥
      ♥♥ ♥♥
        ♥
"""

ASCII_DECISION = r"""
    ╔═══════════════╗
    ║  DECISION!    ║
    ╚═══════════════╝
         /   \
        /     \
       /       \
"""

ASCII_CONSEQUENCE = r"""
    ⚡ CONSEQUENCE ⚡

    The path chosen
    cannot be undone...
"""

ASCII_ENDING_HAPPY = r"""
    ✿ ✿ ✿ ✿ ✿ ✿ ✿

      A Happy Ending

    ✿ ✿ ✿ ✿ ✿ ✿ ✿
"""

ASCII_ENDING_SAD = r"""
    ╔═══════════════╗
    ║               ║
    ║  A Sad Fate   ║
    ║               ║
    ╚═══════════════╝
"""

ASCII_ENDING_BITTERSWEET = r"""
    ~ ~ ~ ~ ~ ~ ~ ~

     Bittersweet...

    ~ ~ ~ ~ ~ ~ ~ ~
"""

ASCII_LOCATION_NYC = r"""
    ║║║   NEW YORK CITY   ║║║
    ╔══ The Big City ══╗
"""

ASCII_LOCATION_FRANKLIN = r"""
    ═══ FRANKLIN ═══
    ~ Small Town Life ~
"""

ASCII_LOCATION_EUROPE = r"""
    ✈ EUROPEAN ADVENTURE ✈
    ~ Across the Ocean ~
"""

class ConsiderTheConsequencesGame:
    def __init__(self):
        self.current_segment = None
        self.character = None
        self.choices_made = []
        self.story_data = STORY_DATA

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_centered(self, text, width=80):
        """Print text centered"""
        lines = text.split('\n')
        for line in lines:
            print(line.center(width))

    def print_fancy_divider(self, char="═", length=80, color=Color.CYAN):
        """Print a fancy colored divider"""
        print(color + char * length + Color.RESET)

    def print_slow(self, text, delay=0.02, color=Color.WHITE):
        """Print text with a typewriter effect"""
        for char in text:
            sys.stdout.write(color + char + Color.RESET)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def show_transition_animation(self):
        """Display transition animation between scenes"""
        print()
        print(Color.CYAN + ASCII_TRANSITION + Color.RESET)
        time.sleep(0.8)

    def show_decision_prompt(self):
        """Display decision visual before choices"""
        print()
        print(Color.YELLOW + ASCII_DECISION + Color.RESET)
        time.sleep(0.5)

    def show_chapter_transition(self, segment_id):
        """Display chapter transition for major story milestones"""
        # Define major chapter breaks for each character
        chapter_breaks = {
            'H-1': 'Chapter 1: The Choice Between Two Men',
            'H-7': 'Chapter 2: New York Adventure',
            'H-13': 'Chapter 3: Career and Romance',
            'H-21': 'Chapter 4: Love and Ambition',
            'J-1': 'Chapter 1: Consequences of Passion',
            'J-4': 'Chapter 2: Managing the Estate',
            'J-6': 'Chapter 3: Marriage and Temptation',
            'J-14': 'Chapter 4: Choosing Between Duty and Love',
            'S-1': 'Chapter 1: Family Responsibility',
            'S-5': 'Chapter 2: Integrity and Opportunity',
            'S-12': 'Chapter 3: Love and Career',
            'S-20': 'Chapter 4: Second Chances'
        }

        if segment_id in chapter_breaks:
            self.clear_screen()
            print(Color.MAGENTA + Color.BOLD)
            for line in ASCII_CHAPTER_DIVIDER.split('\n'):
                print(line.center(80))
            print(Color.RESET)
            time.sleep(0.3)
            print()
            self.print_centered(Color.CYAN + Color.BOLD + chapter_breaks[segment_id])
            print()
            time.sleep(1.5)
            input(Color.WHITE + "\n  Press ENTER to continue..." + Color.RESET)
            self.clear_screen()

    def show_contextual_art(self, segment_id, text):
        """Display contextual ASCII art based on story content"""
        text_lower = text.lower()

        # Location-based visuals
        if 'new york' in text_lower and segment_id in ['H-7', 'H-13', 'H-21', 'J-3', 'J-5', 'S-11']:
            print()
            print(Color.CYAN)
            for line in ASCII_LOCATION_NYC.split('\n'):
                print(line.center(80))
            print(Color.RESET)
            time.sleep(0.4)

        # Europe/Paris scenes
        if any(word in text_lower for word in ['paris', 'europe', 'france', 'abroad']) and segment_id in ['J-4', 'J-5', 'J-11', 'J-13', 'S-11']:
            print()
            print(Color.MAGENTA)
            for line in ASCII_LOCATION_EUROPE.split('\n'):
                print(line.center(80))
            print(Color.RESET)
            time.sleep(0.4)

        # Romance/love scenes
        if any(word in text_lower for word in ['marry', 'marriage', 'honeymoon', 'wedding']):
            if segment_id in ['H-4', 'H-18', 'H-20', 'J-2', 'J-6', 'J-10', 'S-12', 'S-18', 'S-22', 'S-24']:
                print()
                print(Color.RED)
                for line in ASCII_LOVE.split('\n'):
                    print(line.center(80))
                print(Color.RESET)
                time.sleep(0.5)

    def display_title(self):
        """Display the game title screen with animations"""
        self.clear_screen()

        # Animated title
        print(Color.WHITE + Color.BOLD)
        for line in ASCII_TITLE.split('\n'):
            print(line.center(80))
            time.sleep(0.05)
        print(Color.RESET)

        time.sleep(0.5)

        # Subtitle with color
        print()
        self.print_centered(Color.YELLOW + Color.BOLD + "+" + "=" * 60 + "+")
        self.print_centered(Color.YELLOW + Color.BOLD + "|" + " " * 60 + "|")
        self.print_centered(Color.YELLOW + Color.BOLD + "|" + Color.WHITE + Color.BOLD + "        An Interactive Fiction Adventure Game        " + Color.YELLOW + Color.BOLD + "|")
        self.print_centered(Color.YELLOW + Color.BOLD + "|" + Color.WHITE + Color.BOLD + "           Based on the 1930 Classic Book            " + Color.YELLOW + Color.BOLD + "|")
        self.print_centered(Color.YELLOW + Color.BOLD + "|" + Color.MAGENTA + Color.BOLD + "      by Doris Webster & Mary Alden Hopkins         " + Color.YELLOW + Color.BOLD + "|")
        self.print_centered(Color.YELLOW + Color.BOLD + "|" + " " * 60 + "|")
        self.print_centered(Color.YELLOW + Color.BOLD + "|" + Color.GREEN + Color.BOLD + "    (The First Choose-Your-Own-Adventure Book!)     " + Color.YELLOW + Color.BOLD + "|")
        self.print_centered(Color.YELLOW + Color.BOLD + "|" + " " * 60 + "|")
        self.print_centered(Color.YELLOW + Color.BOLD + "+" + "=" * 60 + "+")
        print(Color.RESET)

        # Book ASCII art
        print(Color.CYAN)
        for line in ASCII_BOOK.split('\n'):
            print(line.center(80))
        print(Color.RESET)

    def select_character(self):
        """Let player choose which character to play with fancy display"""
        self.clear_screen()

        print()
        self.print_fancy_divider("═", 80, Color.MAGENTA)
        self.print_centered(Color.YELLOW + Color.BOLD + "★ ★ ★  SELECT YOUR CHARACTER  ★ ★ ★")
        self.print_fancy_divider("═", 80, Color.MAGENTA)
        print()

        # Display character options with ASCII art
        print(Color.RED + Color.BOLD + ASCII_HELEN + Color.RESET)
        print(Color.RED + "  [1] HELEN" + Color.WHITE + " - A young woman torn between passion and security")
        print(Color.WHITE + "      Will you follow your heart or choose the practical path?")
        print()

        print(Color.BLUE + Color.BOLD + ASCII_JED + Color.RESET)
        print(Color.BLUE + "  [2] JED" + Color.WHITE + " - A wealthy heir with charm and privilege")
        print(Color.WHITE + "      Your choices will reveal your true character...")
        print()

        print(Color.GREEN + Color.BOLD + ASCII_SAUNDERS + Color.RESET)
        print(Color.GREEN + "  [3] SAUNDERS" + Color.WHITE + " - The responsible eldest son")
        print(Color.WHITE + "      Duty calls, but what about your own dreams?")
        print()

        self.print_fancy_divider("─", 80, Color.MAGENTA)

        while True:
            choice = input(Color.YELLOW + "\n  " + ASCII_CHOICE + " Select character (1-3): " + Color.RESET).strip()
            if choice == "1":
                self.character = "Helen"
                self.current_segment = "H-START"
                char_color = Color.RED
                break
            elif choice == "2":
                self.character = "Jed"
                self.current_segment = "J-START"
                char_color = Color.BLUE
                break
            elif choice == "3":
                self.character = "Saunders"
                self.current_segment = "S-START"
                char_color = Color.GREEN
                break
            else:
                print(Color.RED + "  ✗ Invalid choice. Please enter 1, 2, or 3." + Color.RESET)

        # Confirmation animation
        print()
        confirmation_text = f"  {ASCII_STAR} You have chosen to play as {char_color}{Color.BOLD}{self.character.upper()}{Color.RESET} {ASCII_STAR}"
        print(confirmation_text)
        print()

        # Loading animation
        print(Color.CYAN + "  Loading your story", end='', flush=True)
        for _ in range(5):
            print(Color.CYAN + ".", end='', flush=True)
            time.sleep(0.3)
        print(Color.RESET)
        time.sleep(0.5)

    def display_segment(self, segment_id):
        """Display a story segment with fancy formatting"""
        if segment_id not in self.story_data:
            self.clear_screen()
            print(Color.RED + Color.BOLD + "\n  ⚠ ERROR: Segment not found! ⚠\n" + Color.RESET)
            print(Color.YELLOW + f"  Segment '{segment_id}' is not in the current story data.")
            print(Color.CYAN + "\n  NOTE: This is a demo version. Full game requires all 83 segments")
            print(Color.CYAN + "  See: Story_Structure_Analysis.md for complete story structure" + Color.RESET)
            input(Color.WHITE + "\n  Press ENTER to continue..." + Color.RESET)
            return False

        # Show chapter transition if this is a major milestone
        self.show_chapter_transition(segment_id)

        segment = self.story_data[segment_id]
        self.clear_screen()

        # Character-specific colors
        char_colors = {
            "Helen": Color.RED,
            "Jed": Color.BLUE,
            "Saunders": Color.GREEN
        }
        char_color = char_colors.get(segment['character'], Color.WHITE)

        # Header
        self.print_fancy_divider("═", 80, char_color)
        print(char_color + Color.BOLD + f"  CHARACTER: {segment['character'].upper()}" + Color.RESET, end='')

        if segment_id not in ["H-START", "J-START", "S-START"]:
            print(Color.CYAN + f"  │  SEGMENT: {segment_id}" + Color.RESET, end='')
            print(Color.YELLOW + f"  │  CHOICES MADE: {len(self.choices_made)}" + Color.RESET)

            # Progress bar visualization - scale based on typical path length (8-15 choices)
            max_expected_choices = 15
            progress_filled = min(int((len(self.choices_made) / max_expected_choices) * 20), 20)
            progress_bar = "█" * progress_filled + "░" * (20 - progress_filled)
            print(Color.DIM + f"  Progress: [{char_color}{progress_bar}{Color.DIM}] ({len(self.choices_made)} choices)" + Color.RESET)
        else:
            print()

        self.print_fancy_divider("═", 80, char_color)
        print()

        # Story text with typewriter effect for important parts
        story_lines = segment['text'].split('\n')
        for i, line in enumerate(story_lines):
            if i == 0 or line.strip().startswith('['):
                print(Color.WHITE + Color.BOLD + "  " + line + Color.RESET)
            else:
                print(Color.WHITE + "  " + line + Color.RESET)
            time.sleep(0.1)

        # Show contextual ASCII art based on story content
        self.show_contextual_art(segment_id, segment['text'])

        print()

        # Check if this is an ending
        if 'ending' in segment:
            self.print_fancy_divider("═", 80, Color.YELLOW)
            print()
            ending_text = f"  {ASCII_BOOK_ICON}  THE END  {ASCII_BOOK_ICON}"
            self.print_centered(Color.YELLOW + Color.BOLD + ending_text)
            print()
            self.print_fancy_divider("═", 80, Color.YELLOW)

            # Show ending type visual based on sentiment
            ending_lower = segment['ending'].lower()
            print()
            if any(word in ending_lower for word in ['happy', 'success', 'wonderful', 'delightful', 'harmonious', 'joyous']):
                print(Color.GREEN)
                for line in ASCII_ENDING_HAPPY.split('\n'):
                    print(line.center(80))
                print(Color.RESET)
            elif any(word in ending_lower for word in ['tragedy', 'died', 'death', 'failure', 'lost', 'broke', 'unhappy', 'miserable']):
                print(Color.RED)
                for line in ASCII_ENDING_SAD.split('\n'):
                    print(line.center(80))
                print(Color.RESET)
            else:
                print(Color.YELLOW)
                for line in ASCII_ENDING_BITTERSWEET.split('\n'):
                    print(line.center(80))
                print(Color.RESET)

            print()
            print(Color.CYAN + "  " + segment['ending'] + Color.RESET)
            print()
            self.print_fancy_divider("═", 80, Color.YELLOW)
            return False

        # Display choices with fancy formatting
        if 'choices' in segment and len(segment['choices']) > 0:
            self.print_fancy_divider("─", 80, char_color)

            # Show decision visual
            self.show_decision_prompt()

            print(Color.YELLOW + Color.BOLD + "  ⚡ What will you do? ⚡" + Color.RESET)
            print()

            for i, choice in enumerate(segment['choices'], 1):
                choice_symbol = f"{ASCII_CHOICE} "
                print(f"  {Color.CYAN}{choice_symbol}{Color.WHITE}[{i}] {choice['text']}" + Color.RESET)

            print()
            return True

        return False

    def get_player_choice(self, segment_id):
        """Get the player's choice with validation"""
        segment = self.story_data[segment_id]
        num_choices = len(segment['choices'])

        while True:
            try:
                choice = input(Color.YELLOW + f"  {ASCII_CHOICE} Enter your choice (1-{num_choices}): " + Color.RESET).strip()
                choice_num = int(choice)

                if 1 <= choice_num <= num_choices:
                    selected_choice = segment['choices'][choice_num - 1]
                    self.choices_made.append({
                        'segment': segment_id,
                        'choice': selected_choice['text']
                    })

                    # Choice confirmation animation
                    print()
                    print(Color.GREEN + f"  ✓ You chose: {selected_choice['text']}" + Color.RESET)
                    print(Color.DIM + "\n  " + ASCII_CONSEQUENCE.strip() + Color.RESET)
                    time.sleep(1.2)

                    # Show transition animation before next scene
                    self.show_transition_animation()

                    return selected_choice['goto']
                else:
                    print(Color.RED + f"  ✗ Please enter a number between 1 and {num_choices}." + Color.RESET)
            except ValueError:
                print(Color.RED + "  ✗ Please enter a valid number." + Color.RESET)
            except KeyboardInterrupt:
                print(Color.YELLOW + "\n\n  Game interrupted. Goodbye!" + Color.RESET)
                sys.exit(0)

    def show_choice_history(self):
        """Display all choices made during the game"""
        self.clear_screen()
        print()
        self.print_fancy_divider("═", 80, Color.MAGENTA)
        self.print_centered(Color.YELLOW + Color.BOLD + f"{ASCII_STAR} YOUR JOURNEY AS {self.character.upper()} {ASCII_STAR}")
        self.print_fancy_divider("═", 80, Color.MAGENTA)
        print()

        for i, choice in enumerate(self.choices_made, 1):
            segment_color = Color.CYAN if i % 2 == 0 else Color.GREEN
            print(f"  {segment_color}{i}. [{choice['segment']}] {Color.WHITE}{choice['choice']}" + Color.RESET)
            time.sleep(0.1)

        print()
        self.print_fancy_divider("═", 80, Color.MAGENTA)
        print()

    def play_again(self):
        """Ask if player wants to play again with fancy prompt"""
        self.print_fancy_divider("─", 80, Color.CYAN)
        print()
        choice = input(Color.YELLOW + f"  {ASCII_STAR} Would you like to play again? (y/n): " + Color.RESET).strip().lower()
        return choice in ['y', 'yes']

    def run(self):
        """Main game loop"""
        self.display_title()
        input(Color.GREEN + "\n  Press ENTER to begin your story..." + Color.RESET)

        self.select_character()

        # Game loop
        has_choices = True
        while has_choices:
            has_choices = self.display_segment(self.current_segment)

            if has_choices:
                next_segment = self.get_player_choice(self.current_segment)
                self.current_segment = next_segment

        # Game ended
        self.show_choice_history()

        if self.play_again():
            self.__init__()  # Reset game state
            self.run()
        else:
            self.clear_screen()
            print()
            self.print_fancy_divider("═", 80, Color.MAGENTA)
            self.print_centered(Color.CYAN + Color.BOLD + "Thank you for playing!")
            self.print_centered(Color.YELLOW + "CONSIDER THE CONSEQUENCES")
            self.print_centered(Color.WHITE + "A game based on the 1930 interactive fiction book")
            self.print_fancy_divider("═", 80, Color.MAGENTA)
            print()

def main():
    """Entry point for the game"""
    game = ConsiderTheConsequencesGame()
    game.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n\nGame terminated. Goodbye!" + Color.RESET)
        sys.exit(0)
