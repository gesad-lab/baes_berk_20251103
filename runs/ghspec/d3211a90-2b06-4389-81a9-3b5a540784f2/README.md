# Run Summary

**Run ID**: d3211a90-2b06-4389-81a9-3b5a540784f2
**Framework**: ghspec
**Started**: 2025-10-29T15:50:11.831791Z
**Completed**: 2025-10-29T16:09:08.927336Z
**Duration**: 1137.10s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 167.07 |
| 2 | 2 | completed | 0/0 | 0 | 212.35 |
| 3 | 3 | completed | 0/0 | 0 | 157.17 |
| 4 | 4 | completed | 0/0 | 0 | 219.57 |
| 5 | 5 | completed | 0/0 | 0 | 196.61 |
| 6 | 6 | completed | 0/0 | 0 | 184.32 |

## Directory Structure

```
d3211a90-2b06-4389-81a9-3b5a540784f2/
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
