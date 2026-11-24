import os

LINE = "One star. Gravity has perfect attendance and never takes a day off, yet it always drops my phone screen-first onto concrete."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
