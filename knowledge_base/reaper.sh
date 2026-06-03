#!/bin/bash
# The Reaper Job: Harvests, validates, and merges local decentralized logs.

# Explicitly set PATH to ensure dependencies like jq are found in restrictive cron environments
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Dynamically resolve the root of the repository
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

KNOWLEDGE_BASE="$REPO_ROOT/knowledge_base"
CENTRAL_LOG="$KNOWLEDGE_BASE/central_archive.jsonl"

# Check if jq is installed before proceeding to prevent data loss
if ! command -v jq >/dev/null 2>&1; then
  echo "CRITICAL ERROR: jq is not installed or not in PATH. Aborting to prevent data loss." >&2
  exit 1
fi

# In this sandbox, some agents were created outside the repository. We must scan both locations.
for agent_dir in "$REPO_ROOT"/agents/* "$REPO_ROOT"/../agents/*; do
  if [ -d "$agent_dir" ]; then
    local_log="$agent_dir/local_knowledge.jsonl"
    
    if [ -f "$local_log" ] && [ -s "$local_log" ]; then
      success_count=0
      error_count=0
      
      # Process each new knowledge delta
      while IFS= read -r line || [ -n "$line" ]; do
        # Skip empty lines
        [ -z "$line" ] && continue
        
        # True JSON validation using jq to ensure required schema keys are present
        if echo "$line" | jq -e 'has("agent") and has("timestamp") and has("knowledge_delta")' > /dev/null 2>&1; then
          # Append to Central Archive
          echo "$line" >> "$CENTRAL_LOG"
          ((success_count++))
        else
          echo "Validation Error: Rejected malformed delta from $agent_dir" >&2
          ((error_count++))
        fi
      done < "$local_log"
      
      # Only clear the local log if we processed lines and didn't encounter system-level failures
      if [ "$success_count" -gt 0 ] || [ "$error_count" -gt 0 ]; then
        > "$local_log"
      fi
    fi
  fi
done
