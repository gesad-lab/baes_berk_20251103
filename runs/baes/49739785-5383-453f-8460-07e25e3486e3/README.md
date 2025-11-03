# Run Summary

**Run ID**: 49739785-5383-453f-8460-07e25e3486e3
**Framework**: baes
**Started**: 2025-10-29T02:01:53.820063Z
**Completed**: 2025-10-29T02:04:34.846720Z
**Duration**: 161.03s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 25.16 |
| 2 | 2 | completed | 0/0 | 0 | 38.24 |
| 3 | 3 | completed | 0/0 | 0 | 22.89 |
| 4 | 4 | completed | 0/0 | 0 | 22.66 |
| 5 | 5 | completed | 0/0 | 0 | 22.44 |
| 6 | 6 | completed | 0/0 | 0 | 29.63 |

## Directory Structure

```
49739785-5383-453f-8460-07e25e3486e3/
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
