# Run Summary

**Run ID**: 55fbc0fb-c76b-416a-a5f7-c6c996254e74
**Framework**: baes
**Started**: 2025-10-31T05:13:24.706818Z
**Completed**: 2025-10-31T05:19:32.104294Z
**Duration**: 367.40s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 62.93 |
| 2 | 2 | completed | 0/0 | 0 | 63.14 |
| 3 | 3 | completed | 0/0 | 0 | 63.03 |
| 4 | 4 | completed | 0/0 | 0 | 55.17 |
| 5 | 5 | completed | 0/0 | 0 | 63.35 |
| 6 | 6 | completed | 0/0 | 0 | 59.78 |

## Directory Structure

```
55fbc0fb-c76b-416a-a5f7-c6c996254e74/
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
