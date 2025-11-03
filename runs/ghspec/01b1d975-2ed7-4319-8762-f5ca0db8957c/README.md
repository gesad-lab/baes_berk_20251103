# Run Summary

**Run ID**: 01b1d975-2ed7-4319-8762-f5ca0db8957c
**Framework**: ghspec
**Started**: 2025-10-31T11:45:07.628416Z
**Completed**: 2025-10-31T12:04:09.387194Z
**Duration**: 1141.76s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 164.95 |
| 2 | 2 | completed | 0/0 | 0 | 106.09 |
| 3 | 3 | completed | 0/0 | 0 | 172.03 |
| 4 | 4 | completed | 0/0 | 0 | 211.39 |
| 5 | 5 | completed | 0/0 | 0 | 252.10 |
| 6 | 6 | completed | 0/0 | 0 | 235.20 |

## Directory Structure

```
01b1d975-2ed7-4319-8762-f5ca0db8957c/
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
