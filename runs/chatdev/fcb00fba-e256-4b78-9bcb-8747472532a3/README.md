# Run Summary

**Run ID**: fcb00fba-e256-4b78-9bcb-8747472532a3
**Framework**: chatdev
**Started**: 2025-10-31T18:07:33.614893Z
**Completed**: 2025-10-31T18:24:34.804479Z
**Duration**: 1021.19s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 145.38 |
| 2 | 2 | completed | 0/0 | 0 | 125.62 |
| 3 | 3 | completed | 0/0 | 0 | 144.97 |
| 4 | 4 | completed | 0/0 | 0 | 173.39 |
| 5 | 5 | completed | 0/0 | 0 | 225.69 |
| 6 | 6 | completed | 0/0 | 0 | 206.14 |

## Directory Structure

```
fcb00fba-e256-4b78-9bcb-8747472532a3/
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
