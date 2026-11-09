#!/usr/bin/env python3
"""
Claude & Human 3D Shorts CLI Generator
Works cross-platform on macOS, Windows, and Linux.

Usage:
    python make_video.py -t "The man who sold the Eiffel Tower twice"
    python make_video.py --list
    python make_video.py -t "Casino loophole" --open
"""

import sys
import os
import argparse
import webbrowser
import re

# Pre-packaged viral story scripts
STORIES = {
    "bank": {
        "title": "$1 Bank Loophole",
        "script": """[Human]
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
That might be the greatest legal heist in human history!"""
    },
    "pudding": {
        "title": "1.25M Miles Pudding Guy",
        "script": """[Human]
Claude, what is the craziest frequent flyer loophole that anyone has ever pulled off?

[Claude]
In 1999, a civil engineer named David Phillips cracked the airline miles code using chocolate pudding.

[Human]
Wait... chocolate pudding got him free flights?!

[Claude]
Every individual twenty-five cent Healthy Choice pudding cup had a barcode worth one hundred free airline miles!

[Human]
So what did he do?!

[Claude]
He spent three thousand dollars buying twelve thousand pudding cups, donated the pudding to food banks for a tax write-off, and walked away with one point two five million miles!

[Human]
Lifetime free first class tickets off chocolate pudding!"""
    },
    "eiffel": {
        "title": "Sold the Eiffel Tower Twice",
        "script": """[Human]
Claude, how did a con artist manage to sell the actual Eiffel Tower for scrap metal?

[Claude]
His name was Victor Lustig. And he didn't just sell it once—he sold it twice!

[Human]
Wait, how do you sell a national monument?!

[Claude]
In 1925, Paris was struggling with monument maintenance costs. Lustig forged government credentials, invited top scrap dealers to a secret hotel, and told them the city was tearing down the tower.

[Human]
And someone actually handed him the cash?!

[Claude]
One dealer paid him seventy thousand dollars in cash plus a massive bribe. Lustig hopped on a train to Vienna with a suitcase of cash and never looked back!"""
    },
    "matrix": {
        "title": "The Reality Render Glitch",
        "script": """[Human]
Claude, tell me one scientific fact that proves our universe operates like a simulated video game.

[Claude]
The speed of light is not about light at all. It is the maximum render speed of our reality.

[Human]
Wait, what do you mean by the render speed?!

[Claude]
Whenever information moves across space, the universe caps it at exactly three hundred thousand kilometers per second to prevent calculation lag.

[Human]
Are you telling me we are trapped inside a cosmic graphics processor?

[Claude]
And when nobody is observing a quantum particle, it does not even render a physical position!"""
    },
    "disappear": {
        "title": "How to Legally Disappear (Jouhatsu)",
        "script": """[Human]
Claude, if a person wanted to legally disappear off the face of the Earth tomorrow, could they actually do it?

[Claude]
Yes. And thousands of people in Japan do it every single year. It's called 'Jouhatsu' — the Evaporated People.

[Human]
Wait, there are actual companies that help you vanish?!

[Claude]
Specialized moving companies known as Night Movers show up at three in the morning, pack your entire room into unmarked vans, and relocate you to secret untraceable districts under complete legal protection.

[Human]
They literally press the restart button on life!"""
    }
}

def generate_procedural_script(topic):
    """Generates a viral retention dialogue script for any user topic."""
    return f"""[Human]
Claude, what is the craziest untold story about {topic}?

[Claude]
Most people think it is an urban legend, but official declassified archives tell a terrifyingly real story.

[Human]
Wait, what actually happened?!

[Claude]
In the middle of the operation, an unexpected flaw in the protocol was exploited, causing chaos that officials tried to cover up for years.

[Human]
How did anyone even figure out the loophole?

[Claude]
By the time authorities stepped in, over tens of millions of dollars had vanished without leaving a single trace!

[Human]
That might be the smartest maneuver in history!"""

def update_index_html_with_script(script_text):
    """Injects script as default into index.html if present."""
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    if not os.path.exists(html_path):
        return False

    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Escape backticks and dollars for JS template literal
    escaped_script = script_text.replace("`", "\\`").replace("${", "\\${")
    
    # Replace default script in textarea or bank template
    pattern = r'(bank:\s*`)([\s\S]*?)(`,\s*pudding:)'
    if re.search(pattern, content):
        new_content = re.sub(pattern, rf'\1{escaped_script}\3', content)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description="Claude & Human 3D Shorts Generator")
    parser.add_argument("-t", "--topic", help="Topic to generate a viral short about", type=str)
    parser.add_argument("-l", "--list", help="List all pre-built viral stories", action="store_true")
    parser.add_argument("-s", "--story", help="Choose a pre-built story key (bank, pudding, eiffel, matrix, disappear)", type=str)
    parser.add_argument("-o", "--open", help="Automatically open the studio in your browser", action="store_true", default=True)

    args = parser.parse_args()

    if args.list:
        print("\n📚 Available Viral Stories:")
        for key, item in STORIES.items():
            print(f"  • {key.ljust(12)} : {item['title']}")
        print("\nRun: python make_video.py -s <key>\n")
        return

    script = None
    title = "Custom Short"

    if args.story:
        key = args.story.lower()
        if key in STORIES:
            script = STORIES[key]["script"]
            title = STORIES[key]["title"]
        else:
            print(f"❌ Unknown story '{key}'. Use --list to see available stories.")
            return
    elif args.topic:
        title = args.topic
        script = generate_procedural_script(args.topic)
    else:
        # Default to bank loophole
        script = STORIES["bank"]["script"]
        title = STORIES["bank"]["title"]

    print(f"\n🎬 Story: {title}")
    print("=" * 50)
    print(script.strip())
    print("=" * 50)

    # Inject into index.html
    html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    if os.path.exists(html_file):
        update_index_html_with_script(script)
        print(f"\n✅ Updated {html_file}")
        if args.open:
            print("🚀 Opening 3D Shorts Studio in your browser...")
            webbrowser.open("file://" + os.path.abspath(html_file))
    else:
        print("⚠️ index.html not found in current directory.")

if __name__ == "__main__":
    main()

