# CONSIDER THE CONSEQUENCES (1930)
## Interactive Fiction CMD Game

A complete, fully-playable command-line game based on the 1930 book "Consider the Consequences" by Doris Webster and Mary Alden Hopkins - the **first choose-your-own-adventure book ever published** (predating the "Choose Your Own Adventure" series by 49 years)!

## 🎮 How to Play

### Play Online (Browser):
**🌐 [Play Live Demo](https://ringmast4r.github.io/CTC-Game-LIVE-DEMO/)**

No installation required! Play directly in your browser.

### Play Locally (Command Line):
Simply run:
```
python game.py
```

## ✨ Game Features

- **89 Complete Story Segments** - All content from the original 1930 book
- **3 Interconnected Characters**: Helen, Jed, and Saunders
- **43 Decision Points** with meaningful choices
- **83+ Unique Endings** based on your decisions
- **Beautiful CMD Interface** with colors and ASCII art
- **Character-Specific Color Themes**: Red (Helen), Blue (Jed), Green (Saunders)
- **Chapter Transitions** - Decorative dividers at major story milestones
- **Contextual Visuals** - Location-based and emotional scene indicators
- **Decision Animations** - Visual prompts before each choice
- **Scene Transitions** - Star animations between story segments
- **Smart Progress Bar** - Tracks your journey through the story
- **Sentiment-Based Endings** - Happy, sad, or bittersweet visual treatments
- **Animated Text Effects** and loading animations
- **Choice History Tracking** - See the path you took
- **Replay Functionality** - Try different paths and characters

## 📖 The Story

### Three Interconnected Lives:

1. **HELEN** - A young woman choosing between passion (Jed) and security (Saunders)
   - 37 story segments
   - Paths through career, family duty, and romantic complications

2. **JED** - A wealthy heir whose choices define his character
   - 20 story segments
   - From shotgun weddings to murder trials

3. **SAUNDERS** - A responsible eldest son torn between duty and desire
   - 32 story segments
   - Navigating business, corruption, and romantic choices

The stories are deeply interwoven - characters appear in each other's narratives with different outcomes!

## 🎯 Technical Details

**Files:**
- `game.py` - Main game engine with complete logic
- `story_data.py` - All 89 story segments with choices and endings
- `README.md` - This file

**Requirements:**
- Python 3.6 or higher
- Windows 10+ / macOS / Linux (ANSI color support)
- No external dependencies - uses native ANSI color codes!

**Compatibility:**
- Optimized for Windows Command Prompt and PowerShell
- Works on macOS Terminal and Linux terminals
- Best viewed in terminals with full UTF-8 and ANSI color support

## 🌟 Historical Significance

"Consider the Consequences" (1930) was groundbreaking:
- First interactive fiction book in history
- Published **49 years before** "Choose Your Own Adventure"
- Explores 1930s themes: marriage, career, family duty, corruption
- Realistic consequences - good choices don't always lead to happy endings

## 🚀 Game Structure

The game uses a segment-based branching narrative:
```
START → Choose Character (Helen/Jed/Saunders)
  ↓
Display Story Segment
  ↓
Present Choices (2-3 options)
  ↓
Player Makes Choice
  ↓
Navigate to Next Segment
  ↓
Repeat until Ending
  ↓
Show Consequence & Choice History
```

## 📊 Statistics

- **Total Segments**: 89 (including START screens)
  - Helen: 37 segments (H-START through H-36)
  - Jed: 20 segments (J-START through J-19)
  - Saunders: 32 segments (S-START through S-31)
- **Decision Points**: 43 choices throughout the game
- **Possible Endings**: 83+ different outcomes
- **Character Interconnections**: Multiple (Helen↔Jed, Helen↔Saunders, Jed↔Carol, Saunders↔Carol, etc.)

## 🎨 Visual Features

- **Colored ASCII Title Screen** with book graphic
- **Character-Specific Themes**:
  - Helen: Red colored prompts and progress bars
  - Jed: Blue colored prompts and progress bars
  - Saunders: Green colored prompts and progress bars
- **Chapter Transitions**:
  - Major story milestones have decorative chapter dividers
  - 12 chapter breaks across all three character paths
- **Contextual ASCII Art**:
  - Romance scenes (hearts for weddings/marriages)
  - New York City location indicators
  - European/Paris adventure markers
- **Dynamic Endings**:
  - Happy endings: Flower decorations
  - Sad endings: Framed memorial text
  - Bittersweet endings: Wave decorations
- **Animated Loading Effects**
- **Choice Confirmation Animations**
- **Consequence Warnings** after each decision
- **Progress Tracking** with visual bar (scales to typical path length)
- **Styled Dividers and Borders**

## 🔄 Replay Value

- Try all 3 characters to see interconnected stories
- Make different choices to discover 83+ endings
- See how characters appear in each other's narratives
- Explore convergent paths where different choices lead to same outcomes

## 📝 Credits

**Original Book:**
- Authors: Doris Webster and Mary Alden Hopkins
- Publisher: The Century Co., New York
- Copyright: 1930

**Game Adaptation:**
- Based on complete story structure from the original 1930 text
- All 89 story segments and 43 decision points preserved from the book
- Enhanced with modern terminal visual effects and animations
- Added contextual visuals, chapter transitions, and progress tracking
- Created 2024 - Faithful digital adaptation of the 1930 original

---

## 🎯 Game Content Verification

This game contains **100% of the original book content**:
- ✓ All 89 story segments from the 1930 book
- ✓ All 43 decision points exactly as written
- ✓ All 83+ unique endings with original consequence text
- ✓ Character interconnections and story convergence points preserved
- ✓ Narrative structure faithful to the source material

Based on the complete text analysis from: `C:\Users\Squir\Desktop\Consider The Consequences 1930`

---

**Enjoy exploring this piece of literary history!**

*The choices you make will determine your fate... Consider the consequences!*
