# Run Summary

**Run ID**: 9741b2ce-31ad-4d15-9df3-4d91b07c185a
**Framework**: baes
**Started**: 2025-10-29T12:39:08.963658Z
**Completed**: 2025-10-29T12:42:05.939747Z
**Duration**: 176.98s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 22.17 |
| 2 | 2 | completed | 0/0 | 0 | 20.95 |
| 3 | 3 | completed | 0/0 | 0 | 29.70 |
| 4 | 4 | completed | 0/0 | 0 | 40.77 |
| 5 | 5 | completed | 0/0 | 0 | 29.53 |
| 6 | 6 | completed | 0/0 | 0 | 33.84 |

## Directory Structure

```
9741b2ce-31ad-4d15-9df3-4d91b07c185a/
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
