# Run Summary

**Run ID**: 668b55d1-26f2-4430-b3dc-d556237c347f
**Framework**: chatdev
**Started**: 2025-10-30T01:53:08.198557Z
**Completed**: 2025-10-30T02:11:25.039245Z
**Duration**: 1096.84s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 235.24 |
| 2 | 2 | completed | 0/0 | 0 | 134.33 |
| 3 | 3 | completed | 0/0 | 0 | 162.87 |
| 4 | 4 | completed | 0/0 | 0 | 175.88 |
| 5 | 5 | completed | 0/0 | 0 | 191.32 |
| 6 | 6 | completed | 0/0 | 0 | 197.19 |

## Directory Structure

```
668b55d1-26f2-4430-b3dc-d556237c347f/
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
