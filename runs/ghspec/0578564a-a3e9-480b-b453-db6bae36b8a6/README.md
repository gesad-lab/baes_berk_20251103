# Run Summary

**Run ID**: 0578564a-a3e9-480b-b453-db6bae36b8a6
**Framework**: ghspec
**Started**: 2025-10-29T20:18:12.618589Z
**Completed**: 2025-10-29T20:34:46.879021Z
**Duration**: 994.26s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 137.16 |
| 2 | 2 | completed | 0/0 | 0 | 131.40 |
| 3 | 3 | completed | 0/0 | 0 | 119.81 |
| 4 | 4 | completed | 0/0 | 0 | 118.56 |
| 5 | 5 | completed | 0/0 | 0 | 319.05 |
| 6 | 6 | completed | 0/0 | 0 | 168.28 |

## Directory Structure

```
0578564a-a3e9-480b-b453-db6bae36b8a6/
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
