# RCOS Evolution Protocol

## Goal

Define how RCOS DNA evolves across:

- the core RCOS system
- tenant projects
- example seeds
- release artifacts

This protocol exists to preserve:

- DNA integrity
- contributor traceability
- sync discipline
- release stability

while avoiding sync storms.

---

## Core Terms

### Core DNA

The reusable RCOS rules, templates, prompts, and collaboration patterns that live in the main RCOS repository's active `.rcos/` paths.

### Tenant Project

A real project that uses RCOS and may:

- absorb promoted RCOS DNA from the main RCOS repository
- produce local RCOS innovations
- contribute reusable DNA back upstream

### DNA Item

A single reusable RCOS evolution unit, such as:

- a new high-value project-specific file type
- a new planning or tracking rule
- a new onboarding or maintenance discipline
- a new upstream/downstream sync rule

### Example Seed

A delayed-promotion sample of a successful tenant project's RCOS context.

It is:

- a reference seed
- not the active truth source for the main RCOS system
- not a high-frequency sync layer

### Artifact

A release-oriented packaged output such as:

- `rcos_bootstrap_pack_with_examples.zip`

Artifacts are the slowest-changing layer.

---

## Protocol Version

Current protocol identifier:

- `rcos-evolution-v1`

This protocol version describes the sync model itself, not every individual DNA item.

---

## DNA Layers

RCOS DNA should be handled in three different cadence layers:

### 1. Core Layer

Contains:

- main `.rcos/manifest/templates/*`
- main `.rcos/prompts/*`
- main rules and documentation

Cadence:

- highest frequency

### 2. Seed Layer

Contains:

- `.rcos_examples/<tenant-project>/...`

Cadence:

- delayed promotion
- lower frequency than core layer

### 3. Artifact Layer

Contains:

- packaged bootstrap outputs

Cadence:

- release-level only
- lower frequency than seed layer

---

## Required Default Rule

Do not treat these three layers as one synchronous unit.

Default behavior:

- core DNA may evolve first
- example seeds may lag intentionally
- artifacts may lag even further

This separation is required to avoid sync storms.

---

## DNA Lifecycle

Each RCOS evolution should move through explicit states:

- `local_only`
- `candidate_upstream`
- `promoted_upstream`
- `candidate_downstream_intake`
- `intake_applied`

Notes:

- tenant projects may keep local-only DNA without forcing immediate upstream sync
- promoted DNA belongs to the main RCOS core layer
- example seed sync is a separate decision from core promotion
- artifact release is a separate decision from seed sync

---

## Contributor Project Rule

When reusable DNA is discovered in a tenant project:

1. first stabilize it in the tenant project
2. summarize what is reusable vs project-specific
3. tag the contributor project explicitly
4. only then propose upstream promotion

The contributor project tag must remain attached to the promoted DNA record.

---

## Seed Sync Rule

Example seeds are delayed-promotion samples.

Therefore:

- a promoted core DNA item does not automatically require seed updates
- tenant RCOS context should not be copied into an unrelated example seed
- if a seed is updated, it should preferentially be the seed path matching the contributor project

Seed sync should happen only when:

- the tenant project has become a stable success seed
- a milestone or delivery boundary has been reached
- the human explicitly wants the project promoted as a seed

---

## Artifact Release Rule

Artifacts such as `rcos_bootstrap_pack_with_examples.zip` are release outputs.

Therefore:

- do not rebuild them for every core DNA change
- do not rebuild them for every seed adjustment
- rebuild them only when there is a release-worthy change

Typical triggers:

- a new example seed is added
- an existing example seed is materially updated as a released seed
- the core RCOS pack has accumulated a meaningful promoted change set
- the human explicitly asks for a new distributable bundle

---

## Seed / Artifact Decoupling Rule

Default rule:

- do not update example seeds and release artifacts in the same routine maintenance step

Allowed exception:

- an explicitly approved release exception may update both seed and artifact together

Such an exception must state:

- why the exception is needed
- which seed is being synchronized
- which artifact is being rebuilt
- why waiting for the normal release cadence is not appropriate

---

## Downstream Intake Rule

Tenant projects should not be forced to immediately absorb every newly promoted core DNA item.

Instead:

- track the tenant's current core DNA base
- track pending downstream intake candidates
- evaluate intake during:
  - onboarding
  - roadmap review
  - RCOS maintenance review
  - explicit human sync tasks

---

## Required Registry Discipline

Promoted DNA should be recorded in a registry with:

- DNA id
- title
- contributor project
- status
- affected layer(s)
- seed sync policy
- artifact impact
- dependencies or superseded DNA if relevant

Use `RCOS_DNA_REGISTRY_TEMPLATE.yaml` as the reusable shape.

---

## Current Bootstrap Exception

For the initial rollout of the RCOS DNA system itself, one out-of-band exception release may:

- update the core RCOS layer
- update corresponding example seed content
- rebuild the bootstrap artifact

After that one-time initialization, normal decoupled cadence resumes.
