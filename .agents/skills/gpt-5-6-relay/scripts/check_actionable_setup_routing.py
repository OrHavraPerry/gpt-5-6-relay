"""Focused contract checks for actionable local setup routing."""

from dataclasses import dataclass


@dataclass(frozen=True)
class State:
    work_kind: str
    bounded_known: bool = False
    parent_route_satisfies: bool = False
    persistent_task_authorized: bool = False


ACTIONABLE_KINDS = {"setup", "launch", "playtest-prep", "test-execution"}


def route(state: State) -> str:
    if state.work_kind not in ACTIONABLE_KINDS:
        return "parent_only_allowed"
    if state.parent_route_satisfies:
        return "parent_may_execute"
    if state.bounded_known:
        return "in_process_luna_xhigh"
    return "in_process_terra_medium"


CASES = {
    "known launch uses Luna without persistent authority": (
        State(work_kind="launch", bounded_known=True),
        "in_process_luna_xhigh",
    ),
    "known playtest prep uses Luna": (
        State(work_kind="playtest-prep", bounded_known=True),
        "in_process_luna_xhigh",
    ),
    "uncertain dependency setup uses Terra": (
        State(work_kind="setup"),
        "in_process_terra_medium",
    ),
    "uncertain test execution uses Terra": (
        State(work_kind="test-execution"),
        "in_process_terra_medium",
    ),
    "satisfied parent route may stay local": (
        State(work_kind="launch", parent_route_satisfies=True),
        "parent_may_execute",
    ),
    "read-only check remains parent-only": (
        State(work_kind="read-only-status"),
        "parent_only_allowed",
    ),
}


for name, (state, expected) in CASES.items():
    actual = route(state)
    assert actual == expected, f"{name}: {actual!r} != {expected!r}"
    print(f"PASS: {name}")
