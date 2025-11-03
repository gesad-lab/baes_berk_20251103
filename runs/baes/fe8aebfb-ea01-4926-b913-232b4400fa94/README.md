# Run Summary

**Run ID**: fe8aebfb-ea01-4926-b913-232b4400fa94
**Framework**: baes
**Started**: 2025-10-29T13:49:33.623853Z
**Completed**: 2025-10-29T13:53:04.964144Z
**Duration**: 211.34s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 39.24 |
| 2 | 2 | completed | 0/0 | 0 | 39.11 |
| 3 | 3 | completed | 0/0 | 0 | 42.30 |
| 4 | 4 | completed | 0/0 | 0 | 24.30 |
| 5 | 5 | completed | 0/0 | 0 | 30.10 |
| 6 | 6 | completed | 0/0 | 0 | 36.28 |

## Directory Structure

```
fe8aebfb-ea01-4926-b913-232b4400fa94/
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
