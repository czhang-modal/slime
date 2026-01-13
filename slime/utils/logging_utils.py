import logging

_LOGGER_CONFIGURED = False


# ref: SGLang
def configure_logger(prefix: str = "", rank: int = None):
    global _LOGGER_CONFIGURED
    if _LOGGER_CONFIGURED:
        return

    _LOGGER_CONFIGURED = True

    rank_str = f" rank={rank}" if rank is not None else ""
    logging.basicConfig(
        level=logging.INFO,
        format=f"[%(asctime)s{prefix}{rank_str}] %(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True,
    )
