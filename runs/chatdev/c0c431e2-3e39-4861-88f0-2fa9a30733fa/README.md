# Run Summary

**Run ID**: c0c431e2-3e39-4861-88f0-2fa9a30733fa
**Framework**: chatdev
**Started**: 2025-10-29T05:40:36.032402Z
**Completed**: 2025-10-29T06:07:07.498371Z
**Duration**: 1591.47s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 215.01 |
| 2 | 2 | completed | 0/0 | 0 | 228.31 |
| 3 | 3 | completed | 0/0 | 0 | 211.61 |
| 4 | 4 | completed | 0/0 | 0 | 293.46 |
| 5 | 5 | completed | 0/0 | 0 | 319.12 |
| 6 | 6 | completed | 0/0 | 0 | 323.94 |

## Directory Structure

```
c0c431e2-3e39-4861-88f0-2fa9a30733fa/
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
