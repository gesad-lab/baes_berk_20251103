# Run Summary

**Run ID**: 166ef4de-9ddf-4602-8da5-40f9f8912573
**Framework**: baes
**Started**: 2025-10-29T22:38:36.775024Z
**Completed**: 2025-10-29T22:41:37.333626Z
**Duration**: 180.56s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 16.93 |
| 2 | 2 | completed | 0/0 | 0 | 37.23 |
| 3 | 3 | completed | 0/0 | 0 | 31.48 |
| 4 | 4 | completed | 0/0 | 0 | 26.73 |
| 5 | 5 | completed | 0/0 | 0 | 32.24 |
| 6 | 6 | completed | 0/0 | 0 | 35.94 |

## Directory Structure

```
166ef4de-9ddf-4602-8da5-40f9f8912573/
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
