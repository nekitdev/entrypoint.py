from entrypoint import entrypoint

called = 0


@entrypoint()
def main() -> None:
    global called

    called += 1
