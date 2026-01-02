# Tasks: CLI Todo Application

**Input**: Design documents from `specs/001-cli-todo-app/`
**Prerequisites**: plan.md, spec.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (US1, US2, etc.)

## Path Conventions

- Paths assume a single project structure based on `plan.md`.

---
## Phase 1: Setup (Shared Infrastructure)
**Purpose**: Project initialization and basic structure.

- [x] T001 Initialize `uv` environment and create `src/` directory.
- [x] T002 Create `requirements.txt` and add `typer` and `rich`.
- [x] T003 [P] Install dependencies using `uv pip install -r requirements.txt`.
- [x] T004 [P] Configure `ruff` for linting and formatting by creating a `ruff.toml` or `pyproject.toml` file.

---
## Phase 2: Foundational (Blocking Prerequisites)
**Purpose**: Core infrastructure needed for all user stories.

- [x] T005 Define the `Task` data class in `src/models.py`.
- [x] T006 Create the `TaskService` class in `src/service.py` to manage the in-memory list of tasks.
- [x] T007 Set up the main `typer` application in `src/main.py`.

**Checkpoint**: Foundation ready. User story implementation can begin.

---
## Phase 3: User Story 1 - Add a new task (Priority: P1) 🎯 MVP
**Goal**: Allow users to add a new task.

### Implementation for User Story 1
- [x] T008 [US1] Implement the `add_task` method in `src/service.py`.
- [x] T009 [US1] Implement the `add` command in `src/cli.py` using `typer`, calling the service layer.

**Checkpoint**: `add` command is functional.

---
## Phase 4: User Story 2 - View all tasks (Priority: P1)
**Goal**: Allow users to see all their tasks.

### Implementation for User Story 2
- [x] T010 [US2] Implement the `get_all_tasks` method in `src/service.py`.
- [x] T011 [US2] Implement the `view` command in `src/cli.py` to format and print the tasks.

**Checkpoint**: `view` command is functional.

---
## Phase 5: User Story 3 - Mark a task as complete (Priority: P2)
**Goal**: Allow users to mark a task as complete.

### Implementation for User Story 3
- [x] T012 [US3] Implement the `mark_task_complete` method in `src/service.py`.
- [x] T013 [US3] Implement the `complete` command in `src/cli.py`.

**Checkpoint**: `complete` command is functional.

---
## Phase 6: User Story 4 - Update a task (Priority: P2)
**Goal**: Allow users to edit an existing task.

### Implementation for User Story 4
- [x] T014 [US4] Implement the `update_task` method in `src/service.py`.
- [x] T015 [US4] Implement the `update` command in `src/cli.py`.

**Checkpoint**: `update` command is functional.

---
## Phase 7: User Story 5 - Delete a task (Priority: P3)
**Goal**: Allow users to remove a task.

### Implementation for User Story 5
- [x] T016 [US5] Implement the `delete_task` method in `src/service.py`.
- [x] T017 [US5] Implement the `delete` command in `src/cli.py`.

**Checkpoint**: `delete` command is functional.

---
## Phase 8: Polish & Cross-Cutting Concerns
**Purpose**: Final improvements and documentation.

- [x] T018 [P] Review and refine all CLI output for clarity and consistency.
- [x] T019 [P] Add comprehensive error handling for invalid inputs across all commands.
- [x] T020 [P] Update `README.md` with final usage instructions from `quickstart.md`.

---
## Dependencies & Execution Order

- **Phase 1 & 2**: Must be completed before any user story work begins.
- **User Stories**: Can be implemented in priority order (US1/US2 -> US3/US4 -> US5). US1 and US2 are P1 and can be developed together.
- **Within each story**: The service method should be implemented before the CLI command.

## Implementation Strategy

### MVP First (User Stories 1 & 2)
1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (add)
4. Complete Phase 4: User Story 2 (view)
5. **STOP and VALIDATE**: At this point, the application is a functional MVP. A user can add and view tasks.
