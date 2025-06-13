from datetime import datetime, timezone
import os

# === 参数配置 ===
TITLE = "距离26赛季结束还有"
END_TIME = datetime(2026, 8, 20, 12, 0, 0, tzinfo=timezone.utc)
OUTPUT_PATH = "assets/countdown.svg"

# === 获取当前时间并计算倒计时 ===
now = datetime.now(timezone.utc)
remaining = END_TIME - now

days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

countdown_text = f"{days}d {hours:02d}h {minutes:02d}m {seconds:02d}s"
end_text = END_TIME.strftime("End: %Y-%-m-%-d %H:%M:%S UTC")

# === 构建 SVG ===
svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="600" height="200" xmlns="http://www.w3.org/2000/svg">
  <style>
    .title {{ font-size: 28px; font-weight: bold; fill: white; font-family: sans-serif; }}
    .countdown {{ font-size: 32px; fill: white; font-family: monospace; }}
    .endtime {{ font-size: 16px; fill: white; font-family: sans-serif; }}
  </style>
  <rect width="100%" height="100%" fill="#4d6bb1" rx="10" ry="10" stroke="#66ccff" stroke-width="4"/>
  
  <text x="50%" y="50" text-anchor="middle" class="title">{TITLE}</text>
  <text x="50%" y="110" text-anchor="middle" class="countdown">{countdown_text}</text>
  <text x="50%" y="150" text-anchor="middle" class="endtime">{end_text}</text>
</svg>
'''

# === 保存 SVG 文件 ===
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"✅ SVG 倒计时已保存至 {OUTPUT_PATH}")
