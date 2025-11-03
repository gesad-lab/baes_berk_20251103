# Run Summary

**Run ID**: 2d0ae9b0-57ac-45b1-b89f-d625cf1b8a32
**Framework**: baes
**Started**: 2025-10-31T15:37:05.075750Z
**Completed**: 2025-10-31T15:40:20.616608Z
**Duration**: 195.54s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 34.91 |
| 2 | 2 | completed | 0/0 | 0 | 30.70 |
| 3 | 3 | completed | 0/0 | 0 | 32.86 |
| 4 | 4 | completed | 0/0 | 0 | 34.81 |
| 5 | 5 | completed | 0/0 | 0 | 28.62 |
| 6 | 6 | completed | 0/0 | 0 | 33.64 |

## Directory Structure

```
2d0ae9b0-57ac-45b1-b89f-d625cf1b8a32/
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
