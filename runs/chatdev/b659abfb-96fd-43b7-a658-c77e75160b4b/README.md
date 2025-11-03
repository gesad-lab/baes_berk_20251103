# Run Summary

**Run ID**: b659abfb-96fd-43b7-a658-c77e75160b4b
**Framework**: chatdev
**Started**: 2025-10-29T21:19:04.489501Z
**Completed**: 2025-10-29T21:37:22.083918Z
**Duration**: 1097.59s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 186.56 |
| 2 | 2 | completed | 0/0 | 0 | 145.13 |
| 3 | 3 | completed | 0/0 | 0 | 170.76 |
| 4 | 4 | completed | 0/0 | 0 | 168.77 |
| 5 | 5 | completed | 0/0 | 0 | 202.81 |
| 6 | 6 | completed | 0/0 | 0 | 223.55 |

## Directory Structure

```
b659abfb-96fd-43b7-a658-c77e75160b4b/
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
