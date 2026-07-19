#!/usr/bin/env python3
"""
PreToolUse hook — enforce vùng cấm ghi của learning-vault (multi-domain).
Đăng ký sẵn trong .claude/settings.json (dùng $CLAUDE_PROJECT_DIR). Yêu cầu: python3 trong PATH.

Nguyên tắc: rule an toàn enforce bằng hook, không dựa vào text trong CLAUDE.md.
Exit 0 = cho phép; exit 2 = chặn (stderr trả về cho Claude đọc lý do).

DANH TÍNH SKILL — cơ chế sentinel file (env export trong bash KHÔNG truyền được
vào tiến trình hook, vì hook do Claude Code spawn khi tool Write/Edit chạy):
  - Skill khai danh tính TRƯỚC khi ghi vùng bảo vệ:
      mkdir -p .claude/state && echo vault-sync > .claude/state/active_skill
  - Skill xóa sentinel khi xong: rm -f .claude/state/active_skill
  - Sentinel quá TTL (30 phút) tự mất hiệu lực — chống quyền treo vĩnh viễn.
"""
import json
import os
import re
import sys
import time

BLOCK = 2
ALLOW = 0
WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}

PROJECT_DIR = os.environ.get("CLAUDE_PROJECT_DIR", ".")
SENTINEL = os.path.join(PROJECT_DIR, ".claude", "state", "active_skill")
SENTINEL_TTL_SEC = 30 * 60


def read_active_skill() -> str:
    try:
        if time.time() - os.path.getmtime(SENTINEL) > SENTINEL_TTL_SEC:
            return ""
        return open(SENTINEL, encoding="utf-8").read().strip()
    except OSError:
        return ""


def deny(msg: str):
    print(f"[vault-hook] CHAN: {msg}", file=sys.stderr)
    sys.exit(BLOCK)


def main():
    data = json.load(sys.stdin)
    tool = data.get("tool_name", "")
    tin = data.get("tool_input", {}) or {}
    path = tin.get("file_path", "") or tin.get("path", "") or ""

    # --- Luật 0: không bao giờ chạm .env ---
    if ".env" in path:
        deny(".env là vùng cấm tuyệt đối.")

    if tool not in WRITE_TOOLS or not path:
        sys.exit(ALLOW)

    norm = path.replace("\\", "/")
    skill = read_active_skill()

    # --- Luật 1: 00_Templates (mọi domain) chỉ con người HOẶC skill template-editor ---
    if "/00_Templates/" in norm and skill != "template-editor":
        deny("00_Templates/ chỉ con người hoặc skill template-editor được sửa "
             "(khai sentinel active_skill=template-editor; đề xuất diff trước khi ghi).")

    # --- Luật 2: Dashboard (domain + global) chỉ vault-sync / *-compile ---
    if ("/99_Dashboard/" in norm or "/99_Global_Dashboard/" in norm) and \
            skill not in ("vault-sync", "topik-grammar-compile", "ba-compile"):
        deny("Dashboard là render output. Chạy vault-sync hoặc skill compile của domain "
             "(skill phải khai sentinel .claude/state/active_skill trước khi ghi).")

    # --- Luật 3: note trong immutable_when_verified là bất biến khi verified ---
    # (mở rộng regex theo .claude/domains.yaml khi domain mới có thư mục immutable)
    m = re.search(r"(?:^|/)TOPIK/50_Exams/([^/]+\.md)$", norm)
    if m and os.path.exists(path):
        try:
            head = open(path, encoding="utf-8").read(600)
            if re.search(r"^status:\s*verified\s*$", head, re.M):
                deny(f"{m.group(1)} đã verified — immutable. Sai sót thật sự: con người hạ status trước.")
        except OSError:
            pass

    # --- Luật 4: field sr-* chỉ review-scheduler được sửa ---
    if skill != "review-scheduler":
        new_text = (tin.get("new_string", "") or "") + (tin.get("content", "") or "")
        if tool in ("Edit", "MultiEdit") and re.search(r"^sr-(due|interval|ease):\s*\S", new_text, re.M):
            old_text = tin.get("old_string", "") or ""
            if not re.search(r"^sr-(due|interval|ease):", old_text, re.M) or \
                    re.findall(r"^sr-\w+:.*$", new_text, re.M) != re.findall(r"^sr-\w+:.*$", old_text, re.M):
                deny("Field sr-* chỉ review-scheduler được cập nhật (khai sentinel active_skill=review-scheduler).")

    sys.exit(ALLOW)


if __name__ == "__main__":
    main()
