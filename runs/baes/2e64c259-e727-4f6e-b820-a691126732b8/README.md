# Run Summary

**Run ID**: 2e64c259-e727-4f6e-b820-a691126732b8
**Framework**: baes
**Started**: 2025-10-28T17:16:44.457881Z
**Completed**: 2025-10-28T17:20:58.089016Z
**Duration**: 253.63s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 20.57 |
| 2 | 2 | completed | 0/0 | 0 | 27.45 |
| 3 | 3 | completed | 0/0 | 0 | 49.33 |
| 4 | 4 | completed | 0/0 | 0 | 40.29 |
| 5 | 5 | completed | 0/0 | 0 | 39.82 |
| 6 | 6 | completed | 0/0 | 0 | 76.15 |

## Directory Structure

```
2e64c259-e727-4f6e-b820-a691126732b8/
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
