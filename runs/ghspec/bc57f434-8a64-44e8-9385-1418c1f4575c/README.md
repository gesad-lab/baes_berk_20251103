# Run Summary

**Run ID**: bc57f434-8a64-44e8-9385-1418c1f4575c
**Framework**: ghspec
**Started**: 2025-10-30T23:06:08.369506Z
**Completed**: 2025-10-30T23:28:12.053806Z
**Duration**: 1323.68s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 224.67 |
| 2 | 2 | completed | 0/0 | 0 | 191.01 |
| 3 | 3 | completed | 0/0 | 0 | 300.62 |
| 4 | 4 | completed | 0/0 | 0 | 319.89 |
| 5 | 5 | completed | 0/0 | 0 | 144.03 |
| 6 | 6 | completed | 0/0 | 0 | 143.46 |

## Directory Structure

```
bc57f434-8a64-44e8-9385-1418c1f4575c/
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
