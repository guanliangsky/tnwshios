#!/bin/bash

# Monitor commits script for SilenceHoldsApp
# Shows recent commits and auto-commit status

echo "=== SILENCE HOLDS APP - COMMIT MONITOR ==="
echo "Current time: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Show recent commits
echo "=== RECENT COMMITS ==="
git log --oneline -10

echo ""
echo "=== TODAY'S COMMITS (09/19) ==="
git log --since="2025-09-19" --until="2025-09-20" --pretty=format:"%h - %an, %ad : %s" --date=format:"%Y-%m-%d %H:%M:%S"

echo ""
echo "=== AUTO-COMMIT STATUS ==="
if [ -f "auto_commit.log" ]; then
    echo "Auto-commit log exists. Last 5 entries:"
    tail -5 auto_commit.log
else
    echo "No auto-commit log found yet"
fi

echo ""
echo "=== CRON JOB STATUS ==="
crontab -l | grep -E "(auto_commit|SilenceHoldsApp)" || echo "No auto-commit cron job found"

echo ""
echo "=== CURRENT STATUS ==="
git status --short
