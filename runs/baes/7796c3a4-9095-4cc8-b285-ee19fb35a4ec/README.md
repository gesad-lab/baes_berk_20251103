# Run Summary

**Run ID**: 7796c3a4-9095-4cc8-b285-ee19fb35a4ec
**Framework**: baes
**Started**: 2025-10-29T07:10:43.716131Z
**Completed**: 2025-10-29T07:14:42.525911Z
**Duration**: 238.81s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 33.04 |
| 2 | 2 | completed | 0/0 | 0 | 58.65 |
| 3 | 3 | completed | 0/0 | 0 | 35.85 |
| 4 | 4 | completed | 0/0 | 0 | 32.20 |
| 5 | 5 | completed | 0/0 | 0 | 39.29 |
| 6 | 6 | completed | 0/0 | 0 | 39.76 |

## Directory Structure

```
7796c3a4-9095-4cc8-b285-ee19fb35a4ec/
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
