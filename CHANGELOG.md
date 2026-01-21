# Changelog

All notable changes to OPC Skills are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Documentation: Comprehensive AGENTS.md with version management and git workflow guidelines
- Infrastructure: CHANGELOG.md for tracking version history and skill changes

## [1.0.0] - 2025-01-21

### Added - Initial Release

#### Core Skills
- **requesthunt** (v1.0.0): Generate user demand research reports from Reddit, X, and GitHub
  - Collect real user feedback across multiple platforms
  - Filter and search by topic, platform, and timeframe
  - Generate structured demand research reports
  
- **domain-hunter** (v1.0.0): Search domains, compare registrar prices, and find promo codes
  - Query domain availability and pricing
  - Compare prices across registrars
  - Find current promo codes from Twitter and Reddit
  - Dependencies: twitter, reddit

- **logo-creator** (v1.0.0): Create logos using AI image generation
  - Generate logo variations with Gemini
  - Remove background from images
  - Crop logos to desired aspect ratios
  - Export as SVG vector format
  - Dependencies: nanobanana

- **banner-creator** (v1.0.0): Create banners for GitHub, Twitter, LinkedIn, and other platforms
  - Generate banner variations with Gemini
  - Crop to platform-specific ratios (16:9, 21:9, 2:1, etc.)
  - Support for different banner formats and styles
  - Dependencies: nanobanana

#### Image Generation
- **nanobanana** (v1.0.0): Generate and edit images using Google Gemini 3 Pro Image
  - Text-to-image generation
  - Image-to-image editing and variations
  - Support for multiple aspect ratios (1:1, 2:3, 3:2, 16:9, 21:9, etc.)
  - 2K and 4K high-resolution output options
  - Batch image generation

#### Data Collection & Integration
- **reddit** (v1.0.0): Search and retrieve content from Reddit
  - Access public JSON API without authentication
  - Search posts and subreddits
  - Get user profiles and comment threads
  - No API key required

- **twitter** (v1.0.0): Search and retrieve content from Twitter/X
  - User information and tweet retrieval
  - Search tweets by keyword
  - Get follower information and trends
  - Via twitterapi.io API service

- **producthunt** (v1.0.0): Search and retrieve content from Product Hunt
  - Query posts, topics, and collections
  - Get user and product information
  - Access GraphQL API for detailed data
  - Requires Product Hunt API access token

#### SEO & Optimization
- **seo-geo** (v1.0.0): SEO & GEO (Generative Engine Optimization) for websites
  - Optimize for traditional search engines (Google, Bing)
  - Optimize for AI search engines (ChatGPT, Perplexity, Gemini, Copilot, Claude)
  - Generate schema markup and JSON-LD
  - Keyword research and SERP analysis
  - Princeton GEO research methods for +40% AI visibility
  - Optional DataForSEO API integration for advanced features
  - Dependencies: twitter, reddit

### Features
- Unified installation system via `npx skills add`
- Support for 16+ AI agent tools (Claude Code, Cursor, Droid, Windsurf, etc.)
- Composable skills with dependency management
- Comprehensive documentation website (opc.dev)
- SKILL.md standard with YAML frontmatter for all skills
- Example workflows and use cases for each skill
- API documentation and reference links

### Documentation
- Official website: https://opc.dev
- Skill browser: https://skills.sh/ReScienceLab/opc-skills
- Individual skill repositories on GitHub
- Example workflows in each skill directory
- API documentation and rate limit information

### Infrastructure
- GitHub repository: https://github.com/ReScienceLab/opc-skills
- MIT License
- Automated skill installation scripts
- Website deployment pipeline

## Skill Dependencies

### Direct Dependencies
- **domain-hunter** → requires: twitter, reddit
- **logo-creator** → requires: nanobanana
- **banner-creator** → requires: nanobanana
- **seo-geo** → requires: twitter, reddit (optional for basic audit)

### Independent Skills
- **requesthunt**: No dependencies
- **nanobanana**: No dependencies
- **reddit**: No dependencies
- **twitter**: No dependencies
- **producthunt**: No dependencies

## Version Compatibility

| Version | Status | Release Date | Notable Changes |
|---------|--------|--------------|-----------------|
| 1.0.0 | Stable | 2025-01-21 | Initial release with 9 core skills |
| Unreleased | Development | TBD | Documentation and workflow improvements |

## Migration Guides

### Coming Soon
Migration guides for major version upgrades will be documented here.

## Notes

### API Keys Required
- **requesthunt**: REQUESTHUNT_API_KEY (requesthunt.com/settings/api)
- **twitter**: TWITTERAPI_API_KEY (twitterapi.io, ~$0.15-0.18/1k requests)
- **logo-creator**: GEMINI_API_KEY, REMOVE_BG_API_KEY, RECRAFT_API_KEY
- **banner-creator**: GEMINI_API_KEY (Google AI Studio)
- **nanobanana**: GEMINI_API_KEY
- **producthunt**: PRODUCTHUNT_ACCESS_TOKEN
- **seo-geo**: DATAFORSEO_LOGIN, DATAFORSEO_PASSWORD (optional)

### Rate Limits
- **requesthunt**: 1000/month cached, 500/month realtime
- **twitter**: Depends on twitterapi.io plan
- **nanobanana**: Google Gemini API limits apply
- **seo-geo**: DataForSEO API limits apply

### Supported Platforms
- Claude Code (Desktop)
- Cursor
- Factory Droid
- Windsurf
- OpenCode
- Codex
- GitHub Copilot
- Gemini CLI
- Goose
- Kilo Code
- Roo Code
- Trae
- And more via `npx skills add`

## Contributing

Interested in contributing? Please see:
- Contributing Guidelines: https://github.com/ReScienceLab/opc-skills/blob/main/CONTRIBUTING.md (coming soon)
- Issue Tracker: https://github.com/ReScienceLab/opc-skills/issues
- Skill Template: https://github.com/ReScienceLab/opc-skills/tree/main/template

## Support

For issues and questions:
- GitHub Issues: https://github.com/ReScienceLab/opc-skills/issues
- Website: https://opc.dev
- Documentation: https://skills.sh/ReScienceLab/opc-skills

## License

All OPC Skills are released under the [MIT License](https://github.com/ReScienceLab/opc-skills/blob/main/LICENSE).

---

Generated: 2025-01-21
Project: OPC Skills - AI Agent Skills for Solopreneurs
