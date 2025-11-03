# Run Summary

**Run ID**: 3ee8e3f7-8416-4161-8d9d-0daca9379516
**Framework**: chatdev
**Started**: 2025-10-28T12:12:56.307132Z
**Completed**: 2025-10-28T12:30:52.354163Z
**Duration**: 1076.05s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 180.24 |
| 2 | 2 | completed | 0/0 | 0 | 144.39 |
| 3 | 3 | completed | 0/0 | 0 | 159.07 |
| 4 | 4 | completed | 0/0 | 0 | 194.51 |
| 5 | 5 | completed | 0/0 | 0 | 177.90 |
| 6 | 6 | completed | 0/0 | 0 | 219.93 |

## Directory Structure

```
3ee8e3f7-8416-4161-8d9d-0daca9379516/
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
