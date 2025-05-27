from collections import defaultdict

def analyze_keywords(words, keywords, transcript):
    word_map = defaultdict(list)

    for word in words:
        cleaned = word["word"].strip().lower().strip(".,!?")
        word_map[cleaned].append((word["start"], word["end"]))

    lines = []

    for kw in keywords:
        matches = word_map.get(kw.lower(), [])
        if matches:
            time_strs = [f"**[{round(s, 2)}s - {round(e, 2)}s]**" for s, e in matches]
            if len(matches) == 1:
                lines.append(f"✅ The word **{kw}** occurred once at {time_strs[0]}.")
            else:
                lines.append(f"✅ The word **{kw}** occurred {len(matches)} times at {', '.join(time_strs)}.")

    if not lines:
        lines.append("⚠️ No defined keywords were found in the audio.")

    paragraph = "\n\n".join(lines)
    paragraph += f"\n\n📝 **Transcript:**\n_{transcript}_"
    return paragraph
