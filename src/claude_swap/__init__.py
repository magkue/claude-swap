"""Multi-account switcher for Claude Code."""

from importlib.metadata import PackageNotFoundError, version

# The fork ships as the ``ccswap`` distribution; fall back to upstream's name so
# the package still imports when installed from an unmodified checkout.
try:
    __version__ = version("ccswap")
except PackageNotFoundError:  # pragma: no cover - depends on install layout
    __version__ = version("claude-swap")

from claude_swap.switcher import ClaudeAccountSwitcher

__all__ = ["ClaudeAccountSwitcher", "__version__"]
