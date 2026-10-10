# AAI AI-Assisted Development Policy

**Owner:** AAI Innovations GmbH
**Status:** Mandatory
**Version:** 1.0

## Purpose
This policy defines the mandatory requirements for AI-assisted software development within AAI.

It supports:
- ISO 9001
- ISO/IEC 27001
- ISO/IEC 42001
- TISAX
- Customer-specific contractual obligations

## Scope
This policy applies to all AAI repositories, employees, contractors and approved AI tools.

## Mandatory Jira Traceability
Every development activity shall reference an approved Jira Ticket or Epic.

The Jira ID must appear in:
- Branch name
- Commit message
- Pull Request

Example:

```text
Branch: feature/AAI-123-add-validation
Commit: AAI-123 Add validation
PR: [AAI-123] Add validation
```

If no Jira ticket exists, one shall be created before development starts.

## Human Responsibility
AI suggestions must always be reviewed by a human developer.

The developer remains responsible for correctness, security, testing, documentation, licensing and compliance.

## Security
Never expose passwords, API keys, secrets, customer confidential information or personal data to unauthorized AI services.

## Development Requirements
AI-generated code shall:
- follow repository conventions
- include tests where appropriate
- update documentation
- pass CI
- avoid unnecessary dependencies

## Pull Requests
Every PR shall include:
- Jira reference
- implementation summary
- testing performed
- risks
- AI usage declaration

## Prohibited
AI shall not be used to bypass reviews, fabricate evidence, commit secrets or merge without approval.

## Traceability

```text
Requirement
→ Jira
→ Branch
→ Commit
→ Pull Request
→ Review
→ Test
→ Release
```

## Exceptions
Exceptions require documented management approval.
