# Run Summary

**Run ID**: 8904dd77-85ad-4216-af8b-4569b505c854
**Framework**: chatdev
**Started**: 2025-10-31T01:38:48.174929Z
**Completed**: 2025-10-31T01:55:15.852394Z
**Duration**: 987.68s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 146.05 |
| 2 | 2 | completed | 0/0 | 0 | 125.87 |
| 3 | 3 | completed | 0/0 | 0 | 164.97 |
| 4 | 4 | completed | 0/0 | 0 | 208.05 |
| 5 | 5 | completed | 0/0 | 0 | 178.55 |
| 6 | 6 | completed | 0/0 | 0 | 164.18 |

## Directory Structure

```
8904dd77-85ad-4216-af8b-4569b505c854/
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
