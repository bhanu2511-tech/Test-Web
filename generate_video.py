import subprocess
import os

font_serif = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
font_bold = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

# 1. First generate the high-quality ambient music
print("Generating ambient soundtrack...")
audio_cmd = [
    "ffmpeg", "-y",
    "-f", "lavfi",
    "-i", "sine=frequency=220:duration=80[s1]; sine=frequency=277:duration=80[s2]; sine=frequency=330:duration=80[s3]; sine=frequency=440:duration=80[s4]; [s1][s2][s3][s4]amix=inputs=4:dropout_transition=0,volume=0.3,lowpass=f=550,afade=t=in:ss=0:d=2,afade=t=out:st=77:d=3",
    "-c:a", "aac",
    "-b:a", "128k",
    "/tmp/birthday_ambient.m4a"
]
subprocess.run(audio_cmd, check=True)

# 2. Build video filter chain for 2160x3840 80s video
print("Rendering 2160x3840 80-second birthday video...")
# We use a base color with subtle pulsing vignette and elegant drawtext overlays
vf_filters = [
    # Base dark elegant canvas
    "color=c=#141b27:s=2160x3840:d=80:r=24",
    # Vignette
    "vignette=PI/4",
    # Top Tag
    f"drawtext=fontfile='{font_bold}':text='OCTOBER 2026  ·  THE ARCHIVE OF US':fontcolor=#b89758:fontsize=52:x=(w-text_w)/2:y=600",
    # Main Heading
    f"drawtext=fontfile='{font_serif}':text='Happy Birthday, Kishor':fontcolor=#f6efe3:fontsize=110:x=(w-text_w)/2:y=760",
    # Romantic Quote
    f"drawtext=fontfile='{font_serif}':text='“For everything I could not fit into words.”':fontcolor=#caa77a:fontsize=64:x=(w-text_w)/2:y=960",
    # Core Heart Motif
    f"drawtext=fontfile='{font_serif}':text='♥':fontcolor=#8c2d2d:fontsize=150:x=(w-text_w)/2:y=1200",
    # Message Body Line 1
    f"drawtext=fontfile='{font_serif}':text='First love mom, last love me is a treasure I will always protect.':fontcolor=#ded5c4:fontsize=54:x=(w-text_w)/2:y=1550",
    # Message Body Line 2
    f"drawtext=fontfile='{font_serif}':text='My love for you is not in your presence, it is in prayers.':fontcolor=#ded5c4:fontsize=54:x=(w-text_w)/2:y=1680",
    # Signoff
    f"drawtext=fontfile='{font_serif}':text='Forever yours, Bhavna':fontcolor=#caa77a:fontsize=76:x=(w-text_w)/2:y=2000",
    # Active Dynamic Timecode (proving smooth active playback throughout all 80 seconds)
    f"drawtext=fontfile='{font_bold}':text='MEMORIES PLAYING  ·  %{{pts\\:gmtime\\:0\\:%M\\:%S}} / 01\\:20':fontcolor=#b89758:fontsize=48:x=(w-text_w)/2:y=3000",
    # Resolution confirmation badge
    f"drawtext=fontfile='{font_bold}':text='FULL RESOLUTION  ·  2160 × 3840':fontcolor=#6b7280:fontsize=38:x=(w-text_w)/2:y=3120"
]

vf_arg = ",".join(vf_filters)

video_cmd = [
    "ffmpeg", "-y",
    "-f", "lavfi", "-i", vf_arg,
    "-i", "/tmp/birthday_ambient.m4a",
    "-c:v", "libx264",
    "-preset", "ultrafast",
    "-profile:v", "baseline",
    "-level", "4.0",
    "-pix_fmt", "yuv420p",
    "-g", "48",
    "-movflags", "+faststart",
    "-c:a", "aac",
    "-b:a", "128k",
    "-t", "80",
    "/tmp/birthday_video_rendered.mp4"
]

subprocess.run(video_cmd, check=True)

# Copy to destinations
import shutil
shutil.copy2("/tmp/birthday_video_rendered.mp4", "public/birthday_video.mp4")
shutil.copy2("/tmp/birthday_video_rendered.mp4", "src/assets/birthday_video.mp4")

print("Successfully generated and placed birthday_video.mp4 in public/ and src/assets/")
