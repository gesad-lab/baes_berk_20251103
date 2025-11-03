# Run Summary

**Run ID**: 8c20554f-2b6e-4634-97d4-423c81d22293
**Framework**: chatdev
**Started**: 2025-10-29T03:32:32.001252Z
**Completed**: 2025-10-29T03:48:19.287446Z
**Duration**: 947.29s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 92.82 |
| 2 | 2 | completed | 0/0 | 0 | 167.50 |
| 3 | 3 | completed | 0/0 | 0 | 109.99 |
| 4 | 4 | completed | 0/0 | 0 | 134.84 |
| 5 | 5 | completed | 0/0 | 0 | 263.26 |
| 6 | 6 | completed | 0/0 | 0 | 178.88 |

## Directory Structure

```
8c20554f-2b6e-4634-97d4-423c81d22293/
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
