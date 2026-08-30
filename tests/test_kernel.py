import unittest

from core import KernelCore, Entity


class TestKernelCore(unittest.TestCase):

    def test_tick(self):
        kernel = KernelCore()

        kernel.world.add_entity(
            Entity("A", velocity=[1.0, 0.0, 0.0])
        )

        kernel.tick(0.5)

        state = kernel.snapshot()

        self.assertEqual(state["tick"], 1)
        self.assertEqual(state["simulation_time"], 0.5)
        self.assertEqual(
            state["entities"]["A"]["position"],
            [0.5, 0.0, 0.0]
        )

    def test_snapshot_restore(self):
        kernel = KernelCore()

        kernel.world.add_entity(
            Entity("A", velocity=[1.0, 0.0, 0.0])
        )

        kernel.tick(1.0)

        snapshot = kernel.snapshot()

        kernel.tick(10.0)

        kernel.recovery(snapshot)

        restored = kernel.observe()

        self.assertEqual(
            restored["entities"]["A"]["position"],
            [1.0, 0.0, 0.0]
        )

        self.assertEqual(restored["tick"], 1)
        self.assertEqual(restored["simulation_time"], 1.0)


if __name__ == "__main__":
    unittest.main()
