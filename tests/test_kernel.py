from core import KernelCore, Entity


def test_tick():
    kernel = KernelCore()
    kernel.world.add_entity(
        Entity("A", velocity=[1.0, 0.0, 0.0])
    )

    kernel.tick(0.5)

    state = kernel.snapshot()

    assert state["tick"] == 1
    assert state["simulation_time"] == 0.5
    assert state["entities"]["A"]["position"] == [0.5, 0.0, 0.0]


def test_snapshot_restore():
    kernel = KernelCore()
    kernel.world.add_entity(
        Entity("A", velocity=[1.0, 0.0, 0.0])
    )

    kernel.tick(1.0)
    snapshot = kernel.snapshot()

    kernel.tick(10.0)
    kernel.recovery(snapshot)

    assert kernel.observe()["entities"]["A"]["position"] == [1.0, 0.0, 0.0]
