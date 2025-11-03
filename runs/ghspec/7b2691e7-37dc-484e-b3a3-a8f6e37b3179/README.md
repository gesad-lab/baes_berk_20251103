# Run Summary

**Run ID**: 7b2691e7-37dc-484e-b3a3-a8f6e37b3179
**Framework**: ghspec
**Started**: 2025-10-29T06:43:58.039993Z
**Completed**: 2025-10-29T07:10:42.333838Z
**Duration**: 1604.29s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 255.07 |
| 2 | 2 | completed | 0/0 | 0 | 230.19 |
| 3 | 3 | completed | 0/0 | 0 | 283.75 |
| 4 | 4 | completed | 0/0 | 0 | 191.74 |
| 5 | 5 | completed | 0/0 | 0 | 247.98 |
| 6 | 6 | completed | 0/0 | 0 | 395.57 |

## Directory Structure

```
7b2691e7-37dc-484e-b3a3-a8f6e37b3179/
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
