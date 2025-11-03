# Run Summary

**Run ID**: a54d9700-d71a-4f9c-ae43-73a4bab473d3
**Framework**: baes
**Started**: 2025-10-29T13:07:57.596566Z
**Completed**: 2025-10-29T13:11:40.069673Z
**Duration**: 222.47s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 35.86 |
| 2 | 2 | completed | 0/0 | 0 | 39.46 |
| 3 | 3 | completed | 0/0 | 0 | 41.11 |
| 4 | 4 | completed | 0/0 | 0 | 26.65 |
| 5 | 5 | completed | 0/0 | 0 | 40.98 |
| 6 | 6 | completed | 0/0 | 0 | 38.41 |

## Directory Structure

```
a54d9700-d71a-4f9c-ae43-73a4bab473d3/
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
