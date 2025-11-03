# Run Summary

**Run ID**: 9c4f9f60-8260-438c-9481-f4bdba1098cc
**Framework**: baes
**Started**: 2025-10-30T19:12:01.042443Z
**Completed**: 2025-10-30T19:15:44.088063Z
**Duration**: 223.05s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 34.05 |
| 2 | 2 | completed | 0/0 | 0 | 41.00 |
| 3 | 3 | completed | 0/0 | 0 | 38.70 |
| 4 | 4 | completed | 0/0 | 0 | 37.74 |
| 5 | 5 | completed | 0/0 | 0 | 30.06 |
| 6 | 6 | completed | 0/0 | 0 | 41.48 |

## Directory Structure

```
9c4f9f60-8260-438c-9481-f4bdba1098cc/
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
