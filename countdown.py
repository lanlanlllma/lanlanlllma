from datetime import datetime, timezone
import os

# 设置目标时间（UTC时间）
TARGET_DATE = datetime(2026, 8, 20, 20, 0, 0, tzinfo=timezone.utc)

# 获取当前时间（UTC）
now = datetime.now(timezone.utc)
remaining = TARGET_DATE - now

days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

# 构建 SVG 内容
svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="600" height="100" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#4d6bb1" rx="15" ry="15"/>
  <text x="50%" y="55%" dominant-baseline="middle" text-anchor="middle" 
        font-size="28" font-family="Arial, sans-serif" fill="#e0f1f0">
    距离26赛季结束还有 {days}天 {hours}时 {minutes}分
  </text>
</svg>'''

# 输出 SVG 文件
os.makedirs("assets", exist_ok=True)
with open("assets/countdown.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("✅ 已生成 SVG：assets/countdown.svg")
