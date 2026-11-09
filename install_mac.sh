#!/bin/bash
# -------------------------------------------------------------
# 1-Click Installer for Claude & Human Shorts Skill on macOS
# -------------------------------------------------------------

echo "🎬 Installing Claude & Human Shorts Skill on macOS..."

# Target directories
AGY_DIR="$HOME/.gemini/config/skills/claude-human-shorts"
CLAUDE_DIR="$HOME/.claude/skills/claude-human-shorts"

# Create directories
mkdir -p "$AGY_DIR"
mkdir -p "$CLAUDE_DIR"

# Copy SKILL.md
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -f "$SCRIPT_DIR/SKILL.md" ]; then
    cp "$SCRIPT_DIR/SKILL.md" "$AGY_DIR/SKILL.md"
    cp "$SCRIPT_DIR/SKILL.md" "$CLAUDE_DIR/SKILL.md"
    echo "✅ Successfully installed to:"
    echo "   • $AGY_DIR/SKILL.md"
    echo "   • $CLAUDE_DIR/SKILL.md"
    echo ""
    echo "🚀 You can now open Antigravity or Claude Code on your Mac and say:"
    echo "   'Make a viral 3D Claude & Human short about the man who bought a bank for \$1'"
else
    echo "❌ Error: SKILL.md not found in the same folder."
fi

