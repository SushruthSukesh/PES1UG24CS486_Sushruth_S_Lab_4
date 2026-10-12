# High-Low Card Predictor Repair Lab

This project is a card prediction game using **Pygame**. It introduces students to deck state management, lexicographical vs. numerical evaluation, probability assessment, and UI button interaction within an object-oriented codebase.
---

## What's Provided

A working High or Low Card Predictor game with:

- A complete 52-card deck model supporting suits, ranks, and auto-reshuffling when depleted
- Procedural card rendering featuring suit symbols and colors (Hearts, Diamonds, Clubs, Spades)
- Clickable HIGHER and LOWER interactive buttons
- Live score tracking, deck count indicators, and round feedback messaging

The implementation includes the repaired comparison logic and the three gameplay
features from the lab: consecutive-win multipliers, tie handling, and a
side-by-side reveal animation.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**
---

## Getting Started

### Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install pygame
```

3. Run the game from the project folder:

```bash
python main.py
```

**Controls:** Left-click on the HIGHER or LOWER buttons to predict the next card.   

The game uses the numeric card values 2 through Ace for comparisons. Correct
predictions increase the score by the current consecutive-win streak, incorrect
predictions reset the streak, and equal ranks produce a neutral `PUSH` without
changing the score or streak. During the 0.7-second reveal, both cards are
shown side by side and new input is ignored until the reveal completes.


## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Fix the card rank comparison bug

Face cards and tens behave inconsistently during higher/lower evaluations. Ensure that card comparisons follow actual numerical values rather than alphabetical ordering so all card values evaluate in their true order.

### Task 2: Implement Consecutive Win Streak Multipliers

Correct predictions currently award only a flat score increase with no reward for extended winning runs. Implement a streak tracker that rewards consecutive correct guesses with escalating score multipliers, resetting the bonus back to baseline on an incorrect pick.

### Task 3: Implement Tie Evaluation Rules

Drawing a card of identical rank to the current one is currently penalized as a flat loss. Add tie-handling logic that preserves the player's current score and active streak, presenting a neutral "PUSH" notification instead of docking points.

### Task 4: Implement side-by-side card reveal animation

The active card currently snaps immediately to the newly drawn card, making rapid comparisons hard to follow visually. Enhance the layout to show the previous and new cards side-by-side with a brief reveal pause before advancing to the next guess

---

## Expected Behavior

- Clicking HIGHER or LOWER draws the next card from the deck and updates the score.
- Number and face cards evaluate according to their real hierarchy (2 < 3 <...< K < A).
- The deck counter accurately decrements with each draw and reshuffles automatically when empty. 
- Visual feedback clearly displays whether the previous guess was correct or incorrect.
---

## Folder Structure

```
card_predictor/
├── game/
│   ├── card.py
│   ├── deck.py
│   └── game_engine.py
├── main.py
└── README.md
```

---

## Submission Checklist

Submission is only the following three things:

- [] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [] The Chat/LLM used page link, with the complete chat history

## Video Demo

- [After changes - gameplay recording](videos/after.mp4)

The supplied recording demonstrates the completed game. A separate before-change
recording was not available in the project workspace.
