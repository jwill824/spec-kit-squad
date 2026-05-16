### Extension ID

squad

### Extension Name

Squad Bridge

### Version

$VERSION

### Description

Bootstrap and synchronize a Squad agent team from your Speckit spec and tasks.

### Author

jwill824

### Repository URL

<https://github.com/jwill824/spec-kit-squad>

### Download URL

$DOWNLOAD_URL

### License

MIT

### Homepage (optional)

<https://github.com/jwill824/spec-kit-squad>

### Documentation URL (optional)

<https://github.com/jwill824/spec-kit-squad/blob/main/README.md>

### Changelog URL (optional)

<https://github.com/jwill824/spec-kit-squad/blob/main/docs/CHANGELOG.md>

### Required Spec Kit Version

$SPECKIT_VERSION

### Required Tools (optional)

$REQUIRED_TOOLS

### Number of Commands

$COMMANDS_COUNT

### Number of Hooks (optional)

$HOOKS_COUNT

### Tags

multi-agent, agents, orchestration, process, integration

### Key Features

- Bootstrap a Squad agent team from your Speckit spec and tasks
- Generate agent configurations from spec requirements
- Route tasks to appropriate agents based on complexity tiers (full/standard/lightweight)
- Check status and health of your Squad team with `squad doctor`

### Testing Checklist

- [x] Extension installs successfully via download URL
- [x] All commands execute without errors
- [x] Documentation is complete and accurate
- [x] No security vulnerabilities identified
- [x] Tested on at least one real project

### Submission Requirements

- [x] Valid `extension.yml` manifest included
- [x] README.md with installation and usage instructions
- [x] LICENSE file included
- [x] GitHub release created with version tag
- [x] All command files exist and are properly formatted
- [x] Extension ID follows naming conventions (lowercase-with-hyphens)

### Testing Details

Tested on macOS with Spec Kit >=0.1.0. Commands tested: `/speckit.squad.init`, `/speckit.squad.generate`, `/speckit.squad.route`, `/speckit.squad.status`.

### Example Usage

```bash
# Install the extension
specify extension add squad --from $DOWNLOAD_URL

# Initialize a Squad team from your spec
# /speckit.squad.init

# Generate agent configs
# /speckit.squad.generate

# Route tasks to agents
# /speckit.squad.route

# Check Squad health
# /speckit.squad.status
```

### Proposed Catalog Entry

```json
{
  "squad": {
    "name": "Squad Bridge",
    "id": "squad",
    "description": "Bootstrap and synchronize a Squad agent team from your Speckit spec and tasks.",
    "author": "jwill824",
    "version": "$VERSION",
    "download_url": "$DOWNLOAD_URL",
    "repository": "https://github.com/jwill824/spec-kit-squad",
    "homepage": "https://github.com/jwill824/spec-kit-squad",
    "documentation": "https://github.com/jwill824/spec-kit-squad/blob/main/README.md",
    "changelog": "https://github.com/jwill824/spec-kit-squad/blob/main/docs/CHANGELOG.md",
    "license": "MIT",
    "requires": {
      "speckit_version": "$SPECKIT_VERSION"
    },
    "provides": {
      "commands": $COMMANDS_COUNT,
      "hooks": $HOOKS_COUNT
    },
    "tags": ["multi-agent", "agents", "orchestration", "process", "integration"],
    "verified": false,
    "downloads": 0,
    "stars": 0,
    "created_at": "$DATE",
    "updated_at": "$DATE"
  }
}
```

### Additional Context

Automated submission opened by the [catalog-submit workflow](https://github.com/jwill824/spec-kit-squad/actions/workflows/catalog-submit.yml) on release of v$VERSION. If an entry for `squad` already exists in the catalog, please treat this as a version update.
