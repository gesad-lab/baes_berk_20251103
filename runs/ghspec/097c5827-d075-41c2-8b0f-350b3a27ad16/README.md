# Run Summary

**Run ID**: 097c5827-d075-41c2-8b0f-350b3a27ad16
**Framework**: ghspec
**Started**: 2025-10-31T19:57:39.009946Z
**Completed**: 2025-10-31T20:12:33.688871Z
**Duration**: 894.68s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 115.48 |
| 2 | 2 | completed | 0/0 | 0 | 187.77 |
| 3 | 3 | completed | 0/0 | 0 | 121.77 |
| 4 | 4 | completed | 0/0 | 0 | 184.08 |
| 5 | 5 | completed | 0/0 | 0 | 136.15 |
| 6 | 6 | completed | 0/0 | 0 | 149.42 |

## Directory Structure

```
097c5827-d075-41c2-8b0f-350b3a27ad16/
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
