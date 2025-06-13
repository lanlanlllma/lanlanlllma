from datetime import datetime, timezone

# 配置目标时间（UTC）
TARGET = datetime(2026, 8, 20, 12, 0, 0, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
diff = TARGET - now

days = diff.days
hours = diff.seconds // 3600
minutes = (diff.seconds % 3600) // 60

countdown_str = countdown_str = (
    f"<div align=\"center\" style=\"background:#f9f9f9;padding:10px;border-radius:8px;\">"
    f"  <h2 style=\"margin:0;color:#d9534f;\"><strong>{days} 天 {hours} 小时 {minutes} 分</strong></h2>"
    f"  <p style=\"margin:4px 0 0;\">（目标时间：2026 年 8 月 20 日 12:00 UTC）</p>"
    "</div>"
)

# 更新 README 中 countdown 部分
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = content.split("<!-- countdown-start -->")[0] + \
              "<!-- countdown-start -->\n" + \
              countdown_str + "\n" + \
              "<!-- countdown-end -->" + \
              content.split("<!-- countdown-end -->")[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ README 倒计时已更新")
