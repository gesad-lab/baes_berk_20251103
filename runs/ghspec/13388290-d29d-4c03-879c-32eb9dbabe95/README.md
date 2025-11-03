# Run Summary

**Run ID**: 13388290-d29d-4c03-879c-32eb9dbabe95
**Framework**: ghspec
**Started**: 2025-10-29T00:19:00.374475Z
**Completed**: 2025-10-29T00:32:29.502579Z
**Duration**: 809.13s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 109.86 |
| 2 | 2 | completed | 0/0 | 0 | 104.60 |
| 3 | 3 | completed | 0/0 | 0 | 161.18 |
| 4 | 4 | completed | 0/0 | 0 | 208.02 |
| 5 | 5 | completed | 0/0 | 0 | 111.36 |
| 6 | 6 | completed | 0/0 | 0 | 114.11 |

## Directory Structure

```
13388290-d29d-4c03-879c-32eb9dbabe95/
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
