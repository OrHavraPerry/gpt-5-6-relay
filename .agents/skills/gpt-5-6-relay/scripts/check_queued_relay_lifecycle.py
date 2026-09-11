"""Focused contract checks for Relay queued-child lifecycle guidance."""

from dataclasses import dataclass


@dataclass(frozen=True)
class State:
    receipt: str | None = None
    exact_id: str | None = None
    identity_matches: bool = False
    listing_seen: bool = False
    discovery_attempts: int = 0
    create_attempts: int = 1
    creation_or_status_failure: bool = False
    wait_timed_out: bool = False
    wait_target: str | None = None
    wait_target_verified_exact: bool = False
    wait_target_matches_exact_id: bool = False
    terminal: str | None = None
    expected_parent_id: str | None = None
    parent_id: str | None = None
    delivery_accepted: bool = False


def decision(state: State) -> str:
    if state.create_attempts > 1:
        return "violation_duplicate_create; retain_original_lease"
    if state.discovery_attempts > 1:
        return "violation_repeat_discovery; retain_original_lease"
    if state.creation_or_status_failure:
        return "report_explicit_failure; retry_only_after_cancellation_or_failure"
    if state.wait_target and (
        not state.wait_target_verified_exact
        or not state.wait_target_matches_exact_id
    ):
        return "reject_client_receipt_as_wait_target; queued_identity_unresolved"
    if state.exact_id and not state.identity_matches:
        return "reject_unmatched_id; queued_identity_unresolved"
    if state.exact_id and state.wait_timed_out:
        return "remain_active_or_unknown; retain_lease"
    if state.exact_id and not state.terminal:
        return "bind_receipt; wait_threads"
    if state.exact_id and state.terminal and (
        not state.parent_id
        or state.parent_id != state.expected_parent_id
        or not state.delivery_accepted
    ):
        return "require_terminal_notification; retain_lease"
    if state.exact_id and state.terminal and state.delivery_accepted:
        return "read_once_verify_release_lease"
    if state.receipt:
        return "queued_identity_unresolved; retain_lease_no_duplicate"
    return "no_child_receipt"


CASES = {
    "queued receipt is not failure": (
        State(receipt="client-new-thread:abc"),
        "queued_identity_unresolved; retain_lease_no_duplicate",
    ),
    "omitted active listing is not failure": (
        State(receipt="client-new-thread:abc", listing_seen=False),
        "queued_identity_unresolved; retain_lease_no_duplicate",
    ),
    "authoritative supplied ID enables event wait": (
        State(receipt="client-new-thread:abc", exact_id="01abc", identity_matches=True),
        "bind_receipt; wait_threads",
    ),
    "verified exact wait target is accepted": (
        State(receipt="opaque-receipt", exact_id="01abc", identity_matches=True, wait_target="01abc", wait_target_verified_exact=True, wait_target_matches_exact_id=True),
        "bind_receipt; wait_threads",
    ),
    "unmatched supplied ID stays unresolved": (
        State(receipt="client-new-thread:abc", exact_id="invented"),
        "reject_unmatched_id; queued_identity_unresolved",
    ),
    "wait timeout is not terminal": (
        State(receipt="client-new-thread:abc", exact_id="01abc", identity_matches=True, wait_timed_out=True),
        "remain_active_or_unknown; retain_lease",
    ),
    "client receipt cannot target event wait": (
        State(receipt="client-new-thread:abc", wait_target="client-new-thread:abc"),
        "reject_client_receipt_as_wait_target; queued_identity_unresolved",
    ),
    "opaque receipt cannot target event wait": (
        State(receipt="opaque-receipt", exact_id="01abc", identity_matches=True, wait_target="opaque-receipt"),
        "reject_client_receipt_as_wait_target; queued_identity_unresolved",
    ),
    "mismatched wait target stays unresolved": (
        State(receipt="opaque-receipt", exact_id="01abc", identity_matches=True, wait_target="01other", wait_target_verified_exact=True),
        "reject_client_receipt_as_wait_target; queued_identity_unresolved",
    ),
    "genuine failure permits retry gate": (
        State(receipt="client-new-thread:abc", creation_or_status_failure=True),
        "report_explicit_failure; retry_only_after_cancellation_or_failure",
    ),
    "second creation violates one-worker lease": (
        State(receipt="client-new-thread:abc", create_attempts=2),
        "violation_duplicate_create; retain_original_lease",
    ),
    "repeated discovery violates bounded recovery": (
        State(receipt="client-new-thread:abc", discovery_attempts=2),
        "violation_repeat_discovery; retain_original_lease",
    ),
    "terminal child still owes parent notification": (
        State(receipt="client-new-thread:abc", exact_id="01abc", identity_matches=True, terminal="failed"),
        "require_terminal_notification; retain_lease",
    ),
    "unaccepted terminal delivery retains lease": (
        State(receipt="client-new-thread:abc", exact_id="01abc", identity_matches=True, terminal="done", expected_parent_id="01parent", parent_id="01parent"),
        "require_terminal_notification; retain_lease",
    ),
    "wrong parent ID retains lease": (
        State(receipt="client-new-thread:abc", exact_id="01abc", identity_matches=True, terminal="done", expected_parent_id="01parent", parent_id="wrong", delivery_accepted=True),
        "require_terminal_notification; retain_lease",
    ),
    "notified terminal child releases lease": (
        State(receipt="client-new-thread:abc", exact_id="01abc", identity_matches=True, terminal="done", expected_parent_id="01parent", parent_id="01parent", delivery_accepted=True),
        "read_once_verify_release_lease",
    ),
}


for name, (state, expected) in CASES.items():
    actual = decision(state)
    assert actual == expected, f"{name}: {actual!r} != {expected!r}"
    print(f"PASS: {name}")
