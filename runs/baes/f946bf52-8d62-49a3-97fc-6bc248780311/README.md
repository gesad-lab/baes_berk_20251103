# Run Summary

**Run ID**: f946bf52-8d62-49a3-97fc-6bc248780311
**Framework**: baes
**Started**: 2025-10-29T19:12:50.777247Z
**Completed**: 2025-10-29T19:16:34.090958Z
**Duration**: 223.31s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 42.53 |
| 2 | 2 | completed | 0/0 | 0 | 33.14 |
| 3 | 3 | completed | 0/0 | 0 | 38.05 |
| 4 | 4 | completed | 0/0 | 0 | 35.94 |
| 5 | 5 | completed | 0/0 | 0 | 39.24 |
| 6 | 6 | completed | 0/0 | 0 | 34.39 |

## Directory Structure

```
f946bf52-8d62-49a3-97fc-6bc248780311/
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
