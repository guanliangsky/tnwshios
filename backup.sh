#!/bin/bash

# Backup script for SilenceHoldsApp
# This creates timestamped backups of your main files

BACKUP_DIR="backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create backup with timestamp
cp index.html "$BACKUP_DIR/index_$TIMESTAMP.html"

echo "✅ Backup created: $BACKUP_DIR/index_$TIMESTAMP.html"

# List recent backups
echo ""
echo "📁 Recent backups:"
ls -lt "$BACKUP_DIR" | head -10

echo ""
echo "💡 To restore a backup, copy it back to index.html:"
echo "   cp $BACKUP_DIR/index_YYYYMMDD_HHMMSS.html index.html"


