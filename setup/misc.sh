#!/bin/bash

# Alias
printf "Adding proper aliases to .zshrc\n"
# shellcheck disable=SC2129
echo "alias c='clear'" >> "$HOME"/.zshrc
echo "alias gs='git status'" >> "$HOME"/.zshrc
echo "alias upd='sudo apt update'" >> "$HOME"/.zshrc
echo "alias upg='sudo apt full-upgrade'" >> "$HOME"/.zshrc
echo "alias dc='docker compose'" >> "$HOME"/.zshrc
echo "alias s='screen'" >> "$HOME"/.zshrc

