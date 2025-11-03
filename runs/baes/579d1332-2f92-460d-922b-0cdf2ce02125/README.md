# Run Summary

**Run ID**: 579d1332-2f92-460d-922b-0cdf2ce02125
**Framework**: baes
**Started**: 2025-10-30T22:04:26.199519Z
**Completed**: 2025-10-30T22:07:51.463354Z
**Duration**: 205.26s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 31.00 |
| 2 | 2 | completed | 0/0 | 0 | 33.76 |
| 3 | 3 | completed | 0/0 | 0 | 31.25 |
| 4 | 4 | completed | 0/0 | 0 | 42.82 |
| 5 | 5 | completed | 0/0 | 0 | 30.05 |
| 6 | 6 | completed | 0/0 | 0 | 36.37 |

## Directory Structure

```
579d1332-2f92-460d-922b-0cdf2ce02125/
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
