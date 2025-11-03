# Run Summary

**Run ID**: 9b53a5b0-40ec-4d68-8858-83b90c194547
**Framework**: chatdev
**Started**: 2025-10-31T13:47:47.452231Z
**Completed**: 2025-10-31T14:20:31.538927Z
**Duration**: 1964.09s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 240.82 |
| 2 | 2 | completed | 0/0 | 0 | 258.06 |
| 3 | 3 | completed | 0/0 | 0 | 269.40 |
| 4 | 4 | completed | 0/0 | 0 | 325.42 |
| 5 | 5 | completed | 0/0 | 0 | 454.43 |
| 6 | 6 | completed | 0/0 | 0 | 415.84 |

## Directory Structure

```
9b53a5b0-40ec-4d68-8858-83b90c194547/
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
