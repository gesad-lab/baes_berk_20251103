# Run Summary

**Run ID**: be8af0b7-53a6-44be-a1ca-8ceaaca27839
**Framework**: chatdev
**Started**: 2025-10-29T11:58:57.969886Z
**Completed**: 2025-10-29T12:20:10.494144Z
**Duration**: 1272.52s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 180.43 |
| 2 | 2 | completed | 0/0 | 0 | 219.38 |
| 3 | 3 | completed | 0/0 | 0 | 173.54 |
| 4 | 4 | completed | 0/0 | 0 | 217.03 |
| 5 | 5 | completed | 0/0 | 0 | 199.63 |
| 6 | 6 | completed | 0/0 | 0 | 282.52 |

## Directory Structure

```
be8af0b7-53a6-44be-a1ca-8ceaaca27839/
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
