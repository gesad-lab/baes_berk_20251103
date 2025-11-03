# Run Summary

**Run ID**: 48c1653d-323d-4e1d-95aa-ddea0b0454a8
**Framework**: chatdev
**Started**: 2025-10-31T16:36:06.108873Z
**Completed**: 2025-10-31T16:51:09.553522Z
**Duration**: 903.44s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 160.00 |
| 2 | 2 | completed | 0/0 | 0 | 121.88 |
| 3 | 3 | completed | 0/0 | 0 | 137.30 |
| 4 | 4 | completed | 0/0 | 0 | 174.18 |
| 5 | 5 | completed | 0/0 | 0 | 150.73 |
| 6 | 6 | completed | 0/0 | 0 | 159.34 |

## Directory Structure

```
48c1653d-323d-4e1d-95aa-ddea0b0454a8/
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
