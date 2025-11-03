# Run Summary

**Run ID**: 70eb9c5c-bfd2-4b92-9b1f-e3d81e95714f
**Framework**: chatdev
**Started**: 2025-10-29T19:56:26.943125Z
**Completed**: 2025-10-29T20:18:08.291276Z
**Duration**: 1301.35s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 217.74 |
| 2 | 2 | completed | 0/0 | 0 | 210.73 |
| 3 | 3 | completed | 0/0 | 0 | 242.97 |
| 4 | 4 | completed | 0/0 | 0 | 227.58 |
| 5 | 5 | completed | 0/0 | 0 | 185.92 |
| 6 | 6 | completed | 0/0 | 0 | 216.38 |

## Directory Structure

```
70eb9c5c-bfd2-4b92-9b1f-e3d81e95714f/
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
