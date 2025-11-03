# Run Summary

**Run ID**: 0f70200b-e6b3-46a6-bce5-843f55c3005b
**Framework**: ghspec
**Started**: 2025-10-29T16:29:48.272279Z
**Completed**: 2025-10-29T16:47:08.875080Z
**Duration**: 1040.60s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 181.58 |
| 2 | 2 | completed | 0/0 | 0 | 163.00 |
| 3 | 3 | completed | 0/0 | 0 | 119.15 |
| 4 | 4 | completed | 0/0 | 0 | 228.30 |
| 5 | 5 | completed | 0/0 | 0 | 189.94 |
| 6 | 6 | completed | 0/0 | 0 | 158.62 |

## Directory Structure

```
0f70200b-e6b3-46a6-bce5-843f55c3005b/
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
