# Run Summary

**Run ID**: e648d2d3-34c6-4de9-84de-c813f7cad22f
**Framework**: baes
**Started**: 2025-10-29T10:21:20.376081Z
**Completed**: 2025-10-29T10:25:20.613852Z
**Duration**: 240.24s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 33.70 |
| 2 | 2 | completed | 0/0 | 0 | 46.81 |
| 3 | 3 | completed | 0/0 | 0 | 45.85 |
| 4 | 4 | completed | 0/0 | 0 | 37.14 |
| 5 | 5 | completed | 0/0 | 0 | 37.38 |
| 6 | 6 | completed | 0/0 | 0 | 39.36 |

## Directory Structure

```
e648d2d3-34c6-4de9-84de-c813f7cad22f/
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
