# Run Summary

**Run ID**: 9f712214-24c3-4a5c-ad83-5e52d2ff7eaa
**Framework**: chatdev
**Started**: 2025-10-30T04:48:02.039691Z
**Completed**: 2025-10-30T05:17:20.283113Z
**Duration**: 1758.24s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 242.01 |
| 2 | 2 | completed | 0/0 | 0 | 207.06 |
| 3 | 3 | completed | 0/0 | 0 | 304.62 |
| 4 | 4 | completed | 0/0 | 0 | 317.94 |
| 5 | 5 | completed | 0/0 | 0 | 369.21 |
| 6 | 6 | completed | 0/0 | 0 | 317.40 |

## Directory Structure

```
9f712214-24c3-4a5c-ad83-5e52d2ff7eaa/
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
