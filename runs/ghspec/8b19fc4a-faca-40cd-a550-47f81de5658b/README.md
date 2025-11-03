# Run Summary

**Run ID**: 8b19fc4a-faca-40cd-a550-47f81de5658b
**Framework**: ghspec
**Started**: 2025-10-28T23:51:54.470772Z
**Completed**: 2025-10-29T00:04:04.422769Z
**Duration**: 729.95s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 128.31 |
| 2 | 2 | completed | 0/0 | 0 | 98.07 |
| 3 | 3 | completed | 0/0 | 0 | 87.25 |
| 4 | 4 | completed | 0/0 | 0 | 166.69 |
| 5 | 5 | completed | 0/0 | 0 | 132.86 |
| 6 | 6 | completed | 0/0 | 0 | 116.76 |

## Directory Structure

```
8b19fc4a-faca-40cd-a550-47f81de5658b/
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
