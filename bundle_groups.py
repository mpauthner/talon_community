TERMINAL_BUNDLES = ("com.apple.Terminal", "com.googlecode.iterm2")

EDITOR_BUNDLES = (
    "com.microsoft.VSCode",
    "com.github.atom",
    "com.apple.TextEdit",
    "com.sublimetext.3",
    # jetbrains
    "com.jetbrains.intellij",
    "com.jetbrains.intellij.ce",
    "com.jetbrains.AppCode",
    "com.jetbrains.CLion",
    "com.jetbrains.datagrip",
    "com.jetbrains.goland",
    "com.jetbrains.PhpStorm",
    "com.jetbrains.pycharm",
    "com.jetbrains.rider",
    "com.jetbrains.rubymine",
    "com.jetbrains.WebStorm",
    "com.google.android.studio",
)

BROWSER_BUNDLES = ("org.mozilla.firefox", "com.google.Chrome", "com.brave.Browser")

FILETYPE_SENSITIVE_BUNDLES = (
    # *BROWSER_BUNDLES,
    *EDITOR_BUNDLES,
    *TERMINAL_BUNDLES,
)
