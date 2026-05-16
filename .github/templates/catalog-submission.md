### Extension ID

$EXT_ID

### Extension Name

$EXT_NAME

### Version

$VERSION

### Description

$EXT_DESCRIPTION

### Author

$EXT_AUTHOR

### Repository URL

<$EXT_REPOSITORY>

### Download URL

$DOWNLOAD_URL

### License

$EXT_LICENSE

### Homepage (optional)

<$EXT_HOMEPAGE>

### Documentation URL (optional)

<$EXT_DOCUMENTATION>

### Changelog URL (optional)

<$EXT_CHANGELOG>

### Required Spec Kit Version

$SPECKIT_VERSION

### Required Tools (optional)

$REQUIRED_TOOLS

### Number of Commands

$COMMANDS_COUNT

### Number of Hooks (optional)

$HOOKS_COUNT

### Tags

$TAGS

### Key Features

$KEY_FEATURES

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

Tested on macOS with Spec Kit $SPECKIT_VERSION. Commands tested: $COMMANDS_LIST.

### Example Usage

```bash
# Install the extension
specify extension add $EXT_ID --from $DOWNLOAD_URL

$COMMANDS_USAGE
```

### Proposed Catalog Entry

```json
{
  "$EXT_ID": {
    "name": "$EXT_NAME",
    "id": "$EXT_ID",
    "description": "$EXT_DESCRIPTION",
    "author": "$EXT_AUTHOR",
    "version": "$VERSION",
    "download_url": "$DOWNLOAD_URL",
    "repository": "$EXT_REPOSITORY",
    "homepage": "$EXT_HOMEPAGE",
    "documentation": "$EXT_DOCUMENTATION",
    "changelog": "$EXT_CHANGELOG",
    "license": "$EXT_LICENSE",
    "requires": {
      "speckit_version": "$SPECKIT_VERSION"
    },
    "provides": {
      "commands": $COMMANDS_COUNT,
      "hooks": $HOOKS_COUNT
    },
    "tags": $TAGS_JSON,
    "verified": false,
    "downloads": 0,
    "stars": 0,
    "created_at": "$DATE",
    "updated_at": "$DATE"
  }
}
```

### Additional Context

Automated submission opened by the [catalog-submit workflow]($EXT_REPOSITORY/actions/workflows/catalog-submit.yml) on release of v$VERSION. If an entry for `$EXT_ID` already exists in the catalog, please treat this as a version update.
