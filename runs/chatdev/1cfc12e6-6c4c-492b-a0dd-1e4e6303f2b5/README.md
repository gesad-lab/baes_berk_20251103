# Run Summary

**Run ID**: 1cfc12e6-6c4c-492b-a0dd-1e4e6303f2b5
**Framework**: chatdev
**Started**: 2025-10-29T10:25:25.525231Z
**Completed**: 2025-10-29T10:53:45.047756Z
**Duration**: 1699.52s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 227.63 |
| 2 | 2 | completed | 0/0 | 0 | 190.62 |
| 3 | 3 | completed | 0/0 | 0 | 191.95 |
| 4 | 4 | completed | 0/0 | 0 | 300.80 |
| 5 | 5 | completed | 0/0 | 0 | 387.97 |
| 6 | 6 | completed | 0/0 | 0 | 400.53 |

## Directory Structure

```
1cfc12e6-6c4c-492b-a0dd-1e4e6303f2b5/
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
