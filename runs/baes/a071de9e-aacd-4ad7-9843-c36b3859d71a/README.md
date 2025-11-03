# Run Summary

**Run ID**: a071de9e-aacd-4ad7-9843-c36b3859d71a
**Framework**: baes
**Started**: 2025-10-29T14:34:09.685049Z
**Completed**: 2025-10-29T14:37:41.953152Z
**Duration**: 212.27s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 21.15 |
| 2 | 2 | completed | 0/0 | 0 | 64.80 |
| 3 | 3 | completed | 0/0 | 0 | 33.37 |
| 4 | 4 | completed | 0/0 | 0 | 22.60 |
| 5 | 5 | completed | 0/0 | 0 | 30.36 |
| 6 | 6 | completed | 0/0 | 0 | 39.98 |

## Directory Structure

```
a071de9e-aacd-4ad7-9843-c36b3859d71a/
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
