# Run Summary

**Run ID**: 666c49e3-e35d-4365-93c0-47273942a1c5
**Framework**: chatdev
**Started**: 2025-10-31T14:53:44.205214Z
**Completed**: 2025-10-31T15:11:48.379473Z
**Duration**: 1084.17s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 156.74 |
| 2 | 2 | completed | 0/0 | 0 | 130.98 |
| 3 | 3 | completed | 0/0 | 0 | 163.46 |
| 4 | 4 | completed | 0/0 | 0 | 198.98 |
| 5 | 5 | completed | 0/0 | 0 | 221.45 |
| 6 | 6 | completed | 0/0 | 0 | 212.55 |

## Directory Structure

```
666c49e3-e35d-4365-93c0-47273942a1c5/
├── sprint_001/          # First sprint artifacts
│   ├── generated_artifacts/
│   ├── logs/
│   ├── metadata.json
│   └── validation.json
├── sprint_002/          # Second sprint artifacts
│   └── ...
├── final/               # Symlink to last successful sprint
└── metrics.json         # Run-level metrics (single source of truth)
```

## Accessing Results

### View final artifacts
```bash
cd final/generated_artifacts/managed_system/
```

### Compare sprints
```bash
diff -r sprint_001/generated_artifacts sprint_002/generated_artifacts
```

### View metrics (single source of truth)
```bash
cat metrics.json | jq
```

### Check specific sprint
```bash
cat sprint_001/metadata.json
```
