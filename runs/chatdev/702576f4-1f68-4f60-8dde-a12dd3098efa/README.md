# Run Summary

**Run ID**: 702576f4-1f68-4f60-8dde-a12dd3098efa
**Framework**: chatdev
**Started**: 2025-10-30T21:13:09.696689Z
**Completed**: 2025-10-30T21:45:48.564853Z
**Duration**: 1958.87s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 173.40 |
| 2 | 2 | completed | 0/0 | 0 | 150.11 |
| 3 | 3 | completed | 0/0 | 0 | 489.16 |
| 4 | 4 | completed | 0/0 | 0 | 321.72 |
| 5 | 5 | completed | 0/0 | 0 | 437.06 |
| 6 | 6 | completed | 0/0 | 0 | 387.41 |

## Directory Structure

```
702576f4-1f68-4f60-8dde-a12dd3098efa/
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
