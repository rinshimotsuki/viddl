import subprocess
import os
from pathlib import Path
from subtitle import json_to_ass

def download_and_process(url, platform, mode):
    output_dir = Path.home() / "Download" / "Viddl" / platform.capitalize()
    output_dir.mkdir(parents=True, exist_ok=True)

    base_name = "video_temp"
    json_name = f"{base_name}.comments.json"
    ass_name = f"{base_name}_comments.ass"
    output_video = output_dir / (base_name + "_burned.mp4")

    cmd = ["yt-dlp", url, "-o", str(output_dir / base_name)]
    if mode == "audio":
        cmd += ["-x", "--audio-format", "mp3"]
    else:
        cmd += ["--write-subs", "--sub-langs", "comments", "--convert-subs", "ass"]

    try:
        yt_out = subprocess.run(cmd, capture_output=True, text=True)
    except Exception as e:
        return f"Error running yt-dlp: {e}"

    json_path = output_dir / json_name
    if json_path.exists():
        ass_path = output_dir / ass_name
        json_to_ass(json_path, ass_path)
        burn_cmd = [
            "ffmpeg", "-y", "-i", str(output_dir / f"{base_name}.mp4"),
            "-vf", f"ass={ass_path}", "-c:a", "copy", str(output_video)
        ]
        try:
            subprocess.run(burn_cmd, capture_output=True, text=True)
        except Exception as e:
            return f"FFmpeg error: {e}"
        return f"✅ Downloaded and burned subs!
Saved: {output_video}"
    else:
        return f"✅ Download complete, no subtitles found.
Saved to: {output_dir}"
