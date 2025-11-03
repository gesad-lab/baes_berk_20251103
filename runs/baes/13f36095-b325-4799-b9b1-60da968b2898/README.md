# Run Summary

**Run ID**: 13f36095-b325-4799-b9b1-60da968b2898
**Framework**: baes
**Started**: 2025-10-29T09:34:19.106570Z
**Completed**: 2025-10-29T09:38:13.946416Z
**Duration**: 234.84s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 39.64 |
| 2 | 2 | completed | 0/0 | 0 | 35.98 |
| 3 | 3 | completed | 0/0 | 0 | 57.63 |
| 4 | 4 | completed | 0/0 | 0 | 35.65 |
| 5 | 5 | completed | 0/0 | 0 | 30.61 |
| 6 | 6 | completed | 0/0 | 0 | 35.31 |

## Directory Structure

```
13f36095-b325-4799-b9b1-60da968b2898/
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
