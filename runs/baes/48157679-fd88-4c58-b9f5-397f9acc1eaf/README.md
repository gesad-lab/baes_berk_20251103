# Run Summary

**Run ID**: 48157679-fd88-4c58-b9f5-397f9acc1eaf
**Framework**: baes
**Started**: 2025-10-29T02:33:59.895797Z
**Completed**: 2025-10-29T02:36:25.463458Z
**Duration**: 145.57s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 19.84 |
| 2 | 2 | completed | 0/0 | 0 | 22.15 |
| 3 | 3 | completed | 0/0 | 0 | 38.45 |
| 4 | 4 | completed | 0/0 | 0 | 21.18 |
| 5 | 5 | completed | 0/0 | 0 | 20.26 |
| 6 | 6 | completed | 0/0 | 0 | 23.68 |

## Directory Structure

```
48157679-fd88-4c58-b9f5-397f9acc1eaf/
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
