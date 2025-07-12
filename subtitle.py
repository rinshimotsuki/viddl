import json
import random

HEADER = """[Script Info]
ScriptType: v4.00+
PlayResX: 640
PlayResY: 360
Timer: 100.0000

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, 
StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,20,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,1,0,7,10,10,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

def sec_to_timestamp(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    cs = int((seconds - int(seconds)) * 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"

def json_to_ass(json_path, ass_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        comments = json.load(f)

    with open(ass_path, 'w', encoding='utf-8') as out:
        out.write(HEADER)
        for c in comments:
            body = c.get("body") or c.get("content")
            vpos_ms = c.get("vposMs")
            if not body or vpos_ms is None:
                continue
            start = vpos_ms / 1000.0
            end = start + 5.0
            y = random.randint(50, 300)
            text = body.replace("\n", " ").replace(",", "␣")
            line = f"Dialogue: 0,{sec_to_timestamp(start)},{sec_to_timestamp(end)},Default,,0,0,0,,{{\move(640,{y},0,{y})}}{text}\n"
            out.write(line)
