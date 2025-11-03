# Run Summary

**Run ID**: e4de5d81-a861-4e63-ae29-724ebf6855b2
**Framework**: chatdev
**Started**: 2025-10-30T15:11:54.380345Z
**Completed**: 2025-10-30T15:39:49.560140Z
**Duration**: 1675.18s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 158.26 |
| 2 | 2 | completed | 0/0 | 0 | 156.87 |
| 3 | 3 | completed | 0/0 | 0 | 315.90 |
| 4 | 4 | completed | 0/0 | 0 | 347.55 |
| 5 | 5 | completed | 0/0 | 0 | 380.93 |
| 6 | 6 | completed | 0/0 | 0 | 315.67 |

## Directory Structure

```
e4de5d81-a861-4e63-ae29-724ebf6855b2/
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
