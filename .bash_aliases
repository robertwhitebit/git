#!/bin/bash
# sourced from ~/.bash_aliases
source /usr/share/bash-completion/completions/git

alias g='git '
__git_complete g _git

alias gut='git '
__git_complete gut _git

alias got='git '
__git_complete got _git

function _git_guilt() {
	_git_rebase
}

function _git_pr() {
	_git_tag
}

function _git_squash() {
	_git_checkout
}

function _git_fu() {
	_git_reset
}
