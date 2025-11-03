# Run Summary

**Run ID**: a0f5c853-9bab-4920-8506-00e1eead2a76
**Framework**: chatdev
**Started**: 2025-10-29T17:33:33.391964Z
**Completed**: 2025-10-29T18:04:40.342155Z
**Duration**: 1866.95s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 215.40 |
| 2 | 2 | completed | 0/0 | 0 | 226.96 |
| 3 | 3 | completed | 0/0 | 0 | 292.48 |
| 4 | 4 | completed | 0/0 | 0 | 370.42 |
| 5 | 5 | completed | 0/0 | 0 | 375.00 |
| 6 | 6 | completed | 0/0 | 0 | 386.69 |

## Directory Structure

```
a0f5c853-9bab-4920-8506-00e1eead2a76/
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
