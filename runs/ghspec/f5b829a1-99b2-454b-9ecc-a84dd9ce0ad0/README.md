# Run Summary

**Run ID**: f5b829a1-99b2-454b-9ecc-a84dd9ce0ad0
**Framework**: ghspec
**Started**: 2025-10-29T20:56:33.877778Z
**Completed**: 2025-10-29T21:16:07.113633Z
**Duration**: 1173.24s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 261.86 |
| 2 | 2 | completed | 0/0 | 0 | 170.04 |
| 3 | 3 | completed | 0/0 | 0 | 166.48 |
| 4 | 4 | completed | 0/0 | 0 | 206.57 |
| 5 | 5 | completed | 0/0 | 0 | 183.32 |
| 6 | 6 | completed | 0/0 | 0 | 184.97 |

## Directory Structure

```
f5b829a1-99b2-454b-9ecc-a84dd9ce0ad0/
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
