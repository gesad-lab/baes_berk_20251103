# Run Summary

**Run ID**: 7044ecc8-47c9-4346-b354-2ec307fd20ca
**Framework**: baes
**Started**: 2025-10-30T07:59:02.015604Z
**Completed**: 2025-10-30T08:02:31.577887Z
**Duration**: 209.56s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 27.47 |
| 2 | 2 | completed | 0/0 | 0 | 44.99 |
| 3 | 3 | completed | 0/0 | 0 | 32.42 |
| 4 | 4 | completed | 0/0 | 0 | 34.11 |
| 5 | 5 | completed | 0/0 | 0 | 32.54 |
| 6 | 6 | completed | 0/0 | 0 | 38.03 |

## Directory Structure

```
7044ecc8-47c9-4346-b354-2ec307fd20ca/
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
