# Run Summary

**Run ID**: 4ba9da38-d3f9-4e55-be50-9d8a56c7594e
**Framework**: chatdev
**Started**: 2025-10-31T04:27:28.350779Z
**Completed**: 2025-10-31T04:33:02.671935Z
**Duration**: 334.32s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 330.84 |
| 2 | 2 | completed | 0/0 | 0 | 0.69 |
| 3 | 3 | completed | 0/0 | 0 | 0.69 |
| 4 | 4 | completed | 0/0 | 0 | 0.70 |
| 5 | 5 | completed | 0/0 | 0 | 0.70 |
| 6 | 6 | completed | 0/0 | 0 | 0.69 |

## Directory Structure

```
4ba9da38-d3f9-4e55-be50-9d8a56c7594e/
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
