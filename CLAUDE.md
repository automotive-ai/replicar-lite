<!-- AAI-ENGINEERING-STANDARD:START -->

# AAI Engineering Standard for Claude Code

This section is centrally managed by AAI.

Claude shall follow:
- AAI_POLICY.md
- Repository-specific documentation
- Repository-specific instructions outside this managed section

## Jira Requirement

Every change requires a Jira Ticket or Epic.

Include the Jira ID in:
- Branch
- Commit
- Pull Request

## Development Rules

Claude shall:
- understand existing code before changing it
- preserve repository-specific instructions
- make the smallest appropriate change
- update tests
- update documentation
- avoid unrelated modifications
- never commit secrets

## Human Review

All Claude-generated changes require human review before merge.

## Completion Checklist

- [ ] Jira referenced
- [ ] Tests updated
- [ ] Documentation updated
- [ ] No secrets committed
- [ ] CI passes
- [ ] Human review completed

<!-- AAI-ENGINEERING-STANDARD:END -->
