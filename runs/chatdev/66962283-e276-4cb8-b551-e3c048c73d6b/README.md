# Run Summary

**Run ID**: 66962283-e276-4cb8-b551-e3c048c73d6b
**Framework**: chatdev
**Started**: 2025-10-31T05:19:34.875066Z
**Completed**: 2025-10-31T05:25:08.284331Z
**Duration**: 333.41s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 329.92 |
| 2 | 2 | completed | 0/0 | 0 | 0.70 |
| 3 | 3 | completed | 0/0 | 0 | 0.69 |
| 4 | 4 | completed | 0/0 | 0 | 0.69 |
| 5 | 5 | completed | 0/0 | 0 | 0.70 |
| 6 | 6 | completed | 0/0 | 0 | 0.69 |

## Directory Structure

```
66962283-e276-4cb8-b551-e3c048c73d6b/
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
