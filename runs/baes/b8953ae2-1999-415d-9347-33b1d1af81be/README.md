# Run Summary

**Run ID**: b8953ae2-1999-415d-9347-33b1d1af81be
**Framework**: baes
**Started**: 2025-10-31T04:08:17.773006Z
**Completed**: 2025-10-31T04:14:31.203732Z
**Duration**: 373.43s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 63.39 |
| 2 | 2 | completed | 0/0 | 0 | 62.98 |
| 3 | 3 | completed | 0/0 | 0 | 62.06 |
| 4 | 4 | completed | 0/0 | 0 | 58.86 |
| 5 | 5 | completed | 0/0 | 0 | 63.23 |
| 6 | 6 | completed | 0/0 | 0 | 62.90 |

## Directory Structure

```
b8953ae2-1999-415d-9347-33b1d1af81be/
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
