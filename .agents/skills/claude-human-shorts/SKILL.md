---
name: claude-human-shorts
description: >-
  Generate viral 9:16 vertical animated shorts and reels featuring conversational
  dialogue between Claude AI and a human character. Use this skill whenever the user
  wants to create faceless videos, produce animated 3D Claude & Human stories, write
  high-retention scripts (bank loopholes, life hacks, mysteries), or scaffold the
  instant browser-based 3D video studio on any Mac, Windows, or Linux machine.
---

# Claude & Human Viral 3D Shorts Generator

This skill teaches the agent how to write, scaffold, and generate viral 9:16 vertical shorts (TikTok, Instagram Reels, YouTube Shorts) featuring **3D character models of Claude AI and a Human character** having rapid-fire dialogue about fascinating true stories, legal loopholes, science glitches, and crazy mysteries.

Works **100% locally with zero API costs, zero monthly subscriptions, and zero external dependencies**.

---

## 🚀 Quick Setup on macOS (MacBook)

To use this skill on any MacBook or new project:

1. **Global Install (Available everywhere in Antigravity / Claude)**:
   Place this skill folder in your global skills directory:
   ```bash
   mkdir -p ~/.gemini/config/skills/claude-human-shorts
   # Or for Claude Code:
   mkdir -p ~/.claude/skills/claude-human-shorts
   ```
   Copy `SKILL.md` into that directory.

2. **Project-Level Install**:
   Put `SKILL.md` inside your project root at `.agents/skills/claude-human-shorts/SKILL.md`.

---

## 🎬 Step-by-Step Production Workflow

When the user asks to create a video:

### Step 1: Craft the High-Retention Dialogue Script
Follow the **Viral Retention Formula** (Average duration: 30–45 seconds):
* **0–2s Hook**: No intro! Immediate provocative statement or question.
* **3–12s Setup**: Surprising real-world context with verified specifics.
* **13–24s Escalation**: Disbelief from the Human, mind-blowing twist from Claude.
* **25–35s Punchline & Loop**: The unbelievable payoff, ending with a phrase that loops naturally back into the opening hook.

#### Required Format:
```text
[Human]
Claude, is it actually true that a man bought a billion-dollar bank for just ONE dollar?

[Claude]
Not only is it true, but the United States government practically begged him to take it.

[Human]
Wait, what?! How is that even legally possible?

[Claude]
During the 2008 crash, Texas billionaire Andy Beal saw a collapsing bank drowning in toxic debt. He walked in, slid a single one-dollar bill across the desk, and signed for it.

[Human]
Did he actually make any profit off that?

[Claude]
Three years later, he liquidated the distressed assets and walked away with over two point five billion dollars in pure profit!

[Human]
That might be the greatest legal heist in human history!
```

---

### Step 2: Scaffold or Launch the 3D Studio Engine

Whenever the user wants to preview or render the video on their machine, scaffold the standalone `index.html` file into the current directory.

#### On macOS:
```bash
# Open directly in Google Chrome, Brave, or Safari
open index.html
```

#### On Windows:
```powershell
Start-Process "index.html"
```

---

## 🎨 3D Character Model Architecture

The studio uses HTML5 Canvas vector-sculpted 3D character models with natural physics:

1. **Human Character Model**:
   * **Bust & Hoodie**: Multi-stop gradient-shaded creator hoodie (`#1d273b` to `#2b3954`) with 3D collar folds and drawstrings.
   * **Expressive Face**: Rounded 3D jawline, natural blush highlights (`rgba(239,68,68,0.14)`), and wavy volumetric hair.
   * **Natural Eye Blinking**: Periodic eyelid closure every ~3 seconds with high-gloss specular reflections.
   * **Anatomical Mouth**: Realistic phoneme mouth opening dynamically to speech, showing upper teeth and tongue.
   * **Studio Mic**: Shaded condenser microphone capsule with reactive speech bounce.

2. **Claude AI Character Model**:
   * **Matte Porcelain Chassis**: Sculpted cybernetic chassis with warm bronze undertones and glowing orange conduits (`#d97706`).
   * **Anthropic Spark Reactor**: Pulsing 8-point geometric energy core in the chest.
   * **Digital Visor**: Curved glass visor with glowing optical sensors and dynamic laser matrix scan line.
   * **Audio Equalizer Mouth**: Real-time frequency-modulated neon equalizer bars that dance to audio.
   * **Anti-Gravity Hover**: Smooth floating sine-wave elevation.

---

## 📱 Visual & Typography Specifications

* **Resolution**: 1080 × 1920 (Vertical 9:16 Shorts/Reels standard).
* **Frame Rate**: 60 FPS hardware-accelerated.
* **Layout Modes**:
  1. **Podcast Duet Split**: Top half is Human in acoustic creator studio; bottom half is Claude in cybernetic AI lab.
  2. **Facing 3D Arena**: Side-by-side stage with central story B-roll card.
* **Captions**:
  * Heavyweight bold typography (`Montserrat 900` or `TheBoldFont`).
  * 3–4 words visible at a time inside a high-contrast dark pill.
  * Active word highlighted in bright viral yellow (`#FACC15`) with 9px black stroke outline and glow bloom.
* **Foley & Audio**:
  * Procedural whoosh SFX on speaker change.
  * Pop/blip SFX on each advancing word.
  * Procedural low-pass tension drone background music.

---

## 💻 Standalone Scaffold Generator (`generate_studio.py`)

To automatically create the studio in any new directory on macOS or Linux without copying files:

```python
# Save as generate_studio.py and run: python3 generate_studio.py
import os

STUDIO_HTML = """<!-- Insert full standalone index.html engine here -->"""

def scaffold():
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(STUDIO_HTML)
    print("✅ Created index.html! Run 'open index.html' to preview.")

if __name__ == "__main__":
    scaffold()
```

---

## ⚡ 10 Viral Story Concepts Ready to Generate

1. **The $1 Bank Heist**: Andy Beal buying a collapsing bank for $1 and profiting $2.5B.
2. **The 1.25M Miles Pudding Guy**: David Phillips using chocolate pudding barcodes for lifetime first-class flights.
3. **The Man Who Sold the Eiffel Tower**: Victor Lustig posing as a French minister and selling the monument twice.
4. **The Reality Render Glitch**: Why the speed of light is the maximum processing speed of our simulation.
5. **The Bullet Ant Index**: Experiencing 24 hours of maximum human agony from a jungle sting.
6. **The Evaporated People (Jouhatsu)**: Japan's night-moving companies that help people legally vanish forever.
7. **The Man Who Mailed Himself**: Reginald Bray posting unconventional parcels across the UK postal system.
8. **The Accidental Millionaire**: How a misprinted lottery ticket caused a massive legal standoff.
9. **The Casino Eye in the Sky**: Why casinos fear edge-sorters more than card counters.
10. **The $0 House Loophole**: Adverse possession and how squatters legally claim mansions.

