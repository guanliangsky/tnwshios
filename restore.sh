#!/bin/bash

# Restore script for SilenceHoldsApp
# This helps you restore from any backup

BACKUP_DIR="backups"

if [ $# -eq 0 ]; then
    echo "📁 Available backups:"
    ls -lt "$BACKUP_DIR" | head -20
    echo ""
    echo "💡 Usage: ./restore.sh <backup_filename>"
    echo "   Example: ./restore.sh index_20250917_211353.html"
    exit 1
fi

BACKUP_FILE="$1"

if [ ! -f "$BACKUP_DIR/$BACKUP_FILE" ]; then
    echo "❌ Backup file not found: $BACKUP_DIR/$BACKUP_FILE"
    echo ""
    echo "📁 Available backups:"
    ls -lt "$BACKUP_DIR" | head -10
    exit 1
fi

# Create a backup of current file before restoring
CURRENT_BACKUP="backups/current_before_restore_$(date +%Y%m%d_%H%M%S).html"
cp index.html "$CURRENT_BACKUP"
echo "✅ Current file backed up to: $CURRENT_BACKUP"

# Restore the selected backup
cp "$BACKUP_DIR/$BACKUP_FILE" index.html
echo "✅ Restored from: $BACKUP_DIR/$BACKUP_FILE"
echo "🎉 Your app has been restored to the selected backup!"


