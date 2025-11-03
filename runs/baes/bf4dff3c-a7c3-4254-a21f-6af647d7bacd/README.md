# Run Summary

**Run ID**: bf4dff3c-a7c3-4254-a21f-6af647d7bacd
**Framework**: baes
**Started**: 2025-10-29T16:47:13.709513Z
**Completed**: 2025-10-29T16:50:06.904503Z
**Duration**: 173.19s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 29.38 |
| 2 | 2 | completed | 0/0 | 0 | 33.87 |
| 3 | 3 | completed | 0/0 | 0 | 27.90 |
| 4 | 4 | completed | 0/0 | 0 | 23.01 |
| 5 | 5 | completed | 0/0 | 0 | 28.40 |
| 6 | 6 | completed | 0/0 | 0 | 30.64 |

## Directory Structure

```
bf4dff3c-a7c3-4254-a21f-6af647d7bacd/
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
