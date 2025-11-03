# Run Summary

**Run ID**: 2ca663ea-f8b5-4f4a-ac23-75d722a1d9f2
**Framework**: baes
**Started**: 2025-10-29T15:22:05.948710Z
**Completed**: 2025-10-29T15:25:13.980298Z
**Duration**: 188.03s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 22.55 |
| 2 | 2 | completed | 0/0 | 0 | 20.06 |
| 3 | 3 | completed | 0/0 | 0 | 35.99 |
| 4 | 4 | completed | 0/0 | 0 | 31.83 |
| 5 | 5 | completed | 0/0 | 0 | 38.13 |
| 6 | 6 | completed | 0/0 | 0 | 39.47 |

## Directory Structure

```
2ca663ea-f8b5-4f4a-ac23-75d722a1d9f2/
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
