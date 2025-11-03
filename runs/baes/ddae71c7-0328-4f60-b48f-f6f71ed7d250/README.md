# Run Summary

**Run ID**: ddae71c7-0328-4f60-b48f-f6f71ed7d250
**Framework**: baes
**Started**: 2025-10-29T20:34:48.043352Z
**Completed**: 2025-10-29T20:38:06.925102Z
**Duration**: 198.88s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 29.53 |
| 2 | 2 | completed | 0/0 | 0 | 44.74 |
| 3 | 3 | completed | 0/0 | 0 | 31.79 |
| 4 | 4 | completed | 0/0 | 0 | 23.96 |
| 5 | 5 | completed | 0/0 | 0 | 33.71 |
| 6 | 6 | completed | 0/0 | 0 | 35.15 |

## Directory Structure

```
ddae71c7-0328-4f60-b48f-f6f71ed7d250/
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
