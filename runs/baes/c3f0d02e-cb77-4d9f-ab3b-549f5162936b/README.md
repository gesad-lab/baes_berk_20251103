# Run Summary

**Run ID**: c3f0d02e-cb77-4d9f-ab3b-549f5162936b
**Framework**: baes
**Started**: 2025-10-30T01:07:46.669778Z
**Completed**: 2025-10-30T01:10:24.823015Z
**Duration**: 158.15s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 19.43 |
| 2 | 2 | completed | 0/0 | 0 | 19.76 |
| 3 | 3 | completed | 0/0 | 0 | 29.92 |
| 4 | 4 | completed | 0/0 | 0 | 32.15 |
| 5 | 5 | completed | 0/0 | 0 | 27.23 |
| 6 | 6 | completed | 0/0 | 0 | 29.65 |

## Directory Structure

```
c3f0d02e-cb77-4d9f-ab3b-549f5162936b/
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
