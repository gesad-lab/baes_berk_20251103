# Run Summary

**Run ID**: aaa4c4c4-fa0b-4969-b933-726e24903eae
**Framework**: ghspec
**Started**: 2025-10-31T12:26:58.453264Z
**Completed**: 2025-10-31T12:52:02.368078Z
**Duration**: 1503.91s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 356.52 |
| 2 | 2 | completed | 0/0 | 0 | 158.61 |
| 3 | 3 | completed | 0/0 | 0 | 223.20 |
| 4 | 4 | completed | 0/0 | 0 | 295.73 |
| 5 | 5 | completed | 0/0 | 0 | 259.76 |
| 6 | 6 | completed | 0/0 | 0 | 210.08 |

## Directory Structure

```
aaa4c4c4-fa0b-4969-b933-726e24903eae/
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
