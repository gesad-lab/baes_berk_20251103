# Run Summary

**Run ID**: 674e9311-8184-410c-a723-15418dde63da
**Framework**: ghspec
**Started**: 2025-10-30T20:51:34.186373Z
**Completed**: 2025-10-30T21:09:42.883922Z
**Duration**: 1088.70s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 268.27 |
| 2 | 2 | completed | 0/0 | 0 | 120.59 |
| 3 | 3 | completed | 0/0 | 0 | 149.51 |
| 4 | 4 | completed | 0/0 | 0 | 158.22 |
| 5 | 5 | completed | 0/0 | 0 | 214.53 |
| 6 | 6 | completed | 0/0 | 0 | 177.57 |

## Directory Structure

```
674e9311-8184-410c-a723-15418dde63da/
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
