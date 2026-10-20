#!/bin/bash
set -e

SKILL_DIR="./skills"

if [ -d "$SKILL_DIR" ]; then
  echo "✅ 检测到 skill 目录：$SKILL_DIR"
  for skill_path in "$SKILL_DIR"/*/; do
    if [ -f "${skill_path}SKILL.md" ]; then
      echo "🔄 加载 skill: $skill_path"
      codex skill load "$skill_path"
    fi
  done
  echo "🎉 全部skill加载完成，可以直接调用"
else
  echo "⚠️ skills文件夹不存在，跳过自动加载"
fi
