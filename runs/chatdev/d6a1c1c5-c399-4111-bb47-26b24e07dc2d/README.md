# Run Summary

**Run ID**: d6a1c1c5-c399-4111-bb47-26b24e07dc2d
**Framework**: chatdev
**Started**: 2025-10-31T02:14:34.349664Z
**Completed**: 2025-10-31T02:35:41.639858Z
**Duration**: 1267.29s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 194.72 |
| 2 | 2 | completed | 0/0 | 0 | 126.02 |
| 3 | 3 | completed | 0/0 | 0 | 201.78 |
| 4 | 4 | completed | 0/0 | 0 | 188.15 |
| 5 | 5 | completed | 0/0 | 0 | 385.82 |
| 6 | 6 | completed | 0/0 | 0 | 170.79 |

## Directory Structure

```
d6a1c1c5-c399-4111-bb47-26b24e07dc2d/
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
