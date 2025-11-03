# Run Summary

**Run ID**: f124940e-6d1e-40d3-8c1e-5f04421fc33e
**Framework**: ghspec
**Started**: 2025-10-29T10:53:46.311092Z
**Completed**: 2025-10-29T11:11:35.464395Z
**Duration**: 1069.15s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 134.22 |
| 2 | 2 | completed | 0/0 | 0 | 199.17 |
| 3 | 3 | completed | 0/0 | 0 | 223.30 |
| 4 | 4 | completed | 0/0 | 0 | 178.92 |
| 5 | 5 | completed | 0/0 | 0 | 167.21 |
| 6 | 6 | completed | 0/0 | 0 | 166.33 |

## Directory Structure

```
f124940e-6d1e-40d3-8c1e-5f04421fc33e/
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
