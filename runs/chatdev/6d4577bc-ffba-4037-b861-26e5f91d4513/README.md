# Run Summary

**Run ID**: 6d4577bc-ffba-4037-b861-26e5f91d4513
**Framework**: chatdev
**Started**: 2025-10-30T07:22:06.138953Z
**Completed**: 2025-10-30T07:38:54.991356Z
**Duration**: 1008.85s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 122.78 |
| 2 | 2 | completed | 0/0 | 0 | 165.59 |
| 3 | 3 | completed | 0/0 | 0 | 149.45 |
| 4 | 4 | completed | 0/0 | 0 | 180.68 |
| 5 | 5 | completed | 0/0 | 0 | 204.81 |
| 6 | 6 | completed | 0/0 | 0 | 185.53 |

## Directory Structure

```
6d4577bc-ffba-4037-b861-26e5f91d4513/
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
