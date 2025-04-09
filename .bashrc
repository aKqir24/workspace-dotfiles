# ~/.bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'

# Evironment Variables
export COLORTERM=truecolor
export TERM=xterm-256color
export QT_QPA_PLATFORM=xcb
export QT_QPA_PLATFORMTHEME=qt6ct

# Color definitions
RED="\[\e[1;31m\]"
GREEN="\[\e[1;32m\]"
YELLOW="\[\e[1;33m\]"
BLUE="\[\e[1;34m\]"
MAGENTA="\[\e[1;35m\]"
CYAN="\[\e[1;36m\]"
WHITE="\[\e[1;37m\]"
RESET="\[\e[0m\]"

# All Prompts Config
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

PS1="${GREEN}\u${RESET}@${BLUE}\h${RESET}:${MAGENTA}\w${YELLOW}\$(parse_git_branch)${RESET}\$ "
PS1="\[\033[1m${GREEN}\u\]${RESET} @ ${GREEN}\h${RESET} in ${YELLOW}\w\n${BLUE?}>${RESET} "

# Fzf Inegration
export FZF_DEFAULT_COMMAND="find . -type f"
export FZF_DEFAULT_OPTS="--height 40% --reverse --border 
--color=fg:#DEEDFC,bg:#171826,hl:#F6C8EF,fg+:#DEEDFC,bg+:#356CB5,hl+:#F6C8EF"

source /usr/share/fzf/completion.bash
source /usr/share/fzf/key-bindings.bash
eval $(fzf --bash)
