# OPC Skills

OPC Skills is a library of reusable AI agent skills for solopreneurs, indie hackers, and one-person companies. Each skill extends AI agents with specialized capabilities through structured instructions and automation scripts.

## Core Commands

- **Lint**: `npm run lint` (website) / `python3 -m pylint skills/*/scripts/*.py` (skills)
- **Type-check**: `npm run typecheck` (website)
- **Test**: `npm run test` (website)
- **Dev**: `npm run dev` (website)
- **Build**: `npm run build` (website)
- **Publish**: See [Release Process](#release-process)

## Project Layout

```
├── skills/                    → Source skill implementations
│   ├── requesthunt/           → RequestHunt skill
│   ├── domain-hunter/         → Domain search & pricing
│   ├── logo-creator/          → Logo generation
│   ├── banner-creator/        → Banner creation
│   ├── nanobanana/            → Gemini image generation
│   ├── reddit/                → Reddit integration
│   ├── twitter/               → Twitter/X integration
│   ├── producthunt/           → Product Hunt integration
│   └── seo-geo/               → SEO & GEO optimization
├── .factory/skills/           → Installed skill versions
├── skills.json                → Global metadata and version registry
├── website/                   → Documentation website
├── CHANGELOG.md               → Version history
└── .factory/AGENTS.md         → This file
```

## Skill Structure

Each skill follows this standard structure:

```
skills/<skill-name>/
├── SKILL.md                   → Main skill documentation (required)
│   └── YAML frontmatter:
│       - name: skill identifier
│       - description: what it does
│       - triggers: activation keywords
│       - dependencies: required skills (e.g., ["twitter", "reddit"])
├── scripts/                   → Executable Python/Shell scripts
├── examples/                  → Usage examples
└── references/                → API docs and references
```

**SKILL.md** must include YAML frontmatter with these fields:
- `name`: Unique identifier (kebab-case)
- `description`: Clear description of functionality
- `triggers`: Keywords that activate the skill
- `dependencies`: List of required skill names (optional)

Example:
```yaml
---
name: domain-hunter
description: Search domains, compare registrar prices, and find promo codes
triggers:
  - domain
  - registrar
  - buy domain
dependencies:
  - twitter
  - reddit
---
```

## Skill Development Patterns

### Creating a New Skill

1. **Create skill directory**
   ```bash
   mkdir -p skills/your-skill-name/scripts
   ```

2. **Write SKILL.md** with proper YAML frontmatter and usage instructions

3. **Add Python/Shell scripts** in `scripts/` directory with clear CLI interfaces

4. **Include examples** in `examples/` directory showing real workflows

5. **Add references** in `references/` for API documentation and resources

### Skill Script Guidelines

- Use clear argument names and help text (`--help`)
- Output machine-readable formats (JSON for data, markdown for reports)
- Include error handling and meaningful error messages
- Document dependencies and environment variables required
- Use relative paths or `${SKILL_DIR}` for portability

### Dependencies & Composition

When a skill requires other skills:
- List them in SKILL.md `dependencies` field
- Document which skills and minimum versions are needed
- Users install dependencies via: `npx skills add ReScienceLab/opc-skills --skill <dependency>`

Example (from domain-hunter):
```yaml
dependencies:
  - twitter
  - reddit
```

## Versioning & Dependencies Strategy

### Semantic Versioning

All version numbers follow [Semantic Versioning](https://semver.org/):

```
MAJOR.MINOR.PATCH
- MAJOR: Breaking changes or API incompatibility
- MINOR: New features (backward compatible)
- PATCH: Bug fixes
```

### Individual Skill Versions

Each skill has its own version number in `skills.json`:

```json
{
  "name": "domain-hunter",
  "version": "1.0.0",
  "dependencies": ["twitter", "reddit"]
}
```

**Version updates:**
- Update version when skill functionality changes
- Update `skills.json` entry
- Add entry to `CHANGELOG.md` under the appropriate version

### Global Project Version

The root `version` in `skills.json` tracks the overall project:
- Updated during major releases coordinating multiple skills
- Useful for milestone tracking (1.0.0 = Initial release, 2.0.0 = Major refactor, etc.)
- Individual skills can increment independently

### Dependency Compatibility

When updating dependencies:
1. Test that dependent skills still work with new versions
2. Document breaking changes clearly in CHANGELOG.md
3. Consider running dependent skill tests before merging

**Example breaking change:**
```markdown
## [2.0.0] - 2025-XX-XX

### Changed
- **seo-geo**: Updated DataForSEO API integration (API v3.0 required)

### Fixed
- **twitter**: Fixed rate limiting handling (requires twitter >= 1.1.0)
```

## Git Workflow

We use **Git Flow** for version control. See [Git Flow](https://github.com/nvie/gitflow).

### Branching Strategy

```
main                               → Production releases
develop                            → Integration branch for next release

feature/skill/<name>/<feature>     → New skill feature
fix/skill/<name>/<issue>           → Skill bug fix
release/v<version>                 → Release preparation
hotfix/v<version>                  → Urgent production fixes
```

### Branch Naming Examples

```
feature/skill/domain-hunter/promo-code-scraper
fix/skill/requesthunt/reddit-pagination
feature/skill/seo-geo/perplexity-optimization
hotfix/v1.0.1
```

### Git Flow Commands

```bash
# Initialize git flow (first time only)
git flow init

# Start a new feature
git flow feature start skill/domain-hunter/advanced-filtering

# Finish feature - DO NOT use git flow feature finish
# Instead:
git push -u origin feature/skill/domain-hunter/advanced-filtering
gh pr create --base develop --head feature/skill/domain-hunter/advanced-filtering

# Start a release
git flow release start v2.0.0

# Finish release (merges to main, develop, creates tag)
git flow release finish v2.0.0
git push origin main develop --tags

# Start a hotfix
git flow hotfix start v1.0.1

# Finish hotfix
git flow hotfix finish v1.0.1
git push origin main develop --tags
```

### Important: Features Must Use PRs

**Never directly merge feature branches.** Always:
1. Push feature branch to origin
2. Create PR targeting `develop`
3. Request review and get approval
4. Merge via GitHub UI
5. Verify tests pass before merge

## Commit Convention

Use conventional commits for clear history:

```
feat(skill-name): Add new feature description
fix(skill-name): Fix bug description
docs(skill-name): Update documentation
test(skill-name): Add or update tests
refactor(skill-name): Refactor code without feature change
chore(skills): Maintenance task not specific to one skill
```

**Examples:**
```
feat(domain-hunter): Add WHOIS lookup for domain availability
fix(requesthunt): Handle Reddit API pagination edge case
docs(logo-creator): Add SVG export examples
chore(skills): Update dependencies
```

**Important**: Do not add any watermark or AI-generated signatures to commit messages.

## Issue Management

When creating issues, use type labels to categorize:

### Type Labels
- `bug` - Something isn't working
- `feature` - New skill or feature request
- `enhancement` - Improvement to existing skill
- `documentation` - Documentation improvements
- `refactor` - Code refactoring needed
- `test` - Test-related issues
- `chore` - Maintenance tasks

### Priority Labels
- `priority:high` - Critical or blocking
- `priority:medium` - Important but not blocking
- `priority:low` - Nice-to-have
- `good first issue` - Suitable for newcomers
- `help wanted` - Extra attention needed

### Skill-Specific Labels
One label per skill area:
- `skill:requesthunt`
- `skill:domain-hunter`
- `skill:logo-creator`
- `skill:banner-creator`
- `skill:nanobanana`
- `skill:reddit`
- `skill:twitter`
- `skill:producthunt`
- `skill:seo-geo`
- `infrastructure` - For tooling and overall project

### Writing Clear Issues

**For bugs:**
- Include reproduction steps
- Show expected vs actual behavior
- Link to related code or SKILL.md section

**For features:**
- Describe use case and desired outcome
- Reference any dependencies or related skills
- Provide example commands or workflows

**Example:**
```markdown
## Bug: RequestHunt pagination fails on large subreddits

**Reproduction:**
1. Run: `python3 scripts/list_requests.py --topic "python" --limit 1000`
2. See pagination error after 100 items

**Expected:** Fetch all 1000 items
**Actual:** Error after 100 items

**Related:** Issue #42 for similar Reddit API issue
```

## PR Requirements & Release Checklist

### Before Merging a PR

All of the following must pass:

- [ ] **Tests pass**: `npm run test` (website) passes without errors
- [ ] **Type checking**: `npm run typecheck` (website) shows no errors
- [ ] **Lint**: `npm run lint` (website) passes
- [ ] **Skill files valid**: SKILL.md has proper YAML frontmatter
- [ ] **Version updated**: `skills.json` version field updated (if functionality changed)
- [ ] **CHANGELOG.md updated**: Entry added under `[Unreleased]` section
- [ ] **Documentation updated**: SKILL.md or examples updated as needed
- [ ] **Dependencies checked**: New dependencies declared in SKILL.md
- [ ] **PR description**: References issue number (e.g., `Fixes #123`)

### Version Update Rules

Update versions in `skills.json` when:
- **MAJOR**: Breaking API changes, incompatible updates
- **MINOR**: New features or significant enhancements
- **PATCH**: Bug fixes, minor improvements

Do NOT update versions for:
- Documentation-only changes
- Internal refactoring without behavior changes
- Dependency version bumps (unless breaking)

### Merging and Closing Issues

Use closing keywords in PR description to auto-close issues:
```markdown
Fixes #123
Closes #124
Resolves #125
```

## Release Process

### Single Skill Release

When updating one skill:

1. **Update version** in `skills.json`
   ```json
   {
     "name": "domain-hunter",
     "version": "1.1.0"
   }
   ```

2. **Add changelog entry**
   ```markdown
   ## [1.1.0] - 2025-01-21
   
   ### Added
   - **domain-hunter**: New WHOIS lookup feature (#123)
   ```

3. **Create feature PR** targeting `develop` with changes
4. **Merge after approval** and tests pass
5. **Create release notes** in GitHub releases

### Full Project Release

When coordinating multiple skills for a major release:

1. **Start release branch**
   ```bash
   git flow release start v2.0.0
   ```

2. **Update all skill versions** in `skills.json`
3. **Update CHANGELOG.md** - Move all items from `[Unreleased]` to `[2.0.0]` section
4. **Add release date** in format `[2.0.0] - YYYY-MM-DD`
5. **Organize changes** by Added, Changed, Fixed, Removed, Deprecated
6. **Reference issues and PRs** in changelog entries (e.g., "Issue #63", "PR #64")
7. **Run tests**: `npm run test && npm run typecheck`
8. **Commit and merge**:
   ```bash
   git add skills.json CHANGELOG.md
   git commit -m "chore: Release v2.0.0"
   git flow release finish v2.0.0
   git push origin main develop --tags
   ```

9. **Create GitHub release** with changelog content
10. **Publish skills** via npm registry (if applicable)

## Development Best Practices

### Skill Development
- Start with clear documentation in SKILL.md
- Write example workflows before implementation
- Keep scripts focused on single responsibility
- Make scripts idempotent where possible
- Test with different agent tools (Claude, Cursor, Droid, etc.)

### Testing Skills
- Verify scripts work with sample inputs
- Test dependency installation
- Validate YAML frontmatter format
- Check trigger keywords are discoverable
- Test on different operating systems if applicable

### Documentation
- Write clear, concise SKILL.md instructions
- Include workflow diagrams or step-by-step examples
- Document all required environment variables
- Provide real-world usage examples
- Keep SKILL.md up-to-date with skill changes

### Performance & Efficiency
- Optimize API calls (batch when possible)
- Cache data appropriately
- Provide rate limit information
- Document expected execution time
- Handle errors gracefully

## Troubleshooting Common Issues

### Agent not recognizing skill

**Symptoms**: Skill triggers don't activate the skill

**Solutions**:
1. Verify SKILL.md has valid YAML frontmatter
2. Check `name` field matches directory name (kebab-case)
3. Ensure `triggers` field is a list with reasonable keywords
4. Clear agent cache and reinstall skill
5. Test with: `npx skills add ReScienceLab/opc-skills --skill <name>`

### Skill dependency not found

**Symptoms**: Skill requires another skill but it's not installed

**Solutions**:
1. Verify `dependencies` list in skills.json
2. Install dependencies: `npx skills add ReScienceLab/opc-skills --skill <dep>`
3. Check version compatibility in CHANGELOG.md
4. Look for breaking changes between versions

### Version conflicts

**Symptoms**: Multiple skill versions cause errors

**Solutions**:
1. Check CHANGELOG.md for breaking changes
2. Review version compatibility matrix (if available)
3. Update to compatible versions
4. Report version conflict as issue with details

## Getting Started

### First Time Setup

1. **Clone repository**
   ```bash
   git clone https://github.com/ReScienceLab/opc-skills
   cd opc-skills
   ```

2. **Install dependencies**
   ```bash
   npm install      # For website
   ```

3. **Initialize git flow**
   ```bash
   git flow init
   ```

4. **Create a feature branch**
   ```bash
   git flow feature start skill/your-skill-name/your-feature
   ```

5. **Follow the skill structure** documented above

### Creating Your First Skill

1. **Copy template**
   ```bash
   cp -r template skills/my-new-skill
   ```

2. **Edit SKILL.md** with your skill details

3. **Add scripts** in `scripts/` directory

4. **Add examples** in `examples/` directory

5. **Update skills.json** with new skill entry

6. **Test with your agent** before creating PR

## References

- **Semantic Versioning**: https://semver.org/
- **Keep a Changelog**: https://keepachangelog.com/
- **Conventional Commits**: https://www.conventionalcommits.org/
- **Git Flow**: https://github.com/nvie/gitflow
- **Agent Skills Standard**: https://agentskills.io/
- **Project README**: https://github.com/ReScienceLab/opc-skills/blob/main/README.md
