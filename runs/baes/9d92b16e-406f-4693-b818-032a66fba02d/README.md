# Run Summary

**Run ID**: 9d92b16e-406f-4693-b818-032a66fba02d
**Framework**: baes
**Started**: 2025-10-28T12:09:06.171212Z
**Completed**: 2025-10-28T12:12:51.966953Z
**Duration**: 225.80s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 34.01 |
| 2 | 2 | completed | 0/0 | 0 | 41.99 |
| 3 | 3 | completed | 0/0 | 0 | 35.22 |
| 4 | 4 | completed | 0/0 | 0 | 40.34 |
| 5 | 5 | completed | 0/0 | 0 | 33.86 |
| 6 | 6 | completed | 0/0 | 0 | 40.37 |

## Directory Structure

```
9d92b16e-406f-4693-b818-032a66fba02d/
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
