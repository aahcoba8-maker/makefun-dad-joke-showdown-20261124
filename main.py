import os

# Dad Joke Showdown: one dad joke, at most 200 characters.
# Three puns stacked on one setup (dough / crumby / kneaded), punchline last.
JOKE = "My son asked why I quit my bakery job. I told him I couldn't make enough dough \u2014 and the hours were crumby, so I kneaded a change."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
