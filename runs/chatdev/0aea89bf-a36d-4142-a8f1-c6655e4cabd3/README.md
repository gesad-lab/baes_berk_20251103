# Run Summary

**Run ID**: 0aea89bf-a36d-4142-a8f1-c6655e4cabd3
**Framework**: chatdev
**Started**: 2025-10-29T12:42:09.096129Z
**Completed**: 2025-10-29T13:00:54.290421Z
**Duration**: 1125.19s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 229.87 |
| 2 | 2 | completed | 0/0 | 0 | 137.32 |
| 3 | 3 | completed | 0/0 | 0 | 153.11 |
| 4 | 4 | completed | 0/0 | 0 | 184.31 |
| 5 | 5 | completed | 0/0 | 0 | 200.58 |
| 6 | 6 | completed | 0/0 | 0 | 219.98 |

## Directory Structure

```
0aea89bf-a36d-4142-a8f1-c6655e4cabd3/
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
