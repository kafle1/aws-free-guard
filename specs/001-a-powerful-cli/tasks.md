# Tasks: AWS Free Guard CLI Tool

**Input**: Design documents from `/specs/001-a-powerful-cli/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Execution Flow (main)
```
1. Load plan.md from feature directory
   → If not found: ERROR "No implementation plan found"
   → Extract: tech stack, libraries, structure
2. Load optional design documents:
   → data-model.md: Extract entities → model tasks
   → contracts/: Each file → contract test task
   → research.md: Extract decisions → setup tasks
3. Generate tasks by category:
   → Setup: project init, dependencies, linting
   → Tests: contract tests, integration tests
   → Core: models, services, CLI commands
   → Integration: DB, middleware, logging
   → Polish: unit tests, performance, docs
4. Apply task rules:
   → Different files = mark [P] for parallel
   → Same file = sequential (no [P])
   → Tests before implementation (TDD)
5. Number tasks sequentially (T001, T002...)
6. Generate dependency graph
7. Create parallel execution examples
8. Validate task completeness:
   → All contracts have tests?
   → All entities have models?
   → All endpoints implemented?
9. Return: SUCCESS (tasks ready for execution)
```

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 3.1: Setup
- [ ] T001 Create project structure per implementation plan
- [ ] T002 Initialize Python project with Click, boto3, Rich, pytest dependencies
- [ ] T003 [P] Configure linting and formatting tools (black, isort, flake8, mypy)

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [ ] T004 [P] Contract test for free command in tests/contract/test_free_command.py
- [ ] T005 [P] Contract test for clean command in tests/contract/test_clean_command.py
- [ ] T006 [P] Integration test for primary user story (free command) in tests/integration/test_free_flow.py
- [ ] T007 [P] Integration test for primary user story (clean command) in tests/integration/test_clean_flow.py

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T008 [P] AWS Account model in src/models/aws_account.py
- [ ] T009 [P] AWS Resource model in src/models/aws_resource.py
- [ ] T010 [P] Free Tier Limit model in src/models/free_tier_limit.py
- [ ] T011 [P] Operation Result model in src/models/operation_result.py
- [ ] T012 [P] AWS Free library in src/lib/aws_free.py
- [ ] T013 [P] AWS Clean library in src/lib/aws_clean.py
- [ ] T014 CLI free command in src/cli/commands.py
- [ ] T015 CLI clean command in src/cli/commands.py
- [ ] T016 Main CLI entry point in src/cli/main.py

## Phase 3.4: Integration
- [ ] T017 Connect AWS services to boto3 clients
- [ ] T018 Implement logging with structured JSON format
- [ ] T019 Add error handling for AWS exceptions
- [ ] T020 Implement dry-run functionality

## Phase 3.5: Polish
- [ ] T021 [P] Unit tests for models in tests/unit/test_models.py
- [ ] T022 [P] Unit tests for libraries in tests/unit/test_lib.py
- [ ] T023 Performance tests (<5s execution)
- [ ] T024 [P] Update README.md with installation and usage
- [ ] T025 [P] Create setup.py for packaging
- [ ] T026 Run quickstart.md validation
- [ ] T027 Final integration testing with test AWS account

## Dependencies
- Tests (T004-T007) before implementation (T008-T016)
- T008-T011 blocks T012-T013
- T012-T013 blocks T014-T016
- T014-T016 blocks T017-T020
- Implementation before polish (T021-T027)

## Parallel Example
```
# Launch T004-T007 together:
Task: "Contract test for free command in tests/contract/test_free_command.py"
Task: "Contract test for clean command in tests/contract/test_clean_command.py"
Task: "Integration test for primary user story (free command) in tests/integration/test_free_flow.py"
Task: "Integration test for primary user story (clean command) in tests/integration/test_clean_flow.py"
```

## Notes
- [P] tasks = different files, no dependencies
- Verify tests fail before implementing
- Commit after each task
- Avoid: vague tasks, same file conflicts

## Task Generation Rules
*Applied during main() execution*

1. **From Contracts**:
   - Each contract file → contract test task [P]
   - Each endpoint → implementation task
   
2. **From Data Model**:
   - Each entity → model creation task [P]
   - Relationships → service layer tasks
   
3. **From User Stories**:
   - Each story → integration test [P]
   - Quickstart scenarios → validation tasks

4. **Ordering**:
   - Setup → Tests → Models → Services → Endpoints → Polish
   - Dependencies block parallel execution

## Validation Checklist
*GATE: Checked by main() before returning*

- [x] All contracts have corresponding tests
- [x] All entities have model tasks
- [x] All tests come before implementation
- [x] Parallel tasks truly independent
- [x] Each task specifies exact file path
- [x] No task modifies same file as another [P] task
