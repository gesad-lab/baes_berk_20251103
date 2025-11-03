# Run Summary

**Run ID**: aefa06fe-b881-4f18-880d-a91155e72c09
**Framework**: chatdev
**Started**: 2025-10-29T15:25:16.085708Z
**Completed**: 2025-10-29T15:50:10.655387Z
**Duration**: 1494.57s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 243.75 |
| 2 | 2 | completed | 0/0 | 0 | 261.10 |
| 3 | 3 | completed | 0/0 | 0 | 225.04 |
| 4 | 4 | completed | 0/0 | 0 | 235.84 |
| 5 | 5 | completed | 0/0 | 0 | 224.27 |
| 6 | 6 | completed | 0/0 | 0 | 304.56 |

## Directory Structure

```
aefa06fe-b881-4f18-880d-a91155e72c09/
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
