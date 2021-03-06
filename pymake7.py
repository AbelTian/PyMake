# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""PyMake 7.8.3.

Usage:
  pymake7.py  source
  pymake7.py  source file [ <source-path-file> ]
  pymake7.py  source root [ <source-root-path> ]
  pymake7.py  source config [ --add ] [ <config-file-name> ]
  pymake7.py  source config [ --del ] [ <config-file-name> ]
  pymake7.py  source config [ --mod ] [ <config-file-name> ] [<new-config-file-name>]
  pymake7.py  source config [ --switch ] [ <config-file-name> ]
  pymake7.py  source config [ --edit ] [ <config-file-name> ]
  pymake7.py  source config [ --restore ]
  pymake7.py  source config [ --show ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  set path ( --add | --del | --mod ) <name> [ <value> ]
  pymake7.py  set env [ path ] ( --add | --del | --mod ) <group> <name> [ <value> ]
  pymake7.py  set cmd (--add | --del | --mod ) <name> [ <values> ... ]
  pymake7.py  set cur env <name>
  pymake7.py  list [ path | env | cmd ] [<name>] [-r | --raw] [-a | --all]
  pymake7.py  env [<name>] [-p | --path] [-v | --var] [-r | --raw] [-a | --all]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  clean [ here | hh ] [ there | tt ] [ default | dd ]
  pymake7.py  export [ here | hh ] [ there | tt ] [ default | dd ] [ <env-name> ] [ to <file-name> ]
  pymake7.py  type [ here | hh ] [ there | tt ] [ default | dd ] [ <cmd-name> ] [ to <file-name> ]
  pymake7.py  exec [ here | hh ] [ there | tt ] [ default | dd ] [ <command-names> ... ]
  pymake7.py  cc [ here | hh ] [ there | tt ] [ default | dd ] [ <command-names> ... ]
  pymake7.py  use <env-name> type [ here | hh ] [ there | tt ] [ default | dd ] [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py  use <env-name> exec [ here | hh ] [ there | tt ] [ default | dd ] [ <command-names> ... ]
  pymake7.py  use <env-name> cc [ here | hh ] [ there | tt ] [ default | dd ] [ <command-names> ... ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  set current env <name>
  pymake7.py  set default env <name>
  pymake7.py  show [ path | env | cmd ] [<name>] [-r | --raw] [-a | --all]
  pymake7.py  environ [<name>] [-p | --path] [-v | --var] [-r | --raw] [-a | --all]
  pymake7.py  see [ <cmd-name> ] [ use <env-name> ] [-r | --raw] [-a | --all] [ -l | --linenumber ]
  pymake7.py  ss [ <cmd-name> ] [ use <env-name> ] [-r | --raw] [-a | --all] [ -l | --linenumber ]
  pymake7.py  cmd [ <cmd-name> ] [ use <env-name> ] [-r | --raw] [-a | --all] [ -l | --linenumber ]
  pymake7.py  use <env-name> see [ <cmd-name> ] [-r | --raw] [-a | --all] [ -l | --linenumber ]
  pymake7.py  use <env-name> ss [ <cmd-name> ] [-r | --raw] [-a | --all] [ -l | --linenumber ]
  pymake7.py  use <env-name> cmd [ <cmd-name> ] [-r | --raw] [-a | --all] [ -l | --linenumber ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  have path <name> [-r | --raw]
  pymake7.py  have env [ path ] [ <group> ] [ <name> ] [-r | --raw]
  pymake7.py  have cmd <name> [-r | --raw]
  pymake7.py  has path <name> [-r | --raw]
  pymake7.py  has env [ path ] [ <group> ] [ <name> ] [-r | --raw]
  pymake7.py  has cmd <name> [-r | --raw]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  get cur env
  pymake7.py  get current env
  pymake7.py  get default env
  pymake7.py  get env
  pymake7.py  get env ( cur | current | default )
  pymake7.py  -------------------------------------------------------------
  pymake7.py  program
  pymake7.py  program root
  pymake7.py  program file
  pymake7.py  program configure
  pymake7.py  program configure root
  pymake7.py  program configure file
  pymake7.py  program configure [ --edit ]
  pymake7.py  initialize
  pymake7.py  debug
  pymake7.py  debug [ open | close ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  get all
  pymake7.py  get all ( info | information )
  pymake7.py  get all ( stat | status )
  pymake7.py  get all settings [ path | env | cmd ] [<name>] [-r | --raw] [-a | --all]
  pymake7.py  get all settings [ -l | --local ] [ -c | --custom ] [ -s | --system ] [ --current ] [ --envname=<env-name> ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  set exec root
  pymake7.py  set exec root [ to <work-root-path> ]
  pymake7.py  set exec root to [ here | hh ] [ there | tt ] [ default | dd ]
  pymake7.py  set [ default | dd ] exec root
  pymake7.py  set [ there | tt ] exec root
  pymake7.py  set [ here | hh ] exec root
  pymake7.py  set [ there | tt ] exec root [ to <work-root-path> ]
  pymake7.py  set [ current | starting ] exec root [ to <work-root-path> ]
  pymake7.py  set [ current | starting ] exec root to [ here | hh ] [ there | tt ] [ default | dd ]
  pymake7.py  get exec root
  pymake7.py  get exec root [ here | hh ] [ there | tt ] [ default | dd ]
  pymake7.py  get [ here | hh ] [ there | tt ] [ default | dd ] exec root
  pymake7.py  get [ default | dd ] exec root
  pymake7.py  get [ there | tt ] exec root
  pymake7.py  get [ here | hh ] exec root
  pymake7.py  get [ current | starting ] exec root [ --position | -p ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  port
  pymake7.py  port root [ <source-config-root> ] [ to <target-config-root> ]
  pymake7.py  port config [ <source-config-file> ] [ to <target-config-file> ]
  pymake7.py  port file [ <source-path-file> ] [ to <target-path-file> ]
  pymake7.py  port root ( --source | --target ) <config-root>
  pymake7.py  port config ( --source | --target ) <config-file>
  pymake7.py  port file ( --source | --target ) <path-file>
  pymake7.py  port reset
  pymake7.py  translate
  pymake7.py  translate ( path | env | cmd )
  pymake7.py  translate ( path | env | cmd ) <key-name> [ to <target-key-name> ] [ -f | --force ]
  pymake7.py  translate ( path | env | cmd ) [ -a | --all ] [ -f | --force ]
  pymake7.py  translate path-env-cmd [ -a | --all ] [ -f | --force ]
  pymake7.py  translate all [ -a | --all ] [ -f | --force ]
  pymake7.py  translate section
  pymake7.py  translate section <section-name> [ to <target-section-name> ] [ -f | --force ]
  pymake7.py  translate section [ -a | --all ] [ -f | --force ]
  pymake7.py  translate config [ -f | --force ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  use <env-name> exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  use <env-name> execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  use <env-name> ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  import cmd [ here | hh ] [ there | tt ] [ default | dd ] [ <script-file> ] [ to <command-name> ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --filter=<name-filter> ... ]
  pymake7.py  outport cmd [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  use <env-name> outport cmd [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  backup [ here | hh ] [ there | tt ] [ default | dd ] [ <zip-file-name> ]
  pymake7.py  recovery [ here | hh ] [ there | tt ] [ default | dd ] [ <zip-file-name> ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  system
  pymake7.py  system [ stat | status ]
  pymake7.py  system [ info | information ]
  pymake7.py  system path [ --add | --del ] [ <value> ]
  pymake7.py  system var [ --add | --del ] [ <key> ] [ <value> ]
  pymake7.py  system env [ -r | --raw ]
  pymake7.py  system exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  system use <env-name> exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  system execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  system use <env-name> execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  system ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  system use <env-name> ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  local
  pymake7.py  local [ open | close ]
  pymake7.py  local [ stat | status ]
  pymake7.py  local [ info | information ]
  pymake7.py  local edit
  pymake7.py  local path [ --add | --del ] [ <value> ]
  pymake7.py  local var [ --add | --del ] [ <key> ] [ <value> ]
  pymake7.py  local env [ -r | --raw ]
  pymake7.py  local export [ here | hh ] [ there | tt ] [ default | dd ] [ to <file-name> ]
  pymake7.py  local exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  local use <env-name> exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  local execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  local use <env-name> execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  local ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  local use <env-name> ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  custom
  pymake7.py  custom [ open | close ]
  pymake7.py  custom [ stat | status ]
  pymake7.py  custom [ info | information ]
  pymake7.py  custom edit
  pymake7.py  custom path [ --add | --del ] [ <value> ]
  pymake7.py  custom var [ --add | --del ] [ <key> ] [ <value> ]
  pymake7.py  custom env [ -r | --raw ]
  pymake7.py  custom export [ here | hh ] [ there | tt ] [ default | dd ] [ to <file-name> ]
  pymake7.py  custom exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  custom use <env-name> exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  custom execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  custom use <env-name> execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  custom ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  custom use <env-name> ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  powershell
  pymake7.py  powershell [ info | information ]
  pymake7.py  powershell [ stat | status ]
  pymake7.py  powershell clean [ here | hh ] [ there | tt ] [ default | dd ]
  pymake7.py  powershell export [ here | hh ] [ there | tt ] [ default | dd ] [ <env-name> ] [ to <file-name> ]
  pymake7.py  powershell type [ here | hh ] [ there | tt ] [ default | dd ] [ <cmd-name> ] [ to <file-name> ]
  pymake7.py  powershell use <env-name> type [ here | hh ] [ there | tt ] [ default | dd ] [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py  powershell exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  powershell use <env-name> exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  powershell execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  powershell use <env-name> execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  powershell ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  powershell use <env-name> ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  python
  pymake7.py  python [ info | information ]
  pymake7.py  python [ stat | status ]
  pymake7.py  python clean [ here | hh ] [ there | tt ] [ default | dd ]
  pymake7.py  python type [ here | hh ] [ there | tt ] [ default | dd ] [ <cmd-name> ] [ to <file-name> ]
  pymake7.py  python use <env-name> type [ here | hh ] [ there | tt ] [ default | dd ] [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py  python exec-with-params [ here | hh ] [ there | tt ] [ default | dd ][ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  python use <env-name> exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  python execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  python use <env-name> execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  python ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  python use <env-name> ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  language
  pymake7.py  language [ info | information ]
  pymake7.py  language [ stat | status ]
  pymake7.py  language clean [ here | hh ] [ there | tt ] [ default | dd ] [ --suffix=<.suffix-name> ]
  pymake7.py  language type [ here | hh ] [ there | tt ] [ default | dd ] [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  language use <env-name> type [ here | hh ] [ there | tt ] [ default | dd ] [ <cmd-name> ]  [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  language exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  language use <env-name> exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  language execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  language use <env-name> execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  language ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  language use <env-name> ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  sys
  pymake7.py  sys [ stat | status ]
  pymake7.py  sys [ info | information ]
  pymake7.py  sys path [ --add | --del ] [ <value> ]
  pymake7.py  sys var [ --add | --del ] [ <key> ] [ <value> ]
  pymake7.py  sys env [ -r | --raw ]
  pymake7.py  sys exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  sys use <env-name> exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  sys execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  sys use <env-name> execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  sys ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  sys use <env-name> ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  export2 [ powershell ] [ here | hh ] [ there | tt ] [ default | dd ] [ <env-name> ] [ to <file-name> ] [ -c | --custom ] [ -l | --local ] [ -s | --system ]
  pymake7.py  type2 [ here | hh ] [ there | tt ] [ default | dd ] [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  use <env-name> type2 [ here | hh ] [ there | tt ] [ default | dd ] [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  open [ <path-name> ... ] [ -c | --custom ] [ --current ] [ --envname=<env-name> ] [ -i | --ignorecase ]
  pymake7.py  use <env-name> open [ <path-name> ... ] [ -i | --ignorecase ]
  pymake7.py  check path [ <item-name> ] [ --item=<item-name> ] [ -a | --all ]
  pymake7.py  check cmd [ <item-name> ] [ --item=<item-name> ] [ -a | --all ]
  pymake7.py  check [ env ] [ vc ] [ <env-name> ] [ --current ] [ --envname=<env-name> ] [ -a | --all ] [ -s | --system ] [ -l | --local ] [ -c | --custom ]
  pymake7.py  chk path [ <item-name> ] [ --item=<item-name> ] [ -a | --all ]
  pymake7.py  chk cmd [ <item-name> ] [ --item=<item-name> ] [ -a | --all ]
  pymake7.py  chk [ env ] [ vc ] [ <env-name> ] [ --current ] [ --envname=<env-name> ] [ -a | --all ] [ -s | --system ] [ -l | --local ] [ -c | --custom ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  vc
  pymake7.py  vc [ info | information ]
  pymake7.py  vc [ stat | status ]
  pymake7.py  vc settings [ <env-name> ]
  pymake7.py  vc init [ <env-name> ] [ -a | --all ]
  pymake7.py  vc deinit [ <env-name> ]
  pymake7.py  vc env [ <env-name> ]
  pymake7.py  vc clean [ here | hh ] [ there | tt ] [ default | dd ]
  pymake7.py  vc type [ here | hh ] [ there | tt ] [ default | dd ] [ <cmd-name> ] [ to <file-name> ]
  pymake7.py  vc use <env-name> type [ here | hh ] [ there | tt ] [ default | dd ] [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py  vc export [ here | hh ] [ there | tt ] [ default | dd ] [ <env-name> ] [ to <file-name> ]
  pymake7.py  vc exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc use <env-name> exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc use <env-name> execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc use <env-name> ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc powershell exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc powershell use <env-name> exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc powershell execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc powershell use <env-name> execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc powershell ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc powershell use <env-name> ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc python exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc python use <env-name> exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc python execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc python use <env-name> execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc python ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc python use <env-name> ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  vc language exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  vc language use <env-name> exec-with-params [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  vc language execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  vc language use <env-name> execvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  vc language ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  vc language use <env-name> ccvp [ here | hh ] [ there | tt ] [ default | dd ] [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ]
  pymake7.py  vc export2 [ powershell ] [ here | hh ] [ there | tt ] [ default | dd ] [ <env-name> ] [ to <file-name> ] [ -c | --custom ] [ -l | --local ] [ -s | --system ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  default clean
  pymake7.py  default export [ <env-name> ] [ to <file-name> ]
  pymake7.py  default type [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py  default use <env-name> exec [ <command-names> ... ]
  pymake7.py  default exec [ <command-names> ... ]
  pymake7.py  default use <env-name> cc [ <command-names> ... ]
  pymake7.py  default cc [ <command-names> ... ]
  pymake7.py  dd clean
  pymake7.py  dd export [ <env-name> ] [ to <file-name> ]
  pymake7.py  dd type [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py  dd use <env-name> exec [ <command-names> ... ]
  pymake7.py  dd exec [ <command-names> ... ]
  pymake7.py  dd use <env-name> cc [ <command-names> ... ]
  pymake7.py  dd cc [ <command-names> ... ]
  pymake7.py  default exec-with-params [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  default use <env-name> exec-with-params [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  dd exec-with-params [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  dd use <env-name> exec-with-params [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  default execvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  default use <env-name> execvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  dd execvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  dd use <env-name> execvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  default ccvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  default use <env-name> ccvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  dd ccvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  dd use <env-name> ccvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  default import cmd [ <script-file> ] [ to <command-name> ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --filter=<name-filter> ... ]
  pymake7.py  dd import cmd [ <script-file> ] [ to <command-name> ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --filter=<name-filter> ... ]
  pymake7.py  default outport cmd [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  dd outport cmd [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  default use <env-name> outport cmd [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  dd use <env-name> outport cmd [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  default backup [ <zip-file-name> ]
  pymake7.py  dd backup [ <zip-file-name> ]
  pymake7.py  default recovery [ <zip-file-name> ]
  pymake7.py  dd recovery [ <zip-file-name> ]
  pymake7.py  default export2 [ powershell ] [ <env-name> ] [ to <file-name> ] [ -c | --custom ] [ -l | --local ] [ -s | --system ]
  pymake7.py  default type2 [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  default use <env-name> type2 [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  dd export2 [ powershell ] [ <env-name> ] [ to <file-name> ] [ -c | --custom ] [ -l | --local ] [ -s | --system ]
  pymake7.py  dd type2 [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  dd use <env-name> type2 [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  there clean
  pymake7.py  there export [ <env-name> ] [ to <file-name> ]
  pymake7.py  there type [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py  there use <env-name> exec [ <command-names> ... ]
  pymake7.py  there exec [ <command-names> ... ]
  pymake7.py  there use <env-name> cc [ <command-names> ... ]
  pymake7.py  there cc [ <command-names> ... ]
  pymake7.py  tt clean
  pymake7.py  tt export [ <env-name> ] [ to <file-name> ]
  pymake7.py  tt type [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py  tt use <env-name> exec [ <command-names> ... ]
  pymake7.py  tt exec [ <command-names> ... ]
  pymake7.py  tt use <env-name> cc [ <command-names> ... ]
  pymake7.py  tt cc [ <command-names> ... ]
  pymake7.py  there exec-with-params [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  there use <env-name> exec-with-params [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  tt exec-with-params [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  tt use <env-name> exec-with-params [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  there execvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  there use <env-name> execvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  tt execvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  tt use <env-name> execvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  there ccvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  there use <env-name> ccvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  tt ccvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  tt use <env-name> ccvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  there import cmd [ <script-file> ] [ to <command-name> ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --filter=<name-filter> ... ]
  pymake7.py  tt import cmd [ <script-file> ] [ to <command-name> ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --filter=<name-filter> ... ]
  pymake7.py  there outport cmd [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  tt outport cmd [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  there use <env-name> outport cmd [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  tt use <env-name> outport cmd [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  there backup [ <zip-file-name> ]
  pymake7.py  tt backup [ <zip-file-name> ]
  pymake7.py  there recovery [ <zip-file-name> ]
  pymake7.py  tt recovery [ <zip-file-name> ]
  pymake7.py  there export2 [ powershell ] [ <env-name> ] [ to <file-name> ] [ -c | --custom ] [ -l | --local ] [ -s | --system ]
  pymake7.py  there type2 [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  there use <env-name> type2 [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  tt export2 [ powershell ] [ <env-name> ] [ to <file-name> ] [ -c | --custom ] [ -l | --local ] [ -s | --system ]
  pymake7.py  tt type2 [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  tt use <env-name> type2 [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  here clean
  pymake7.py  here export [ <env-name> ] [ to <file-name> ]
  pymake7.py  here type [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py  here use <env-name> exec [ <command-names> ... ]
  pymake7.py  here exec [ <command-names> ... ]
  pymake7.py  here use <env-name> cc [ <command-names> ... ]
  pymake7.py  here cc [ <command-names> ... ]
  pymake7.py  hh clean
  pymake7.py  hh export [ <env-name> ] [ to <file-name> ]
  pymake7.py  hh type [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py  hh use <env-name> exec [ <command-names> ... ]
  pymake7.py  hh exec [ <command-names> ... ]
  pymake7.py  hh use <env-name> cc [ <command-names> ... ]
  pymake7.py  hh cc [ <command-names> ... ]
  pymake7.py  here execvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  here use <env-name> execvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  hh execvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  hh use <env-name> execvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  here ccvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  here use <env-name> ccvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  hh ccvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  hh use <env-name> ccvp [ <command-name> ] [ <command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  here import cmd [ <script-file> ] [ to <command-name> ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --filter=<name-filter> ... ]
  pymake7.py  hh import cmd [ <script-file> ] [ to <command-name> ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --filter=<name-filter> ... ]
  pymake7.py  here outport cmd [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  hh outport cmd [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  here use <env-name> outport cmd [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  hh use <env-name> outport cmd [ <command-name> ] [ to <script-file> ] [ -r | --raw ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --encoding=<encoding-name> ] [ --suffix=<.suffix-name> ]
  pymake7.py  here backup [ <zip-file-name> ]
  pymake7.py  hh backup [ <zip-file-name> ]
  pymake7.py  here recovery [ <zip-file-name> ]
  pymake7.py  hh recovery [ <zip-file-name> ]
  pymake7.py  here exec-with-params [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  here use <env-name> exec-with-params [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  hh exec-with-params [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  hh use <env-name> exec-with-params [ <command-name> ] [ --params=<command-params> ... ] [ --workroot=<work-root-path> ]
  pymake7.py  here export2 [ powershell ] [ <env-name> ] [ to <file-name> ] [ -c | --custom ] [ -l | --local ] [ -s | --system ]
  pymake7.py  here type2 [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  here use <env-name> type2 [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  hh export2 [ powershell ] [ <env-name> ] [ to <file-name> ] [ -c | --custom ] [ -l | --local ] [ -s | --system ]
  pymake7.py  hh type2 [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  hh use <env-name> type2 [ <cmd-name> ] [ to <file-name> ] [ --suffix=<.suffix-name> ] [ --encoding=<encoding-name> ] [ --samename ] [ -a | --all ]
  pymake7.py  -------------------------------------------------------------
  pymake7.py  (-h | --help)
  pymake7.py  --version

Command:
  source            switch to another source file
  source root       config root directory
  source config     config source conf file
  set path          path assemblage
  set env           set env variable
  set cmd           set cmd stream
  export            output private env variable and paths to a bat file or sh file
  type              output command to a bat file or sh file
  see               check command stream
  ss                check command stream
  cmd               check command stream
  list              list config values, show command also too.
  set cur env       set default env, set current env.
  use               use selected env exec commands
  default           at default ( pymake default exec root ) do exec commands e.g. [default]
  dd                at default ( pymake default exec root ) do exec commands e.g. [default]
  there             at there (user default exec root) do exec commands e.g.
  tt                at there (user default exec root) do exec commands e.g.
  here              at here do exec commands e.g.
  hh                at here do exec commands e.g.
  exec              exec commands list.
  cc                exec commands list.
  have              check env or path or cmd item whether user has configured.
  has               check env or path or cmd item whether user has configured.
  clean             clean *_effect.sh *_unset.sh *_exec.sh, or .bat.
  program           pymake.py program information.
  get               lots of important information about pymake.py.
  initialize        if program crashed, user can use this command to reset.
  port              port from source to target .json file, configure source root and config file.
  translate         translate section from source to target, and other section.
  exec-with-params  exec a command with params, it is also execvp and ccvp.
  backup            backup all env .json to a zip file.
  recovery          recovery all env .json from a zip file.
  import            import user path or env or cmd to env .json file. example, import cmd [ <script-file>: x.bat x.cmd x.sh x.ps1 x.py x.java... ]
  custom            custom environment is helpping for calling large dimentions of scripts in computer, manually in console. defined in sourceroot. [ default: close ]
  powershell        environ for powershell, and to execute in powershell. [cross]
  python            list python information, and execute python script.
  outport           outport user path or env or cmd to script file. example, outport cmd [ <command-name> ] [ to <script-file>: ... ]
  language          find script file automatically and execute it. example, language ccvp java xxx.java ...
  local             using pymake local expanding environ, read only.
  system            using system environ, read only.
  export2           output private environ and custom environ to a bat file or sh file, a powerfull function from export, support powershell also. [default:current, env]
  type2             output command to a bat file or sh file, user can appoint file suffix and encoding.
  open              open path by stored name in path-assemblage. support .../${path-name}/..., support search in env, support two or more path.
  vc                start visual studio environment directly, easy to use. [system, local, custom, .json, vc]

Options:
  -h --help     Show this screen.
  --version     Show version.
  --add
  --del
  --mod         add or delete or modify a config or path
  --switch      switch to another source
  --show        display source config files
  --restore     reset to source config file pymake.json.
  -r, --raw     expand editing config values

  --encoding=<encoding-name>    script file encoding, support utf8, gbk, ansi, ... and so on. [default:utf8]
  --filter=<name-filter> ...    filter file name postfix, separated by |. example: .bat | .sh | .ps1 | .py | .java.
"""

import os
import re
import sys
import uuid
import shutil
import time
import json
import copy
import types
from pycore.pycore import *
from pycore.docopt import docopt


def main_function():

    d = {
        "path-assemblage": {
            "root": "/Users/abel/Develop",
            "root.src": "${root}/a0-develop",
            "root.prod": "${root}/d0-product",
            "root.sdk": "${root}/d1-sdks",
            "root.tool": "${root}/b0-toolskits",
            "root.build": "${root}/c0-buildstation",
            "root.test": "${root}/f0-test",
            "root.webrc": "${root}/e0-webrc",
            "cc": "${root.tool}/a0-compiler",
            "wincc": "${root.tool}/macCompilers",
			"cmake.bin": "${wincc}/CMake.app/Contents/bin",
            "pymake": "${cc}/PyMake",
            "qt": "${root.tool}/macLibraries/Qt",
            "qt4.8.version": "4.8.6",
            "qt4.8.clang": "${qt}/${qt4.8.version}/clang_64",
            "qt4.8.clang.bin": "${qt4.8.clang}/bin",
            "qt5.8.version": "5.8",
            "qt5.8.android_x86": "${qt}/${qt5.8.version}/android_x86",
            "qt5.8.android_x86.bin": "${qt5.8.android_x86}/bin",
            "qt5.8.android_arm": "${qt}/${qt5.8.version}/android_armv7",
            "qt5.8.android_arm.bin": "${qt5.8.android_arm}/bin",
            "qt5.8.clang": "${qt}/${qt5.8.version}/clang_64",
            "qt5.8.clang.bin": "${qt5.8.clang}/bin",
            "qt5.8.ios": "${qt}/${qt5.8.version}/ios",
            "qt5.8.ios.bin": "${qt5.8.ios}/bin",
            "qt5.9.version": "5.9.2",
            "qt5.9.ios": "${qt}/${qt5.9.version}/ios",
            "qt5.9.ios.bin": "${qt}/${qt5.9.version}/ios/bin",
            "qt5.9.clang": "${qt}/${qt5.9.version}/clang_64",
            "qt5.9.clang.bin": "${qt}/${qt5.9.version}/clang_64/bin",
            "qt5.9.android_arm": "${qt}/${qt5.9.version}/android_armv7",
            "qt5.9.android_arm.bin": "${qt}/${qt5.9.version}/android_armv7/bin",
            "qt5.9.android_x86": "${qt}/${qt5.9.version}/android_x86",
            "qt5.9.android_x86.bin": "${qt}/${qt5.9.version}/android_x86/bin",
            "android": "${root.tool}/macAndroidLibraries",
            "android.sdk": "${android}/android-sdk-macosx",
            "android.ndk": "${android}/android-ndk-r13b",
            "android.ant": "${android}/apache-ant-1.10.1",
            "android.java": "${android}/java-macosx/Java/JavaVirtualMachines",
            "sdk.plat.tool": "${android.sdk}/platform-tools",
            "sdk.build.tool": "${android.sdk}/build-tools",
            "sdk.tool": "${android.sdk}/tools",
            "java1.7.home": "${android.java}/jdk1.7.0_79.jdk/Contents/Home",
            "java1.8.home": "${android.java}/jdk1.8.0_111.jdk/Contents/Home",
            "java1.9.home": "${android.java}/jdk9.jdk/Contents/Home",
            "java1.7.bin": "${java1.7.home}/bin",
            "java1.8.bin": "${java1.8.home}/bin",
            "java1.9.bin": "${java1.9.home}/bin",
            "ant.bin": "${android.ant}/bin",
            "ndk.arm": "${android.ndk}/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64",
            "ndk.x86": "${android.ndk}/toolchains/x86-4.9/prebuilt/darwin-x86_64",
            "ndk.x86_64": "${android.ndk}/toolchains/x86_64-4.9/prebuilt/darwin-x86_64",
            "ndk.arm.bin": "${ndk.arm}/bin",
            "ndk.x86.bin": "${ndk.x86}/bin",
            "ndk.x86_64.bin": "${ndk.x86_64}/bin",
            "ios.simulator.sysroot": "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk",
            "xcode.bin": "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin",
            "mac.sysroot": "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk"
        },
        "environ": {
            "android.mobile": {
                "path+": [
                    "${qt5.9.android_arm.bin}",
                    "${java1.8.bin}",
                    "${android.sdk}",
                    "${sdk.plat.tool}",
                    "${sdk.build.tool}",
                    "${sdk.tool}",
                    "${ant.bin}",
                    "${ndk.arm.bin}"
                ],
                "make0": "make",
                "CMAKEGENERATOR": "Unix Makefiles",
                "ANDROID_API_VERSION": "android-23",
                "ANDROID_SDK_ROOT": "${android.sdk}",
                "ANDROID_NDK_ROOT": "${android.ndk}",
                "ANDROID_NDK_HOST": "darwin-x86_64",
                "ANDROID_NDK_TOOLCHAIN_PREFIX": "arm-linux-androideabi",
                "ANDROID_NDK_TOOLCHAIN_VERSION": "4.9",
                "ANDROID_NDK_PLATFORM": "android-23",
                "NDK_TOOLCHAIN_PATH": "${ndk.arm.bin}",
                "NDK_TOOLS_PREFIX": "arm-linux-androideabi",
                "QTVERSION": "${qt5.9.version}",
                "QTDIR": "${qt5.9.android_arm}",
                "QTSPEC": "-spec android-g++",
                "QTCONFIG": "",
                "JAVA_HOME": "${java1.8.home}",
                "CLASSPATH": ".:${JAVA_HOME}/lib/dt/jar:${JAVA_HOME}/lib/tools.jar",
                "PYMAKE_MYNAME": "T.D.R",
                "a_special_var_const": "hello world",
                "QKIT": "ANDROID",
                "QSYS": "Android"
            },
            "android.x86": {
                "path+": [
                    "${qt5.9.android_x86.bin}",
                    "${java1.8.bin}",
                    "${android.sdk}",
                    "${sdk.plat.tool}",
                    "${sdk.build.tool}",
                    "${sdk.tool}",
                    "${ant.bin}",
                    "${ndk.x86.bin}"
                ],
                "make0": "make",
                "CMAKEGENERATOR": "Unix Makefiles",
                "CLICOLOR": "1",
                "ANDROID_API_VERSION": "android-23",
                "ANDROID_HOME": "${android.sdk}",
                "ANDROID_SDK_ROOT": "${android.sdk}",
                "ANDROID_NDK_PLATFORM": "android-23",
                "ANDROID_NDK_ROOT": "${android.ndk}",
                "ANDROID_NDK_HOST": "darwin-x86_64",
                "ANDROID_NDK_TOOLCHAIN_PREFIX": "x86_64",
                "ANDROID_NDK_TOOLCHAIN_VERSION": "4.9",
                "ANDROID_NDK_TOOLS_PREFIX": "x86_64-linux-android",
                "NDK_TOOLCHAIN_PATH": "${ndk.x86.bin}",
                "NDK_TOOLS_PREFIX": "x86_64-linux-android",
                "PYMAKE_MYNAME": "T.D.R",
                "a_special_var_const": "hello world",
                "QTDIR": "${qt5.android_x86}",
                "QTSPEC": "-spec android-g++",
                "QTCONFIG": "",
                "JAVA_HOME": "${java1.8.home}",
                "CLASSPATH": ".:${JAVA_HOME}/lib/dt/jar:${JAVA_HOME}/lib/tools.jar",
                "QTVERSION": "${qt5.android_x86.version}",
                "QKIT": "ANDROIDX86",
                "QSYS": "AndroidX86"
            },
            "qt4": {
                "path+": [
                    "${qt4.8.clang.bin}"
                ],
                "make0": "make",
                "CMAKEGENERATOR": "Unix Makefiles",
                "QTVERSION": "${qt4.version}",
                "QTDIR": "${qt4.8.clang}",
                "QTSPEC": "-spec macx-llvm",
                "QTCONFIG": "CONFIG+=x86_64",
                "QKIT": "macOS",
                "QSYS": "macOS"
            },
            "ios": {
                "path+": [
                    "${qt5.9.ios.bin}"
                ],
                "make0": "make",
                "CMAKEGENERATOR": "Unix Makefiles",
                "QTVERSION": "${qt5.9.version}",
                "QTDIR": "${qt5.9.ios}",
                "QTSPEC": "-spec macx-ios-clang",
                "QTCONFIG": "CONFIG+=iphoneos CONFIG+=device -after QMAKE_MAC_XCODE_SETTINGS+=qteam qteam.name=DEVELOPMENT_TEAM qteam.value=4EGMLT3G6T",
                "QKIT": "iOS",
                "QSYS": "iOS"
            },
            "iossimulator": {
                "path+": [
                    "${qt5.9.ios.bin}"
                ],
                "make0": "make",
                "CMAKEGENERATOR": "Unix Makefiles",
                "QTVERSION": "${qt5.9.version}",
                "QTDIR": "${qt5.9.ios}",
                "QTSPEC": "-spec macx-ios-clang",
                "QTCONFIG": "CONFIG+=iphonesimulator CONFIG+=simulator",
                "QKIT": "iOSSimulator",
                "QSYS": "iOSSimulator"
            },
            "macos": {
                "path+": [
                    "${qt5.9.clang.bin}"
                ],
                "make0": "make",
                "CMAKEGENERATOR": "Unix Makefiles",
                "QTVERSION": "${qt5.9.version}",
                "QTDIR": "${qt5.9.clang}",
                "QTSPEC": "-spec macx-clang",
                "QTCONFIG": "CONFIG+=x86_64",
                "QKIT": "macOS",
                "QSYS": "macOS"
            },
            "current": "macos"
        },
        "command": {
            "test": [
                "echo $(pwd)"
            ],
            "test.6": [
                "echo 中文"
            ],
            "test.7": [
                "echo $PATH"
            ],
            "qqt.build": [
                "src_path=${root.src}/LibQQt",
                "src=${root.src}/LibQQt/QQt.pro",
                "build=${root.build}/QQt/$QSYS/$QTVERSION/Debug",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "qmake ${src} $QTSPEC CONFIG+=debug CONFIG+=qml_debug $QTCONFIG && make qmake_all",
                "make -j4"
            ],
            "qqt.clean": [
                "src=${root.src}/LibQQt/QQt.pro",
                "build=${root.build}/QQt/$QSYS/$QTVERSION/Debug",
                "cd $build",
                "make clean"
            ],
            "qt": [
                "open \"/Applications/Qt Creator.app\""
            ],
            "cmake0": [
                "open ${wincc}/CMake.app"
            ],
            "prod": [
                "open /Users/abel/Develop/d0-product/ProductExecTool/macOS/ProductExecTool_debug.app"
            ],
            "libtool": [
                "open /Users/abel/Develop/d0-product/AddLibraryTool/macOS/AddLibraryTool_debug.app"
            ],
            "qt.check": [
                "src=${root.tool}/z0-Source/qt-everywhere-opensource-src-4.8.7",
                "build=${root.build}/qt4.8.7",
                "install=${root.tool}/macLibraries/Qt/4.8.7/gcc_64",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "${src}/configure --help"
            ],
            "qt4.build": [
                "src=${root.tool}/z0-Source/qt",
                "build=${root.build}/qt",
                "install=${root.tool}/macLibraries/Qt/4.8/gcc_64",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "CXXFLAGS=-stdlib=libc++",
                "${src}/configure -prefix ${install}",
                "make -j4",
                "make install"
            ],
            "qt4.8.7.build": [
                "src=${root.tool}/z0-Source/qt-everywhere-opensource-src-4.8.7",
                "build=${root.build}/qt4.8.7",
                "install=${root.tool}/macLibraries/Qt/4.8.7/gcc_64",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "${src}/configure -prefix ${install}",
                "make -j4",
                "make install"
            ],
            "qtsoap.build": [
                "src=/Users/abel/Develop/c1-webrc/qt-solutions/qtsoap",
                "build=${root.build}/qtsoap",
                "install=/Users/abel/Develop/d1-product/QtSoap",
                "cd $build",
                "${src}/configure -library"
            ],
            "qqt.push": [
                "src=${root.src}/LibQQt",
                "cd $src",
                "git push",
                "git push --tag"
            ],
            "qqt.pull": [
                "src=${root.src}/LibQQt",
                "cd $src",
                "git pull"
            ],
            "qqt.cloc": [
                "src=${root.src}/LibQQt",
                "cd $src",
                "perl ${pymake}/demo/cloc-1.74.pl  .",
                "date"
            ],
            "android.sdk": [
                "/Users/abel/Develop/b0-toolskits/macAndroidLibraries/android-sdk-macosx/tools/android"
            ],
            "test.2": [
                "#echo $*",
                "param=$*",
                "ping 127.0.0.1 $param"
            ],
            "open-dir": [
                "open $1"
            ],
            "daily.qqt": [
                "src_path=/Users/abel/Develop/a0-develop/LibQQt",
                "src=$src_path/QQt.pro",
                "build=/Users/abel/Develop/c0-buildstation/QQt/$QSYS/$QTVERSION/Debug",
                "mkdir -p $build",
                "cd $build",
                "rm -rf src examples",
                "qmake $src $QTSPEC $QTCONFIG CONFIG+=debug CONFIG+=qml_debug && make qmake_all",
                "make -j4"
            ],
            "daily.qqt.release": [
                "src_path=/Users/abel/Develop/a0-develop/LibQQt",
                "src=$src_path/QQt.pro",
                "build=/Users/abel/Develop/c0-buildstation/QQt/$QSYS/$QTVERSION/Release",
                "mkdir -p $build",
                "cd $build",
                "rm -rf src examples",
                "qmake $src $QTSPEC $QTCONFIG CONFIG+=release && make qmake_all",
                "make -j4"
            ],
            "build.qqt": [
                "src_path=/Users/abel/Develop/a0-develop/LibQQt",
                "src=/Users/abel/Develop/a0-develop/LibQQt/QQt.pro",
                "build=/Users/abel/Develop/c0-buildstation/QQt/$QSYS/$QTVERSION/Debug",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "qmake ${src} $QTSPEC CONFIG+=debug CONFIG+=qml_debug $QTCONFIG && make qmake_all",
                "make -j4"
            ],
            "build.qqt.release": [
                "src_path=/Users/abel/Develop/a0-develop/LibQQt",
                "src=$src_path/QQt.pro",
                "build=/Users/abel/Develop/c0-buildstation/QQt/$QSYS/$QTVERSION/Release",
                "mkdir -p $build",
                "cd $build",
                "qmake $src $QTSPEC $QTCONFIG CONFIG+=release && make qmake_all",
                "make -j4"
            ],
            "clean.qqt": [
                "src=/Users/abel/Develop/a0-develop/LibQQt/QQt.pro",
                "build=/Users/abel/Develop/c0-buildstation/QQt/$QSYS/$QTVERSION/Debug",
                "cd $build",
                "make clean"
            ],
            "clean.qqt.release": [
                "src=/Users/abel/Develop/a0-develop/LibQQt/QQt.pro",
                "build=/Users/abel/Develop/c0-buildstation/QQt/$QSYS/$QTVERSION/Release",
                "cd $build",
                "make clean"
            ],
            "check.qt": [
                "src=/Users/abel/Develop/b0-toolskits/z0-Source/qt-everywhere-opensource-src-4.8.7",
                "build=/Users/abel/Develop/c0-buildstation/qt4.8.7",
                "install=/Users/abel/Develop/b0-toolskits/macLibraries/Qt/4.8.7/gcc_64",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "${src}/configure --help"
            ],
            "build.qt": [
                "src=/Users/abel/Develop/b0-toolskits/z0-Source/qt",
                "build=/Users/abel/Develop/c0-buildstation/qt",
                "install=/Users/abel/Develop/b0-toolskits/macLibraries/Qt/4.8/gcc_64",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "CXXFLAGS=-stdlib=libc++",
                "${src}/configure -prefix ${install}",
                "make -j4",
                "make install"
            ],
            "build.qt4.8.7": [
                "src=/Users/abel/Develop/b0-toolskits/z0-Source/qt-everywhere-opensource-src-4.8.7",
                "build=/Users/abel/Develop/c0-buildstation/qt4.8.7",
                "install=/Users/abel/Develop/b0-toolskits/macLibraries/Qt/4.8.7/gcc_64",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "${src}/configure -prefix ${install}",
                "make -j4",
                "make install"
            ],
            "build.soap": [
                "src=/Users/abel/Develop/c1-webrc/qt-solutions/qtsoap",
                "build=/Users/abel/Develop/c0-buildstation/qtsoap",
                "install=/Users/abel/Develop/d1-product/QtSoap",
                "cd $build",
                "${src}/configure -library"
            ],
            "push.qqt": [
                "src=/Users/abel/Develop/a0-develop/LibQQt",
                "cd $src",
                "git push",
                "git push --tag"
            ],
            "pull.qqt": [
                "src=/Users/abel/Develop/a0-develop/LibQQt",
                "cd $src",
                "git pull"
            ],
            "cloc.qqt": [
                "src=/Users/abel/Develop/a0-develop/LibQQt",
                "cd $src",
                "perl ${pymake}/demo/cloc-1.74.pl  .",
                "date"
            ],
            "cloc.light": [
                "src=/Users/abel/Develop/a0-develop/LightUnderWater/App",
                "cd $src",
                "perl /Users/abel/Develop/b1-buildshell/cloc-1.74.pl  .",
                "date"
            ],
            "qtdir": [
                "echo $QTDIR"
            ],
            "test.3": [
                "#echo $*",
                "ping $*"
            ],
            "test.4": [
                "echo param1: $1",
                "echo param2: $2",
                "echo param3: $3",
                "echo param4: $4"
            ],
            "build.qmake": [
                "while [ 1 ]",
                "do",
                "src_path=$(pwd)",
                "profilename=$1",
                "if [ \"$profilename\" == \"\" ]; then",
                "   echo please input a project name",
                "   break",
                "fi",
                "if [ -f \"$1.pro\" ]; then",
                "   echo $1.pro existed.",
                "else",
                "   echo has $1.pro? please add here command to restrict.",
                "   break",
                "fi",
                "src=$src_path/$profilename.pro",
                "build=${root.build}/$profilename/$QSYS/$QTVERSION/Debug",
                "prod=${root.prod}/$profilename/$QSYS",
                "sdk=${root.sdk}/$profilename/$QSYS",
                "mkdir -p $build",
                "cd $build",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "echo build at: $build",
                "echo $QTSPEC $QTCONFIG",
                "qmake $src $QTSPEC CONFIG+=debug CONFIG+=qml_debug $QTCONFIG && make qmake_all",
                "make -j4",
                "echo build inf $QTSPEC $QTCONFIG",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo build at: $build",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "break",
                "done"
            ],
            "cmake": [
                "while [ 1 ]",
                "do",
                "src_path=$(pwd)",
                "profilename=$1",
                "if [ \"$profilename\" == \"\" ]; then",
                "   echo please input a project name",
                "   break",
                "fi",
                "if [ -f \"CMakeLists.txt\" ]; then",
                "   echo CMakeLists.txt existed.",
                "else",
                "   echo has CMakeLists.txt? please add here command to restrict.",
                "   break",
                "fi",
                "src=$src_path/CMakeLists.txt",
                "build=${root.build}/$profilename/$QSYS/$QTVERSION/Debug",
                "prod=${root.prod}/$profilename/$QSYS",
                "sdk=${root.sdk}/$profilename/$QSYS",
                "mkdir -p $build",
                "cd $build",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "echo build at: $build",
                "echo $QTSPEC $QTCONFIG",
                "open ${wincc}/CMake.app",
                "errorlevel=$?",
                "if [ $errorlevel -ne 0 ]; then",
                "   echo cmake exit code: $errorlevel",
                "   break",
                "fi",
                "echo build inf $QTSPEC $QTCONFIG",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo build at: $build",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "break",
                "done"
            ],
            "build.cmake.sdk": [
                "while [ 1 ]",
                "do",
                "src_path=$(pwd)",
                "profilename=$1",
                "if [ \"$profilename\" == \"\" ]; then",
                "   echo please input a project name",
                "   break",
                "fi",
                "if [ -f \"CMakeLists.txt\" ]; then",
                "   echo CMakeLists.txt existed.",
                "else",
                "   echo has CMakeLists.txt? please add here command to restrict.",
                "   break",
                "fi",
                "src=$src_path/CMakeLists.txt",
                "build=${root.build}/$profilename/$QSYS/$QTVERSION/Debug",
                "prod=${root.prod}/$profilename/$QSYS",
                "sdk=${root.sdk}/$profilename/$QSYS",
                "mkdir -p $build",
                "cd $build",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "echo build at: $build",
                "echo $QTSPEC $QTCONFIG",
                "cmake $src_path -G\"$CMAKEGENERATOR\" -DCMAKE_INSTALL_PREFIX=${root.sdk}/$profilename/$QSYS -DCMAKE_BUILD_TYPE=Debug",
                "errorlevel=$?",
                "if [ $errorlevel -ne 0 ]; then",
                "   echo cmake exit code: $errorlevel",
                "   break",
                "fi",
                "echo build inf $QTSPEC $QTCONFIG",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo build at: $build",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "break",
                "done"
            ],
            "build.cmake.app": [
                "while [ 1 ]",
                "do",
                "src_path=$(pwd)",
                "profilename=$1",
                "if [ \"$profilename\" == \"\" ]; then",
                "   echo please input a project name",
                "   break",
                "fi",
                "if [ -f \"CMakeLists.txt\" ]; then",
                "   echo CMakeLists.txt existed.",
                "else",
                "   echo has CMakeLists.txt? please add here command to restrict.",
                "   break",
                "fi",
                "src=$src_path/CMakeLists.txt",
                "build=${root.build}/$profilename/$QSYS/$QTVERSION/Debug",
                "prod=${root.prod}/$profilename/$QSYS",
                "sdk=${root.sdk}/$profilename/$QSYS",
                "mkdir -p $build",
                "cd $build",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "echo build at: $build",
                "echo $QTSPEC $QTCONFIG",
                "cmake $src_path -G\"$CMAKEGENERATOR\" -DCMAKE_INSTALL_PREFIX=${root.prod}/$profilename/$QSYS -DCMAKE_BUILD_TYPE=Debug",
                "errorlevel=$?",
                "if [ $errorlevel -ne 0 ]; then",
                "   echo cmake exit code: $errorlevel",
                "   break",
                "fi",
                "echo build inf $QTSPEC $QTCONFIG",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo build at: $build",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "break",
                "done"
            ],
            "test.5": [
                "exit 0"
            ]
        }
    }

    # record current directory [pwd, execute path]
    pymakeworkpath = os.getcwd()
    #print( "pymake work path:", pymakeworkpath )
    #here work root

    # record pymake file directory [program file path]
    pymakefilepath = os.path.split(os.path.realpath(__file__))[0]
    #print( "pymake file path:", pymakefilepath )

    # record pymake user source root [env, *.json] [ + auto create ]
    pymakesourceroot = pymakefilepath + os.path.sep + 'UserSource'
    if (not os.path.exists(pymakesourceroot)):
        os.makedirs(pymakesourceroot)
    #print( "pymake user source path:", pymakesourceroot )

    #record default user source config file name
    pymakedefaultsourcefile = 'pymake.json'
    #print( "pymake user default source file:", pymakedefaultsourcefile )

    # record pymake user shell root [ dynamic work path ]
    pymakeshellroot = pymakesourceroot + os.path.sep + 'UserShell'
    if (not os.path.exists(pymakeshellroot)):
        os.makedirs(pymakeshellroot)
    #print( "pymake user shell path:", pymakeshellroot )
    #default work root

    """
    [pymake]

    [source]
    root = $pymakesourceroot
    config = pymake.json
    """
    userroot = getuserroot()
    configroot = getconfigroot()
    plat = getplatform()
    #record pymake configure directory. [ in user config path ]
    pymakeroot = userroot + os.path.sep + '.pymake'
    if (not os.path.exists(pymakeroot)):
        os.makedirs(pymakeroot)

    #initial pymake.ini
    pymakeini = pymakeroot + os.path.sep + 'pymake.ini'
    conf = MyConfigParser()
    conf.read(pymakeini)
    if( not conf.has_section('pymake') ):
        conf.add_section('pymake')
        conf.write(open(pymakeini, 'w'))
    if( not conf.has_section('source') ):
        conf.add_section('source')
        conf.write(open(pymakeini, 'w'))
    if( not conf.has_option('source', 'root') ):
        conf.set('source', 'root', pymakesourceroot)
        conf.write(open(pymakeini, 'w'))
    if(not conf.has_option('source', 'config')):
        conf.set('source', 'config', pymakedefaultsourcefile)
        conf.write(open(pymakeini, 'w'))

    args = docopt(__doc__, version='pymake7.py v7.8.3')
    #print(args)

    #initialize
    while (True):
        if(args['initialize'] is True):
            conf.set('source', 'root', pymakesourceroot)
            conf.set('source', 'config', pymakedefaultsourcefile)
            conf.write(open(pymakeini, 'w'))
            r = conf.get('source', 'root')
            f = conf.get('source', 'config')
            print("SOURCE        : %s%s%s" % (r, os.path.sep, f))
            print("SOURCE ROOT   : %s" % (r))
            print("SOURCE CONFIG : %s" % (f))

            print("successed")
            return
        else:
            ""
        break

    # init pymake.json in sourceroot [ + program create ]
    #record user source root directory
    sourceroot = conf.get('source', 'root')
    #record source config file name
    sourcefile = conf.get('source', 'config')
    #record source config file
    sourceconfigfile = sourceroot + os.path.sep + sourcefile
    #print("root: %s, config: %s" % (sourceroot, sourcefile))
    #print("use source config: %s" % (sourceconfigfile) )
    #record default source config file
    defaultsourceconfigfile = sourceroot + os.path.sep + pymakedefaultsourcefile
    #print ("root: %s, default config: %s" % (sourceroot, pymakedefaultsourcefile))
    #print("default source config: %s" % (defaultsourceconfigfile) )

    #check source root
    #prepare to user source root
    if (not os.path.exists(sourceroot)):
        os.makedirs(sourceroot)
    os.chdir(sourceroot)

    # check default source file [default:d]
    if (os.path.exists(sourceroot)):
        if (os.path.abspath(sourceroot) != os.path.abspath(pymakeroot)
            and os.path.abspath(sourceroot) != os.path.abspath(pymakefilepath)):
            if (not os.path.exists(defaultsourceconfigfile)):
                writeJsonData(defaultsourceconfigfile, d)

    #check source file [default:d]
    if (os.path.exists(sourceroot)):
        if (os.path.abspath(sourceroot) != os.path.abspath(pymakeroot)
            and os.path.abspath(sourceroot) != os.path.abspath(pymakefilepath)):
            if (not os.path.exists(sourceconfigfile)):
                writeJsonData(sourceconfigfile, d)

    def open_file(file0):
        plat = getplatform()
        cmd0 = ''
        if (plat == "Windows"):
            if (file0.__contains__(' ')):
                cmd0 = 'start "" ' + '"%s"' % file0
            else:
                cmd0 = "start " + file0
        elif (plat == "Darwin"):
            if (file0.__contains__(' ')):
                cmd0 = 'open ' + '"%s"' % file0
            else:
                cmd0 = "open " + file0
        else:
            if (file0.__contains__(' ')):
                cmd0 = 'xdg-open ' + '"%s" ' % file0 + ">/dev/null 2>&1"
            else:
                cmd0 = "xdg-open " + '%s ' % file0 + ">/dev/null 2>&1"
        return cmd0

    #record source config file postfix
    pymakesuffix = '.json'
    #source
    while (True):
        if(args['source'] is True):
            if(args['root'] is True):
                if ( args['<source-root-path>'] is not None):
                    r = args['<source-root-path>']
                    if(os.path.isabs(r) is False):
                        r = pymakeworkpath + os.path.sep + args['<source-root-path>']
                    if(os.path.isdir(r) is False):
                        print("failed: %s is not a dir." % args['<source-root-path>'])
                        return
                    conf.set('source', 'root', r)
                    conf.write(open(pymakeini, 'w'))
                    print ("successed: change source root to %s" % r)
                else:
                    print ("%s" % conf.get('source', 'root'))
            elif(args['config'] is True):
                sourceroot = conf.get('source', 'root')
                if(args['--del'] is True):
                    if (args['<config-file-name>'] is not None and args['<config-file-name>'] == 'pymake.json'):
                        print('You can\'t remove pymake\'s file...')
                    elif (args['<config-file-name>'] is not None and args['<config-file-name>'].endswith(pymakesuffix)):
                        os.remove(args['<config-file-name>'])
                        conf.set('source', 'config', 'pymake.json')
                        conf.write(open(pymakeini, 'w'))
                        print ("successed: %s" % args['<config-file-name>'])
                    else:
                        print ('You can\'t remove pymake.json and un.json\'s file...')
                elif(args['--add'] is True):
                    if (args['<config-file-name>'] is not None and args['<config-file-name>'].endswith(pymakesuffix) and args['<config-file-name>'] != 'pymake.json'):
                        f = conf.get('source', 'config')
                        if( f != args['<config-file-name>']):
                            shutil.copyfile(f, args['<config-file-name>'])
                            conf.set('source', 'config', args['<config-file-name>'])
                            conf.write(open(pymakeini, 'w'))
                            print ("successed: %s" % args['<config-file-name>'])
                        else:
                            print('You can\'t add same named file...')
                    else:
                        print ('You can\'t add pymake.json and un.json\'s file...')
                elif (args['--mod'] is True):
                    if ( ( args['<config-file-name>'] and args['<new-config-file-name>']) is not None and args['<config-file-name>'].endswith(pymakesuffix)):
                        os.rename(args['<config-file-name>'],args['<new-config-file-name>'])
                        f = conf.get('source', 'config')
                        if (f == args['<config-file-name>']):
                            conf.set('source', 'config',args['<new-config-file-name>'])
                            conf.write(open(pymakeini, 'w'))
                        print ("successed: %s" % args['<new-config-file-name>'])
                    else:
                        print ('You can\'t mod pymake.json and un.json\'s file...')
                elif(args['--show'] is True):
                    files = os.listdir(os.getcwd())
                    for f in files:
                        if (f.endswith(pymakesuffix)):
                            print(f)
                    return
                elif (args['--edit'] is True):
                    file0 = 'pymake.json'
                    if(args['<config-file-name>'] is None):
                        file0 = sourcefile
                    else:
                        if(os.path.isfile(args['<config-file-name>']) is False):
                            print ('please input an existed .json file.')
                            return
                        file0 = args['<config-file-name>']

                    cmd0 = open_file(file0)
                    os.system(cmd0)
                    print('successed: %s' % file0)
                    return
                elif(args['--restore'] is True):
                    conf.set('source', 'config', 'pymake.json')
                    conf.write(open(pymakeini, 'w'))
                    print ("successed: %s" % 'pymake.json')
                elif (args['--switch'] is True or ( args['<config-file-name>'] is not None )):
                    if (args['<config-file-name>'] is not None and args['<config-file-name>'].endswith(pymakesuffix) ):
                        if (os.path.exists(args['<config-file-name>'])):
                            conf.set('source', 'config', args['<config-file-name>'])
                            conf.write(open(pymakeini, 'w'))
                            print("successed: switch to source config %s" % args['<config-file-name>'])
                        else:
                            print("failed: source file %s isn't exists, please --add it" % args['<config-file-name>'])
                    else:
                        print ('You can\'t switch pymake.json and un.json\'s file...')
                else:
                    print ("%s" % conf.get("source", "config"))
            elif (args['file'] is True):
                if(args['<source-path-file>'] is None):
                    #print("please input an abspath .json file.")
                    r = conf.get('source', 'root')
                    f = conf.get('source', 'config')
                    print("%s%s%s" % (r, os.path.sep, f))
                    return
                #path0 = args['<source-path-file>']
                #path1 = os.path.relpath(args['<source-path-file>'], pymakeworkpath)
                #path2 = os.path.relpath(args['<source-path-file>'], pymakesourceroot)
                #path3 = os.path.relpath(args['<source-path-file>'], pymakeshellroot)
                #print ("source config file: %s" % path0)
                #print ("rel path: pwd     : %s" % path1)
                #print ("rel path: src     : %s" % path2)
                #print ("rel path: exec    : %s" % path3)
                #print ("real path: %s" % os.path.realpath(path0))
                #print ("real path: %s" % os.path.realpath(path1))
                #print ("real path: %s" % os.path.realpath(path2))
                #print ("real path: %s" % os.path.realpath(path3))
                #print ("abspath: %s" % os.path.abspath(path0))
                #print ("abspath: %s" % os.path.abspath(path1))
                #print ("abspath: %s" % os.path.abspath(path2))
                #print ("abspath: %s" % os.path.abspath(path3))
                if(not args['<source-path-file>'].endswith(pymakesuffix)):
                    print("you can't set an un.json file.")
                    return
                if(os.path.isdir(args['<source-path-file>'])):
                    print("please input an abspath .json file.")
                    return
                #if(os.path.islink(args['<source-path-file>'])):
                #    print("your file path cant be a link.")
                #    return
                if(not os.path.isabs(args['<source-path-file>'])):
                    print("your file path is not an abspath.")
                    return
                r = os.path.split(os.path.realpath(args['<source-path-file>']))[0]
                f = os.path.split(os.path.realpath(args['<source-path-file>']))[1]
                conf.set('source', 'root', r)
                conf.set('source', 'config', f)
                conf.write(open(pymakeini, 'w'))
                print ("change source to %s" % os.path.realpath(args['<source-path-file>']))
                print ("source root    : %s" % r)
                print ("source config  : %s" % f)
            else:
                r = conf.get('source', 'root')
                f = conf.get('source', 'config')
                print ("%s%s%s" % (r, os.path.sep, f))

            # check source status
            # record user source root directory
            sourceroot = conf.get('source', 'root')
            # record source config file name
            sourcefile = conf.get('source', 'config')
            # record source config file
            sourceconfigfile = sourceroot + os.path.sep + sourcefile
            # print ("root: %s config: %s" % (sourceroot, sourcefile))
            # print("use source config: %s" % (sourceconfigfile) )
            if (not os.path.exists(sourceroot)):
                os.makedirs(sourceroot)
            os.chdir(sourceroot)
            if (os.path.exists(sourceroot)):
                if (os.path.abspath(sourceroot) != os.path.abspath(pymakeroot)
                    and os.path.abspath(sourceroot) != os.path.abspath(pymakefilepath)):
                    if (not os.path.exists(sourceconfigfile)):
                        writeJsonData(sourceconfigfile, d)
            return
        else:
            ''
        break

    # check source root directory
    if (os.path.exists(sourceroot) is False):
        print("You have changed sourceroot manually, please change it using source command")
        return

    # check source root .json file
    if (os.path.abspath(sourceroot) == os.path.abspath(pymakeroot) or
            os.path.abspath(sourceroot) == os.path.abspath(pymakefilepath)):
        print ("I checked you use pymakeroot or pymakefileroot to be sourceroot, suggestting you use source command changing one.")
        print ("this progrom can store building env and building command forever, please repleace source root then using me.")
        return
    elif (os.path.abspath(sourceroot) != os.path.abspath(pymakeroot)):
        if (not os.path.exists(defaultsourceconfigfile)):
            writeJsonData(defaultsourceconfigfile, d)
            print ("initialize pymake.json in source root %s." % sourceroot)
        if(not os.path.exists(sourceconfigfile)):
            print ("source config file %s is not existed." % sourceconfigfile)
            print ("You can use source command to fix it.")
            return

    # record user shell root directory [default]
    shellroot = sourceroot + os.path.sep + "UserShell"
    # print("execute directory: %s" % (shellroot) )
    
    # support pymake default shell root, pymake custom shell root, pymake current shell root.
    pymakeexecini = sourceroot + os.path.sep + 'exec.ini'
    execconf = MyConfigParser()
    execconf.read(pymakeexecini)
    if( not execconf.has_section('exec') ):
        execconf.add_section('exec')
        execconf.write(open(pymakeexecini, 'w'))
    if( not execconf.has_section('work') ):
        execconf.add_section('work')
        execconf.write(open(pymakeexecini, 'w'))
    if( not execconf.has_section('root') ):
        execconf.add_section('root')
        execconf.write(open(pymakeexecini, 'w'))
    if( not execconf.has_option('work', 'where') ):
        execconf.set('work', 'where', 'default')
        execconf.write(open(pymakeexecini, 'w'))
    if(not execconf.has_option('root', 'default')):
        execconf.set('root', 'default', pymakeshellroot)
        execconf.write(open(pymakeexecini, 'w'))
    if( not execconf.has_option('root', 'there') ):
        execconf.set('root', 'there', pymakeshellroot)
        execconf.write(open(pymakeexecini, 'w'))
    if(not execconf.has_option('root', 'here')):
        execconf.set('root', 'here', '')
        execconf.write(open(pymakeexecini, 'w'))

    # record pymake custom shell root [ user custom work path ]
    workroottype = execconf.get('work', 'where')
    customshellroot = execconf.get('root', 'there')
    if (not os.path.exists(customshellroot)):
        os.makedirs(customshellroot)
    #custom work root

    if(workroottype == 'default'):
       shellroot = pymakeshellroot
    elif (workroottype == 'here'):
       shellroot = pymakeworkpath
    elif (workroottype == 'there'):
       shellroot = customshellroot

    # if(workroottype == 'default'):
    #    print("WORK STARTING : %s" % (pymakeshellroot))
    # elif (workroottype == 'here'):
    #    print("WORK STARTING : %s" % (pymakeworkpath))
    # elif (workroottype == 'there'):
    #    print("WORK STARTING : %s" % (c))
    # print("execute directory: %s" % (shellroot) )

    # I set this,
    # pymake execute user bat/sh in shellroot,
    # user can use here param to restrict exec action.
    # cd user shell root [ default shell execute path ]
    #prepare to user shell root
    if (not os.path.exists(shellroot)):
        os.makedirs(shellroot)
    os.chdir(shellroot)

    #backup
    while (True):
        if ( args['backup'] is True ):
            import zipfile

            #os.chdir(sourceroot)

            if(args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)
            elif(args['there'] or args['tt'] is True):
                os.chdir(customshellroot)
            elif(args['default'] or args['dd'] is True):
                os.chdir(pymakeshellroot)

            #print(args['<zip-file-name>'])
            if(args['<zip-file-name>'] is None):
                files = os.listdir(os.getcwd())
                for f in files:
                    if (f.endswith('.zip')):
                        print(f)
                return

            file = os.path.realpath(args['<zip-file-name>'])
            if (file.endswith('.zip') is False):
                print("please use a .zip file name.")
                return

            os.chdir(sourceroot)

            files = os.listdir(os.getcwd())
            if ( files.__len__() < 1 ):
                print("has no .json file in %s" % sourceroot)
                return

            ziphandle = zipfile.ZipFile(file, 'w')
            for f in files:
                if (f.endswith('.json') or f.endswith('.ini')):
                    print(f)
                    ziphandle.write(f, compress_type=zipfile.ZIP_DEFLATED)
            ziphandle.close()
            return
        else:
            ''
        break

    # recovery
    while (True):
        if ( args['recovery'] is True ):
            import zipfile

            #os.chdir(sourceroot)

            if(args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)
            elif(args['there'] or args['tt'] is True):
                os.chdir(customshellroot)
            elif(args['default'] or args['dd'] is True):
                os.chdir(pymakeshellroot)

            #print(args['<zip-file-name>'])
            if(args['<zip-file-name>'] is None):
                files = os.listdir(os.getcwd())
                for f in files:
                    if (f.endswith('.zip')):
                        print(f)
                return

            file = os.path.realpath(args['<zip-file-name>'])
            if (file.endswith('.zip') is False):
                print("please use a .zip file name.")
                return

            #ziphandle = zipfile.ZipFile(file, 'r')
            #print(ziphandle.testzip())
            #if(ziphandle.testzip() is None):
            #    ziphandle.close()
            #    print("it is not a valid zip file.")
            #    return
            #ziphandle.close()

            os.chdir(sourceroot)

            files = os.listdir(os.getcwd())
            num = 0
            for f in files:
                if(f.endswith('.json')):
                    num += 1
            #print(num)
            if ( num > 1 ):
                print("there are %d .json files in %s" % ( num, sourceroot ) )
                print("please remove them.")
                return

            ziphandle = zipfile.ZipFile(file, 'r')
            ziphandle.extractall()
            for f in ziphandle.namelist():
                print(f)
            ziphandle.close()
            return
        else:
            ''
        break

    #port translate function
    portdefaultsourceconfig = pymakedefaultsourcefile
    portdefaulttargetconfig = 'temporary-target.json'
    portiniconfig = 'port.ini'
    portinifile = os.path.join(sourceroot, "port.ini")
    def init_portconf():
        portconf = MyConfigParser()
        portconf.read(portinifile)
        if (not portconf.has_section('port')):
            portconf.add_section('port')
            portconf.write(open(portinifile, 'w'))
        if (not portconf.has_option('port', 'sourceroot')):
            portconf.set('port', 'sourceroot', sourceroot)
            portconf.write(open(portinifile, 'w'))
        if (not portconf.has_option('port', 'sourceconfig')):
            portconf.set('port', 'sourceconfig', portdefaultsourceconfig)
            portconf.write(open(portinifile, 'w'))
        if (not portconf.has_option('port', 'targetroot')):
            portconf.set('port', 'targetroot', sourceroot)
            portconf.write(open(portinifile, 'w'))
        if (not portconf.has_option('port', 'targetconfig')):
            portconf.set('port', 'targetconfig', portdefaulttargetconfig)
            portconf.write(open(portinifile, 'w'))
        #print (portinifile)
        #print ("sourceroot  :", portconf['port']['sourceroot'])
        #print ("sourceconfig:", portconf['port']['sourceconfig'])
        #print ("targetroot  :", portconf['port']['targetroot'])
        #print ("targetconfig:", portconf['port']['targetconfig'])
        return portconf, portinifile

    def init_portconfig(portconf = MyConfigParser()):
        portsourceconfigfile=os.path.join(portconf['port']['sourceroot'], portconf['port']['sourceconfig'])
        porttargetconfigfile=os.path.join(portconf['port']['targetroot'], portconf['port']['targetconfig'])
        d_temp = {
            "path-assemblage": {
            },
            "environ":{
                "default":{
                    "path+": [
                    ]
                },
                "current": "default"
            },
            "command":{
            }
        }
        if(not os.path.exists(portsourceconfigfile)):
            writeJsonData(portsourceconfigfile, d_temp)
        if(not os.path.exists(porttargetconfigfile)):
            writeJsonData(porttargetconfigfile, d_temp)

        srcsize = os.path.getsize(portsourceconfigfile)
        tarsize = os.path.getsize(porttargetconfigfile)
        if(srcsize < 166):
            writeJsonData(portsourceconfigfile, d_temp)
        if(tarsize < 166):
            writeJsonData(porttargetconfigfile, d_temp)

        portconfig = readJsonData(portsourceconfigfile)
        porttargetconfig = readJsonData(porttargetconfigfile)

        #hard
        if(portconfig.__contains__("path-assemblage") is False):
            portconfig['path-assemblage']={}
            writeJsonData(portsourceconfigfile, portconfig)
        if(portconfig.__contains__("environ") is False):
            portconfig['environ']={}
            writeJsonData(portsourceconfigfile, portconfig)
        if (portconfig.__contains__("command") is False):
            portconfig['command'] = {}
            writeJsonData(portsourceconfigfile, portconfig)

        #soft
        #if(portconfig['environ'].__contains__("default") is False):
        #    portconfig['environ']['default']={"path+":[]}
        #    writeJsonData(portsourceconfigfile, portconfig)
        #if(portconfig['environ']['default'].__contains__("path+") is False):
        #    portconfig['environ']['default']['path+']=[]
        #    writeJsonData(portsourceconfigfile, portconfig)
        #if(portconfig['environ'].__contains__("current") is False):
        #    portconfig['environ']['current']='default'
        #    writeJsonData(portsourceconfigfile, portconfig)

        #hard
        if(porttargetconfig.__contains__("path-assemblage") is False):
            porttargetconfig['path-assemblage']={}
            writeJsonData(porttargetconfigfile, porttargetconfig)
        if(porttargetconfig.__contains__("environ") is False):
            porttargetconfig['environ']={}
            writeJsonData(porttargetconfigfile, porttargetconfig)
        if(porttargetconfig.__contains__("command") is False):
            porttargetconfig['command']={}
            writeJsonData(porttargetconfigfile, porttargetconfig)

        #soft
        order_of_keys = porttargetconfig['environ'].keys()
        list_of_tuples = [key for key in order_of_keys]
        if (list_of_tuples.__len__() < 2):
            if(porttargetconfig['environ'].__contains__("default") is False):
                porttargetconfig['environ']['default']={"path+":[]}
                writeJsonData(porttargetconfigfile, porttargetconfig)
            if(porttargetconfig['environ']['default'].__contains__("path+") is False):
                porttargetconfig['environ']['default']['path+']=[]
                writeJsonData(porttargetconfigfile, porttargetconfig)
            if(porttargetconfig['environ'].__contains__("current") is False):
                porttargetconfig['environ']['current']='default'
                writeJsonData(porttargetconfigfile, porttargetconfig)

        #move 'current' to be last key
        order_of_keys = porttargetconfig['environ'].keys()
        list_of_tuples = [key for key in order_of_keys]
        #print(order_of_keys)
        #print(list_of_tuples)
        #print(list_of_tuples[-1])
        if(list_of_tuples[-1] != 'current'):
            #print(".....")
            current_var = porttargetconfig['environ']['current']
            porttargetconfig['environ'].__delitem__('current')
            porttargetconfig['environ']['current']=current_var
            writeJsonData(porttargetconfigfile, porttargetconfig)
        return portconfig, porttargetconfig

    # port translate
    while (True):
        if (args['port'] is True):
            portconf, portinifile = init_portconf()
            if (args['root'] is True):
                if( args['--source'] is True ):
                    if (not os.path.isdir(args['<config-root>'])
                        #or os.path.islink(args['<config-root>'])
                        or not os.path.isabs(args['<config-root>'])):
                        print("please input a legal source abspath.")
                        return
                    portconf.set('port', 'sourceroot', args['<config-root>'])
                    portconf.write(open(portinifile, 'w'))
                    print("port: source root is %s" % portconf['port']['sourceroot'])
                    return

                if( args['--target'] is True ):
                    if (not os.path.isdir(args['<config-root>'])
                        #or os.path.islink(args['<config-root>'])
                        or not os.path.isabs(args['<config-root>'])):
                        print("please input a legal target abspath.")
                        return
                    portconf.set('port', 'targetroot', args['<config-root>'])
                    portconf.write(open(portinifile, 'w'))
                    print("port: target root is %s" % portconf['port']['targetroot'])
                    return

                if( args['<source-config-root>'] is not None ):
                    if (not os.path.isdir(args['<source-config-root>'])
                        #or os.path.islink(args['<source-config-root>'])
                        or not os.path.isabs(args['<source-config-root>'])):
                        print("please input a legal source abspath.")
                        return
                    portconf.set('port', 'sourceroot', args['<source-config-root>'])
                    portconf.write(open(portinifile, 'w'))
                    #print("port: source config root is %s." % portconf['port']['sourceroot'])

                if( args['<target-config-root>'] is not None ):
                    if (not os.path.isdir(args['<target-config-root>'])
                        #or os.path.islink(args['<target-config-root>'])
                        or not os.path.isabs(args['<target-config-root>'])):
                        print("please input a legal target abspath.")
                        return
                    portconf.set('port', 'targetroot', args['<target-config-root>'])
                    portconf.write(open(portinifile, 'w'))
                    #print("port: target config root is %s." % portconf['port']['targetroot'])

                print("port: source root is %s" % portconf['port']['sourceroot'])
                print("port: target root is %s" % portconf['port']['targetroot'])
            elif (args['config'] is True):
                if( args['--source'] is True ):
                    if (not args['<config-file>'].endswith(pymakesuffix)
                        or os.path.isdir(args['<config-file>'])
                        #or os.path.islink(args['<config-file>'])
                        or os.path.isabs(args['<config-file>'])):
                        print("please input a real source .json file.")
                        return
                    portconf.set('port', 'sourceconfig', args['<config-file>'])
                    portconf.write(open(portinifile, 'w'))
                    print("port: source config is %s" % portconf['port']['sourceconfig'])
                    return

                if( args['--target'] is True ):
                    if (not args['<config-file>'].endswith(pymakesuffix)
                        or os.path.isdir(args['<config-file>'])
                        #or os.path.islink(args['<config-file>'])
                        or os.path.isabs(args['<config-file>'])):
                        print("please input a real target .json file.")
                        return
                    portconf.set('port', 'targetconfig', args['<config-file>'])
                    portconf.write(open(portinifile, 'w'))
                    print("port: target config is %s" % portconf['port']['targetconfig'])
                    return

                if( args['<source-config-file>'] is not None ):
                    if (not args['<source-config-file>'].endswith(pymakesuffix)
                        or os.path.isdir(args['<source-config-file>'])
                        #or os.path.islink(args['<source-config-file>'])
                        or os.path.isabs(args['<source-config-file>'])):
                        print("please input a real source .json file.")
                        return
                    portconf.set('port', 'sourceconfig', args['<source-config-file>'])
                    portconf.write(open(portinifile, 'w'))
                    #print("port: source config file is %s." % portconf['port']['sourceconfig'])

                if( args['<target-config-file>'] is not None ):
                    if (not args['<target-config-file>'].endswith(pymakesuffix)
                        or os.path.isdir(args['<target-config-file>'])
                        #or os.path.islink(args['<target-config-file>'])
                        or os.path.isabs(args['<target-config-file>'])):
                        print("please input a real target .json file.")
                        return
                    portconf.set('port', 'targetconfig', args['<target-config-file>'])
                    portconf.write(open(portinifile, 'w'))
                    #print("port: target config file is %s." % portconf['port']['targetconfig'])

                print("port: source config is %s" % portconf['port']['sourceconfig'])
                print("port: target config is %s" % portconf['port']['targetconfig'])
            elif (args['file'] is True):
                if( args['--source'] is True ):
                    if (not args['<path-file>'].endswith(pymakesuffix)
                        or os.path.isdir(args['<path-file>'])
                        #or os.path.islink(args['<path-file>'])
                        or not os.path.isabs(args['<path-file>'])):
                        print("please input a legal source abspath .json file.")
                        return
                    r = os.path.split(os.path.realpath(args['<path-file>']))[0]
                    f = os.path.split(os.path.realpath(args['<path-file>']))[1]
                    portconf.set('port', 'sourceroot', r)
                    portconf.set('port', 'sourceconfig', f)
                    portconf.write(open(portinifile, 'w'))
                    print("port: source file   is %s" % os.path.join(portconf['port']['sourceroot'], portconf['port']['sourceconfig']))
                    print("port: source root   is %s" % portconf['port']['sourceroot'])
                    print("port: source config is %s" % portconf['port']['sourceconfig'])
                    return

                if( args['--target'] is True ):
                    if (not args['<path-file>'].endswith(pymakesuffix)
                        or os.path.isdir(args['<path-file>'])
                        #or os.path.islink(args['<path-file>'])
                        or not os.path.isabs(args['<path-file>'])):
                        print("please input a legal target abspath .json file.")
                        return
                    r = os.path.split(os.path.realpath(args['<path-file>']))[0]
                    f = os.path.split(os.path.realpath(args['<path-file>']))[1]
                    portconf.set('port', 'targetroot', r)
                    portconf.set('port', 'targetconfig', f)
                    portconf.write(open(portinifile, 'w'))
                    print("port: target file   is %s" % os.path.join(portconf['port']['targetroot'], portconf['port']['targetconfig']))
                    print("port: target root   is %s" % portconf['port']['targetroot'])
                    print("port: target config is %s" % portconf['port']['targetconfig'])
                    return

                if(args['<source-path-file>'] is not None):
                   if( not args['<source-path-file>'].endswith(pymakesuffix)
                       or os.path.isdir(args['<source-path-file>'])
                       #or os.path.islink(args['<source-path-file>'])
                       or not os.path.isabs(args['<source-path-file>'])):
                        print("please input a legal source abspath .json file.")
                        return
                   r = os.path.split(os.path.realpath(args['<source-path-file>']))[0]
                   f = os.path.split(os.path.realpath(args['<source-path-file>']))[1]
                   portconf.set('port', 'sourceroot', r)
                   portconf.set('port', 'sourceconfig', f)
                   portconf.write(open(portinifile, 'w'))

                if(args['<target-path-file>'] is not None):
                   if(not args['<target-path-file>'].endswith(pymakesuffix)
                      or os.path.isdir(args['<target-path-file>'])
                      #or os.path.islink(args['<target-path-file>'])
                      or not os.path.isabs(args['<target-path-file>'])):
                        print("please input a legal target abspath .json file.")
                        return
                   r = os.path.split(os.path.realpath(args['<target-path-file>']))[0]
                   f = os.path.split(os.path.realpath(args['<target-path-file>']))[1]
                   portconf.set('port', 'targetroot', r)
                   portconf.set('port', 'targetconfig', f)
                   portconf.write(open(portinifile, 'w'))

                print("port: source file   is %s" % os.path.join(portconf['port']['sourceroot'], portconf['port']['sourceconfig']))
                print("port: source root   is %s" % portconf['port']['sourceroot'])
                print("port: source config is %s" % portconf['port']['sourceconfig'])
                print("port: target file   is %s" % os.path.join(portconf['port']['targetroot'], portconf['port']['targetconfig']))
                print("port: target root   is %s" % portconf['port']['targetroot'])
                print("port: target config is %s" % portconf['port']['targetconfig'])
            elif (args['reset'] is True):
                portconf.set('port', 'sourceroot', sourceroot)
                portconf.set('port', 'sourceconfig', pymakedefaultsourcefile)
                portconf.set('port', 'targetroot', sourceroot)
                portconf.set('port', 'targetconfig', portdefaulttargetconfig)
                portconf.write(open(portinifile, 'w'))
                print("port: source file   is %s" % os.path.join(portconf['port']['sourceroot'], portconf['port']['sourceconfig']))
                print("port: source root   is %s" % portconf['port']['sourceroot'])
                print("port: source config is %s" % portconf['port']['sourceconfig'])
                print("port: target file   is %s" % os.path.join(portconf['port']['targetroot'], portconf['port']['targetconfig']))
                print("port: target root   is %s" % portconf['port']['targetroot'])
                print("port: target config is %s" % portconf['port']['targetconfig'])
                print("successed")
            else:
                print("port: source file   is %s" % os.path.join(portconf['port']['sourceroot'], portconf['port']['sourceconfig']))
                print("port: source root   is %s" % portconf['port']['sourceroot'])
                print("port: source config is %s" % portconf['port']['sourceconfig'])
                print("port: target file   is %s" % os.path.join(portconf['port']['targetroot'], portconf['port']['targetconfig']))
                print("port: target root   is %s" % portconf['port']['targetroot'])
                print("port: target config is %s" % portconf['port']['targetconfig'])
            return
        elif (args['translate'] is True):
            import itertools
            portconf, portinifile = init_portconf()
            portconfig, porttargetconfig = init_portconfig(portconf)
            portsourceconfigfile = os.path.join(portconf['port']['sourceroot'], portconf['port']['sourceconfig'])
            porttargetconfigfile = os.path.join(portconf['port']['targetroot'], portconf['port']['targetconfig'])
            print("translate: source file   is %s" % portsourceconfigfile)
            print("translate: source root   is %s" % portconf['port']['sourceroot'])
            print("translate: source config is %s" % portconf['port']['sourceconfig'])
            print("translate: target file   is %s" % porttargetconfigfile)
            print("translate: target root   is %s" % portconf['port']['targetroot'])
            print("translate: target config is %s" % portconf['port']['targetconfig'])
            print("---------------------------------------------------------------------")
            print(Fore.MAGENTA + "%-30s%-30s%s" % ( "[source] " + portconf['port']['sourceconfig'], "[target] " + portconf['port']['targetconfig'], "[status]"))

            def translate_section(section_name = None):
                if(section_name is None):
                    return

                masterkey = section_name

                srckey = ''
                tarkey = ''
                #print(args['<key-name>'], args['<target-key-name>'])
                if (args['<key-name>'] is not None):
                    srckey = args['<key-name>']
                # print("src key:%s" % srckey)

                if (args['<target-key-name>'] is not None):
                    tarkey = args['<target-key-name>']
                else:
                    tarkey = srckey
                # print("tar key:%s" % tarkey)

                if (args['<key-name>'] is not None
                    or args['<target-key-name>'] is not None):
                    # print("src key:%s, tar key:%s" % (srckey, tarkey))

                    existedflag = '[       ]'
                    if (porttargetconfig[masterkey].__contains__(tarkey)):
                        existedflag = '[EXISTED]'

                    if (args['-f'] or args['--force'] is True):
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS]" + existedflag + "[FORCE]"))
                        return

                    if (porttargetconfig[masterkey].__contains__(tarkey)):
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[CANCEL ]" + existedflag))
                        return
                    else:
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS][     ]" + existedflag))
                    return

                if (args['-a'] or args['--all'] is True):
                    for key in portconfig[masterkey].keys():
                        existedflag = '[       ]'
                        if (porttargetconfig[masterkey].__contains__(key)):
                            existedflag = '[EXISTED]'

                        if (args['-f'] or args['--force'] is True):
                            porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag + "[FORCE]"))
                        else:
                            if (porttargetconfig[masterkey].__contains__(key)):
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag))
                            else:
                                porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag))

                    writeJsonData(porttargetconfigfile, porttargetconfig)
                    return

                keylist1 = []
                keylist2 = []
                # print(portconfig.keys())
                for key in portconfig[masterkey].keys():
                    keylist1.append(key)
                for key in porttargetconfig[masterkey].keys():
                    keylist2.append(key)
                # print(keylist1)
                # print(keylist2)
                count = 1
                for (key1, key2) in itertools.zip_longest(keylist1, keylist2):
                    if (key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if (key2 is None):
                        key2 = str("[EMPTY] %s" % count)
                        count += 1
                    print("%-30s%-30s%s" % (key1, key2, '[NORMAL]'))
                return

            def translate_envsection(section_name = None):
                if(section_name is None):
                    return

                masterkey = section_name

                srckey = ''
                tarkey = ''
                #print(args['<key-name>'], args['<target-key-name>'])
                if(args['<key-name>'] is not None):
                    srckey = args['<key-name>']
                #print("src key:%s" % srckey)

                if(args['<target-key-name>'] is not None):
                    tarkey = args['<target-key-name>']
                else:
                    tarkey = srckey
                #print("tar key:%s" % tarkey)

                if(args['<key-name>'] is not None
                   or args['<target-key-name>'] is not None):
                    #print("src key:%s, tar key:%s" % (srckey, tarkey))

                    existedflag = '[       ]'
                    if (porttargetconfig[masterkey].__contains__(tarkey)):
                        existedflag = '[EXISTED]'

                    if(args['-f'] or args['--force'] is True):
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        porttargetconfig[masterkey].__delitem__('current')
                        porttargetconfig[masterkey]['current'] = tarkey
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS]"+existedflag+"[FORCE]"))
                        return

                    if(porttargetconfig[masterkey].__contains__(tarkey)):
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[CANCEL ]"+existedflag))
                        return
                    else:
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        porttargetconfig[masterkey].__delitem__('current')
                        porttargetconfig[masterkey]['current'] = tarkey
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS][     ]"+existedflag))
                    return

                if(args['-a'] or args['--all'] is True):
                    for key in portconfig[masterkey].keys():
                        existedflag = '[       ]'
                        if (porttargetconfig[masterkey].__contains__(key)):
                            existedflag = '[EXISTED]'

                        if(args['-f'] or args['--force'] is True):
                            porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]"+existedflag+"[FORCE]"))
                        else:
                            if (porttargetconfig[masterkey].__contains__(key)):
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag))
                            else:
                                porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag))

                    tarkey = ''
                    if (args['-f'] or args['--force'] is True):
                        tarkey = portconfig[masterkey]['current']
                    else:
                        tarkey = porttargetconfig[masterkey]['current']
                    porttargetconfig[masterkey].__delitem__('current')
                    porttargetconfig[masterkey]['current'] = tarkey
                    writeJsonData(porttargetconfigfile, porttargetconfig)
                    return

                keylist1 = []
                keylist2 = []
                #print(portconfig.keys())
                for key in portconfig[masterkey].keys():
                    keylist1.append(key)
                for key in porttargetconfig[masterkey].keys():
                    keylist2.append(key)
                #print(keylist1)
                #print(keylist2)
                count = 1
                for (key1,key2) in itertools.zip_longest(keylist1, keylist2):
                    if(key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if(key2 is None):
                        key2 = str("[EMPTY] %s" %count)
                        count += 1
                    print("%-30s%-30s%s" % (key1, key2, '[NORMAL]'))
                return

            if (args['path'] is True):
                print(Fore.CYAN + "path-assemblage:")

                srckey = ''
                tarkey = ''
                #print(args['<key-name>'], args['<target-key-name>'])
                if(args['<key-name>'] is not None):
                    srckey = args['<key-name>']
                #print("src key:%s" % srckey)

                if(args['<target-key-name>'] is not None):
                    tarkey = args['<target-key-name>']
                else:
                    tarkey = srckey
                #print("tar key:%s" % tarkey)

                if(args['<key-name>'] is not None
                   or args['<target-key-name>'] is not None):
                    #print("src key:%s, tar key:%s" % (srckey, tarkey))

                    existedflag = '[       ]'
                    if (porttargetconfig['path-assemblage'].__contains__(tarkey)):
                        existedflag = '[EXISTED]'

                    if(args['-f'] or args['--force'] is True):
                        if (portconfig['path-assemblage'].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig['path-assemblage'][tarkey] = copy.deepcopy(portconfig['path-assemblage'][srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS]"+existedflag+"[FORCE]"))
                        return

                    if(porttargetconfig['path-assemblage'].__contains__(tarkey)):
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[CANCEL ]"+existedflag))
                        return
                    else:
                        if (portconfig['path-assemblage'].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig['path-assemblage'][tarkey] = copy.deepcopy(portconfig['path-assemblage'][srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS][     ]"+existedflag))
                    return

                if(args['-a'] or args['--all'] is True):
                    for key in portconfig['path-assemblage'].keys():
                        existedflag = '[       ]'
                        if (porttargetconfig['path-assemblage'].__contains__(key)):
                            existedflag = '[EXISTED]'

                        if(args['-f'] or args['--force'] is True):
                            porttargetconfig['path-assemblage'][key] = copy.deepcopy(portconfig['path-assemblage'][key])
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]"+existedflag+"[FORCE]"))
                        else:
                            if (porttargetconfig['path-assemblage'].__contains__(key)):
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag))
                            else:
                                porttargetconfig['path-assemblage'][key] = copy.deepcopy(portconfig['path-assemblage'][key])
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag))

                    writeJsonData(porttargetconfigfile, porttargetconfig)
                    return

                keylist1 = []
                keylist2 = []
                #print(portconfig.keys())
                for key in portconfig['path-assemblage'].keys():
                    keylist1.append(key)
                for key in porttargetconfig['path-assemblage'].keys():
                    keylist2.append(key)
                #print(keylist1)
                #print(keylist2)
                count = 1
                for (key1,key2) in itertools.zip_longest(keylist1, keylist2):
                    if(key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if(key2 is None):
                        key2 = str("[EMPTY] %s" %count)
                        count += 1
                    print("%-30s%-30s%s" % (key1, key2, '[NORMAL]'))
                return
            elif (args['env'] is True):
                print(Fore.CYAN + "environ:")
                masterkey = "environ"

                srckey = ''
                tarkey = ''
                #print(args['<key-name>'], args['<target-key-name>'])
                if(args['<key-name>'] is not None):
                    srckey = args['<key-name>']
                #print("src key:%s" % srckey)

                if(args['<target-key-name>'] is not None):
                    tarkey = args['<target-key-name>']
                else:
                    tarkey = srckey
                #print("tar key:%s" % tarkey)

                if(args['<key-name>'] is not None
                   or args['<target-key-name>'] is not None):
                    #print("src key:%s, tar key:%s" % (srckey, tarkey))

                    existedflag = '[       ]'
                    if (porttargetconfig[masterkey].__contains__(tarkey)):
                        existedflag = '[EXISTED]'

                    if(args['-f'] or args['--force'] is True):
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        porttargetconfig[masterkey].__delitem__('current')
                        porttargetconfig[masterkey]['current'] = tarkey
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS]"+existedflag+"[FORCE]"))
                        return

                    if(porttargetconfig[masterkey].__contains__(tarkey)):
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[CANCEL ]"+existedflag))
                        return
                    else:
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        porttargetconfig[masterkey].__delitem__('current')
                        porttargetconfig[masterkey]['current'] = tarkey
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS][     ]"+existedflag))
                    return

                if(args['-a'] or args['--all'] is True):
                    for key in portconfig[masterkey].keys():
                        existedflag = '[       ]'
                        if (porttargetconfig[masterkey].__contains__(key)):
                            existedflag = '[EXISTED]'

                        if(args['-f'] or args['--force'] is True):
                            porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]"+existedflag+"[FORCE]"))
                        else:
                            if (porttargetconfig[masterkey].__contains__(key)):
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag))
                            else:
                                porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag))

                    tarkey = ''
                    if (args['-f'] or args['--force'] is True):
                        tarkey = portconfig[masterkey]['current']
                    else:
                        tarkey = porttargetconfig[masterkey]['current']
                    porttargetconfig[masterkey].__delitem__('current')
                    porttargetconfig[masterkey]['current'] = tarkey
                    writeJsonData(porttargetconfigfile, porttargetconfig)
                    return

                keylist1 = []
                keylist2 = []
                #print(portconfig.keys())
                for key in portconfig[masterkey].keys():
                    keylist1.append(key)
                for key in porttargetconfig[masterkey].keys():
                    keylist2.append(key)
                #print(keylist1)
                #print(keylist2)
                count = 1
                for (key1,key2) in itertools.zip_longest(keylist1, keylist2):
                    if(key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if(key2 is None):
                        key2 = str("[EMPTY] %s" %count)
                        count += 1
                    print("%-30s%-30s%s" % (key1, key2, '[NORMAL]'))
                return
            elif (args['cmd'] is True):
                print(Fore.CYAN + "command:")
                masterkey = "command"

                srckey = ''
                tarkey = ''
                # print(args['<key-name>'], args['<target-key-name>'])
                if (args['<key-name>'] is not None):
                    srckey = args['<key-name>']
                # print("src key:%s" % srckey)

                if (args['<target-key-name>'] is not None):
                    tarkey = args['<target-key-name>']
                else:
                    tarkey = srckey
                # print("tar key:%s" % tarkey)

                if (args['<key-name>'] is not None
                    or args['<target-key-name>'] is not None):
                    # print("src key:%s, tar key:%s" % (srckey, tarkey))

                    existedflag = '[       ]'
                    if (porttargetconfig[masterkey].__contains__(tarkey)):
                        existedflag = '[EXISTED]'

                    if (args['-f'] or args['--force'] is True):
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS]" + existedflag + "[FORCE]"))
                        return

                    if (porttargetconfig[masterkey].__contains__(tarkey)):
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[CANCEL ]" + existedflag))
                        return
                    else:
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS][     ]" + existedflag))
                    return

                if (args['-a'] or args['--all'] is True):
                    for key in portconfig[masterkey].keys():
                        existedflag = '[       ]'
                        if (porttargetconfig[masterkey].__contains__(key)):
                            existedflag = '[EXISTED]'

                        if (args['-f'] or args['--force'] is True):
                            porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag + "[FORCE]"))
                        else:
                            if (porttargetconfig[masterkey].__contains__(key)):
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag))
                            else:
                                porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag))

                    writeJsonData(porttargetconfigfile, porttargetconfig)
                    return

                keylist1 = []
                keylist2 = []
                # print(portconfig.keys())
                for key in portconfig[masterkey].keys():
                    keylist1.append(key)
                for key in porttargetconfig[masterkey].keys():
                    keylist2.append(key)
                # print(keylist1)
                # print(keylist2)
                count = 1
                for (key1, key2) in itertools.zip_longest(keylist1, keylist2):
                    if (key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if (key2 is None):
                        key2 = str("[EMPTY] %s" % count)
                        count += 1
                    print("%-30s%-30s%s" % (key1, key2, '[NORMAL]'))
                return
            elif (args['path-env-cmd'] or args['all'] is True):
                print(Fore.CYAN + "path-assemblage:")
                masterkey = "path-assemblage"
                translate_section(masterkey)

                print(Fore.CYAN + "environ:")
                masterkey = "environ"
                translate_envsection(masterkey)

                print(Fore.CYAN + "command:")
                masterkey = "command"
                translate_section(masterkey)
            elif (args['section'] is True):
                print(Fore.CYAN + "section:")
                srckey = ''
                tarkey = ''
                #print(args['<section-name>'], args['<target-section-name>'])
                if (args['<section-name>'] is not None):
                    srckey = args['<section-name>']
                #print("src section:%s" % srckey)

                if (args['<target-section-name>'] is not None):
                    tarkey = args['<target-section-name>']
                else:
                    tarkey = srckey
                #print("tar section:%s" % tarkey)

                if (args['<section-name>'] is not None
                    or args['<target-section-name>'] is not None):
                    #print("src section:%s, tar section:%s" % (srckey, tarkey))

                    if(tarkey == "path-assemblage"
                       or tarkey == "environ"
                       or tarkey == "command"):
                        print("please ensure your target section name, it cant be pymake's section.")
                        return

                    existedflag = '[       ]'
                    if (porttargetconfig.__contains__(tarkey)):
                        existedflag = '[EXISTED]'

                    if (args['-f'] or args['--force'] is True):
                        if (portconfig.__contains__(srckey) is False):
                            print("please ensure the source section %s is existed." % srckey)
                            return
                        porttargetconfig[tarkey] = copy.deepcopy(portconfig[srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS]" + existedflag + "[FORCE]"))
                        return

                    if (porttargetconfig.__contains__(tarkey)):
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[CANCEL ]" + existedflag))
                        return
                    else:
                        if (portconfig.__contains__(srckey) is False):
                            print("please ensure the source section %s is existed." % srckey)
                            return
                        porttargetconfig[tarkey] = copy.deepcopy(portconfig[srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS][     ]" + existedflag))
                    return

                if (args['-a'] or args['--all'] is True):
                    for key in portconfig.keys():
                        existedflag = '[       ]'
                        if (porttargetconfig.__contains__(key)):
                            existedflag = '[EXISTED]'

                        if (key == "path-assemblage"
                            or key == "environ"
                            or key == "command"):
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag + "[RESERVED]"))
                            continue

                        if (args['-f'] or args['--force'] is True):
                            porttargetconfig[key] = copy.deepcopy(portconfig[key])
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag + "[FORCE]"))
                        else:
                            if (porttargetconfig.__contains__(key)):
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag))
                            else:
                                porttargetconfig[key] = copy.deepcopy(portconfig[key])
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag))

                    writeJsonData(porttargetconfigfile, porttargetconfig)
                    return

                keylist1 = []
                keylist2 = []
                # print(portconfig.keys())
                for key in portconfig.keys():
                    keylist1.append(key)
                for key in porttargetconfig.keys():
                    keylist2.append(key)
                # print(keylist1)
                # print(keylist2)
                count = 1
                for (key1, key2) in itertools.zip_longest(keylist1, keylist2):
                    if (key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if (key2 is None):
                        key2 = str("[EMPTY] %s" % count)
                        count += 1
                    print("%-30s%-30s%s" % (key1, key2, '[NORMAL]'))
                return
            elif (args['config'] is True):
                if(not os.path.exists(porttargetconfigfile)
                or args['-f'] is True or args['--force'] is True):
                    ''
                    shutil.copyfile(portsourceconfigfile, porttargetconfigfile)
                    print('successed.')
                elif (os.path.exists(porttargetconfigfile) is True):
                    print('%s is existed.' % porttargetconfigfile)
                else:
                    ''
                return
            else:
                print(Fore.CYAN + "all sections:")
                keylist1 = []
                keylist2 = []
                #print(portconfig.keys())
                for key in portconfig.keys():
                    keylist1.append(key)
                for key in porttargetconfig.keys():
                    keylist2.append(key)
                #print(keylist1)
                #print(keylist2)
                count = 1
                for (key1,key2) in itertools.zip_longest(keylist1, keylist2):
                    if(key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if(key2 is None):
                        key2 = str("[EMPTY] %s" %count)
                        count += 1
                    print("%-30s%-30s%s" % (key1,key2,'[NORMAL]'))
            return
        else:
            ''
        break

    # set this command here .
    # program
    while (True):
        if(args['program'] is True):
            if(args['configure'] is True):
                if(args['root'] is True):
                    print("%s" % os.path.split(os.path.realpath(pymakeini))[0])
                    return
                elif (args['file'] is True):
                    print("%s" % os.path.split(os.path.realpath(pymakeini))[1])
                    return
                elif (args['--edit'] is True):
                    cmd_list = []
                    cmd_list.append(pymakeini)
                    for file0 in cmd_list:
                        cmd0 = open_file(file0)
                        os.system(cmd0)
                        print('successed: %s' % file0)
                    return
                else:
                    print("%s" % os.path.realpath(pymakeini))
                    return
            else:
                if(args['root'] is True):
                    print("%s" % os.path.split(os.path.realpath(__file__))[0])
                    return
                elif (args['file'] is True):
                    print("%s" % os.path.split(os.path.realpath(__file__))[1])
                    return
                else:
                    print("%s" % os.path.realpath(__file__))
                    return
            return
        else:
            ''
        break

    # debug.
    debugini = sourceroot + os.path.sep + "debug.ini"
    debugconf = MyConfigParser()
    debugconf.read(debugini)
    if (not debugconf.has_section('debug')):
        debugconf.add_section('debug')
        debugconf.write(open(debugini, 'w'))

    if( not debugconf.has_option('debug', 'switch') ):
        debugconf.set('debug', 'switch', '0')
        debugconf.write(open(debugini, 'w'))

    debugswitch = debugconf['debug']['switch']
    if(debugswitch != '0' and debugswitch != '1'):
        debugswitch = '0'
        debugconf.set('debug', 'switch', debugswitch)
        debugconf.write(open(debugini, 'w'))

    # debug
    while (True):
        if(args['debug'] is True):
            if(args['open'] is True):
                debugswitch = '1'
                debugconf.set('debug', 'switch', debugswitch)
                debugconf.write(open(debugini, 'w'))
                print('debug: opened.')
                return
            elif (args['close'] is True):
                debugswitch = '0'
                debugconf.set('debug', 'switch', debugswitch)
                debugconf.write(open(debugini, 'w'))
                print('debug: closed.')
                return
            else:
                if(debugswitch == '0'):
                    print('debug: closed.')
                else:
                    print('debug: opened.')
                return
            return
        else:
            ''
        break

    config = readJsonData(sourceconfigfile)
    #print(config)

    def check_config():
        #hard
        if(config.__contains__("path-assemblage") is False):
            config['path-assemblage']={}
            writeJsonData(sourceconfigfile, config)
        if(config.__contains__("environ") is False):
            config['environ']={}
            writeJsonData(sourceconfigfile, config)
        if (config.__contains__("command") is False):
            config['command'] = {}
            writeJsonData(sourceconfigfile, config)

        #soft
        #if(portconfig['environ'].__contains__("default") is False):
        #    portconfig['environ']['default']={"path+":[]}
        #    writeJsonData(portsourceconfigfile, portconfig)
        #if(portconfig['environ']['default'].__contains__("path+") is False):
        #    portconfig['environ']['default']['path+']=[]
        #    writeJsonData(portsourceconfigfile, portconfig)
        #if(portconfig['environ'].__contains__("current") is False):
        #    portconfig['environ']['current']='default'
        #    writeJsonData(portsourceconfigfile, portconfig)

        #soft
        order_of_keys = config['environ'].keys()
        list_of_tuples = [key for key in order_of_keys]
        if (list_of_tuples.__len__() < 2):
            if(config['environ'].__contains__("default") is False):
                config['environ']['default']={"path+":[]}
                writeJsonData(sourceconfigfile, config)
            if(config['environ']['default'].__contains__("path+") is False):
                config['environ']['default']['path+']=[]
                writeJsonData(sourceconfigfile, config)
            if(config['environ'].__contains__("current") is False):
                config['environ']['current']='default'
                writeJsonData(sourceconfigfile, config)

        #move 'current' to be last key
        order_of_keys = config['environ'].keys()
        list_of_tuples = [key for key in order_of_keys]
        #print(order_of_keys)
        #print(list_of_tuples)
        #print(list_of_tuples[-1])
        if(list_of_tuples[-1] != 'current'):
            #print(".....")
            current_var = config['environ']['current']
            config['environ'].__delitem__('current')
            config['environ']['current']=current_var
            writeJsonData(sourceconfigfile, config)
        return

    check_config()

    # import command
    while (True):
        if (args['import'] is True):
            if(args['cmd'] is True):
                print("source file   is %s" % sourceconfigfile)
                print("source root   is %s" % sourceroot)
                print("source config is %s" % sourcefile)
                print("---------------------------------------------------------------------")

                import itertools

                #os.chdir(sourceroot)

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                plat = getplatform()
                if(plat == "Windows"):
                    cmd_header = "@echo off"
                    cmd_codec = "ansi"
                    if(getplatform_release() == "XP"):
                        cmd_codec = None
                    # but windows, it is \r\n, python helpping me?
                    cmd_return = "\n"
                    cmd_suffix = ".bat"
                else:
                    cmd_header = "#!/usr/bin/env bash"
                    cmd_codec = "utf8"
                    cmd_return = "\n"
                    cmd_suffix = ".sh"

                if( args['-a'] or args['--all'] is True):
                    #print('-a')
                    #print("%-30s %-5s %-5s" % (args['<script-file>'], os.path.isdir(args['<script-file>']), os.path.islink(args['<script-file>'])))
                    root_path = ""
                    if (os.path.isdir(args['<script-file>'])):
                        root_path = args['<script-file>']
                    else:
                        root_path = os.getcwd()

                    print(Fore.CYAN + "%-30s%-30s%s" % ("[command] ", "[status] ", "[file] "))
                    keylist1 = []
                    if(args['--recursive'] is True):
                        for ( dirpath, dirnames, filenames ) in os.walk(root_path):
                            for name in filenames:
                                #print(os.path.relpath(os.path.join(dirpath, name), os.getcwd()))
                                keylist1.append(os.path.relpath(os.path.join(dirpath, name), os.getcwd()))
                    else:
                        for key in os.listdir(root_path):
                            keylist1.append(os.path.relpath(os.path.join(root_path, key), os.getcwd()))

                    #print(keylist1)
                    #for file in keylist1:
                    #    print (file)

                    dirlist = []
                    for (key) in keylist1:
                        # print("%-30s %-5s %-5s" % (key, os.path.isdir(key), os.path.islink(key)))
                        if ( os.path.isdir(key)
                            #or os.path.islink(key)
                            ):
                            dirlist.append(key)
                    # print(dirlist)
                    for key in dirlist:
                        keylist1.remove(key)

                    #print(args)
                    tarkeylist = []
                    #print(args['--filter'])
                    if (args['--filter'] == [] or args['--filter'] == [''] or args['--filter'] == ['*']):
                        tarkeylist = keylist1
                    else:
                        filterString = ''
                        for fi in args['--filter']:
                            filterString += fi + '|'
                        filterList = filterString.split('|')
                        while (filterList.__contains__('')):
                            filterList.remove('')
                        #print(filterString)
                        #print(filterList)
                        for fil in filterList:
                            fil = fil.strip()
                            for key in keylist1:
                                if(os.path.splitext(key)[1] == fil):
                                    tarkeylist.append(key)
                                    #print(fil, key)
                    #print(tarkeylist)
                    #for file in tarkeylist:
                    #    print (file)
                    #return

                    useencoding = cmd_codec
                    if(args['--encoding'] is not None):
                        useencoding = args['--encoding']

                    for (key1) in (tarkeylist):
                        local_path = os.path.realpath(key1)
                        command_name = os.path.splitext(os.path.basename(key1))[0]

                        #fixer
                        #ext = os.path.splitext(os.path.basename(key1))[1]
                        #if (ext == '.bat'):
                        #    useencoding = 'gbk'

                        if (config['command'].__contains__(command_name) is False):
                            command_content = []
                            with open(local_path, 'r', encoding=useencoding) as f:
                                for l in f.readlines():
                                    while (l.endswith('\r') or l.endswith('\n') or l.endswith('\r\n')):
                                        l = l.rstrip('\r\n')
                                        l = l.rstrip('\n')
                                        l = l.rstrip('\r')
                                    command_content.append(l)
                            config['command'][command_name] = command_content
                            writeJsonData(sourceconfigfile, config)
                            print("%-30s%-30s%s" % (command_name, "[SUCCESS][       ][     ]", key1))
                        else:
                            if (args['-f'] or args['--force'] is True):
                                command_content = []
                                with open(local_path, 'r', encoding=useencoding) as f:
                                    for l in f.readlines():
                                        while (l.endswith('\r') or l.endswith('\n') or l.endswith('\r\n')):
                                            l = l.rstrip('\r\n')
                                            l = l.rstrip('\n')
                                            l = l.rstrip('\r')
                                        command_content.append(l)
                                config['command'][command_name] = command_content
                                writeJsonData(sourceconfigfile, config)
                                print("%-30s%-30s%s" % (command_name, "[SUCCESS][EXISTED][FORCE]", key1))
                            else:
                                print("%-30s%-30s%s" % (command_name, "[CANCEL ][EXISTED][     ]", key1))
                    return

                if (args['<script-file>'] is None):
                    print(Fore.CYAN + "%-30s%-30s" % ( "[command] ", "[file] " ))
                    keylist1 = []
                    keylist2 = []
                    for key in os.listdir(os.getcwd()):
                        keylist1.append(key)
                    for key in config['command'].keys():
                        keylist2.append(key)

                    dirlist = []
                    for (key) in keylist1:
                        #print("%-30s %-5s %-5s" % (key, os.path.isdir(key), os.path.islink(key)))
                        if (os.path.isdir(key)
                            #or os.path.islink(key)
                            ):
                            dirlist.append(key)
                    #print(dirlist)
                    for key in dirlist:
                        keylist1.remove(key)

                    tarkeylist = []
                    #print(args['--filter'])
                    if (args['--filter'] == [] or args['--filter'] == [''] or args['--filter'] == ['*']):
                        tarkeylist = keylist1
                    else:
                        filterString = ''
                        for fi in args['--filter']:
                            filterString += fi + '|'
                        filterList = filterString.split('|')
                        while (filterList.__contains__('')):
                            filterList.remove('')
                        # print(filterString)
                        #print(filterList)
                        #return
                        for fil in filterList:
                            fil = fil.strip()
                            for key in keylist1:
                                if (os.path.splitext(key)[1] == fil):
                                    tarkeylist.append(key)
                                    # print(fil, key)
                    # print(tarkeylist)
                    # for file in tarkeylist:
                    #    print (file)
                    # return

                    #print(keylist1)
                    #print(keylist2)
                    count2 = 1
                    for (key1, key2) in itertools.zip_longest(tarkeylist, keylist2, fillvalue=""):
                        if (key1 != ""):
                            key1 = str("%s" % (key1))
                        if (key2 != ""):
                            key2 = str("%-4s%s" % (count2, key2))
                            count2 += 1
                        print("%-30s%-30s" % (key2, key1))

                    #print("Those are the files under %s" % os.getcwd())
                    return

                if (args['<script-file>'] is not None):
                    #print("%-30s %-5s %-5s" % (args['<script-file>'], os.path.isdir(args['<script-file>']), os.path.islink(args['<script-file>'])))
                    if (os.path.isdir(args['<script-file>'])):
                        print(Fore.CYAN + "%-30s%-30s" % ("[command] ", "[file] "))
                        keylist1 = []
                        keylist2 = []
                        for key in os.listdir(args['<script-file>']):
                            keylist1.append(os.path.relpath(os.path.join(args['<script-file>'], key), os.getcwd()))
                        for key in config['command'].keys():
                            keylist2.append(key)

                        dirlist = []
                        for (key) in keylist1:
                            # print("%-30s %-5s %-5s" % (key, os.path.isdir(key), os.path.islink(key)))
                            if (os.path.isdir(key)
                                #or os.path.islink(key)
                                ):
                                dirlist.append(key)
                        #print(dirlist)
                        #for file in dirlist:
                        #   print ('dir : ' + file)
                        for key in dirlist:
                            keylist1.remove(key)

                        tarkeylist = []
                        #print(args['--filter'])
                        if (args['--filter'] == [] or args['--filter'] == [''] or args['--filter'] == ['*']):
                            tarkeylist = keylist1
                        else:
                            filterString = ''
                            for fi in args['--filter']:
                                filterString += fi + '|'
                            filterList = filterString.split('|')
                            while (filterList.__contains__('')):
                                filterList.remove('')
                            # print(filterString)
                            # print(filterList)
                            for fil in filterList:
                                fil = fil.strip()
                                for key in keylist1:
                                    if (os.path.splitext(key)[1] == fil):
                                        tarkeylist.append(key)
                                        # print(fil, key)
                        # print(tarkeylist)
                        #for file in tarkeylist:
                        #   print ('file: ' + file)
                        #return

                        # print(keylist1)
                        # print(keylist2)
                        count2 = 1
                        for (key1, key2) in itertools.zip_longest(tarkeylist, keylist2, fillvalue=""):
                            if (key1 != ""):
                                key1 = str("%s" % (key1))
                            if (key2 != ""):
                                key2 = str("%-4s%s" % (count2, key2))
                                count2 += 1
                            print("%-30s%-30s" % (key2, key1))

                        #print("Those are the files under %s" % os.path.realpath(args['<script-file>']))
                        return

                    if (os.path.isdir(args['<script-file>'])
                        #or os.path.islink(args['<script-file>'])
                        ):
                        print("please input a legal script file.")
                        return

                    useencoding = cmd_codec
                    if(args['--encoding'] is not None):
                        useencoding = args['--encoding']

                    local_path = os.path.realpath(args['<script-file>'])
                    #print(os.path.dirname(local_path))
                    #print(os.path.basename(local_path) )
                    #print(os.path.splitext(os.path.basename(local_path))[0])
                    #print(os.path.splitext(os.path.basename(local_path))[1])
                    if(os.path.exists(local_path) is False):
                        print('failed: %s is not existed.' % args['<script-file>'])
                        return

                    command_name = os.path.splitext(os.path.basename(local_path))[0]

                    #print(args['<command-name>'])
                    if (args['<command-name>'] is not None):
                        command_name = args['<command-name>']

                    #print(args)
                    if(config['command'].__contains__(command_name) is True):
                        if ( args['-f'] or args['--force'] is True):
                            #print('-f')
                            #set in force
                            command_content = []
                            with open(local_path, 'r', encoding=useencoding) as f:
                                for l in f.readlines():
                                    while (l.endswith('\r') or l.endswith('\n') or l.endswith('\r\n')):
                                        l = l.rstrip('\r\n')
                                        l = l.rstrip('\n')
                                        l = l.rstrip('\r')
                                    command_content.append(l)
                            config['command'][command_name] = command_content
                            writeJsonData(sourceconfigfile, config)
                            print('successed: %s' % command_name)
                            return
                        print("failed: command %s is existed." % command_name)
                        return

                    # set in
                    command_content = []
                    with open(local_path, 'r', encoding=useencoding) as f:
                        for l in f.readlines():
                            while (l.endswith('\r') or l.endswith('\n') or l.endswith('\r\n')):
                                l = l.rstrip('\r\n')
                                l = l.rstrip('\n')
                                l = l.rstrip('\r')
                            command_content.append(l)
                    config['command'][command_name] = command_content
                    writeJsonData(sourceconfigfile, config)
                    print('successed: %s' % command_name)
                    return
                return
            else:
                ''
        else:
            ''
        break

    # set
    while (True):
        if(args['set'] is True):
            if(args['exec'] is True):
                if(args['<work-root-path>'] is not None):

                    #print(args['default'])
                    #print(args['there'])
                    #print(args['here'])

                    if (args['here'] or args['hh'] is True
                    or args['default'] or args['dd'] is True):
                        workroottype1 = 'default'
                        if (args['here'] or args['hh'] is True):
                            workroottype1 = 'here'
                        elif (args['default'] or args['dd'] is True):
                            workroottype1 = 'default'
                        else:
                            workroottype1 = 'default'
                        execconf.set('work', 'where', workroottype1)
                        execconf.write(open(pymakeexecini, 'w'))
                        print("successed: change work root to %s." % workroottype1)
                        return
                    

                    # force there
                    if (args['there'] or args['tt'] is True):
                        workroot1 = pymakeshellroot
                        if (args['<work-root-path>'] == 'here' or args['<work-root-path>'] == 'hh' ):
                            workroot1 = pymakeworkpath
                        elif (args['<work-root-path>'] == 'there' or args['<work-root-path>'] == 'tt' ):
                            workroot1 = customshellroot
                        elif (args['<work-root-path>'] == 'default' or args['<work-root-path>'] == 'dd'  ):
                            workroot1 = pymakeshellroot
                        else:
                            workroot1 = args['<work-root-path>']
                            if (os.path.isabs(workroot1) is False):
                                print("please appoint an absolute work root for setting there starting work root path.")
                                return
                            if (os.path.isdir(workroot1) is False):
                                print("failed: %s is not a dir." % args['<work-root-path>'])
                                return

                        execconf.set('root', 'there', workroot1)
                        execconf.write(open(pymakeexecini, 'w'))
                        print("successed: change there work root to %s." % workroot1)
                        return

                    if(args['<work-root-path>'] == 'here' or args['<work-root-path>'] == 'hh'
                    or args['<work-root-path>'] == 'there' or args['<work-root-path>'] == 'tt'
                    or args['<work-root-path>'] == 'default' or args['<work-root-path>'] == 'dd' ):
                        workroottype1 = args['<work-root-path>']
                        execconf.set('work', 'where', workroottype1)
                        execconf.write(open(pymakeexecini, 'w'))
                        print("successed: change starting work root to %s." % workroottype1)
                        return

                    workroot1 = args['<work-root-path>']
                    if(os.path.isabs(workroot1) is False):
                        print("please appoint an absolute work root for setting there starting work root path.")
                        return

                    if(os.path.isdir(workroot1) is False):
                        print("failed: %s is not a dir." % args['<work-root-path>'])
                        return

                    execconf.set('work', 'where', 'there')
                    execconf.set('root', 'there', workroot1)
                    execconf.write(open(pymakeexecini, 'w'))
                    print ("successed: change work root to custom position %s." % workroot1)
                    return
                else:
                    workroottype1 = 'default'
                    if (args['here'] or args['hh'] is True):
                        workroottype1 = 'here'
                    elif (args['there'] or args['tt'] is True):
                        workroottype1 = 'there'
                    elif (args['default'] or args['dd'] is True):
                        workroottype1 = 'default'
                    else:
                        workroottype1 = 'default'
                    execconf.set('work', 'where', workroottype1)
                    execconf.write(open(pymakeexecini, 'w'))
                    print ("successed: change starting work root to %s." % workroottype1)
                    return
            else:
                ''
        else:
            ''
        break

    # set
    while (True):
        if (args['set'] == True):
            if (args['env'] is True):
                if (args['default'] or args['current'] or args['cur'] is True):
                    if (args["<name>"] is not None):
                        if (config['environ'].__contains__(args['<name>']) is False
                            or args['<name>'] == "current"):
                            print("please ensure the environ is right")
                            return
                        config["environ"]["current"] = args["<name>"]
                        print("successed: %s" % (args['<name>']))
                    else:
                        ""
                elif (args["path"] is True):
                    if(args['<group>'] is not None):
                        if(args['<group>'] == 'current'):
                            args['<group>'] = config['environ']['current']
                            #print('failed: group name canot be \'current\'.')
                            #return
                    if (args['--add'] == True):
                        if (args['<group>'] and args['<name>'] is not None):
                            config['environ'][args['<group>']]["path+"].append(args["<name>"])
                            print ("successed: %s:%s" % (args['<group>'], args['<name>']))
                        else:""
                    elif (args['--del'] == True):
                        if (args['<group>'] and args["<name>"] is not None):
                            if (config['environ'][args['<group>']]["path+"].__contains__(args['<name>'])):
                                config['environ'][args['<group>']]["path+"].__delitem__(args['<name>'])
                                print("successed: %s:%s" % (args['<group>'], args['<name>']))
                            else:
                                print("failed %s:%s" % (args['<group>'], args['<name>']))
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            if (config['environ'][args['<group>']]["path+"].__contains__(args['<name>'])):
                                index = config['environ'][args['<group>']]["path+"].index(args['<name>'])
                                config['environ'][args['<group>']]["path+"][index] = [args['<value>']]
                                print ("successed: %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                            else:
                                print("failed %s:%s" % (args['<group>'], args['<name>']))
                        else:
                            ''
                else:
                    if(args['<group>'] is not None):
                        if(args['<group>'] == 'current'):
                            args['<group>'] = config['environ']['current']
                            #print(args['<group>'])
                            #print('failed: env name canot be \'current\'.')
                            #return
                    if (args['<name>'] is not None):
                        if (args['<name>'] == 'path+'):
                            print('failed: var name canot be \'path+\'.')
                            return
                    if (args['--add'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            config['environ'][args['<group>']][args['<name>']] = args["<value>"]
                            print ("successed: %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                        else:
                            print ("failed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                    elif (args['--del'] == True):
                        if (args['<group>'] and args["<name>"] is not None):
                            if (config['environ'][args['<group>']].__contains__(args['<name>'])):
                                config['environ'][args['<group>']].__delitem__(args['<name>'])
                                print ("successed: %s:%s" % (args['<group>'], args['<name>']))
                            else:
                                print ("failed %s:%s" % (args['<group>'], args['<name>']))
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            if (config['environ'][args['<group>']].__contains__(args['<name>'])):
                                config['environ'][args['<group>']][args['<name>']] = args["<value>"]
                                print ("successed: %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                            else:
                                print ("failed: %s { %s : %s }" % (args['<group>'], args['<name>'], args["<value>"]))
                        else:
                            ''
                    else:
                        ''
            elif (args['cmd'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<values>"] is not None):
                        config["command"][args['<name>']] = args["<values>"]
                        #print("successed: %s:%s" % (args['<name>'], args["<values>"]))
                        print('successed: %s is added.' % args['<name>'])
                        for cmd in args['<values>']:
                            print('  ' + cmd)
                    else:
                        print("failed %s:%s" % (args['<name>'], args["<values>"]))
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['command'].__contains__(args['<name>'])):
                            config["command"].__delitem__(args['<name>'])
                            print("successed: %s is deleted." % (args['<name>']))
                        else:
                            print("failed %s" % (args['<name>']))
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<values>"] is not None):
                        config["command"][args['<name>']] = args["<values>"]
                        #print("successed: %s:%s" % (args['<name>'], args["<values>"]))
                        print('successed: %s is modified.' % args['<name>'])
                        for cmd in args['<values>']:
                            print('  ' + cmd)
                    else:
                        print("failed %s:%s" % (args['<name>'], args["<values>"]))
                else:
                    ''
            elif (args['path'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        config['path-assemblage'][args['<name>']] = args["<value>"]
                        print ("successed: %s:%s" % (args['<name>'], args["<value>"]))
                    else:
                        print ("failed %s:%s" % (args['<name>'], args["<value>"]))
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['path-assemblage'].__contains__(args['<name>'])):
                            config['path-assemblage'].__delitem__(args['<name>'])
                            print ("successed: %s" % (args['<name>']))
                        else:
                            print ("failed %s" % (args['<name>']))
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        if (config['path-assemblage'].__contains__(args['<name>'])):
                            config['path-assemblage'][args['<name>']] = args["<value>"]
                            print ("successed: %s:%s" % (args['<name>'], args["<value>"]))
                        else:
                            print ("failed %s:%s" % (args['<name>'], args["<value>"]))
                    else:
                        ''
                else:
                    for (key,path0) in config['path-assemblage'].items():
                        print("%-30s %s" % (key, path0))
            else:
                ''
            # print(config)
            writeJsonData(sourceconfigfile, config)
            return
        else:
            ''
        break

    # get
    while (True):
        if(args['get'] is True):
            if(args['exec'] is True):
                if (args['here'] or args['hh'] is True):
                    print("%s" % (pymakeworkpath))
                    return
                elif (args['there'] or args['tt'] is True):
                    print("%s" % (customshellroot))
                    return
                elif (args['default'] or args['dd'] is True):
                    print("%s" % (pymakeshellroot))
                    return
                else:
                    ""
                if (args['--position'] or args['-p'] is True):
                    print("%s" % (workroottype))
                    return
                #workroottype1 = execconf.get("work", "where")
                #print("WORK ROOT TYPE     : %s" % (workroottype1))
                #print("STARTING WORK ROOT : %s" % (shellroot))
                print("%s" % (shellroot))
                return
            else:
                ''
        else:
            ''
        break

    # record system environ
    pymakesystemenviron = copy.deepcopy(os.environ)

    ### config -> raw config
    rawconfig = copy.deepcopy(config)
    # print ( config )
    # print ( rawconfig )

    #replace path
    for (key, value) in rawconfig["path-assemblage"].items():
        #print (key) #...

        startpos = 0
        while (True):
            #print (startpos)

            index = value.find('${', startpos)
            if (index == -1):
                break

            index2 = value.find('}', index)
            startpos = index2

            key_replace = value[index:index2 + 1]
            #print ( key0 ) #${...}
            key_from = key_replace.split('{')[1].split('}')[0].strip()
            #print ( key1 ) #...

            for (find_key, find_value) in rawconfig["path-assemblage"].items():
                if (key == find_key):
                    break
                if (find_key == key_from):
                    rawconfig["path-assemblage"][key] = rawconfig["path-assemblage"][key].replace(
                        key_replace, rawconfig["path-assemblage"][key_from])
                    #print("xxx %s" % rawconfig["path-assemblage"][key])
                    break

            #NO! ignore [in command, has various interpretations]
            #for (find_key, find_value) in pymakesystemenviron.items():
            #    if (key == find_key):
            #        break
            #    if (str(find_key).lower() == 'path'):
            #        continue
            #    if (find_key == key_from):
            #        rawconfig["path-assemblage"][key] = rawconfig["path-assemblage"][key].replace(
            #            key_replace, pymakesystemenviron[key_from])
            #        # print("xxx %s" % rawconfig["path-assemblage"][key])
            #        break

        #fix windows platform path sep
        #but no nessesary
        plat = getplatform()
        if (plat == "Windows"):
            ""
            #rawconfig["path-assemblage"][key] = rawconfig["path-assemblage"][key].replace('/', os.path.sep)

    #replace env
    #from path var env
    for current_var in rawconfig["environ"].keys():
        if( current_var == "current"):
            continue
        #replace path+
        step = 0
        for value in rawconfig["environ"][current_var]['path+']:
            startpos = 0
            while (True):
                # print (startpos)
                # print (value)

                index = value.find('${', startpos)
                if (index == -1):
                    break

                index2 = value.find('}', index)
                startpos = index2

                key_replace = value[index:index2 + 1]
                # print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                # print ( key1 ) #...

                for (find_key, find_value) in rawconfig["path-assemblage"].items():
                    if (find_key == key_from):
                        rawconfig["environ"][current_var]['path+'][step] = rawconfig["environ"][current_var]['path+'][step].replace(
                            key_replace, rawconfig["path-assemblage"][key_from])
                        break
            step += 1
        for (key, value) in rawconfig["environ"][current_var].items():
            #print (key) #...
            if(key == "path+"):
                continue

            startpos = 0
            while (True):
                #print (startpos)

                index = value.find('${', startpos)
                if (index == -1):
                    break

                index2 = value.find('}', index)
                startpos = index2

                key_replace = value[index:index2 + 1]
                #print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                #print ( key1 ) #...

                for (find_key, find_value) in rawconfig["path-assemblage"].items():
                    if (find_key == key_from):
                        rawconfig["environ"][current_var][key] = rawconfig["environ"][current_var][key].replace(
                            key_replace, rawconfig["path-assemblage"][key_from])
                        break

                for (find_key, find_value) in rawconfig["environ"][current_var].items():
                    if (key == find_key):
                        break
                    if (find_key == key_from):
                        rawconfig["environ"][current_var][key] = rawconfig["environ"][current_var][key].replace(
                            key_replace, rawconfig["environ"][current_var][key_from])
                        break

    # replace cmd
    # from path env
    for (cmd, stream) in rawconfig["command"].items():
        #print (key) #...

        step = 0
        for value in stream:
            startpos = 0
            while (True):
                # print (startpos)
                # print (value)

                index = value.find('${', startpos)
                if (index == -1):
                    break

                index2 = value.find('}', index)
                startpos = index2

                key_replace = value[index:index2 + 1]
                #print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                #print ( key1 ) #...

                for (find_key, find_value) in rawconfig["path-assemblage"].items():
                    if (find_key == key_from):
                        rawconfig['command'][cmd][step] = rawconfig['command'][cmd][step].replace(
                            key_replace, rawconfig["path-assemblage"][key_from])
                        break

                current_env_var = rawconfig["environ"]["current"]
                for (find_key, find_value) in rawconfig["environ"][current_env_var].items():
                    if (find_key == key_from):
                        rawconfig['command'][cmd][step] = rawconfig['command'][cmd][step].replace(
                            key_replace, rawconfig["environ"][current_env_var][key_from])
                        break
            step += 1

    # raw path function, parse custom path tuple
    def raw_path(pathgroup0):
        pathgroup = copy.deepcopy(pathgroup0)

        # replace path
        for (key, value) in enumerate(pathgroup):
            # print (key) #...

            startpos = 0
            while (True):
                # print (startpos)

                index = value.find('${', startpos)
                if (index == -1):
                    break

                index2 = value.find('}', index)
                startpos = index2

                key_replace = value[index:index2 + 1]
                # print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                # print ( key1 ) #...

                for (find_key, find_value) in rawconfig["path-assemblage"].items():
                    if (key == find_key):
                        break
                    if (find_key == key_from):
                        pathgroup[key] = pathgroup[key].replace(key_replace, rawconfig["path-assemblage"][key_from])
                        # print("xxx %s" % pathgroup[key])
                        break
        return pathgroup

    # custom command function
    # custom command stream from rawconfig
    def raw_command(env_name=None):
        command_dict = copy.deepcopy(config['command'])

        # replace cmd
        # from path env
        for (cmd, stream) in command_dict.items():
            # print (key) #...

            step = 0
            for value in stream:
                startpos = 0
                while (True):
                    # print (startpos)
                    # print (value)

                    index = value.find('${', startpos)
                    if (index == -1):
                        break

                    index2 = value.find('}', index)
                    startpos = index2

                    key_replace = value[index:index2 + 1]
                    # print ( key0 ) #${...}
                    key_from = key_replace.split('{')[1].split('}')[0].strip()
                    # print ( key1 ) #...

                    for (find_key, find_value) in rawconfig["path-assemblage"].items():
                        if (find_key == key_from):
                            command_dict[cmd][step] = command_dict[cmd][step].replace(
                                key_replace, rawconfig["path-assemblage"][key_from])
                            break

                    current_env_var = env_name
                    if (env_name is None):
                        current_env_var = config["environ"]["current"]
                    for (find_key, find_value) in rawconfig["environ"][current_env_var].items():
                        if (find_key == key_from):
                            command_dict[cmd][step] = command_dict[cmd][step].replace(
                                key_replace, rawconfig["environ"][current_env_var][key_from])
                            break
                step += 1
        return command_dict

    # custom string dict -> raw dict
    def raw_string(pathgroup0, env_name=None):
        pathgroup = {k: v for k, v in pathgroup0.items()}
        #print(pathgroup)

        dict0 = {k: v for k, v in rawconfig['path-assemblage'].items()}
        dict1 = {}
        current_env = env_name
        if(current_env == "current"):
            current_env = rawconfig['environ']['current']
        if(env_name is not None):
            dict1 = {k: v for k, v in rawconfig['environ'][current_env].items()}
        dict2 = {k: v for k, v in os.environ.items()}

        # replace path
        for (key, value) in pathgroup.items():
            #print (key, value) #...

            if(instanceof(value) != 'str'):
                continue

            if (dict0.__contains__(value) is True):
                pathgroup[key] = dict0[value]
                #print(pathgroup[key])
                continue

            if (dict2.__contains__(value) is True):
                pathgroup[key] = dict2[value]
                continue

            if (dict1.__contains__(value) is True):
                pathgroup[key] = dict1[value]
                continue

            startpos = 0
            while (True):
                # print (startpos)

                index = value.find('${', startpos)
                if (index == -1):
                    break

                index2 = value.find('}', index)
                startpos = index2

                key_replace = value[index:index2 + 1]
                # print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                # print ( key1 ) #...

                for (find_key, find_value) in dict0.items():
                    #print("%-30s, %-30s, %-30s, path-assemblage" % (key, key_from, find_key))
                    if (key == find_key):
                        break
                    #if (find_key == 'path+'):
                    #    continue
                    #if (find_key == "path"):
                    #    continue
                    if (find_key == key_from):
                        pathgroup[key] = pathgroup[key].replace(key_replace, dict0[key_from])
                        #print("path-assemblage %s" % pathgroup[key])
                        break

                for (find_key, find_value) in dict2.items():
                    #print("%-30s, %-30s, %-30s, system env" % (key, key_from, find_key))
                    if (key == find_key):
                        break
                    #if (find_key == 'path+'):
                    #    continue
                    if (find_key == "path"):
                        continue
                    if (find_key == key_from):
                        pathgroup[key] = pathgroup[key].replace(key_replace, dict2[key_from])
                        # print("system env %s" % pathgroup[key])
                        break

                for (find_key, find_value) in dict1.items():
                    #print("%-30s, %-30s, %-30s, separate env" % (key, key_from, find_key))
                    if (key == find_key):
                        break
                    if (find_key == 'path+'):
                        continue
                    # if (find_key == "path"):
                    #    continue
                    if (find_key == key_from):
                        pathgroup[key] = pathgroup[key].replace(key_replace, dict1[key_from])
                        # print("separate env %s" % pathgroup[key])
                        break

        return pathgroup

    # custom string dict -> raw dict [ignore case]
    def raw_string1(pathgroup0, env_name=None):
        #pathgroup = {k: v.lower() for k, v in pathgroup0.items()}
        pathgroup1 = {k: v for k, v in pathgroup0.items()}
        #print(pathgroup)

        dict0 = {k.lower(): v for k, v in rawconfig['path-assemblage'].items()}
        dict1 = {}
        current_env = env_name
        if(current_env == "current"):
            current_env = rawconfig['environ']['current']
        if(env_name is not None):
            dict1 = {k.lower(): v for k, v in rawconfig['environ'][current_env].items()}
        dict2 = {k.lower(): v for k, v in os.environ.items()}

        # replace path
        for (key, value) in pathgroup0.items():
            #print (key, value) #...

            if(instanceof(value) != 'str'):
                continue

            if (dict0.__contains__(value.lower()) is True):
                pathgroup1[key] = dict0[value.lower()]
                #print(pathgroup1[key])
                continue

            if (dict2.__contains__(value.lower()) is True):
                pathgroup1[key] = dict2[value.lower()]
                continue

            if (dict1.__contains__(value.lower()) is True):
                pathgroup1[key] = dict1[value.lower()]
                continue

            startpos = 0
            while (True):
                # print (startpos)

                index = value.find('${', startpos)
                if (index == -1):
                    break

                index2 = value.find('}', index)
                startpos = index2

                key_replace = value[index:index2 + 1]
                # print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                # print ( key1 ) #...

                for (find_key, find_value) in dict0.items():
                    #print("%-30s, %-30s, %-30s, path-assemblage" % (key, key_from, find_key))
                    if (key.lower() == find_key):
                        break
                    #if (find_key == 'path+'):
                    #    continue
                    #if (find_key == "path"):
                    #    continue
                    if (find_key == key_from.lower()):
                        pathgroup1[key] = pathgroup1[key].replace(key_replace, key_replace.lower())
                        pathgroup1[key] = pathgroup1[key].replace(key_replace.lower(), dict0[key_from.lower()])
                        #print("path-assemblage %s" % pathgroup1[key])
                        break

                for (find_key, find_value) in dict2.items():
                    #print("%-30s, %-30s, %-30s, system env" % (key, key_from, find_key))
                    if (key.lower() == find_key):
                        break
                    #if (find_key == 'path+'):
                    #    continue
                    if (find_key == "path"):
                        continue
                    if (find_key == key_from.lower()):
                        pathgroup1[key] = pathgroup1[key].replace(key_replace, key_replace.lower())
                        pathgroup1[key] = pathgroup1[key].replace(key_replace.lower(), dict2[key_from.lower()])
                        # print("system env %s" % pathgroup1[key])
                        break

                for (find_key, find_value) in dict1.items():
                    #print("%-30s, %-30s, %-30s, separate env" % (key, key_from, find_key))
                    if (key.lower() == find_key):
                        break
                    if (find_key == 'path+'):
                        continue
                    # if (find_key == "path"):
                    #    continue
                    if (find_key == key_from.lower()):
                        pathgroup1[key] = pathgroup1[key].replace(key_replace, key_replace.lower())
                        pathgroup1[key] = pathgroup1[key].replace(key_replace.lower(), dict1[key_from.lower()])
                        #print("separate env %s" % pathgroup1[key])
                        break

        return pathgroup1

    # which command [internal]
    def which_command(env_name = None, name = '', postfix = []):
        if(name is None or name == ''):
            return None

        #get python command.
        pycmd = name

        #get path ext
        pathext = []
        pathext.append('')
        pathext.extend(postfix)
        plat = getplatform()
        if(plat == "Windows"):
            pathext.extend(os.environ['PATHEXT'].split(os.path.pathsep))
        else:
            pathext.extend(['.sh','.out','.cmd'])

        #find in current path
        specialpath = [
            pymakeworkpath,
            os.getcwd()
        ]
        list0 = copy.deepcopy(specialpath)
        list0.reverse()
        for path0a in list0:
            for path0 in path0a.split(os.path.pathsep):
                path0 = path0.strip()
                # print(path0)
                path1 = ''
                for pext0 in pathext:
                    path1 = path0 + os.path.sep + pycmd + pext0
                    if(os.path.isfile(path1)):
                        if (plat == "Windows"):
                            return path1.replace('/', '\\')
                        else:
                            return path1.replace('\\', '/')

        if(env_name is not None):
            if(rawconfig['environ'].__contains__(env_name) is False):
                print("Fault Error! .json file is broken, env %s is losing!" % env_name)
                return None

            #find in separate env
            list0 = copy.deepcopy(rawconfig['environ'][env_name]['path+'])
            list0.reverse()
            for path0a in list0:
                for path0 in path0a.split(os.path.pathsep):
                    path0 = path0.strip()
                    # print(path0)
                    path1 = ''
                    for pext0 in pathext:
                        path1 = path0 + os.path.sep + pycmd + pext0
                        if(os.path.isfile(path1)):
                            if (plat == "Windows"):
                                return path1.replace('/', '\\')
                            else:
                                return path1.replace('\\', '/')

        # find in env. [custom+, local+, system]
        env = os.environ
        #for pathA in env['PATH'].split(os.path.pathsep):
        #    print(pathA)
        list0 = copy.deepcopy(env['PATH'].split(os.path.pathsep))
        #list0.reverse()
        for path0a in list0:
            for path0 in path0a.split(os.path.pathsep):
                path0 = path0.strip()
                #print(path0)
                path1 = ''
                for pext0 in pathext:
                    path1 = path0 + os.path.sep + pycmd + pext0
                    #print("[%s]" % path1)
                    if(os.path.isfile(path1)):
                        if (plat == "Windows"):
                            return path1.replace('/', '\\')
                        else:
                            return path1.replace('\\', '/')

        return None

    # which file [internal]
    def which_file(env_name = None, name = '', postfix = []):
        if(name is None or name == ''):
            return None

        #get python command.
        pycmd = name

        #get path ext
        pathext = []
        pathext.append('')
        pathext.extend(postfix)
        plat = getplatform()
        if(plat == "Windows"):
            pathext.extend([])
        else:
            pathext.extend([])

        #find in current path
        specialpath = [
            pymakeworkpath,
            os.getcwd()
        ]
        list0 = copy.deepcopy(specialpath)
        list0.reverse()
        for path0a in list0:
            for path0 in path0a.split(os.path.pathsep):
                path0 = path0.strip()
                # print(path0)
                path1 = ''
                for pext0 in pathext:
                    path1 = path0 + os.path.sep + pycmd + pext0
                    if(os.path.isfile(path1)):
                        if (plat == "Windows"):
                            return path1.replace('/', '\\')
                        else:
                            return path1.replace('\\', '/')

        if(env_name is not None):
            if(rawconfig['environ'].__contains__(env_name) is False):
                print("Fault Error! .json file is broken, env %s is losing!" % env_name)
                return None

            #find in separate env
            list0 = copy.deepcopy(rawconfig['environ'][env_name]['path+'])
            list0.reverse()
            for path0a in list0:
                for path0 in path0a.split(os.path.pathsep):
                    path0 = path0.strip()
                    # print(path0)
                    path1 = ''
                    for pext0 in pathext:
                        path1 = path0 + os.path.sep + pycmd + pext0
                        if(os.path.isfile(path1)):
                            if (plat == "Windows"):
                                return path1.replace('/', '\\')
                            else:
                                return path1.replace('\\', '/')

        # find in env. [custom+, local+, system]
        env = os.environ
        #for pathA in env['PATH'].split(os.path.pathsep):
        #    print(pathA)
        list0 = copy.deepcopy(env['PATH'].split(os.path.pathsep))
        #list0.reverse()
        for path0a in list0:
            for path0 in path0a.split(os.path.pathsep):
                path0 = path0.strip()
                #print(path0)
                path1 = ''
                for pext0 in pathext:
                    path1 = path0 + os.path.sep + pycmd + pext0
                    #print("[%s]" % path1)
                    if(os.path.isfile(path1)):
                        if (plat == "Windows"):
                            return path1.replace('/', '\\')
                        else:
                            return path1.replace('\\', '/')

        return None

    # pymake expand command-line.
    #current_var = args['<env-name>']
    #args = raw_string(args, current_var)
    #print(args)
    #for (k, v) in args.items():
    #    if(isinstance(v, str)):
    #        print(k, v)
    #return

    # system command function
    # system command stream from rawconfig path-assemblage
    def raw_command_system():
        command_dict = copy.deepcopy(config['command'])

        # replace cmd
        # from path env
        for (cmd, stream) in command_dict.items():
            # print (key) #...

            step = 0
            for value in stream:
                startpos = 0
                while (True):
                    # print (startpos)
                    # print (value)

                    index = value.find('${', startpos)
                    if (index == -1):
                        break

                    index2 = value.find('}', index)
                    startpos = index2

                    key_replace = value[index:index2 + 1]
                    # print ( key0 ) #${...}
                    key_from = key_replace.split('{')[1].split('}')[0].strip()
                    # print ( key1 ) #...

                    for (find_key, find_value) in rawconfig["path-assemblage"].items():
                        if (find_key == key_from):
                            command_dict[cmd][step] = command_dict[cmd][step].replace(
                                key_replace, rawconfig["path-assemblage"][key_from])
                            break

                step += 1
        return command_dict

    #.bat .sh, windows, unix, system
    def createCmdList06(env_name = None, local = True, list0 = [], params0 = []):
        cmd_list = []

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            cmd_call = "call "
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            if(env_name != None):
                cmd_list.append("call %s_effect.bat" % name)
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            if(env_name != None):
                cmd_list.append("source %s_effect.sh" % name)

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        if ( local is True):
            for cmd in list0:
                cmd_list.append(cmd)
        else:
            for cmd in list0:
                if (str(cmd).__contains__(' ')):
                    pycmd = which_command(env_name, str(cmd))
                    #print(pycmd)
                    if(pycmd is not None and os.path.isfile(pycmd)):
                        cmd_list.append('"' + cmd + '"' + ' ' + params_string)
                    else:
                        cmd_list.append(cmd + ' ' + params_string)
                else:
                    cmd_list.append(cmd + ' ' + params_string)

        # append exit 0
        cmd_list.append(cmd_exit)
        #print( cmd_list )

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        #print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("call " + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("./" + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)

        cmd_list.append(cmd_exit)

        # print (cmd_list)
        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        return cmd_list, name

    # system export function
    def system_env_export (env_name = None, file_name = None):
        if(env_name == None):
            return env_name, '', ''

        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name
        dict0 = copy.deepcopy(rawconfig['environ'][current_var])

        plat = getplatform()
        if (plat == "Windows"):
            cmd_suffix = ".bat"
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_return = "\n"
            cmd_header = "@echo off" + cmd_return
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash" + cmd_return
            env_set = 'export '

        #export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = file_name
        cmd_effect += '_effect' + cmd_suffix

        #export path
        lines = ""
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
            else:
                lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + cmd_return)
            else:
                lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        #export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = file_name
        cmd_unset += '_unset' + cmd_suffix

        #export unset path
        lines = ""
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

        #export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + cmd_return)
            else:
                lines += ('unset ' + key + cmd_return)
        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_effect)
            os.system("chmod +x " + cmd_unset)

        #return file name
        return current_var, cmd_effect, cmd_unset

    #print(args)
    # system ccvp
    while (True):
        if(args['sys'] or args['system'] is True):
            # print('system ccvp command.')
            if(args['ccvp'] or args['execvp'] or args['exec-with-params'] is True):
                current_env = ""
                if (args['use'] is True):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (current_env == 'current'
                        or rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = None

                if (args['<command-name>'] is None):
                    print("please appoint your command")
                    return

                #print(args['hh'])
                #print(args['here'])
                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                #print(args['--workroot'])
                if (args['--workroot'] is not None):
                    if (os.path.isdir(args['--workroot'])
                        and os.path.isabs(args['--workroot'])):
                        os.chdir(args['--workroot'])
                    else:
                        print('please input an existed and legal work root.')
                        return

                # create cmd_list
                current_var = current_env
                local_command = ''
                if(current_var == None):
                    local_command = raw_command_system()
                else:
                    local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                list0 = []
                local = True
                current_var = args['<command-name>']
                if (current_var in dict0):
                    list0.extend(dict0[current_var])
                    local = True
                else:
                    list0.append(current_var)
                    local = False

                params0 = []
                # print(args['--params'])
                # print(args['<command-params>'])
                for current_var in args['--params']:
                    params0.append(current_var)
                for current_var in args['<command-params>']:
                    params0.append(current_var)

                current_var = current_env
                cmd_list = []
                temp_file_name = ""
                # if (getplatform() == "Windows"):
                #    cmd_list, temp_file_name = createCmdList0(list0)
                # else:
                #    cmd_list, temp_file_name = createCmdList01(list0)
                # good compatibility
                cmd_list, temp_file_name = createCmdList06(current_var, local, list0, params0)

                # export env
                current_var = current_env
                # print (current_var, temp_file_name)
                system_env_export(current_var, temp_file_name)

                ret = communicateWithCommandLine(cmd_list)

                # delete env file and cmd file
                if (getplatform() == "Windows"):
                    temp_file = temp_file_name + "_exec.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                else:
                    temp_file = temp_file_name + "_exec.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)

                os._exit(ret)
                return
            else:
                ''
        else:
            ''
        break

    # outport command
    while (True):
        if (args['outport'] is True):
            if (args['cmd'] is True):
                print("source file   is %s" % sourceconfigfile)
                print("source root   is %s" % sourceroot)
                print("source config is %s" % sourcefile)
                print("---------------------------------------------------------------------")
                current_env = ""

                if (args['use'] is True):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = rawconfig['environ']['current']

                dict0 = {}
                #print(args)
                #args['-r'] or args['--raw'] all can effect here.
                if(args['--raw'] is True):
                    if (current_env == rawconfig['environ']['current']):
                        dict0 = copy.deepcopy(rawconfig['command'])
                    else:
                        dict0 = copy.deepcopy(raw_command(current_env))
                else:
                    dict0 = copy.deepcopy(config['command'])

                import itertools

                #os.chdir(sourceroot)

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                if (args['-a'] or args['--all'] is True):
                    # print('-a')
                    # print("%-30s %-5s %-5s" % (args['<script-file>'], os.path.isdir(args['<script-file>']), os.path.islink(args['<script-file>'])))

                    plat = getplatform()
                    if(plat == "Windows"):
                        cmd_header = "@echo off"
                        cmd_codec = "ansi"
                        if (getplatform_release() == "XP"):
                            cmd_codec = None
                        # but windows, it is \r\n, python helpping me?
                        cmd_return = "\n"
                        cmd_suffix = ".bat"
                    else:
                        cmd_header = "#!/usr/bin/env bash"
                        cmd_codec = "utf8"
                        cmd_return = "\n"
                        cmd_suffix = ".sh"

                    cmd_suffix_custom = cmd_suffix
                    suffix = args['--suffix']
                    if (suffix is not None):
                        cmd_suffix_custom = str("%s" % suffix)

                    root_path = ""
                    if (args['<script-file>'] is not None):
                        root_path = args['<script-file>']
                    else:
                        root_path = os.getcwd()

                    if(os.path.exists(root_path) is False):
                        os.mkdir(root_path)

                    print(Fore.CYAN + "%-30s%-30s%s" % ("[command] ", "[status] ", "[file] "))

                    useencoding = cmd_codec
                    if (args['--encoding'] is not None):
                        useencoding = args['--encoding']

                    for (key1) in dict0:
                        local_path = os.path.relpath(os.path.join(root_path, key1+cmd_suffix_custom), os.getcwd())
                        command_name = key1
                        #print(command_name, local_path)

                        # fixer
                        # ext = os.path.splitext(os.path.basename(key1))[1]
                        # if (ext == '.bat'):
                        #    useencoding = 'gbk'
                        cmd_header_custom = ''
                        # add shebang line
                        if (list(dict0[command_name]).__len__() > 0):
                            cmd_header_custom = dict0[command_name][0]
                        # print(".....")
                        if (plat == "Windows"):
                            if (cmd_header_custom.startswith('@echo') is False):
                                cmd_header_custom = cmd_header
                            else:
                                cmd_header_custom = ''
                        else:
                            if (cmd_header_custom.startswith('#!') is False):
                                cmd_header_custom = cmd_header
                            else:
                                cmd_header_custom = ''

                        if(cmd_suffix_custom != cmd_suffix):
                            cmd_header_custom = ''

                        if (os.path.exists(local_path) is False):
                            with open(local_path, 'w', encoding=useencoding) as f:
                                if(cmd_header_custom != ''):
                                    f.write(cmd_header_custom + cmd_return)
                                for l in dict0[command_name]:
                                    f.write(l + cmd_return)
                            if (plat == "Windows"):
                                ""
                            else:
                                if(cmd_suffix_custom == cmd_suffix):
                                    os.system("chmod +x " + local_path)
                            print("%-30s%-30s%s" % (command_name, "[SUCCESS][       ][     ]", local_path))
                        else:
                            if (args['-f'] or args['--force'] is True):
                                with open(local_path, 'w', encoding=useencoding) as f:
                                    if (cmd_header_custom != ''):
                                        f.write(cmd_header_custom + cmd_return)
                                    for l in dict0[command_name]:
                                        f.write(l + cmd_return)
                                if (plat == "Windows"):
                                    ""
                                else:
                                    if (cmd_suffix_custom == cmd_suffix):
                                        os.system("chmod +x " + local_path)
                                print("%-30s%-30s%s" % (command_name, "[SUCCESS][EXISTED][FORCE]", key1))
                            else:
                                print("%-30s%-30s%s" % (command_name, "[CANCEL ][EXISTED][     ]", key1))
                    return

                if (args['<command-name>'] is None):
                    print(Fore.CYAN + "%-30s%-30s" % ("[command] ", "[file] "))
                    keylist1 = []
                    keylist2 = []

                    #print(args['<command-name>'])
                    #print(args['<script-file>'])

                    root_path = ""
                    if (args['<script-file>'] is not None):
                        root_path = args['<script-file>']
                    else:
                        root_path = os.getcwd()

                    #print(args)
                    #print(args['-r'], args['--recursive'])
                    if(args['--recursive'] is True):
                        for ( dirpath, dirnames, filenames ) in os.walk(root_path):
                            for name in filenames:
                                #print(os.path.relpath(os.path.join(dirpath, name), os.getcwd()))
                                keylist1.append(os.path.relpath(os.path.join(dirpath, name), os.getcwd()))
                    else:
                        for key in os.listdir(root_path):
                            keylist1.append(os.path.relpath(os.path.join(root_path, key), os.getcwd()))

                    #for key in os.listdir(os.getcwd()):
                    #    keylist1.append(key)

                    for key in config['command'].keys():
                        keylist2.append(key)

                    dirlist = []
                    for (key) in keylist1:
                        # print("%-30s %-5s %-5s" % (key, os.path.isdir(key), os.path.islink(key)))
                        if (os.path.isdir(key)
                            # or os.path.islink(key)
                            ):
                            dirlist.append(key)
                    # print(dirlist)
                    for key in dirlist:
                        keylist1.remove(key)

                    tarkeylist = []
                    # print(args['--suffix'])
                    if (args['--suffix'] is None or args['--suffix'] == [] or args['--suffix'] == [''] or args['--suffix'] == ['*']):
                        tarkeylist = keylist1
                    else:
                        filterString = args['--suffix']
                        if(filterString == None):
                            filterString = ''
                        filterList = filterString.split('|')
                        while (filterList.__contains__('')):
                            filterList.remove('')
                        # print(filterString)
                        # print(filterList)
                        for fil in filterList:
                            fil = fil.strip()
                            for key in keylist1:
                                if (os.path.splitext(key)[1] == fil):
                                    tarkeylist.append(key)
                                    # print(fil, key)
                    # print(tarkeylist)
                    # for file in tarkeylist:
                    #    print (file)
                    # return

                    # print(keylist1)
                    # print(keylist2)
                    count2 = 1
                    for (key1, key2) in itertools.zip_longest(tarkeylist, keylist2, fillvalue=""):
                        if (key1 != ""):
                            key1 = str("%s" % (key1))
                        if (key2 != ""):
                            key2 = str("%-4s%s" % (count2, key2))
                            count2 += 1
                        print("%-30s%-30s" % (key2, key1))

                    # print("Those are the files under %s" % os.getcwd())
                    return

                if (args['<command-name>'] is not None):
                    # print("%-30s %-5s %-5s" % (args['<script-file>'], os.path.isdir(args['<script-file>']), os.path.islink(args['<script-file>'])))
                    if(args['<script-file>'] is not None):
                        if (os.path.isdir(args['<script-file>'])):
                            print(Fore.CYAN + "%-30s%-30s" % ("[command] ", "[file] "))
                            keylist1 = []
                            keylist2 = []

                            # print(args['<command-name>'])
                            # print(args['<script-file>'])

                            root_path = ""
                            if (args['<script-file>'] is not None):
                                root_path = args['<script-file>']
                            else:
                                root_path = os.getcwd()

                            # print(args)
                            # print(args['-r'], args['--recursive'])
                            if (args['--recursive'] is True):
                                for (dirpath, dirnames, filenames) in os.walk(root_path):
                                    for name in filenames:
                                        # print(os.path.relpath(os.path.join(dirpath, name), os.getcwd()))
                                        keylist1.append(os.path.relpath(os.path.join(dirpath, name), os.getcwd()))
                            else:
                                for key in os.listdir(root_path):
                                    keylist1.append(os.path.relpath(os.path.join(root_path, key), os.getcwd()))

                            # for key in os.listdir(os.getcwd()):
                            #    keylist1.append(key)

                            for key in config['command'].keys():
                                keylist2.append(key)

                            dirlist = []
                            for (key) in keylist1:
                                # print("%-30s %-5s %-5s" % (key, os.path.isdir(key), os.path.islink(key)))
                                if (os.path.isdir(key)
                                    # or os.path.islink(key)
                                    ):
                                    dirlist.append(key)
                            # print(dirlist)
                            for key in dirlist:
                                keylist1.remove(key)

                            tarkeylist = []
                            # print(args['--suffix'])
                            if (args['--suffix'] is None or args['--suffix'] == [] or args['--suffix'] == [''] or args['--suffix'] == ['*']):
                                tarkeylist = keylist1
                            else:
                                filterString = args['--suffix']
                                if (filterString == None):
                                    filterString = ''
                                filterList = filterString.split('|')
                                while (filterList.__contains__('')):
                                    filterList.remove('')
                                # print(filterString)
                                # print(filterList)
                                for fil in filterList:
                                    fil = fil.strip()
                                    for key in keylist1:
                                        if (os.path.splitext(key)[1] == fil):
                                            tarkeylist.append(key)
                                            # print(fil, key)
                            # print(tarkeylist)
                            # for file in tarkeylist:
                            #    print (file)
                            # return

                            # print(keylist1)
                            # print(keylist2)
                            count2 = 1
                            for (key1, key2) in itertools.zip_longest(tarkeylist, keylist2, fillvalue=""):
                                if (key1 != ""):
                                    key1 = str("%s" % (key1))
                                if (key2 != ""):
                                    key2 = str("%-4s%s" % (count2, key2))
                                    count2 += 1
                                print("%-30s%-30s" % (key2, key1))

                            # print("Those are the files under %s" % os.path.realpath(args['<script-file>']))
                            return

                    plat = getplatform()
                    if(plat == "Windows"):
                        cmd_header = "@echo off"
                        cmd_codec = "ansi"
                        if (getplatform_release() == "XP"):
                            cmd_codec = None
                        # but windows, it is \r\n, python helpping me?
                        cmd_return = "\n"
                        cmd_suffix = ".bat"
                    else:
                        cmd_header = "#!/usr/bin/env bash"
                        cmd_codec = "utf8"
                        cmd_return = "\n"
                        cmd_suffix = ".sh"

                    cmd_suffix_custom = cmd_suffix
                    suffix = args['--suffix']
                    if (suffix is not None):
                        cmd_suffix_custom = str("%s" % suffix)

                    useencoding = cmd_codec
                    if (args['--encoding'] is not None):
                        useencoding = args['--encoding']

                    # args['<script-file>'] is a file.
                    root_path = ""
                    if (args['<script-file>'] is not None):
                        root_path = args['<script-file>'] + cmd_suffix_custom
                    else:
                        root_path = args['<command-name>'] + cmd_suffix_custom

                    command_name = args['<command-name>']
                    local_path = os.path.relpath(root_path, os.getcwd())

                    #print(args['<command-name>'], command_name)
                    #print(args['<script-file>'], local_path)
                    if(config['command'].__contains__(command_name) is False):
                        print ('please ensure your command name is existed.')
                        return

                    cmd_header_custom = ''
                    # add shebang line
                    if (list(dict0[command_name]).__len__() > 0):
                        cmd_header_custom = dict0[command_name][0]
                    #print(cmd_header_custom)
                    if (plat == "Windows"):
                        #print(cmd_header_custom.startswith('@echo'))
                        if (cmd_header_custom.startswith('@echo') is False):
                            cmd_header_custom = cmd_header
                        else:
                            cmd_header_custom = ''
                    else:
                        if (cmd_header_custom.startswith('#!') is False):
                            cmd_header_custom = cmd_header
                        else:
                            cmd_header_custom = ''

                    if (cmd_suffix_custom != cmd_suffix):
                        cmd_header_custom = ''
                    #print(cmd_header_custom)

                    # print(args)
                    if (os.path.exists(local_path) is True):
                        if (args['-f'] or args['--force'] is True):
                            # print('-f')
                            # set in force
                            with open(local_path, 'w', encoding=useencoding) as f:
                                if(cmd_header_custom != ''):
                                    f.write(cmd_header_custom + cmd_return)
                                for l in dict0[command_name]:
                                    f.write(l + cmd_return)
                            if (plat == "Windows"):
                                ""
                            else:
                                if(cmd_suffix_custom == cmd_suffix):
                                    os.system("chmod +x " + local_path)
                            print('successed: outport %s to %s' % (command_name, local_path))
                            return
                        print("failed: script file %s is existed." % local_path)
                        return

                    # set in
                    with open(local_path, 'w', encoding=useencoding) as f:
                        if (cmd_header_custom != ''):
                            f.write(cmd_header_custom + cmd_return)
                        for l in dict0[command_name]:
                            f.write(l + cmd_return)
                    if (plat == "Windows"):
                        ""
                    else:
                        if (cmd_suffix_custom == cmd_suffix):
                            os.system("chmod +x " + local_path)
                    print('successed: outport %s to %s' % (command_name, local_path))
                    return
                return
            else:
                ''
        else:
            ''
        break

    # get open path's cmd list
    def open_command (pathlist0, env_name = None):
        pathgroup0 = {}
        for (k,v) in enumerate(pathlist0):
            pathgroup0[str('-pymake-open-p%d'%k)] = str(v)

        cmd_list = []
        pathgroup1 = {}
        #if(args['-i'] or args['--ignorecase'] is True):
        #    pathgroup1 = raw_string1(pathgroup0, env_name)
        #else:
        #    pathgroup1 = raw_string(pathgroup0, env_name)
        pathgroup1 = raw_string1(pathgroup0, env_name)

        plat = getplatform()
        for (k, v) in pathgroup1.items():
            path0 = str(v)
            pathslist = path0.split(os.path.pathsep)
            while (pathslist.__contains__('')):
                pathslist.remove('')
            #print(pathslist)
            for path0 in pathslist:
                cmd0 = ''
                if (plat == "Windows"):
                    if(path0.__contains__(' ')):
                        cmd0 = 'start "" ' + '"%s"' % path0
                    else:
                        cmd0 = "start " + path0
                elif (plat == "Darwin"):
                    if(path0.__contains__(' ')):
                        cmd0 = 'open ' + '"%s"' % path0
                    else:
                        cmd0 = "open " + path0
                else:
                    if(path0.__contains__(' ')):
                        cmd0 = 'xdg-open ' + '"%s" ' % path0 + ">/dev/null 2>&1"
                    else:
                        cmd0 = "xdg-open " + '%s ' % path0 + ">/dev/null 2>&1"
                cmd_list.append(cmd0)

        return cmd_list

    #print(args)
    # open command
    while (True):
        if(args['open'] is True):
            ''

            if(args['debug'] is True):
                break
            if(args['local'] is True):
                break
            if(args['custom'] is True):
                break

            if(args['<path-name>'] == []):
                ''
                dict0 = copy.deepcopy(rawconfig['path-assemblage'])
                pos0 = 0
                for (key, value) in dict0.items():
                    pos0 = pos0 + 1
                    if(pos0 % 3 == 0):
                        print("%-30s" % key)
                        continue
                    print("%-30s" % key, end=' ')

                return

            #print("use", args['use'])
            #print("-c", args['-c'], args['--custom'])
            #print("-i", args['-i'], args['--ignorecase'])
            #print("--current", args['--current'])
            #print(args['<path-name>'])
            #print("--envname", args['--envname'], args['<env-name>'])
            #return

            if(args['use'] is True):
                break
            if(args['-c'] or args['--custom'] is True):
                break
            if(args['--current'] is True):
                break
            if(args['--envname'] is not None or args['<env-name>'] is not None):
                break
            #print('......')

            pathname = args['<path-name>']
            cmd_list = open_command(pathlist0=pathname, env_name=None)
            for cmd in cmd_list:
                os.system(cmd)
                print('successed: %s' % cmd)
            return
        else:
            ''
        break

    # pymake local const variable.
    localini = sourceroot + os.path.sep + "local.ini"
    localconf = MyConfigParser()
    localconf.read(localini)
    if (not localconf.has_section('local')):
        localconf.add_section('local')
        localconf.write(open(localini, 'w'))
    if (not localconf.has_section('path+')):
        localconf.add_section('path+')
        localconf.write(open(localini, 'w'))
    if (not localconf.has_section('variable')):
        localconf.add_section('variable')
        localconf.write(open(localini, 'w'))

    #status readonly
    #if( not localconf.has_option('local', 'status') ):
    #    localconf.set('local', 'status', 'readonly')
    #    localconf.write(open(localini, 'w'))

    #localswitch = localconf['local']['status']
    #if(localswitch != 'readonly'):
    #    localswitch = 'readonly'
    #    localconf.set('local', 'status', localswitch)
    #    localconf.write(open(localini, 'w'))

    #switch [1, default]
    if( not localconf.has_option('local', 'switch') ):
        localconf.set('local', 'switch', '1')
        localconf.write(open(localini, 'w'))

    localswitch = localconf['local']['switch']
    if(localswitch != '0' and localswitch != '1'):
        localswitch = '1'
        localconf.set('local', 'switch', localswitch)
        localconf.write(open(localini, 'w'))

    localenv = {}
    localenv['path+'] = []

    # set into env [no effect to system environ]
    while (True):
        if(int(localswitch) == 0):
            break

        env = os.environ

        localenv['PYMAKEDEFAULTSOURCEROOT'] = pymakesourceroot
        localenv['PYMAKEDEFAULTSOURCECONFIG'] = pymakedefaultsourcefile

        localenv['PYMAKESOURCEFILE'] = sourceconfigfile
        localenv['PYMAKESOURCEROOT'] = sourceroot
        localenv['PYMAKESOURCECONFIG'] = sourcefile

        localenv['PYMAKEDEFAULTWORKROOT'] = pymakeshellroot
        localenv['PYMAKETHEREWORKROOT'] = customshellroot
        localenv['PYMAKEHEREWORKROOT'] = pymakeworkpath
        localenv['PYMAKEWORKROOT'] = shellroot

        if(args['here'] or args['hh'] is True):
            localenv['PYMAKEWORKROOT'] = pymakeworkpath
        elif(args['there'] or args['tt'] is True):
            localenv['PYMAKEWORKROOT'] = customshellroot
        elif(args['default'] or args['dd'] is True):
            localenv['PYMAKEWORKROOT'] = pymakeshellroot

        if (args['--workroot'] is not None):
            if (os.path.isdir(args['--workroot'])
                and os.path.isabs(args['--workroot'])):
                localenv['PYMAKEWORKROOT'] = args['--workroot']
                #os.chdir(args['--workroot'])
            else:
                print('please input a legal work root.')
                return

        localenv['PYMAKEPROGRAM'] = os.path.realpath(__file__)
        localenv['PYMAKEPROGRAMROOT'] = os.path.split(os.path.realpath(__file__))[0]
        localenv['PYMAKEPROGRAMFILE'] = os.path.split(os.path.realpath(__file__))[1]

        localenv['PYMAKEPROGRAMCONFIGURE'] = os.path.realpath(pymakeini)
        localenv['PYMAKEPROGRAMCONFIGUREROOT'] = os.path.split(os.path.realpath(pymakeini))[0]
        localenv['PYMAKEPROGRAMCONFIGUREFILE'] = os.path.split(os.path.realpath(pymakeini))[1]

        if(getplatform() == 'Windows'):
            localenv['PYMAKEINSTALLROOT'] = env['windir']
        else:
            localenv['PYMAKEINSTALLROOT'] = '/usr/local/bin'

        localenv['path+'].append(localenv['PYMAKESOURCEROOT'])
        localenv['path+'].append(localenv['PYMAKEPROGRAMROOT'])
        localenv['path+'].append(localenv['PYMAKEDEFAULTWORKROOT'])
        #if(localenv['path+'].__contains__(localenv['PYMAKETHEREWORKROOT']) is False):
        localenv['path+'].append(localenv['PYMAKETHEREWORKROOT'])
        #if(localenv['path+'].__contains__(localenv['PYMAKEHEREWORKROOT']) is False):
        localenv['path+'].append(localenv['PYMAKEHEREWORKROOT'])
        #if(localenv['path+'].__contains__(localenv['PYMAKEWORKROOT']) is False):
        localenv['path+'].append(localenv['PYMAKEWORKROOT'])

        #store to file
        for (key, value) in enumerate(localenv["path+"]):
            localconf.set('path+', str("%d" % key), value)

        for (key, value) in localenv.items():
            if (key == 'path+'):
                continue
            localconf.set('variable', key, value)

        localconf.write(open(localini, 'w'))

        #set into env
        for (key) in localenv["path+"]:
            env["PATH"] = key + os.path.pathsep + env["PATH"]

        for (key, value) in localenv.items():
            if (key == 'path+'):
                continue
            env[key] = value
        break

    #local command
    while (True):
        if( args['local'] is True ):
            #print('gggg')
            if(args['open'] is True):
                localconf.set('local', 'switch', '1')
                localconf.write(open(localini, 'w'))
                print('success: local environment is opened.')
                return
            elif (args['close'] is True):
                localconf.set('local', 'switch', '0')
                localconf.write(open(localini, 'w'))
                print('success: local environment is closed.')
                return
            elif (args['export'] is True):
                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                plat = getplatform()
                if (plat == "Windows"):
                    cmd_suffix = ".bat"
                    cmd_codec = "ansi"
                    if (getplatform_release() == "XP"):
                        cmd_codec = None
                    cmd_return = "\n"
                    cmd_header = "@echo off" + cmd_return
                    env_set = 'set '
                else:
                    cmd_suffix = ".sh"
                    cmd_codec = "utf8"
                    cmd_return = "\n"
                    cmd_header = "#!/usr/bin/env bash" + cmd_return
                    env_set = 'export '

                # export effect env
                cmd_effect = 'local.env'
                if (args['<file-name>'] is not None):
                    cmd_effect = "local." + args['<file-name>']
                cmd_effect += '_effect' + cmd_suffix

                lines = ""
                # export path
                #print(localenv['path+'])
                for (key) in localenv['path+']:
                    if (plat == "Windows"):
                        lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
                    else:
                        lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

                # export var
                for (key, value) in localenv.items():
                    if (key == 'path+'):
                        continue
                    if (plat == "Windows"):
                        lines += (env_set + key + '=' + value + cmd_return)
                    else:
                        lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

                #print("------------------")
                #print(lines)
                with open(cmd_effect, 'w') as f:
                    f.write(cmd_header)
                    f.write(lines)

                # export unset env
                cmd_unset = 'local.env'
                if (args['<file-name>'] is not None):
                    cmd_unset = "local." + args['<file-name>']
                cmd_unset += '_unset' + cmd_suffix

                # export unset path
                lines = ""
                for (key) in localenv['path+']:
                    if (plat == "Windows"):
                        lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
                    else:
                        lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

                # export unset var
                for (key, value) in localenv.items():
                    if (key == 'path+'):
                        continue
                    if (plat == "Windows"):
                        lines += ('set ' + key + '=' + cmd_return)
                    else:
                        lines += ('unset ' + key + cmd_return)

                #print("------------------")
                #print(lines)
                with open(cmd_unset, 'w') as f:
                    f.write(cmd_header)
                    f.write(lines)

                if (plat == "Windows"):
                    ""
                else:
                    os.system("chmod +x " + cmd_effect)
                    os.system("chmod +x " + cmd_unset)

                print("successed: export local env to %s %s" % (cmd_effect, cmd_unset))
                return
            elif (args['edit'] is True):
                ''
                cmd_list = []
                cmd_list.append(sourceroot + os.path.sep + 'local.ini')
                for file0 in cmd_list:
                    cmd0 = open_file(file0)
                    os.system(cmd0)
                    print('successed: %s' % file0)
                return
            elif(args['info'] or args['information'] is True):
                print("LOCAL SETTING: %s" % (localini))
                print("LOCAL ENV+   : %s" % (localini + " [variable]"))
                print("LOCAL PATH+  : %s" % (localini + " [path+]"))
                return
            elif (args['ccvp'] or args['execvp'] or args['exec-with-params'] is True):
                # print('local ccvp command.')
                current_env = ""
                if (args['use'] is True):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (current_env == 'current'
                        or rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = None

                if (args['<command-name>'] is None):
                    print("please appoint your command")
                    return

                # print(args['hh'])
                # print(args['here'])
                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                # print(args['--workroot'])
                if (args['--workroot'] is not None):
                    if (os.path.isdir(args['--workroot'])
                        and os.path.isabs(args['--workroot'])):
                        os.chdir(args['--workroot'])
                    else:
                        print('please input an existed and legal work root.')
                        return

                # create cmd_list
                current_var = current_env
                local_command = ''
                if (current_var == None):
                    local_command = raw_command_system()
                else:
                    local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                list0 = []
                local = True
                current_var = args['<command-name>']
                if (current_var in dict0):
                    list0.extend(dict0[current_var])
                    local = True
                else:
                    list0.append(current_var)
                    local = False

                params0 = []
                # print(args['--params'])
                # print(args['<command-params>'])
                for current_var in args['--params']:
                    params0.append(current_var)
                for current_var in args['<command-params>']:
                    params0.append(current_var)

                current_var = current_env
                cmd_list = []
                temp_file_name = ""
                # if (getplatform() == "Windows"):
                #    cmd_list, temp_file_name = createCmdList0(list0)
                # else:
                #    cmd_list, temp_file_name = createCmdList01(list0)
                # good compatibility
                cmd_list, temp_file_name = createCmdList06(current_var, local, list0, params0)

                # export env
                current_var = current_env
                # print (current_var, temp_file_name)
                system_env_export(current_var, temp_file_name)

                ret = communicateWithCommandLine(cmd_list)

                # delete env file and cmd file
                if (getplatform() == "Windows"):
                    temp_file = temp_file_name + "_exec.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                else:
                    temp_file = temp_file_name + "_exec.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)

                os._exit(ret)
                return
            elif (args['path'] is True):
                if(args['<value>'] is None):
                    print(Fore.LIGHTGREEN_EX + "path+:")
                    for (key) in localenv['path+']:
                        print(Fore.LIGHTMAGENTA_EX + "  %s" % key)
                    return
                return
            elif (args['var'] is True):
                if (args['<key>'] is None):
                    print(Fore.LIGHTGREEN_EX + "variable:")
                    for (key, value) in localenv.items():
                        if (key == 'path+'):
                            continue
                        print(Fore.GREEN + "  %-30s %s" % (key, value))
                    return
                return
            elif (args['env'] is True):
                #print(args)
                print (Fore.CYAN+ "local env")

                envcustomlist0 = localenv['path+']
                envcustomlist1 = localenv
                if(args['--raw'] is True):
                    envcustomlist0 = localenv['path+']
                    envcustomlist1 = localenv

                print(Fore.LIGHTGREEN_EX + "path+:")
                for (key) in envcustomlist0:
                    print(Fore.LIGHTMAGENTA_EX + "  %s" % key)
                print(Fore.LIGHTGREEN_EX + "variable:")
                for (key, value) in envcustomlist1.items():
                    if (key == 'path+'):
                        continue
                    print(Fore.GREEN + "  %-30s %s" % (key, value))

                return
            elif (args['stat'] or args['status'] is True):
                status = "closed"
                if(localswitch == '1'):
                    status = "opened"
                print("local env: %s." % status)
                return
            else:
                status = "closed"
                if(localswitch == '1'):
                    status = "opened"
                print("local env: %s." % status)
                if(localswitch == '1'):
                    print(Fore.LIGHTGREEN_EX + "path+:")
                    for (key) in localenv['path+']:
                        print(Fore.LIGHTMAGENTA_EX + "  %s" % key)
                    print(Fore.LIGHTGREEN_EX + "variable:")
                    for (key, value) in localenv.items():
                        if (key == 'path+'):
                            continue
                        print(Fore.GREEN + "  %-30s %s" % (key, value))
                return
        else:
            ''
        break

    #initial custom environ module
    pymakecustomini = sourceroot + os.path.sep + "custom.ini"
    customconf = MyConfigParser()
    customconf.read(pymakecustomini)
    if( not customconf.has_section('custom') ):
        customconf.add_section('custom')
        customconf.write(open(pymakecustomini, 'w'))
    if( not customconf.has_option('custom', 'switch') ):
        customconf.set('custom', 'switch', '1')
        customconf.write(open(pymakecustomini, 'w'))

    switch0 = customconf['custom']['switch']
    if(switch0 != '0' and switch0 != '1'):
        switch0 = '1'
        customconf.set('custom', 'switch', switch0)
        customconf.write(open(pymakecustomini, 'w'))

    custompathfile = sourceroot + os.path.sep + "custom.path+.ini"
    customenvfile = sourceroot + os.path.sep + "custom.var+.ini"

    storecustompaths = []
    storecustomvars = []

    envcustomlistpaths = []
    envcustomlistvars = {}

    envcustomlistrawpaths = []
    envcustomlistrawvars = {}

    plat = getplatform()
    cmd_codec = "utf8"
    cmd_return = "\n"
    if (plat == "Windows"):
        cmd_codec = "ansi"
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
    else:
        cmd_codec = "utf8"
        cmd_return = "\n"

    #custom environ
    #user can use custom environ to effect pymake basic environment.
    #it will effect every executing environment.
    while (True):

        if(int(switch0) == 0):
            break

        #print("open custom environ.")

        # set custom path+ to env.
        # print(sourceroot)
        # print(shellroot)
        # init file
        #custompathfile = sourceroot + os.path.sep + "custom.path+.ini"
        if (os.path.exists(custompathfile) is False):
            with open(custompathfile, 'w', encoding=cmd_codec) as f:
                ''

        # read all
        custompaths = []
        with open(custompathfile, 'r', encoding=cmd_codec) as f:
            for l in f.readlines():
                # important format
                # l = l.strip()
                while (l.endswith('\r') or l.endswith('\n') or l.endswith('\r\n')):
                    l = l.rstrip('\r\n')
                    l = l.rstrip('\n')
                    l = l.rstrip('\r')
                # if(l == ''):
                #    continue
                custompaths.append(l)
        # while(custompaths.__contains__('') is True):
        # custompaths.remove('')
        # print(custompaths)
        # print(os.linesep)
        # for l in custompaths:
        #    print("AAAA:" + l)

        # write back

        #strip
        storecustompaths = copy.deepcopy(custompaths)
        for (i, l) in enumerate(storecustompaths):
            # import format
            l = l.strip()
            storecustompaths[i] = l

        # added by local, ignore
        '''
        # default [ fixed ]
        # add pymake default source root to environ.
        if (storecustompaths.__contains__(pymakesourceroot) is False):
            storecustompaths.append(pymakesourceroot)
        # add pymake default shell root to environ.
        if (storecustompaths.__contains__(pymakeshellroot) is False):
            storecustompaths.append(pymakeshellroot)
        # default [ movable, follow user source root ]
        # add user source root to environ.
        if (sourceroot != pymakesourceroot and storecustompaths.__contains__(sourceroot) is False):
            storecustompaths.append(sourceroot)
        # add user shell root to environ.
        if (customshellroot != pymakeshellroot and storecustompaths.__contains__(customshellroot) is False):
            storecustompaths.append(customshellroot)
        if (pymakeworkpath != pymakeshellroot and storecustompaths.__contains__(pymakeworkpath) is False):
            storecustompaths.append(pymakeworkpath)
        if (shellroot != pymakeshellroot and storecustompaths.__contains__(shellroot) is False):
            storecustompaths.append(shellroot)
        '''
        
        #clean repeat path [for store]
        clean_list = []
        temp_list = []
        for l in storecustompaths:
            if (l == ''):
                continue
            if (os.path.isabs(l) is False):
                continue
            if (temp_list.__contains__(str(l).replace('\\', '/').lower())):
                clean_list.append(l)
                continue
            else:
                temp_list.append(str(l).replace('\\', '/').lower())
        #print(clean_list)
        storecustompaths.reverse()
        for l in clean_list:
            if (storecustompaths.__contains__(l) is True):
                storecustompaths.remove(l)
        storecustompaths.reverse()

        if (custompaths != storecustompaths):
            with open(custompathfile, 'w', encoding=cmd_codec) as f:
                for l in storecustompaths:
                    f.write(l + cmd_return)

        # set into env

        #raw
        envcustompaths = copy.deepcopy(storecustompaths)
        envcustomrawpaths = raw_path(envcustompaths)
        #print(envcustompaths)
        #print(envcustomrawpaths)

        #envcustomlistpaths
        for (key,l) in zip(envcustompaths, envcustomrawpaths):
            if (l == ''):
                continue
            #print(os.path.isabs(l), l)
            if (os.path.isabs(l) is False):
                continue
            envcustomlistpaths.append(key)

        # clean illgal path
        clean_list = []
        for l in envcustomrawpaths:
            if (l == ''):
                clean_list.append(l)
                continue
            if (os.path.isabs(l) is False):
                clean_list.append(l)
                continue
        #print(clean_list)

        for l in clean_list:
            if (envcustomrawpaths.__contains__(l) is True):
                envcustomrawpaths.remove(l)

        env = os.environ
        for l in envcustomrawpaths:
            env["PATH"] = l + os.path.pathsep + env["PATH"]

        for l in envcustomrawpaths:
            envcustomlistrawpaths.append(l)

        # set custom env+ to env.
        #customenvfile = sourceroot + os.path.sep + "custom.var+.ini"
        # print(customenvfile)
        # init
        if (os.path.exists(customenvfile) is False):
            with open(customenvfile, 'w', encoding=cmd_codec) as f:
                ''

        # read all
        customenvs = []
        with open(customenvfile, 'r', encoding=cmd_codec) as f:
            for l in f.readlines():
                # important format
                # l = l.strip()
                while (l.endswith('\r') or l.endswith('\n') or l.endswith('\r\n')):
                    l = l.rstrip('\r\n')
                    l = l.rstrip('\n')
                    l = l.rstrip('\r')
                # if(l == ''):
                #    continue
                customenvs.append(l)

        # write back

        #strip
        storecustomvars = copy.deepcopy(customenvs)
        for (i, l) in enumerate(storecustomvars):
            # important format
            l = l.strip()
            storecustomvars[i] = l

        avarkeyvalue = "PYMAKEAUTHOR=T.D.R."
        if (storecustomvars.__contains__(avarkeyvalue) is False):
            storecustomvars.append(avarkeyvalue)

        #clean repeat var [for store]
        clean_list = []
        temp_list = []
        for l in storecustomvars:
            if (l == ''):
                continue
            if (str(l).__contains__('=') is False):
                continue
            if (temp_list.__contains__(str(l).split('=')[0].strip().lower())):
                clean_list.append(l)
                continue
            else:
                temp_list.append(str(l).split('=')[0].strip().lower())
        #print(clean_list)
        storecustomvars.reverse()
        for l in clean_list:
            if (storecustomvars.__contains__(l) is True):
                storecustomvars.remove(l)
        storecustomvars.reverse()

        if (storecustomvars != customenvs):
            with open(customenvfile, 'w', encoding=cmd_codec) as f:
                for l in storecustomvars:
                    f.write(l + cmd_return)

        # set into env

        #raw
        envcustomvars = copy.deepcopy(storecustomvars)
        envcustomrawvars = raw_path(envcustomvars)
        #print(envcustomvars)
        #print(envcustomrawvars)
        for (key0,l) in zip(envcustomvars, envcustomrawvars):
            if (l == ''):
                continue
            if (str(l).__contains__('=') is False):
                continue
            key = str(key0).split('=')[0].strip()
            value = '='.join(str(key0).split('=')[1:]).strip()
            envcustomlistvars[key] = value

        # clean illgal var
        clean_list = []
        for l in envcustomrawvars:
            if (l == ''):
                clean_list.append(l)
                continue
            if (str(l).__contains__('=') is False):
                clean_list.append(l)
                continue
        # print(clean_list)

        for l in clean_list:
            if (envcustomrawvars.__contains__(l) is True):
                envcustomrawvars.remove(l)

        env = os.environ
        for l in envcustomrawvars:
            key = str(l).split('=')[0].strip()
            value = '='.join(str(l).split('=')[1:]).strip()
            env[key] = value

        for l in envcustomrawvars:
            key = str(l).split('=')[0].strip()
            value = '='.join(str(l).split('=')[1:]).strip()
            envcustomlistrawvars[key] = value

        break

    # initial vc module
    #record vc shell root.
    vcroot = sourceroot + os.path.sep + "VCShell"
    if(not os.path.exists(vcroot)):
        os.mkdir(vcroot)

    # check command
    while (True):
        if(args['chk'] or args['check'] is True):
            ''
            normal_num = 0
            unparsed_num = 0
            unexisted_num = 0
            unknownerror_num = 0

            if(args['path'] is True):
                itemname = None
                if(args['<item-name>'] is not None):
                    itemname = args['<item-name>']
                if(args['--item'] is not None):
                    itemname = args['--item']

                itemgroup = {}
                if(args['-a'] or args['--all'] is True):
                    itemgroup = rawconfig['path-assemblage']
                elif(itemname is None):
                    ''
                else:
                    if(rawconfig['path-assemblage'].__contains__(itemname) is False):
                        print('please input an existed path item.')
                        return
                    itemgroup.__setitem__(itemname, rawconfig['path-assemblage'][itemname])
                print('path-assemblage:')
                for (key, value) in itemgroup.items():
                    path0 = str(value)
                    pathslist = path0.split(os.path.pathsep)
                    while (pathslist.__contains__('')):
                        pathslist.remove('')
                    # print(pathslist)
                    pathslist1 = []
                    for path1 in pathslist:
                        if(os.path.isabs(path1) and os.path.exists(path1)):
                            pathslist1.append(Fore.GREEN + path1)
                            normal_num = normal_num + 1
                        elif(path1.__contains__('${') and path1.__contains__('}')):
                            pathslist1.append(Fore.MAGENTA + path1)
                            unparsed_num = unparsed_num + 1
                        elif(os.path.isabs(path1) and os.path.exists(path1) is False):
                            pathslist1.append(Fore.RED + path1)
                            unexisted_num = unexisted_num + 1
                        else:
                            pathslist1.append(Fore.YELLOW + path1)
                            unknownerror_num = unknownerror_num + 1
                    path2 = os.path.pathsep.join(pathslist1)
                    if(path2.__contains__(Fore.GREEN)):
                        path2 = '%-100s %s %s' % (path2, Fore.RESET+'normal_num:', normal_num)
                    if(path2.__contains__(Fore.MAGENTA)):
                        path2 = '%-100s %s %s' % (path2, Fore.RESET+'unparsed_num:', unparsed_num)
                    if(path2.__contains__(Fore.RED)):
                        path2 = '%-100s %s %s' % (path2, Fore.RESET+'unexisted_num:', unexisted_num)
                    if(path2.__contains__(Fore.YELLOW)):
                        path2 = '%-100s %s %s' % (path2, Fore.RESET+'unknownstring_num:', unknownerror_num)
                    print('  %-30s %s' %(Fore.GREEN+key, path2))

            elif(args['cmd'] is True):
                itemname = None
                if (args['<item-name>'] is not None):
                    itemname = args['<item-name>']
                if (args['--item'] is not None):
                    itemname = args['--item']

                itemgroup = {}
                if (args['-a'] is True or args['--all'] is True):
                    itemgroup = rawconfig['command']
                elif(itemname is None):
                    ''
                else:
                    if (rawconfig['command'].__contains__(itemname) is False):
                        print('please input an existed cmd item.')
                        return
                    itemgroup.__setitem__(itemname, rawconfig['command'][itemname])

                for (current_cmd, env_value) in itemgroup.items():
                    print('cmd %s:' % current_cmd)
                    for (key) in rawconfig['command'][current_cmd]:
                        path0 = str(key)
                        pathslist = path0.split(os.path.pathsep)
                        while (pathslist.__contains__('')):
                            pathslist.remove('')
                        # print(pathslist)
                        pathslist1 = []
                        for path1 in pathslist:
                            if (os.path.isabs(path1) and os.path.exists(path1)):
                                pathslist1.append(Fore.GREEN + path1)
                                normal_num = normal_num + 1
                            elif (path1.__contains__('${') and path1.__contains__('}')):
                                pathslist1.append(Fore.MAGENTA + path1)
                                unparsed_num = unparsed_num + 1
                            elif (os.path.isabs(path1) and os.path.exists(path1) is False):
                                pathslist1.append(Fore.RED + path1)
                                unexisted_num = unexisted_num + 1
                            else:
                                pathslist1.append(Fore.YELLOW + path1)
                                unknownerror_num = unknownerror_num + 1
                        path2 = os.path.pathsep.join(pathslist1)
                        if (path2.__contains__(Fore.GREEN)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET + 'normal_num:', normal_num)
                        if (path2.__contains__(Fore.MAGENTA)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unparsed_num:', unparsed_num)
                        if (path2.__contains__(Fore.RED)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unexisted_num:', unexisted_num)
                        if (path2.__contains__(Fore.YELLOW)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unknownstring_num:', unknownerror_num)
                        print('  ' + path2)

            else:
                current_env = None
                if (args['<env-name>'] is not None):
                    current_var = args['<env-name>']
                    if (current_var is None):
                        current_var = rawconfig['environ']['current']
                    elif (current_var == "current"):
                        current_var = rawconfig['environ']['current']
                    current_env = current_var

                if (args['--current'] is True):
                    current_env = rawconfig['environ']['current']

                if (args['--envname'] is not None):
                    current_var = args['--envname']
                    if (current_var is None):
                        current_var = rawconfig['environ']['current']
                    elif (current_var == "current"):
                        current_var = rawconfig['environ']['current']
                    current_env = current_var

                if (args['-a'] or args['--all'] is True):
                    current_env = rawconfig['environ']['current']

                if (current_env is not None):
                    if (rawconfig['environ'].__contains__(current_env) is False):
                        print("please ensure the environ is right")
                        return

                if (args['-s'] or args['--system'] is True):
                    print('system env')
                    print('path+:')
                    for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                        path0 = str(key)
                        pathslist = path0.split(os.path.pathsep)
                        while (pathslist.__contains__('')):
                            pathslist.remove('')
                        # print(pathslist)
                        pathslist1 = []
                        for path1 in pathslist:
                            if(os.path.isabs(path1) and os.path.exists(path1)):
                                pathslist1.append(Fore.GREEN + path1)
                                normal_num = normal_num + 1
                            elif(path1.__contains__('${') and path1.__contains__('}')):
                                pathslist1.append(Fore.MAGENTA + path1)
                                unparsed_num = unparsed_num + 1
                            elif(os.path.isabs(path1) and os.path.exists(path1) is False):
                                pathslist1.append(Fore.RED + path1)
                                unexisted_num = unexisted_num + 1
                            else:
                                pathslist1.append(Fore.YELLOW + path1)
                                unknownerror_num = unknownerror_num + 1
                        path2 = os.path.pathsep.join(pathslist1)
                        if(path2.__contains__(Fore.GREEN)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'normal_num:', normal_num)
                        if(path2.__contains__(Fore.MAGENTA)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unparsed_num:', unparsed_num)
                        if(path2.__contains__(Fore.RED)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unexisted_num:', unexisted_num)
                        if(path2.__contains__(Fore.YELLOW)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unknownstring_num:', unknownerror_num)
                        print('  ' + path2)
                    print('variable:')
                    for (key, value) in pymakesystemenviron.items():
                        if (key == 'path+'):
                            continue
                        if (str(key).lower() == "path"):
                            continue
                        path0 = str(value)
                        pathslist = path0.split(os.path.pathsep)
                        while (pathslist.__contains__('')):
                            pathslist.remove('')
                        # print(pathslist)
                        pathslist1 = []
                        for path1 in pathslist:
                            if(os.path.isabs(path1) and os.path.exists(path1)):
                                pathslist1.append(Fore.GREEN + path1)
                                normal_num = normal_num + 1
                            elif(path1.__contains__('${') and path1.__contains__('}')):
                                pathslist1.append(Fore.MAGENTA + path1)
                                unparsed_num = unparsed_num + 1
                            elif(os.path.isabs(path1) and os.path.exists(path1) is False):
                                pathslist1.append(Fore.RED + path1)
                                unexisted_num = unexisted_num + 1
                            else:
                                pathslist1.append(Fore.YELLOW + path1)
                                unknownerror_num = unknownerror_num + 1
                        path2 = os.path.pathsep.join(pathslist1)
                        if(path2.__contains__(Fore.GREEN)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'normal_num:', normal_num)
                        if(path2.__contains__(Fore.MAGENTA)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unparsed_num:', unparsed_num)
                        if(path2.__contains__(Fore.RED)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unexisted_num:', unexisted_num)
                        if(path2.__contains__(Fore.YELLOW)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unknownstring_num:', unknownerror_num)
                        print('  %-30s %s' %(Fore.GREEN + key, path2))

                if(args['-l'] or args['--local'] is True):
                    print('local env')
                    print('path+:')
                    for (key) in localenv['path+']:
                        path0 = str(key)
                        pathslist = path0.split(os.path.pathsep)
                        while (pathslist.__contains__('')):
                            pathslist.remove('')
                        # print(pathslist)
                        pathslist1 = []
                        for path1 in pathslist:
                            if(os.path.isabs(path1) and os.path.exists(path1)):
                                pathslist1.append(Fore.GREEN + path1)
                                normal_num = normal_num + 1
                            elif(path1.__contains__('${') and path1.__contains__('}')):
                                pathslist1.append(Fore.MAGENTA + path1)
                                unparsed_num = unparsed_num + 1
                            elif(os.path.isabs(path1) and os.path.exists(path1) is False):
                                pathslist1.append(Fore.RED + path1)
                                unexisted_num = unexisted_num + 1
                            else:
                                pathslist1.append(Fore.YELLOW + path1)
                                unknownerror_num = unknownerror_num + 1
                        path2 = os.path.pathsep.join(pathslist1)
                        if(path2.__contains__(Fore.GREEN)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'normal_num:', normal_num)
                        if(path2.__contains__(Fore.MAGENTA)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unparsed_num:', unparsed_num)
                        if(path2.__contains__(Fore.RED)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unexisted_num:', unexisted_num)
                        if(path2.__contains__(Fore.YELLOW)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unknownstring_num:', unknownerror_num)
                        print('  ' + path2)
                    print('variable:')
                    for (key, value) in localenv.items():
                        if (key == 'path+'):
                            continue
                        path0 = str(value)
                        pathslist = path0.split(os.path.pathsep)
                        while (pathslist.__contains__('')):
                            pathslist.remove('')
                        # print(pathslist)
                        pathslist1 = []
                        for path1 in pathslist:
                            if(os.path.isabs(path1) and os.path.exists(path1)):
                                pathslist1.append(Fore.GREEN + path1)
                                normal_num = normal_num + 1
                            elif(path1.__contains__('${') and path1.__contains__('}')):
                                pathslist1.append(Fore.MAGENTA + path1)
                                unparsed_num = unparsed_num + 1
                            elif(os.path.isabs(path1) and os.path.exists(path1) is False):
                                pathslist1.append(Fore.RED + path1)
                                unexisted_num = unexisted_num + 1
                            else:
                                pathslist1.append(Fore.YELLOW + path1)
                                unknownerror_num = unknownerror_num + 1
                        path2 = os.path.pathsep.join(pathslist1)
                        if(path2.__contains__(Fore.GREEN)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'normal_num:', normal_num)
                        if(path2.__contains__(Fore.MAGENTA)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unparsed_num:', unparsed_num)
                        if(path2.__contains__(Fore.RED)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unexisted_num:', unexisted_num)
                        if(path2.__contains__(Fore.YELLOW)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unknownstring_num:', unknownerror_num)
                        print('  %-30s %s' %(Fore.GREEN+key, path2))

                if(args['-c'] or args['--custom'] is True):
                    print('custom env')
                    print('path+:')
                    for (key) in envcustomlistrawpaths:
                        path0 = str(key)
                        pathslist = path0.split(os.path.pathsep)
                        while (pathslist.__contains__('')):
                            pathslist.remove('')
                        # print(pathslist)
                        pathslist1 = []
                        for path1 in pathslist:
                            if(os.path.isabs(path1) and os.path.exists(path1)):
                                pathslist1.append(Fore.GREEN + path1)
                                normal_num = normal_num + 1
                            elif(path1.__contains__('${') and path1.__contains__('}')):
                                pathslist1.append(Fore.MAGENTA + path1)
                                unparsed_num = unparsed_num + 1
                            elif(os.path.isabs(path1) and os.path.exists(path1) is False):
                                pathslist1.append(Fore.RED + path1)
                                unexisted_num = unexisted_num + 1
                            else:
                                pathslist1.append(Fore.YELLOW + path1)
                                unknownerror_num = unknownerror_num + 1
                        path2 = os.path.pathsep.join(pathslist1)
                        if(path2.__contains__(Fore.GREEN)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'normal_num:', normal_num)
                        if(path2.__contains__(Fore.MAGENTA)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unparsed_num:', unparsed_num)
                        if(path2.__contains__(Fore.RED)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unexisted_num:', unexisted_num)
                        if(path2.__contains__(Fore.YELLOW)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unknownstring_num:', unknownerror_num)
                        print('  ' + path2)
                    print('variable:')
                    for (key, value) in envcustomlistrawvars.items():
                        if (key == 'path+'):
                            continue
                        path0 = str(value)
                        pathslist = path0.split(os.path.pathsep)
                        while (pathslist.__contains__('')):
                            pathslist.remove('')
                        # print(pathslist)
                        pathslist1 = []
                        for path1 in pathslist:
                            if(os.path.isabs(path1) and os.path.exists(path1)):
                                pathslist1.append(Fore.GREEN + path1)
                                normal_num = normal_num + 1
                            elif(path1.__contains__('${') and path1.__contains__('}')):
                                pathslist1.append(Fore.MAGENTA + path1)
                                unparsed_num = unparsed_num + 1
                            elif(os.path.isabs(path1) and os.path.exists(path1) is False):
                                pathslist1.append(Fore.RED + path1)
                                unexisted_num = unexisted_num + 1
                            else:
                                pathslist1.append(Fore.YELLOW + path1)
                                unknownerror_num = unknownerror_num + 1
                        path2 = os.path.pathsep.join(pathslist1)
                        if(path2.__contains__(Fore.GREEN)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'normal_num:', normal_num)
                        if(path2.__contains__(Fore.MAGENTA)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unparsed_num:', unparsed_num)
                        if(path2.__contains__(Fore.RED)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unexisted_num:', unexisted_num)
                        if(path2.__contains__(Fore.YELLOW)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unknownstring_num:', unknownerror_num)
                        print('  %-30s %s' %(Fore.GREEN+key, path2))

                if(current_env is not None):
                    print('env %s' % current_env)
                    print('path+:')
                    for (key) in rawconfig['environ'][current_env]['path+']:
                        path0 = str(key)
                        pathslist = path0.split(os.path.pathsep)
                        while (pathslist.__contains__('')):
                            pathslist.remove('')
                        # print(pathslist)
                        pathslist1 = []
                        for path1 in pathslist:
                            if(os.path.isabs(path1) and os.path.exists(path1)):
                                pathslist1.append(Fore.GREEN + path1)
                                normal_num = normal_num + 1
                            elif(path1.__contains__('${') and path1.__contains__('}')):
                                pathslist1.append(Fore.MAGENTA + path1)
                                unparsed_num = unparsed_num + 1
                            elif(os.path.isabs(path1) and os.path.exists(path1) is False):
                                pathslist1.append(Fore.RED + path1)
                                unexisted_num = unexisted_num + 1
                            else:
                                pathslist1.append(Fore.YELLOW + path1)
                                unknownerror_num = unknownerror_num + 1
                        path2 = os.path.pathsep.join(pathslist1)
                        if(path2.__contains__(Fore.GREEN)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'normal_num:', normal_num)
                        if(path2.__contains__(Fore.MAGENTA)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unparsed_num:', unparsed_num)
                        if(path2.__contains__(Fore.RED)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unexisted_num:', unexisted_num)
                        if(path2.__contains__(Fore.YELLOW)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unknownstring_num:', unknownerror_num)
                        print('  ' + path2)
                    print('variable:')
                    for (key, value) in rawconfig['environ'][current_env].items():
                        if (key == 'path+'):
                            continue
                        path0 = str(value)
                        pathslist = path0.split(os.path.pathsep)
                        while (pathslist.__contains__('')):
                            pathslist.remove('')
                        # print(pathslist)
                        pathslist1 = []
                        for path1 in pathslist:
                            if(os.path.isabs(path1) and os.path.exists(path1)):
                                pathslist1.append(Fore.GREEN + path1)
                                normal_num = normal_num + 1
                            elif(path1.__contains__('${') and path1.__contains__('}')):
                                pathslist1.append(Fore.MAGENTA + path1)
                                unparsed_num = unparsed_num + 1
                            elif(os.path.isabs(path1) and os.path.exists(path1) is False):
                                pathslist1.append(Fore.RED + path1)
                                unexisted_num = unexisted_num + 1
                            else:
                                pathslist1.append(Fore.YELLOW + path1)
                                unknownerror_num = unknownerror_num + 1
                        path2 = os.path.pathsep.join(pathslist1)
                        if(path2.__contains__(Fore.GREEN)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'normal_num:', normal_num)
                        if(path2.__contains__(Fore.MAGENTA)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unparsed_num:', unparsed_num)
                        if(path2.__contains__(Fore.RED)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unexisted_num:', unexisted_num)
                        if(path2.__contains__(Fore.YELLOW)):
                            path2 = '%-100s %s %s' % (path2, Fore.RESET+'unknownstring_num:', unknownerror_num)
                        print('  %-30s %s' %(Fore.GREEN+key, path2))

                    while (args['vc'] is True):
                        print('env %s - vc env' % current_env)
                        current_vcvarsall = 'vcvarsall'
                        current_vcvarsallparam = 'vcvarsallparam'
                        has_set = '0'
                        native_dict = {}
                        while(True):
                            if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                                native_dict = pymakesystemenviron
                                has_set = "system env:"
                            if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                                native_dict = envcustomlistrawvars
                                has_set = "custom env:"
                            if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                                native_dict = rawconfig['environ'][current_env]
                                has_set = str("env %s:" % current_env)
                            break

                        #print(has_set)
                        #if(has_set != '0'):
                        #    print(native_dict[current_vcvarsall])

                        if(has_set == '0'):
                            print("please set env variable: vcvarsall.")
                            break

                        if(native_dict.__contains__(current_vcvarsallparam) is False):
                            print("please set env variable: vcvarsallparam.")
                            break

                        print(has_set + ' %s %s' % (native_dict[current_vcvarsall],native_dict[current_vcvarsallparam]))

                        nowroot = os.getcwd()
                        #dict1 = copy.deepcopy(rawconfig['environ'][current_env])
                        dict1 = {}
                        dict1['path+'] = []
                        #for (k,v) in dict1.items():
                        #    print(k, v)
                        os.chdir(vcroot)
                        jsonfile = 'pymake-vc-command.json'
                        if(not os.path.exists(jsonfile)):
                            print('please init vc.')
                            break
                        dict0 = readJsonData(jsonfile)
                        if(dict0.__contains__('environ') is False):
                            print('please init vc.')
                            break
                        if(dict0['environ'].__contains__(current_env) is False):
                            print('please init vc for %s env.' % current_env)
                            break
                        for (key) in dict0['environ'][current_env]["path+"]:
                            dict1['path+'].append(key)
                        for (key, value) in dict0['environ'][current_env].items():
                            if (key == 'path+'):
                                continue
                            dict1[key]=value
                        os.chdir(nowroot)

                        print('path+:')
                        for (key) in dict1['path+']:
                            path0 = str(key)
                            pathslist = path0.split(os.path.pathsep)
                            while (pathslist.__contains__('')):
                                pathslist.remove('')
                            # print(pathslist)
                            pathslist1 = []
                            for path1 in pathslist:
                                if (os.path.isabs(path1) and os.path.exists(path1)):
                                    pathslist1.append(Fore.GREEN + path1)
                                    normal_num = normal_num + 1
                                elif (path1.__contains__('${') and path1.__contains__('}')):
                                    pathslist1.append(Fore.MAGENTA + path1)
                                    unparsed_num = unparsed_num + 1
                                elif (os.path.isabs(path1) and os.path.exists(path1) is False):
                                    pathslist1.append(Fore.RED + path1)
                                    unexisted_num = unexisted_num + 1
                                else:
                                    pathslist1.append(Fore.YELLOW + path1)
                                    unknownerror_num = unknownerror_num + 1
                            path2 = os.path.pathsep.join(pathslist1)
                            if (path2.__contains__(Fore.GREEN)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'normal_num:', normal_num)
                            if (path2.__contains__(Fore.MAGENTA)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unparsed_num:', unparsed_num)
                            if (path2.__contains__(Fore.RED)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unexisted_num:', unexisted_num)
                            if (path2.__contains__(Fore.YELLOW)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unknownstring_num:', unknownerror_num)
                            print('  ' + path2)
                        print('variable:')
                        for (key, value) in dict1.items():
                            if (key == 'path+'):
                                continue
                            path0 = str(value)
                            pathslist = path0.split(os.path.pathsep)
                            while (pathslist.__contains__('')):
                                pathslist.remove('')
                            # print(pathslist)
                            pathslist1 = []
                            for path1 in pathslist:
                                if (os.path.isabs(path1) and os.path.exists(path1)):
                                    pathslist1.append(Fore.GREEN + path1)
                                    normal_num = normal_num + 1
                                elif (path1.__contains__('${') and path1.__contains__('}')):
                                    pathslist1.append(Fore.MAGENTA + path1)
                                    unparsed_num = unparsed_num + 1
                                elif (os.path.isabs(path1) and os.path.exists(path1) is False):
                                    pathslist1.append(Fore.RED + path1)
                                    unexisted_num = unexisted_num + 1
                                else:
                                    pathslist1.append(Fore.YELLOW + path1)
                                    unknownerror_num = unknownerror_num + 1
                            path2 = os.path.pathsep.join(pathslist1)
                            if (path2.__contains__(Fore.GREEN)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'normal_num:', normal_num)
                            if (path2.__contains__(Fore.MAGENTA)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unparsed_num:', unparsed_num)
                            if (path2.__contains__(Fore.RED)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unexisted_num:', unexisted_num)
                            if (path2.__contains__(Fore.YELLOW)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unknownstring_num:', unknownerror_num)
                            print('  %-30s %s' % (Fore.GREEN + key, path2))

                        break

                if(args['-a'] or args['--all'] is True):
                    ''
                    for (current_env, env_value) in rawconfig['environ'].items():
                        if (current_env == 'current'):
                            continue
                        if (current_env == rawconfig['environ']['current']):
                            continue

                        print('env %s' % current_env)
                        print('path+:')
                        for (key) in rawconfig['environ'][current_env]['path+']:
                            path0 = str(key)
                            pathslist = path0.split(os.path.pathsep)
                            while (pathslist.__contains__('')):
                                pathslist.remove('')
                            # print(pathslist)
                            pathslist1 = []
                            for path1 in pathslist:
                                if (os.path.isabs(path1) and os.path.exists(path1)):
                                    pathslist1.append(Fore.GREEN + path1)
                                    normal_num = normal_num + 1
                                elif (path1.__contains__('${') and path1.__contains__('}')):
                                    pathslist1.append(Fore.MAGENTA + path1)
                                    unparsed_num = unparsed_num + 1
                                elif (os.path.isabs(path1) and os.path.exists(path1) is False):
                                    pathslist1.append(Fore.RED + path1)
                                    unexisted_num = unexisted_num + 1
                                else:
                                    pathslist1.append(Fore.YELLOW + path1)
                                    unknownerror_num = unknownerror_num + 1
                            path2 = os.path.pathsep.join(pathslist1)
                            if (path2.__contains__(Fore.GREEN)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'normal_num:', normal_num)
                            if (path2.__contains__(Fore.MAGENTA)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unparsed_num:', unparsed_num)
                            if (path2.__contains__(Fore.RED)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unexisted_num:', unexisted_num)
                            if (path2.__contains__(Fore.YELLOW)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unknownstring_num:', unknownerror_num)
                            print('  ' + path2)
                        print('variable:')
                        for (key, value) in rawconfig['environ'][current_env].items():
                            if (key == 'path+'):
                                continue
                            path0 = str(value)
                            pathslist = path0.split(os.path.pathsep)
                            while (pathslist.__contains__('')):
                                pathslist.remove('')
                            # print(pathslist)
                            pathslist1 = []
                            for path1 in pathslist:
                                if (os.path.isabs(path1) and os.path.exists(path1)):
                                    pathslist1.append(Fore.GREEN + path1)
                                    normal_num = normal_num + 1
                                elif (path1.__contains__('${') and path1.__contains__('}')):
                                    pathslist1.append(Fore.MAGENTA + path1)
                                    unparsed_num = unparsed_num + 1
                                elif (os.path.isabs(path1) and os.path.exists(path1) is False):
                                    pathslist1.append(Fore.RED + path1)
                                    unexisted_num = unexisted_num + 1
                                else:
                                    pathslist1.append(Fore.YELLOW + path1)
                                    unknownerror_num = unknownerror_num + 1
                            path2 = os.path.pathsep.join(pathslist1)
                            if (path2.__contains__(Fore.GREEN)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'normal_num:', normal_num)
                            if (path2.__contains__(Fore.MAGENTA)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unparsed_num:', unparsed_num)
                            if (path2.__contains__(Fore.RED)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unexisted_num:', unexisted_num)
                            if (path2.__contains__(Fore.YELLOW)):
                                path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unknownstring_num:', unknownerror_num)
                            print('  %-30s %s' % (Fore.GREEN + key, path2))

                        while (args['vc'] is True):
                            print('env %s - vc env' % current_env)
                            current_vcvarsall = 'vcvarsall'
                            current_vcvarsallparam = 'vcvarsallparam'
                            has_set = '0'
                            native_dict = {}
                            while (True):
                                if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                                    native_dict = pymakesystemenviron
                                    has_set = "system env:"
                                if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                                    native_dict = envcustomlistrawvars
                                    has_set = "custom env:"
                                if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                                    native_dict = rawconfig['environ'][current_env]
                                    has_set = str("env %s:" % current_env)
                                break

                            # print(has_set)
                            # if(has_set != '0'):
                            #    print(native_dict[current_vcvarsall])

                            if (has_set == '0'):
                                print("please set env variable: vcvarsall.")
                                break

                            if (native_dict.__contains__(current_vcvarsallparam) is False):
                                print("please set env variable: vcvarsallparam.")
                                break

                            print(has_set + ' %s %s' % (native_dict[current_vcvarsall], native_dict[current_vcvarsallparam]))

                            nowroot = os.getcwd()
                            # dict1 = copy.deepcopy(rawconfig['environ'][current_env])
                            dict1 = {}
                            dict1['path+'] = []
                            # for (k,v) in dict1.items():
                            #    print(k, v)
                            os.chdir(vcroot)
                            jsonfile = 'pymake-vc-command.json'
                            if (not os.path.exists(jsonfile)):
                                print('please init vc.')
                                break
                            dict0 = readJsonData(jsonfile)
                            if (dict0.__contains__('environ') is False):
                                print('please init vc.')
                                break
                            if (dict0['environ'].__contains__(current_env) is False):
                                print('please init vc for %s env.' % current_env)
                                break
                            for (key) in dict0['environ'][current_env]["path+"]:
                                dict1['path+'].append(key)
                            for (key, value) in dict0['environ'][current_env].items():
                                if (key == 'path+'):
                                    continue
                                dict1[key] = value
                            os.chdir(nowroot)

                            print('path+:')
                            for (key) in dict1['path+']:
                                path0 = str(key)
                                pathslist = path0.split(os.path.pathsep)
                                while (pathslist.__contains__('')):
                                    pathslist.remove('')
                                # print(pathslist)
                                pathslist1 = []
                                for path1 in pathslist:
                                    if (os.path.isabs(path1) and os.path.exists(path1)):
                                        pathslist1.append(Fore.GREEN + path1)
                                        normal_num = normal_num + 1
                                    elif (path1.__contains__('${') and path1.__contains__('}')):
                                        pathslist1.append(Fore.MAGENTA + path1)
                                        unparsed_num = unparsed_num + 1
                                    elif (os.path.isabs(path1) and os.path.exists(path1) is False):
                                        pathslist1.append(Fore.RED + path1)
                                        unexisted_num = unexisted_num + 1
                                    else:
                                        pathslist1.append(Fore.YELLOW + path1)
                                        unknownerror_num = unknownerror_num + 1
                                path2 = os.path.pathsep.join(pathslist1)
                                if (path2.__contains__(Fore.GREEN)):
                                    path2 = '%-100s %s %s' % (path2, Fore.RESET + 'normal_num:', normal_num)
                                if (path2.__contains__(Fore.MAGENTA)):
                                    path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unparsed_num:', unparsed_num)
                                if (path2.__contains__(Fore.RED)):
                                    path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unexisted_num:', unexisted_num)
                                if (path2.__contains__(Fore.YELLOW)):
                                    path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unknownstring_num:', unknownerror_num)
                                print('  ' + path2)
                            print('variable:')
                            for (key, value) in dict1.items():
                                if (key == 'path+'):
                                    continue
                                path0 = str(value)
                                pathslist = path0.split(os.path.pathsep)
                                while (pathslist.__contains__('')):
                                    pathslist.remove('')
                                # print(pathslist)
                                pathslist1 = []
                                for path1 in pathslist:
                                    if (os.path.isabs(path1) and os.path.exists(path1)):
                                        pathslist1.append(Fore.GREEN + path1)
                                        normal_num = normal_num + 1
                                    elif (path1.__contains__('${') and path1.__contains__('}')):
                                        pathslist1.append(Fore.MAGENTA + path1)
                                        unparsed_num = unparsed_num + 1
                                    elif (os.path.isabs(path1) and os.path.exists(path1) is False):
                                        pathslist1.append(Fore.RED + path1)
                                        unexisted_num = unexisted_num + 1
                                    else:
                                        pathslist1.append(Fore.YELLOW + path1)
                                        unknownerror_num = unknownerror_num + 1
                                path2 = os.path.pathsep.join(pathslist1)
                                if (path2.__contains__(Fore.GREEN)):
                                    path2 = '%-100s %s %s' % (path2, Fore.RESET + 'normal_num:', normal_num)
                                if (path2.__contains__(Fore.MAGENTA)):
                                    path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unparsed_num:', unparsed_num)
                                if (path2.__contains__(Fore.RED)):
                                    path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unexisted_num:', unexisted_num)
                                if (path2.__contains__(Fore.YELLOW)):
                                    path2 = '%-100s %s %s' % (path2, Fore.RESET + 'unknownstring_num:', unknownerror_num)
                                print('  %-30s %s' % (Fore.GREEN + key, path2))

                            break

            # calculate information
            print('------------------------------------------------------')
            print('calculate:')
            print('  %-20s: %d' % ('Total_num',normal_num+unparsed_num+unexisted_num+unknownerror_num))
            print(Fore.GREEN + '  %-20s: %d' % ('normal_num',normal_num))
            print(Fore.MAGENTA + '  %-20s: %d' % ('unparsed_num',unparsed_num))
            print(Fore.RED + '  %-20s: %d' % ('unexisted_num',unexisted_num))
            print(Fore.YELLOW + '  %-20s: %d' % ('unknownstring_num',unknownerror_num))
            return
        else:
            ''
        break

    def vc_createCmdList08(shellenvname = None, env_name = None, local = True, list0 = [], params0 = []):

        cmd_list = []

        if(env_name is None):
            env_name = rawconfig['environ']['current']
        #print(env_name)

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            cmd_call = "call "
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            cmd_list.append("call %s_effect.bat" % name)
            if (shellenvname is not None):
                cmd_list.append('call \"%s_effect%s\"' % (shellenvname, cmd_suffix))
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)
            if (shellenvname is not None):
                cmd_list.append('source \"%s_effect%s\"' % (shellenvname, cmd_suffix))

        #print(params0)
        params_string = ""
        for param in params0:
            #print(param)
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        if ( local is True):
            for cmd in list0:
                cmd_list.append(cmd)
        else:
            for cmd in list0:
                if(str(cmd).__contains__(' ')):
                    pycmd = which_command(env_name, str(cmd))
                    #print(str(cmd))
                    #print(Fore.RED + "which command:", pycmd)
                    if(pycmd is not None and os.path.isfile(pycmd)):
                        cmd_list.append('"' + cmd + '"' + ' ' + params_string)
                    else:
                        cmd_list.append(cmd + ' ' + params_string)
                else:
                    cmd_list.append(cmd + ' ' + params_string)

        # append exit 0
        cmd_list.append(cmd_exit)
        #print( cmd_list )

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        #print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("call " + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("./" + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)

        cmd_list.append(cmd_exit)

        # print (cmd_list)
        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        return cmd_list, name

    def vc_powershell_createCmdList08(shellenvname = None, env_name = None, local=True, list0=[], params0=[]):

        cmd_list = []

        if(env_name is None):
            env_name = rawconfig['environ']['current']

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        # print (name)

        #plat = getplatform()

        cmd_status = "echo pymake-command-status:$LASTEXITCODE"
        cmd_sep = ';'
        cmd_suffix = ".ps1"
        cmd_suffix_powershell = cmd_suffix
        cmd_exit = 'exit $LASTEXITCODE'
        cmd_codec = 'ansi'
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_header = "#!/usr/bin/env bash"
        cmd_call = "./"
        # cmd_list.append(cmd_header)
        cmd_list.append("./%s_effect%s" % (name, cmd_suffix))

        if(shellenvname is not None):
            cmd_list.append('. \"%s_effect%s\"' % (shellenvname, cmd_suffix))

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        # print(params_string)

        if (local is True):
            for cmd in list0:
                cmd_list.append(cmd)
        else:
            #actually now has only one command.
            for cmd in list0:
                # warning: now pymake is in user setted workroot.
                if(str(cmd).endswith(cmd_suffix_powershell)):
                    cmd_suffix_powershell = ''

                powershellexecfile = ""
                while(True):
                    # find in current path [+workroot]
                    powershellexecfile = os.getcwd() + os.path.sep + cmd + cmd_suffix_powershell
                    if(os.path.exists(powershellexecfile)):
                        break
                    powershellexecfile = pymakeworkpath + os.path.sep + cmd + cmd_suffix_powershell
                    if(os.path.exists(powershellexecfile)):
                        break

                    # find in .json environ
                    separateenvlistpath = os.path.pathsep.join(rawconfig['environ'][env_name]['path+'])
                    separateenvlistpath = separateenvlistpath.split(os.path.pathsep)
                    separateenvlistpath.reverse()
                    #for path0 in separateenvlistpath:
                    #    print(path0)
                    find_flag = 0
                    for path0 in separateenvlistpath:
                        powershellexecfile = path0 + os.path.sep + cmd + cmd_suffix_powershell
                        if (os.path.exists(powershellexecfile)):
                            find_flag = 1
                            break
                    if(find_flag == 1):
                        break

                    # find in basic environ [+custom]
                    env = os.environ
                    find_flag = 0
                    for path0 in env["PATH"].split(os.path.pathsep):
                        powershellexecfile = path0 + os.path.sep + cmd + cmd_suffix_powershell
                        if (os.path.exists(powershellexecfile)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # none? a powershell command, or powershell command-line.
                    powershellexecfile = cmd
                    break

                #print(powershellexecfile)
                #wow
                #cmd_list.append(powershellexecfile + ' ' + params_string)
                if (str(powershellexecfile).__contains__(' ')):
                    if(os.path.isfile(powershellexecfile)):
                        powershellexecfile = powershellexecfile.replace('/', os.path.sep)
                        powershellexecfile = powershellexecfile.replace('\\', os.path.sep)
                        cmd_list.append(". \"%s\" @args" % powershellexecfile)
                    else:
                        cmd_list.append("%s" % powershellexecfile)
                else:
                    if(os.path.isfile(powershellexecfile)):
                        powershellexecfile = powershellexecfile.replace('/', os.path.sep)
                        powershellexecfile = powershellexecfile.replace('\\', os.path.sep)
                        cmd_list.append(". %s @args" % powershellexecfile)
                    else:
                        cmd_list.append("%s" % powershellexecfile)

        # append exit 0
        cmd_list.append(cmd_exit)
        # print( cmd_list )

        cmd_execute = "" + name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        # print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        # if (plat == "Windows"):
        #    ""
        # else:
        #    os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        cmd_list.append(cmd_call + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)
        cmd_list.append(cmd_exit)

        # print (cmd_list)
        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        return cmd_list, name

    def vc_python_createCmdList08(shellenvname = None, env_name = None, local = True, list0 = [], params0 = []):
        cmd_list = []

        if(env_name is None):
            env_name = rawconfig['environ']['current']

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            cmd_call = "call "
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            cmd_list.append("call %s_effect.bat" % name)
            if (shellenvname is not None):
                cmd_list.append('call \"%s_effect%s\"' % (shellenvname, cmd_suffix))
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)
            if (shellenvname is not None):
                cmd_list.append('source \"%s_effect%s\"' % (shellenvname, cmd_suffix))

        cmd_suffix_python = '.py'
        cmd_codec_python = "utf8"
        cmd_return_python = "\n"

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        pythonexecfile = ''
        if ( local is True):
            #fixed
            pythonexecfile = name + '_exec' + cmd_suffix_python
            with open(pythonexecfile, 'w', encoding=cmd_codec_python) as f:
                for cmd in list0:
                    f.write(cmd + cmd_return_python)
            #print(1, pythonexecfile)
        else:
            #actually now has only one command.
            for cmd in list0:
                # warning: now pymake is in user setted workroot.
                if(str(cmd).endswith(cmd_suffix_python)):
                    cmd_suffix_python = ''

                pythonexecfile = ""
                while(True):
                    # find in current path [+workroot]
                    pythonexecfile = os.getcwd() + os.path.sep + cmd + cmd_suffix_python
                    #print(2, pythonexecfile)
                    if(os.path.exists(pythonexecfile)):
                        break
                    pythonexecfile = pymakeworkpath + os.path.sep + cmd + cmd_suffix_python
                    #print(2, pythonexecfile)
                    if(os.path.exists(pythonexecfile)):
                        break

                    # find in .json environ
                    separateenvlistpath = os.path.pathsep.join(rawconfig['environ'][env_name]['path+'])
                    separateenvlistpath = separateenvlistpath.split(os.path.pathsep)
                    separateenvlistpath.reverse()
                    #for path0 in separateenvlistpath:
                    #    print(path0)
                    find_flag = 0
                    for path0 in separateenvlistpath:
                        pythonexecfile = path0 + os.path.sep + cmd + cmd_suffix_python
                        #print(2, pythonexecfile)
                        if (os.path.exists(pythonexecfile)):
                            find_flag = 1
                            break
                    if(find_flag == 1):
                        break

                    # find in basic environ [custom+]
                    env = os.environ
                    find_flag = 0
                    for path0 in env["PATH"].split(os.path.pathsep):
                        pythonexecfile = path0 + os.path.sep + cmd + cmd_suffix_python
                        #print(2, pythonexecfile)
                        if (os.path.exists(pythonexecfile)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # none? a python command, or python command-line.
                    pythonexecfile = cmd
                    break

                #print(2, pythonexecfile)
                #cmd_list.append(pythonexecfile + ' ' + params_string)

        #print params.
        #print(3, pythonexecfile)

        #get python command.
        pycmd = ''
        if(plat == "Windows"):
            pycmd = 'python.exe'
        else:
            pycmd = 'python3'

        pycmd = which_command(env_name, pycmd)

        #print(pycmd)
        if(plat == "Windows"):
            if(pycmd is None):
                pycmd = 'py'
            elif(pycmd != 'py'):
                pycmd = 'python'
        else:
            pycmd = 'python3'

        if(os.path.isfile(pythonexecfile)):
            if(plat == "Windows"):
                cmd_list.append("call %s \"%s\" %s" % (pycmd, pythonexecfile, '%*'))
            else:
                cmd_list.append("%s \"%s\" %s" % (pycmd, pythonexecfile, '"$@"'))
        else:
            if(plat == "Windows"):
                cmd_list.append("call %s -c \"%s\" %s" % (pycmd, pythonexecfile, '%*'))
            else:
                cmd_list.append("%s -c \"%s\" %s" % (pycmd, pythonexecfile, '"$@"'))

        # append exit 0
        cmd_list.append(cmd_exit)

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        #print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("call " + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("./" + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)

        cmd_list.append(cmd_exit)

        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        return cmd_list, name

    def vc_language_createCmdList08(shellenvname = None, suffix = None, encoding = None, env_name = None, local = True, list0 = [], params0 = []):
        cmd_list = []

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            cmd_call = "call "
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            cmd_list.append("call %s_effect.bat" % name)
            if (shellenvname is not None):
                cmd_list.append('call \"%s_effect%s\"' % (shellenvname, cmd_suffix))
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)
            if (shellenvname is not None):
                cmd_list.append('source \"%s_effect%s\"' % (shellenvname, cmd_suffix))

        if(env_name is None):
            env_name = rawconfig['environ']['current']
        if(env_name == "current"):
            env_name = rawconfig['environ']['current']

        cmd_suffix_language = cmd_suffix
        cmd_codec_language = cmd_codec
        cmd_return_language = cmd_return

        if(suffix is not None):
            cmd_suffix_language = suffix
        if(encoding is not None):
            cmd_codec_language = encoding

        list1 = []
        # for current_var in str(args['<command-param>']).split():
        #    list1.append(current_var)
        if (params0.__len__() > 0):
            current_var = params0[0]
            list1.append(current_var)
            params0.pop(0)
        #print(list1)

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        local2 = True
        if (list1.__len__() > 0):
            current_var = list1[0]
            if (current_var in rawconfig['command']):
                local2 = True
            else:
                local2 = False

        languageparams = ''
        #actually only one param.
        if (local2 is True):
            for param1 in list1:
                languageparams += param1
        else:
            for param1 in list1:
                # warning: now pymake is in user setted workroot.

                languageparams = ""
                while (True):
                    # find in current path [+--workroot]
                    languageparams = os.getcwd() + os.path.sep + param1
                    # print(2, languageparams)
                    if (os.path.exists(languageparams)):
                        break
                    languageparams = pymakeworkpath + os.path.sep + param1
                    # print(2, languageparams)
                    if (os.path.exists(languageparams)):
                        break

                    # find in .json environ
                    separateenvlistpath = os.path.pathsep.join(rawconfig['environ'][env_name]['path+'])
                    separateenvlistpath = separateenvlistpath.split(os.path.pathsep)
                    separateenvlistpath.reverse()
                    #for path0 in separateenvlistpath:
                    #    print(path0)
                    find_flag = 0
                    for path0 in separateenvlistpath:
                        languageparams = path0 + os.path.sep + param1
                        #print(2, languageparams)
                        if (os.path.exists(languageparams)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # find in basic environ [custom+]
                    env = os.environ
                    find_flag = 0
                    for path0 in env["PATH"].split(os.path.pathsep):
                        languageparams = path0 + os.path.sep + param1
                        # print(2, languageparams)
                        if (os.path.exists(languageparams)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # none? a language command, or language command-line.
                    languageparams = param1
                    break

                    # print(2, languageparams)
                    # cmd_list.append(languageparams + ' ' + params_string)

        if(list1.__len__() >0):
            ''
            if(local2 is True):
                ''
                current_var = env_name
                local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                inside_name = name + '_2'
                languageparams = inside_name + '_exec' + cmd_suffix_language

                with open(languageparams, 'w', encoding=cmd_codec_language) as f:
                    for cmd1 in list1:
                        for cmd in dict0[cmd1]:
                            f.write(cmd + cmd_return_language)

                #print(1, cmd_suffix_language)
                #print(1, cmd_return_language)
                #print(1, cmd_codec_language)
                #print(1, languageparams)
            else:
                ''

        #print(3, languageparams)
        if(list1.__len__() >0 ):
            if(local2 is True):
                params_string = languageparams + ' ' + params_string
            else:
                if(str(languageparams).__contains__(' ')):
                    params_string = '"' + languageparams + '"' + ' ' + params_string
                else:
                    params_string = languageparams + ' ' + params_string
        #print(params_string)

        languageexecfile = ''
        if ( local is True):
            #fixed
            #inside_name = name
            #inside_name = hex( int( inside_name, 16 ) + 1).split('x')[1]
            inside_name = name + '_1'
            #print(inside_name)
            languageexecfile = inside_name + '_exec' + cmd_suffix
            with open(languageexecfile, 'w', encoding=cmd_codec) as f:
                for cmd in list0:
                    f.write(cmd + cmd_return)
            #print(1, languageexecfile)
        else:
            languageexecfile = ''
            #actually now has only one command.
            for cmd in list0:
                #actually this is a command.
                if (str(cmd).__contains__(' ')):
                    pycmd = which_command(env_name, str(cmd))
                    #print(cmd)
                    #print(pycmd)
                    if(pycmd is not None and os.path.isfile(pycmd)):
                        languageexecfile = '"' + cmd + '"'
                    else:
                        languageexecfile = cmd
                else:
                    languageexecfile = cmd

        #print(3, languageexecfile)
        if(plat == "Windows"):
            cmd_list.append("call %s %s" % (languageexecfile, '%*'))
        else:
            if(languageexecfile.endswith('.sh')):
                cmd_list.append("sh %s %s" % (languageexecfile, '"$@"'))
            else:
                cmd_list.append("%s %s" % (languageexecfile, '"$@"'))

        # append exit 0
        cmd_list.append(cmd_exit)

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("call " + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + ' '+ params_string + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("./" + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)

        cmd_list.append(cmd_exit)

        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        return cmd_list, name, cmd_suffix, cmd_suffix_language

    #vc json export function
    def vc_json_export(dict0 = None, env_name = None, file_name = None):
        if(dict0 is None):
            return "", "", ""

        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name

        cmd_suffix = ".json"
        cmd_codec = 'utf8'
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_header = "#!/usr/bin/env bash" + cmd_return
        env_set = ''

        # export effect env
        cmd_effect = 'vcenv'
        if (file_name is not None):
            cmd_effect = file_name
        cmd_effect += cmd_suffix

        if(os.path.exists(cmd_effect) is False):
            tempdict = {
                'environ': {

                }
            }
            writeJsonData(cmd_effect, tempdict)

        vcdict = readJsonData(cmd_effect)
        if(vcdict.__contains__('environ') is False):
            vcdict['environ'] = {}
        vcdict['environ'][current_var] = dict0
        writeJsonData(cmd_effect, vcdict)

        return cmd_effect

    #vc powershell export function
    def vc_powershell_export(dict0 = None, env_name = None, file_name = None):
        if(dict0 is None):
            return "", "", ""

        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name

        cmd_suffix = ".ps1"
        cmd_codec = 'ansi'
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_header = "#!/usr/bin/env bash" + cmd_return
        env_set = ''

        # export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = "" + file_name
        cmd_effect += '_effect' + cmd_suffix

        # export path
        lines = ""
        for (key) in dict0["path+"]:
            lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

        # export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)

        # print(lines.split('\n'))
        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header)
            f.write(lines)

        # export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = "" + file_name
        cmd_unset += '_unset' + cmd_suffix

        # export unset path
        lines = ""
        for (key) in dict0["path+"]:
            # lines += ("$env:Path = $env:Path.Replace(\"%s;\", \"\")" % key) + cmd_return
            lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return
        # export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            lines += ("${env:%s} = \"\"" % key) + cmd_return

        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header)
            f.write(lines)

        return cmd_effect, cmd_unset

    def vc_powershell_export2(dict0 = None, env_name = None, file_name = None):
        if(dict0 is None):
            return "", "", ""

        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name

        cmd_suffix = ".ps1"
        cmd_codec = 'ansi'
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_header = "#!/usr/bin/env bash" + cmd_return
        env_set = ''

        # export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = "" + file_name
        cmd_effect += '_effect' + cmd_suffix

        lines = ""
        # +system
        if (args['-s'] or args['--system'] is True):
            # export path
            # print(envcustomlistrawpaths)
            for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

            # export var
            for (key, value) in pymakesystemenviron.items():
                if (key == 'path+'):
                    continue
                if (str(key).lower() == "path"):
                    continue
                lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)
        else:
            ''

        # +local
        if (args['-l'] or args['--local'] is True):
            # export path
            for (key) in localenv['path+']:
                lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

            # export var
            for (key, value) in localenv.items():
                if (key == 'path+'):
                    continue
                lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)
        else:
            ''

        # +custom
        if (args['-c'] or args['--custom'] is True):
            # export path
            # print(envcustomlistrawpaths)
            for (key) in envcustomlistrawpaths:
                lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

            # export var
            for (key, value) in envcustomlistrawvars.items():
                if (key == 'path+'):
                    continue
                lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)
        else:
            ''

        # export path
        for (key) in dict0["path+"]:
            lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

        # export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)

        # print(lines.split('\n'))
        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header)
            f.write(lines)

        # export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = "" + file_name
        cmd_unset += '_unset' + cmd_suffix

        lines = ""
        # +system
        if (args['-s'] or args['--system'] is True):
            # export unset path
            for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return

            # export unset var
            for (key, value) in pymakesystemenviron.items():
                if (key == 'path+'):
                    continue
                if (str(key).lower() == "path"):
                    continue
                lines += ("${env:%s} = \"\"" % key) + cmd_return
        else:
            ''

        # +local
        if (args['-l'] or args['--local'] is True):
            # export unset path
            for (key) in localenv['path+']:
                lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return

            # export unset var
            for (key, value) in localenv.items():
                if (key == 'path+'):
                    continue
                lines += ("${env:%s} = \"\"" % key) + cmd_return
        else:
            ''

        # +custom
        if (args['-c'] or args['--custom'] is True):
            # export unset path
            for (key) in envcustomlistrawpaths:
                lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return

            # export unset var
            for (key, value) in envcustomlistrawvars.items():
                if (key == 'path+'):
                    continue
                lines += ("${env:%s} = \"\"" % key) + cmd_return
        else:
            ''

        # export unset path
        for (key) in dict0["path+"]:
            # lines += ("$env:Path = $env:Path.Replace(\"%s;\", \"\")" % key) + cmd_return
            lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return

        # export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            lines += ("${env:%s} = \"\"" % key) + cmd_return

        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header)
            f.write(lines)

        return cmd_effect, cmd_unset

    # vc export function
    # dict0: VC effect env
    # env_name: separate env
    # file_name: script name
    def vc_export (dict0 = None, env_name = None, file_name = None):
        if(dict0 is None):
            return "", "", ""

        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name

        plat = getplatform()
        if (plat == "Windows"):
            cmd_suffix = ".bat"
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_return = "\n"
            cmd_header = "@echo off" + cmd_return
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash" + cmd_return
            env_set = 'export '

        #export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = file_name
        cmd_effect += '_effect' + cmd_suffix

        #export path
        lines = ""
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
            else:
                lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + cmd_return)
            else:
                lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        #export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = file_name
        cmd_unset += '_unset' + cmd_suffix

        #export unset path
        lines = ""
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

        #export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + cmd_return)
            else:
                lines += ('unset ' + key + cmd_return)

        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_effect)
            os.system("chmod +x " + cmd_unset)

        #return file name
        return cmd_effect, cmd_unset

    def vc_export2 (dict0 = None, env_name = None, file_name = None):
        if(dict0 is None):
            return "", "", ""

        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name

        plat = getplatform()
        if (plat == "Windows"):
            cmd_suffix = ".bat"
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_return = "\n"
            cmd_header = "@echo off" + cmd_return
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash" + cmd_return
            env_set = 'export '

        #export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = file_name
        cmd_effect += '_effect' + cmd_suffix

        lines = ""

        # +system
        if (args['-s'] or args['--system'] is True):
            # export path
            # print(envcustomlistrawpaths)
            for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
                else:
                    lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

            # export var
            for (key, value) in pymakesystemenviron.items():
                if (key == 'path+'):
                    continue
                if (str(key).lower() == "path"):
                    continue
                if (plat == "Windows"):
                    lines += (env_set + key + '=' + value + cmd_return)
                else:
                    lines += (env_set + key + '=\"' + value + '\"' + cmd_return)
        else:
            ''

        # +local
        if (args['-l'] or args['--local'] is True):
            # export path
            for (key) in localenv['path+']:
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
                else:
                    lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

            # export var
            for (key, value) in localenv.items():
                if (key == 'path+'):
                    continue
                if (plat == "Windows"):
                    lines += (env_set + key + '=' + value + cmd_return)
                else:
                    lines += (env_set + key + '=\"' + value + '\"' + cmd_return)
        else:
            ''

        # +custom
        if (args['-c'] or args['--custom'] is True):
            # export path
            # print(envcustomlistrawpaths)
            for (key) in envcustomlistrawpaths:
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
                else:
                    lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

            # export var
            for (key, value) in envcustomlistrawvars.items():
                if (key == 'path+'):
                    continue
                if (plat == "Windows"):
                    lines += (env_set + key + '=' + value + cmd_return)
                else:
                    lines += (env_set + key + '=\"' + value + '\"' + cmd_return)
        else:
            ''

        #export path
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
            else:
                lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + cmd_return)
            else:
                lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        #export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = file_name
        cmd_unset += '_unset' + cmd_suffix

        lines = ""

        # +system
        if (args['-s'] or args['--system'] is True):
            # export unset path
            for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
                else:
                    lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

            # export unset var
            for (key, value) in pymakesystemenviron.items():
                if (key == 'path+'):
                    continue
                if (str(key).lower() == "path"):
                    continue
                if (plat == "Windows"):
                    lines += ('set ' + key + '=' + cmd_return)
                else:
                    lines += ('unset ' + key + cmd_return)
        else:
            ''

        # +local
        if (args['-l'] or args['--local'] is True):
            # export unset path
            for (key) in localenv['path+']:
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
                else:
                    lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

            # export unset var
            for (key, value) in localenv.items():
                if (key == 'path+'):
                    continue
                if (plat == "Windows"):
                    lines += ('set ' + key + '=' + cmd_return)
                else:
                    lines += ('unset ' + key + cmd_return)
        else:
            ''

        # +custom
        if (args['-c'] or args['--custom'] is True):
            # export unset path
            for (key) in envcustomlistrawpaths:
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
                else:
                    lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

            # export unset var
            for (key, value) in envcustomlistrawvars.items():
                if (key == 'path+'):
                    continue
                if (plat == "Windows"):
                    lines += ('set ' + key + '=' + cmd_return)
                else:
                    lines += ('unset ' + key + cmd_return)
        else:
            ''

        #export unset path
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

        #export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + cmd_return)
            else:
                lines += ('unset ' + key + cmd_return)

        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_effect)
            os.system("chmod +x " + cmd_unset)

        #return file name
        return cmd_effect, cmd_unset

    # vc settings function
    def vc_settings(env_name = None):
        current_env = env_name
        if(env_name is None):
            current_env = rawconfig['environ']['current']

        print("source file: %s" % sourceconfigfile)
        vcvarslist = [
            'vcvarsall-1998',
            'vcvarsall-2003',
            'vcvarsall-2005',
            'vcvarsall-2008',
            'vcvarsall-2010',
            'vcvarsall-2012',
            'vcvarsall-2013',
            'vcvarsall-2015',
            'vcvarsall-2017',
            'vcvarsall-2019',
            'vcvarsall-20XX'
        ]
        print('path-assemblage:')
        for key in vcvarslist:
            if (rawconfig['path-assemblage'].__contains__(key) is False):
                rawconfig['path-assemblage'][key] = "<CAN SET>"
            print('  "%s": "%s"' % (key, rawconfig['path-assemblage'][key]))

        current_vcvarsall = 'vcvarsall'
        current_vcvarsallparam = 'vcvarsallparam'
        print('system env:')
        if (pymakesystemenviron.__contains__(current_vcvarsall) is False):
            pymakesystemenviron[current_vcvarsall] = "<CAN SET>"
        print('  "%s"     : "%s"' % (current_vcvarsall, pymakesystemenviron[current_vcvarsall]))
        if (pymakesystemenviron.__contains__(current_vcvarsallparam) is False):
            pymakesystemenviron[current_vcvarsallparam] = "<CAN SET>"
        print('  "%s": "%s"' % (current_vcvarsallparam, pymakesystemenviron[current_vcvarsallparam]))

        print('custom env:')
        if (envcustomlistrawvars.__contains__(current_vcvarsall) is False):
            envcustomlistrawvars[current_vcvarsall] = "<CAN SET>"
        print('  "%s"     : "%s"' % (current_vcvarsall, envcustomlistrawvars[current_vcvarsall]))
        if (envcustomlistrawvars.__contains__(current_vcvarsallparam) is False):
            envcustomlistrawvars[current_vcvarsallparam] = "<CAN SET>"
        print('  "%s": "%s"' % (current_vcvarsallparam, envcustomlistrawvars[current_vcvarsallparam]))

        print('env %s:' % current_env)
        if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is False):
            rawconfig['environ'][current_env][current_vcvarsall] = "<CAN SET>"
        print('  "%s"     : "%s"' % (current_vcvarsall, rawconfig['environ'][current_env][current_vcvarsall]))
        if (rawconfig['environ'][current_env].__contains__(current_vcvarsallparam) is False):
            rawconfig['environ'][current_env][current_vcvarsallparam] = "<CAN SET>"
        print('  "%s": "%s"' % (current_vcvarsallparam, rawconfig['environ'][current_env][current_vcvarsallparam]))
        return

    # vc command
    while (True):
        if(args['vc'] is True):
            ''
            if(args['init'] is True):
                current_env = ""

                if (args['<env-name>'] is not None):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = rawconfig['environ']['current']

                if (args['-a'] or args['--all'] is True):
                    break

                current_vcvarsall = 'vcvarsall'
                current_vcvarsallparam = 'vcvarsallparam'
                has_set = '0'
                native_dict = {}
                while(True):
                    if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                        native_dict = pymakesystemenviron
                        has_set = "system env:"
                    if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                        native_dict = envcustomlistrawvars
                        has_set = "custom env:"
                    if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                        native_dict = rawconfig['environ'][current_env]
                        has_set = str("env %s:" % current_env)
                    break

                #print(has_set)
                #if(has_set != '0'):
                #    print(native_dict[current_vcvarsall])

                if(has_set == '0'):
                    print('please set env variable vcvarsall in %s, env %s.' % (sourcefile, current_env))
                    return

                if(native_dict.__contains__(current_vcvarsallparam) is False):
                    print('please set env variable vcvarsallparam in %s, env %s.' % (sourcefile, current_env))
                    return

                print("source file: %s" % sourceconfigfile)

                print(has_set)
                print('  "vcvarsall": "%s"' % native_dict[current_vcvarsall])
                print('  "vcvarsallparam": "%s"' % native_dict[current_vcvarsallparam])

                plat = getplatform()
                if (plat != "Windows"):
                    print('pymake vc command cant support non-windows system.')
                    return

                if(os.path.isfile(native_dict[current_vcvarsall]) is False):
                    print('failed: %s is not existed.' % native_dict[current_vcvarsall])
                    return

                if (debugswitch == '1'):
                    print("debug:" )
                    cmd_string = str('call "%s" %s' % (native_dict[current_vcvarsall], native_dict[current_vcvarsallparam]))
                    print("  ", cmd_string)
                    result = subprocess.getoutput(cmd_string)
                    print("  ", result)

                cmd_string = str('call "%s" %s 1>nul 2>nul & set' % (native_dict[current_vcvarsall], native_dict[current_vcvarsallparam]))
                result = subprocess.getoutput(cmd_string)
                #print(result)
                #print(cmd_string)
                list1 = result.split('\n')
                #print(list1)
                dict1 = {}
                for l in list1:
                    key = str(l).split('=')[0].strip()
                    value = '='.join(str(l).split('=')[1:]).strip()
                    dict1[key.upper()]=value
                #print(dict1)
                #for (key, value) in dict1.items():
                #    print("%-30s %s" % (key, value))

                dict2 = {k.upper(): v for k, v in os.environ.items()}
                #print(dict2)
                #for (key, value) in dict2.items():
                #    print("%-30s %s" % (key, value))

                diff0 = DiffDict(dict1, dict2)
                if (debugswitch == '1'):
                    print("debug: VC ALL")
                    print('VC ADDED:')
                    #print(diff0.get_added())
                    for (k, v) in diff0.get_added().items():
                        print('  %-30s %s' % (k,v))
                    print('VC REMOVED:')
                    for (k, v) in diff0.get_removed().items():
                        print('  %-30s %s' % (k,v))
                    print('VC CHANGED:')
                    k1, k2 = diff0.get_changed()
                    for (k,v) in k1.items():
                        print('  %-30s %s' % (k,v))

                dict11, dict21 = diff0.get_changed()
                #print(dict11)
                #print(dict21)
                if(dict11.__contains__('PATH') is False):
                    print('failed: %s execute failed.' % native_dict[current_vcvarsall])
                    return

                diff1 = DiffList(dict11['PATH'].split(os.path.pathsep), dict21['PATH'].split(os.path.pathsep))
                #print(dict11['PATH'])
                #print(dict21['PATH'])
                #print('AAAAA', diff1.get_added())
                #print('BBBBB', diff1.get_removed())
                #print('CCCCC', diff1.get_changed())
                if (debugswitch == '1'):
                    print("debug: VC PATH")
                    print('VC ADDED:')
                    for k in diff1.get_added():
                        print('  %s' % k)
                    print('VC REMOVED:')
                    for k in diff1.get_removed():
                        print('  %s' % k)
                    print('VC CHANGED:')
                    k1, k2 = diff1.get_changed()
                    for k in k1:
                        print('  %s' % k)
                    #print('VC MIXED:')
                    #k1, k2 = diff1.get_mixed()
                    #for k in k1:
                    #    print('%s' % k)

                dict3 = {}
                pathlist0, pathlist1 = diff1.get_changed()
                dict3['path+'] = copy.deepcopy(pathlist0)
                dict3['path+'].reverse()
                vardict = copy.deepcopy(diff0.get_added())
                dict3.update(vardict)
                #for (key, value) in vardict.items():
                #    if (key == 'PATH'):
                #        continue
                #    if (key == 'path+'):
                #        continue
                #    dict3[key]=value
                #print(dict3)

                os.chdir(vcroot)

                if(dict3.__contains__('VISUALSTUDIOVERSION') is False):
                    print('failed: env var VISUALSTUDIOVERSION is not defined in %s.' % native_dict[current_vcvarsall])
                    print('  1. your shell env is not pure.')
                    print('  2. your vcvarsall.bat is not legal.')
                    return

                #export json
                jsonfile = 'pymake-vc-command'
                f0 = vc_json_export(dict3, current_env, jsonfile)

                #export
                vcname = 'vc' + dict3['VISUALSTUDIOVERSION'] + '_' + native_dict[current_vcvarsallparam]
                filename = 'pymake_' + vcname
                f11, f12 = vc_export(dict3, current_env, filename)

                #export powershell
                f21, f22 = vc_powershell_export(dict3, current_env, filename)

                print("inited at: %s" % vcroot)
                print('  %s' % f0)
                print('  %s, %s' % (f11, f12))
                print('  %s, %s' % (f21, f22))
                print("successed")
                return
            elif (args['deinit'] is True):
                current_env = ""

                if (args['<env-name>'] is not None):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = rawconfig['environ']['current']

                current_vcvarsall = 'vcvarsall'
                current_vcvarsallparam = 'vcvarsallparam'
                has_set = '0'
                native_dict = {}
                while(True):
                    if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                        native_dict = pymakesystemenviron
                        has_set = "system env:"
                    if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                        native_dict = envcustomlistrawvars
                        has_set = "custom env:"
                    if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                        native_dict = rawconfig['environ'][current_env]
                        has_set = str("env %s:" % current_env)
                    break

                #print(has_set)
                #if(has_set != '0'):
                #    print(native_dict[current_vcvarsall])

                if(has_set == '0'):
                    print('please set env variable vcvarsall in %s, env %s.' % (sourcefile, current_env))
                    return

                if(native_dict.__contains__(current_vcvarsallparam) is False):
                    print('please set env variable vcvarsallparam in %s, env %s.' % (sourcefile, current_env))
                    return

                print("source file: %s" % sourceconfigfile)

                print(has_set)
                print('  "vcvarsall": "%s"' % native_dict[current_vcvarsall])
                print('  "vcvarsallparam": "%s"' % native_dict[current_vcvarsallparam])

                plat = getplatform()
                if (plat != "Windows"):
                    print('pymake vc command cant support non-windows system.')
                    return

                if(os.path.isfile(native_dict[current_vcvarsall]) is False):
                    print('failed: %s is not existed.' % native_dict[current_vcvarsall])
                    return

                os.chdir(vcroot)
                jsonfile = 'pymake-vc-command.json'
                if(not os.path.exists(jsonfile)):
                    print('please init vc.')
                    return
                dict0 = readJsonData(jsonfile)
                if(dict0.__contains__('environ') is False):
                    print('please init vc.')
                    return
                if(dict0['environ'].__contains__(current_env) is False):
                    print('please init vc for %s env.' % current_env)
                    return

                dict0['environ'].__delitem__(current_env)
                writeJsonData(jsonfile, dict0)
                print('successed: vc deinit %s' % current_env)
                return
            elif (args['env'] is True):
                ''
                current_env = ""

                if (args['<env-name>'] is not None):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = rawconfig['environ']['current']

                current_vcvarsall = 'vcvarsall'
                current_vcvarsallparam = 'vcvarsallparam'
                has_set = '0'
                native_dict = {}
                while(True):
                    if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                        native_dict = pymakesystemenviron
                        has_set = "system env:"
                    if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                        native_dict = envcustomlistrawvars
                        has_set = "custom env:"
                    if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                        native_dict = rawconfig['environ'][current_env]
                        has_set = str("env %s:" % current_env)
                    break

                #print(has_set)
                #if(has_set != '0'):
                #    print(native_dict[current_vcvarsall])

                if(has_set == '0'):
                    print("please set env variable: vcvarsall.")
                    return

                if(native_dict.__contains__(current_vcvarsallparam) is False):
                    print("please set env variable: vcvarsallparam.")
                    return

                print("source file: %s" % sourceconfigfile)

                print(has_set)
                print('  "%s": "%s"' % (current_vcvarsall, native_dict[current_vcvarsall]))
                print('  "%s": "%s"' % (current_vcvarsallparam, native_dict[current_vcvarsallparam]))

                print (Fore.CYAN+ "env %s" % current_env)
                print(Fore.LIGHTGREEN_EX + "path+:")
                for (key) in rawconfig['environ'][current_env]["path+"]:
                    print(Fore.LIGHTMAGENTA_EX + "  %s" % key)
                print(Fore.LIGHTGREEN_EX + "variable:")
                for (key, value) in rawconfig['environ'][current_env].items():
                    if (key == 'path+'):
                        continue
                    print(Fore.GREEN + "  %-30s %s" % (key, value))

                os.chdir(vcroot)
                jsonfile = 'pymake-vc-command.json'
                if(not os.path.exists(jsonfile)):
                    print('please init vc.')
                    return
                dict0 = readJsonData(jsonfile)
                if(dict0.__contains__('environ') is False):
                    print('please init vc.')
                    return
                if(dict0['environ'].__contains__(current_env) is False):
                    print('please init vc for %s env.' % current_env)
                    return

                print (Fore.CYAN+ "vcenv %s" % current_env)
                print(Fore.LIGHTGREEN_EX + "path+:")
                for (key) in dict0['environ'][current_env]["path+"]:
                    print(Fore.LIGHTMAGENTA_EX + "  %s" % key)
                print(Fore.LIGHTGREEN_EX + "variable:")
                for (key, value) in dict0['environ'][current_env].items():
                    if (key == 'path+'):
                        continue
                    print(Fore.GREEN + "  %-30s %s" % (key, value))

                return
            elif (args['settings'] is True):
                ''
                current_env = ""

                if (args['<env-name>'] is not None):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = rawconfig['environ']['current']

                vc_settings(current_env)
                return
            elif (args['stat'] or args['status'] is True):
                ''
                print("source root: %s" % sourceroot)
                current_vcvarsall = 'vcvarsall'
                current_vcvarsallparam = 'vcvarsallparam'
                has_set = '0'
                set_content = '<CAN SET>'
                while(True):
                    has_set = "system env:"
                    print(has_set)
                    set_content = '<CAN SET>'
                    if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                        set_content = pymakesystemenviron[current_vcvarsall]
                    print('  "%s"     : "%s"' % (current_vcvarsall, set_content))
                    set_content = '<CAN SET>'
                    if (pymakesystemenviron.__contains__(current_vcvarsallparam) is True):
                        set_content = pymakesystemenviron[current_vcvarsallparam]
                    print('  "%s": "%s"' % (current_vcvarsallparam, set_content))

                    has_set = "custom env:"
                    print(has_set)
                    set_content = '<CAN SET>'
                    if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                        set_content = envcustomlistrawvars[current_vcvarsall]
                    print('  "%s"     : "%s"' % (current_vcvarsall, set_content))
                    set_content = '<CAN SET>'
                    if (envcustomlistrawvars.__contains__(current_vcvarsallparam) is True):
                        set_content = envcustomlistrawvars[current_vcvarsallparam]
                    print('  "%s": "%s"' % (current_vcvarsallparam, set_content))
                    break

                os.chdir(vcroot)
                jsonfile = 'pymake-vc-command.json'
                if(not os.path.exists(jsonfile)):
                    print('please init vc.')
                    return
                dict0 = readJsonData(jsonfile)
                if(dict0.__contains__('environ') is False):
                    print('please init vc.')
                    return

                print("source file: %s" % sourceconfigfile)
                print('%-30s %-30s %-30s %s' % ('[env]', '[status]', '[vcvarsall]', '[vcvarsallparam]'))
                set_content = '<CAN INIT>'
                set_content2 = '<CAN SET>'
                for (k, v) in rawconfig['environ'].items():
                    current_env = k
                    status = set_content
                    vcvarsall = set_content2
                    vcvarsallparam = set_content2
                    if(dict0['environ'].__contains__(current_env) is True):
                        if(dict0['environ'][current_env].__contains__('VISUALSTUDIOVERSION') is True):
                            status = 'VC' + dict0['environ'][current_env]['VISUALSTUDIOVERSION']
                    if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                        vcvarsall = rawconfig['environ'][current_env][current_vcvarsall]
                    if (rawconfig['environ'][current_env].__contains__(current_vcvarsallparam) is True):
                        vcvarsallparam = rawconfig['environ'][current_env][current_vcvarsallparam]
                    if(current_env == 'current'):
                        continue
                    if(current_env == rawconfig['environ']['current']):
                        print(Fore.LIGHTMAGENTA_EX +'%-30s %-30s %-30s %s' % (current_env, status, vcvarsall, vcvarsallparam))
                        continue
                    print('%-30s %-30s %-30s %s' % (current_env, status, vcvarsall, vcvarsallparam))

                return
            elif(args['clean'] is True):
                break
            elif (args['type'] is True):
                break
            elif (args['export'] is True):
                current_env = args['<env-name>']
                if (args['<env-name>'] is None):
                    current_env = rawconfig['environ']['current']
                    print(Fore.CYAN + "%s" % current_env)
                    for key in rawconfig['environ'].keys():
                        if (key == 'current'):
                            continue
                        if (key == current_env):
                            continue
                        print("%s" % key)
                    return

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print("please ensure the environ is right")
                    return

                if (args['<env-name>'] == "current"):
                    current_env = rawconfig['environ']['current']

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                    return

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                current_vcvarsall = 'vcvarsall'
                current_vcvarsallparam = 'vcvarsallparam'
                has_set = '0'
                native_dict = {}
                while(True):
                    if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                        native_dict = pymakesystemenviron
                        has_set = "system env:"
                    if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                        native_dict = envcustomlistrawvars
                        has_set = "custom env:"
                    if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                        native_dict = rawconfig['environ'][current_env]
                        has_set = str("env %s:" % current_env)
                    break

                #print(has_set)
                #if(has_set != '0'):
                #    print(native_dict[current_vcvarsall])

                if(has_set == '0'):
                    print("please set env variable: vcvarsall.")
                    return

                if(native_dict.__contains__(current_vcvarsallparam) is False):
                    print("please set env variable: vcvarsallparam.")
                    return

                print("source file: %s" % sourceconfigfile)

                print(has_set)
                print('  "vcvarsall": "%s"' % native_dict[current_vcvarsall])
                print('  "vcvarsallparam": "%s"' % native_dict[current_vcvarsallparam])

                nowroot = os.getcwd()
                dict1 = copy.deepcopy(rawconfig['environ'][current_env])
                #for (k,v) in dict1.items():
                #    print(k, v)
                os.chdir(vcroot)
                jsonfile = 'pymake-vc-command.json'
                if(not os.path.exists(jsonfile)):
                    print('please init vc.')
                    return
                dict0 = readJsonData(jsonfile)
                if(dict0.__contains__('environ') is False):
                    print('please init vc.')
                    return
                if(dict0['environ'].__contains__(current_env) is False):
                    print('please init vc for %s env.' % current_env)
                    return
                for (key) in dict0['environ'][current_env]["path+"]:
                    dict1['path+'].append(key)
                for (key, value) in dict0['environ'][current_env].items():
                    if (key == 'path+'):
                        continue
                    dict1[key]=value
                os.chdir(nowroot)

                cmd_effect, cmd_unset = vc_export(dict1, current_env, args['<file-name>'])

                print("successed: vc export %s to %s %s" % (current_env, cmd_effect, cmd_unset))
                return
            elif (args['export2'] is True):
                current_env = args['<env-name>']
                if (args['<env-name>'] is None):
                    current_env = rawconfig['environ']['current']
                    print(Fore.CYAN + "%s" % current_env)
                    for key in rawconfig['environ'].keys():
                        if (key == 'current'):
                            continue
                        if (key == current_env):
                            continue
                        print("%s" % key)
                    return

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print("please ensure the environ is right")
                    return 1

                if (args['<env-name>'] == "current"):
                    current_env = rawconfig['environ']['current']

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                    return 1

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)


                current_vcvarsall = 'vcvarsall'
                current_vcvarsallparam = 'vcvarsallparam'
                has_set = '0'
                native_dict = {}
                while(True):
                    if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                        native_dict = pymakesystemenviron
                        has_set = "system env:"
                    if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                        native_dict = envcustomlistrawvars
                        has_set = "custom env:"
                    if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                        native_dict = rawconfig['environ'][current_env]
                        has_set = str("env %s:" % current_env)
                    break

                #print(has_set)
                #if(has_set != '0'):
                #    print(native_dict[current_vcvarsall])

                if(has_set == '0'):
                    print("please set env variable: vcvarsall.")
                    return 1

                if(native_dict.__contains__(current_vcvarsallparam) is False):
                    print("please set env variable: vcvarsallparam.")
                    return 1

                print("source file: %s" % sourceconfigfile)

                print(has_set)
                print('  "vcvarsall": "%s"' % native_dict[current_vcvarsall])
                print('  "vcvarsallparam": "%s"' % native_dict[current_vcvarsallparam])

                nowroot = os.getcwd()
                dict1 = copy.deepcopy(rawconfig['environ'][current_env])
                #for (k,v) in dict1.items():
                #    print(k, v)
                os.chdir(vcroot)
                jsonfile = 'pymake-vc-command.json'
                if(not os.path.exists(jsonfile)):
                    print('please init vc.')
                    return 1
                dict0 = readJsonData(jsonfile)
                if(dict0.__contains__('environ') is False):
                    print('please init vc.')
                    return 1
                if(dict0['environ'].__contains__(current_env) is False):
                    print('please init vc for %s env.' % current_env)
                    return 1
                for (key) in dict0['environ'][current_env]["path+"]:
                    dict1['path+'].append(key)
                for (key, value) in dict0['environ'][current_env].items():
                    if (key == 'path+'):
                        continue
                    dict1[key]=value
                os.chdir(nowroot)

                if (args['powershell'] is True):
                    cmd_effect, cmd_unset = vc_powershell_export2(dict1, current_env, args['<file-name>'])
                else:
                    cmd_effect, cmd_unset = vc_export2(dict1, current_env, args['<file-name>'])

                # +system
                if (args['-s'] or args['--system'] is True):
                    print("successed: vc export %s env to %s %s" % ('system', cmd_effect, cmd_unset))
                else:
                    ''
                # +local
                if (args['-l'] or args['--local'] is True):
                    print("successed: vc export %s env to %s %s" % ('local', cmd_effect, cmd_unset))
                else:
                    ''
                # +custom
                if (args['-c'] or args['--custom'] is True):
                    print("successed: vc export %s env to %s %s" % ('custom', cmd_effect, cmd_unset))
                else:
                    ''
                print("successed: vc export %s env to %s %s" % (current_var, cmd_effect, cmd_unset))
                print("successed: vc export %s %s env to %s %s" % ('VC'+dict1['VISUALSTUDIOVERSION'], native_dict[current_vcvarsallparam], cmd_effect, cmd_unset))
                return
            elif (args['powershell'] is True):
                if (args['ccvp'] or args['execvp'] or args['exec-with-params'] is True):
                    current_env = ""
                    if (args['use'] is True):
                        if (args['<env-name>'] is None):
                            print("please appoint a environ")
                            return

                        if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                            print("please ensure the environ is right")
                            return

                        current_env = args['<env-name>']
                        if (args['<env-name>'] == "current"):
                            current_env = rawconfig['environ']['current']

                        if (current_env == 'current'
                            or rawconfig['environ'].__contains__(current_env) is False):
                            print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                            return
                    else:
                        current_env = rawconfig['environ']['current']

                    if (args['<command-name>'] is None):
                        print("please appoint your command")
                        return

                    # print(args['hh'])
                    # print(args['here'])
                    if (args['here'] or args['hh'] is True):
                        os.chdir(pymakeworkpath)
                    elif (args['there'] or args['tt'] is True):
                        os.chdir(customshellroot)
                    elif (args['default'] or args['dd'] is True):
                        os.chdir(pymakeshellroot)

                    # print(args['--workroot'])
                    if (args['--workroot'] is not None):
                        if (os.path.isdir(args['--workroot'])
                            and os.path.isabs(args['--workroot'])):
                            os.chdir(args['--workroot'])
                        else:
                            print('please input an existed and legal work root.')
                            return

                    current_vcvarsall = 'vcvarsall'
                    current_vcvarsallparam = 'vcvarsallparam'
                    has_set = '0'
                    native_dict = {}
                    while (True):
                        if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                            native_dict = pymakesystemenviron
                            has_set = "system env:"
                        if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                            native_dict = envcustomlistrawvars
                            has_set = "custom env:"
                        if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                            native_dict = rawconfig['environ'][current_env]
                            has_set = str("env %s:" % current_env)
                        break

                    # print(has_set)
                    # if(has_set != '0'):
                    #    print(native_dict[current_vcvarsall])

                    if (has_set == '0'):
                        print("please set env variable: vcvarsall.")
                        return

                    if (native_dict.__contains__(current_vcvarsallparam) is False):
                        print("please set env variable: vcvarsallparam.")
                        return

                    #print("source file: %s" % sourceconfigfile)

                    #print(has_set)
                    #print('  "vcvarsall": "%s"' % native_dict[current_vcvarsall])
                    #print('  "vcvarsallparam": "%s"' % native_dict[current_vcvarsallparam])

                    nowroot = os.getcwd()

                    # dict1
                    dict1 = copy.deepcopy(rawconfig['environ'][current_env])
                    os.chdir(vcroot)
                    jsonfile = 'pymake-vc-command.json'
                    if (not os.path.exists(jsonfile)):
                        print('please init vc.')
                        return
                    dict0 = readJsonData(jsonfile)
                    if (dict0.__contains__('environ') is False):
                        print('please init vc.')
                        return
                    if (dict0['environ'].__contains__(current_env) is False):
                        print('please init vc for %s env.' % current_env)
                        return
                    for (key) in dict0['environ'][current_env]["path+"]:
                        dict1['path+'].append(key)
                    for (key, value) in dict0['environ'][current_env].items():
                        if (key == 'path+'):
                            continue
                        dict1[key] = value
                    if (dict1.__contains__('VISUALSTUDIOVERSION') is False):
                        print('failed: env var VISUALSTUDIOVERSION is not defined in %s.' % native_dict[current_vcvarsall])
                        return
                    vcname = 'vc' + dict1['VISUALSTUDIOVERSION'] + '_' + native_dict[current_vcvarsallparam]
                    filename = 'pymake_' + vcname
                    shellenvname = vcroot + os.path.sep + filename
                    #print(shellenvname)
                    os.chdir(nowroot)

                    # create cmd_list
                    current_var = current_env
                    local_command = raw_command(current_var)
                    dict0 = copy.deepcopy(local_command)

                    list0 = []
                    local = True
                    current_var = args['<command-name>']
                    if (current_var in dict0):
                        list0.extend(dict0[current_var])
                        local = True
                    else:
                        list0.append(current_var)
                        local = False

                    params0 = []
                    # print(args['--params'])
                    # print(args['<command-params>'])
                    for current_var in args['--params']:
                        params0.append(current_var)
                    for current_var in args['<command-params>']:
                        params0.append(current_var)

                    # print(list0)
                    # print(params0)

                    cmd_list = []
                    temp_file_name = ""
                    # if (getplatform() == "Windows"):
                    #    cmd_list, temp_file_name = createCmdList0(list0)
                    # else:
                    #    cmd_list, temp_file_name = createCmdList01(list0)
                    # good compatibility
                    cmd_list, temp_file_name = vc_powershell_createCmdList08(shellenvname, current_env, local, list0, params0)

                    # export env
                    current_var = current_env
                    # print (current_var, temp_file_name)
                    vc_powershell_export(dict1, current_var, temp_file_name)

                    ret = communicateWithCommandLine3(cmd_list)

                    #return
                    # delete env file and cmd file
                    temp_file = "" + temp_file_name + "_exec.ps1"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = "" + temp_file_name + "_effect.ps1"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = "" + temp_file_name + "_unset.ps1"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)

                    os._exit(ret)
                    return
                else:
                    ''
                    return
                return
            elif (args['python'] is True):
                if (args['ccvp'] or args['execvp'] or args['exec-with-params'] is True):
                    current_env = ""
                    if (args['use'] is True):
                        if (args['<env-name>'] is None):
                            print("please appoint a environ")
                            return

                        if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                            print("please ensure the environ is right")
                            return

                        current_env = args['<env-name>']
                        if (args['<env-name>'] == "current"):
                            current_env = rawconfig['environ']['current']

                        if (current_env == 'current'
                            or rawconfig['environ'].__contains__(current_env) is False):
                            print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                            return
                    else:
                        current_env = rawconfig['environ']['current']

                    if (args['<command-name>'] is None):
                        print("please appoint your command")
                        return

                    if (args['here'] or args['hh'] is True):
                        os.chdir(pymakeworkpath)
                    elif (args['there'] or args['tt'] is True):
                        os.chdir(customshellroot)
                    elif (args['default'] or args['dd'] is True):
                        os.chdir(pymakeshellroot)

                    # print(args['--workroot'])
                    if (args['--workroot'] is not None):
                        if (os.path.isdir(args['--workroot'])
                            and os.path.isabs(args['--workroot'])):
                            os.chdir(args['--workroot'])
                        else:
                            print('please input an existed and legal work root.')
                            return

                    current_vcvarsall = 'vcvarsall'
                    current_vcvarsallparam = 'vcvarsallparam'
                    has_set = '0'
                    native_dict = {}
                    while (True):
                        if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                            native_dict = pymakesystemenviron
                            has_set = "system env:"
                        if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                            native_dict = envcustomlistrawvars
                            has_set = "custom env:"
                        if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                            native_dict = rawconfig['environ'][current_env]
                            has_set = str("env %s:" % current_env)
                        break

                    # print(has_set)
                    # if(has_set != '0'):
                    #    print(native_dict[current_vcvarsall])

                    if (has_set == '0'):
                        print("please set env variable: vcvarsall.")
                        return

                    if (native_dict.__contains__(current_vcvarsallparam) is False):
                        print("please set env variable: vcvarsallparam.")
                        return

                    #print("source file: %s" % sourceconfigfile)

                    #print(has_set)
                    #print('  "vcvarsall": "%s"' % native_dict[current_vcvarsall])
                    #print('  "vcvarsallparam": "%s"' % native_dict[current_vcvarsallparam])

                    nowroot = os.getcwd()

                    # dict1
                    dict1 = copy.deepcopy(rawconfig['environ'][current_env])
                    os.chdir(vcroot)
                    jsonfile = 'pymake-vc-command.json'
                    if (not os.path.exists(jsonfile)):
                        print('please init vc.')
                        return
                    dict0 = readJsonData(jsonfile)
                    if (dict0.__contains__('environ') is False):
                        print('please init vc.')
                        return
                    if (dict0['environ'].__contains__(current_env) is False):
                        print('please init vc for %s env.' % current_env)
                        return
                    for (key) in dict0['environ'][current_env]["path+"]:
                        dict1['path+'].append(key)
                    for (key, value) in dict0['environ'][current_env].items():
                        if (key == 'path+'):
                            continue
                        dict1[key] = value
                    if (dict1.__contains__('VISUALSTUDIOVERSION') is False):
                        print('failed: env var VISUALSTUDIOVERSION is not defined in %s.' % native_dict[current_vcvarsall])
                        return
                    vcname = 'vc' + dict1['VISUALSTUDIOVERSION'] + '_' + native_dict[current_vcvarsallparam]
                    filename = 'pymake_' + vcname
                    shellenvname = vcroot + os.path.sep + filename
                    #print(shellenvname)
                    os.chdir(nowroot)

                    # create cmd_list
                    current_var = current_env
                    local_command = raw_command(current_var)
                    dict0 = copy.deepcopy(local_command)

                    list0 = []
                    local = True
                    current_var = args['<command-name>']
                    if (current_var in dict0):
                        list0.extend(dict0[current_var])
                        local = True
                    else:
                        list0.append(current_var)
                        local = False

                    params0 = []
                    # print(args['--params'])
                    # print(args['<command-params>'])
                    for current_var in args['--params']:
                        params0.append(current_var)
                    for current_var in args['<command-params>']:
                        params0.append(current_var)

                    cmd_list = []
                    temp_file_name = ""
                    # if (getplatform() == "Windows"):
                    #    cmd_list, temp_file_name = createCmdList0(list0)
                    # else:
                    #    cmd_list, temp_file_name = createCmdList01(list0)
                    # good compatibility
                    cmd_list, temp_file_name = vc_python_createCmdList08(shellenvname, current_env, local, list0, params0)

                    # export env
                    current_var = current_env
                    # print (current_var, temp_file_name)
                    vc_export(dict1, current_var, temp_file_name)

                    ret = communicateWithCommandLine(cmd_list)

                    # delete env file and cmd file
                    cmd_prefix = ''
                    temp_file = cmd_prefix + temp_file_name + "_exec.py"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)

                    if (getplatform() == "Windows"):
                        temp_file = cmd_prefix + temp_file_name + "_exec.bat"
                        if (os.path.exists(temp_file)):
                            os.remove(temp_file)
                        temp_file = cmd_prefix + temp_file_name + "_effect.bat"
                        if (os.path.exists(temp_file)):
                            os.remove(temp_file)
                        temp_file = cmd_prefix + temp_file_name + "_unset.bat"
                        if (os.path.exists(temp_file)):
                            os.remove(temp_file)
                    else:
                        temp_file = cmd_prefix + temp_file_name + "_exec.sh"
                        if (os.path.exists(temp_file)):
                            os.remove(temp_file)
                        temp_file = cmd_prefix + temp_file_name + "_effect.sh"
                        if (os.path.exists(temp_file)):
                            os.remove(temp_file)
                        temp_file = cmd_prefix + temp_file_name + "_unset.sh"
                        if (os.path.exists(temp_file)):
                            os.remove(temp_file)

                    os._exit(ret)
                    return
                else:
                    ''
                    return
                return
            elif (args['language'] is True):
                if (args['ccvp'] or args['execvp'] or args['exec-with-params'] is True):
                    current_env = ""
                    if (args['use'] is True):
                        if (args['<env-name>'] is None):
                            print("please appoint a environ")
                            return

                        if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                            print("please ensure the environ is right")
                            return

                        current_env = args['<env-name>']
                        if (args['<env-name>'] == "current"):
                            current_env = rawconfig['environ']['current']

                        if (current_env == 'current'
                            or rawconfig['environ'].__contains__(current_env) is False):
                            print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                            return
                    else:
                        current_env = rawconfig['environ']['current']

                    if (args['<command-name>'] is None):
                        print("please appoint your command")
                        return

                    if (args['here'] or args['hh'] is True):
                        os.chdir(pymakeworkpath)
                    elif (args['there'] or args['tt'] is True):
                        os.chdir(customshellroot)
                    elif (args['default'] or args['dd'] is True):
                        os.chdir(pymakeshellroot)

                    # print(args['--workroot'])
                    if (args['--workroot'] is not None):
                        if (os.path.isdir(args['--workroot'])
                            and os.path.isabs(args['--workroot'])):
                            os.chdir(args['--workroot'])
                        else:
                            print('please input an existed and legal work root.')
                            return

                    current_vcvarsall = 'vcvarsall'
                    current_vcvarsallparam = 'vcvarsallparam'
                    has_set = '0'
                    native_dict = {}
                    while (True):
                        if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                            native_dict = pymakesystemenviron
                            has_set = "system env:"
                        if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                            native_dict = envcustomlistrawvars
                            has_set = "custom env:"
                        if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                            native_dict = rawconfig['environ'][current_env]
                            has_set = str("env %s:" % current_env)
                        break

                    # print(has_set)
                    # if(has_set != '0'):
                    #    print(native_dict[current_vcvarsall])

                    if (has_set == '0'):
                        print("please set env variable: vcvarsall.")
                        return

                    if (native_dict.__contains__(current_vcvarsallparam) is False):
                        print("please set env variable: vcvarsallparam.")
                        return

                    #print("source file: %s" % sourceconfigfile)

                    #print(has_set)
                    #print('  "vcvarsall": "%s"' % native_dict[current_vcvarsall])
                    #print('  "vcvarsallparam": "%s"' % native_dict[current_vcvarsallparam])

                    nowroot = os.getcwd()

                    # dict1
                    dict1 = copy.deepcopy(rawconfig['environ'][current_env])
                    os.chdir(vcroot)
                    jsonfile = 'pymake-vc-command.json'
                    if (not os.path.exists(jsonfile)):
                        print('please init vc.')
                        return
                    dict0 = readJsonData(jsonfile)
                    if (dict0.__contains__('environ') is False):
                        print('please init vc.')
                        return
                    if (dict0['environ'].__contains__(current_env) is False):
                        print('please init vc for %s env.' % current_env)
                        return
                    for (key) in dict0['environ'][current_env]["path+"]:
                        dict1['path+'].append(key)
                    for (key, value) in dict0['environ'][current_env].items():
                        if (key == 'path+'):
                            continue
                        dict1[key] = value
                    if (dict1.__contains__('VISUALSTUDIOVERSION') is False):
                        print('failed: env var VISUALSTUDIOVERSION is not defined in %s.' % native_dict[current_vcvarsall])
                        return
                    vcname = 'vc' + dict1['VISUALSTUDIOVERSION'] + '_' + native_dict[current_vcvarsallparam]
                    filename = 'pymake_' + vcname
                    shellenvname = vcroot + os.path.sep + filename
                    #print(shellenvname)
                    os.chdir(nowroot)

                    # create cmd_list
                    current_var = current_env
                    local_command = raw_command(current_var)
                    dict0 = copy.deepcopy(local_command)

                    list0 = []
                    local = True
                    current_var = args['<command-name>']
                    if (current_var in dict0):
                        list0.extend(dict0[current_var])
                        local = True
                    else:
                        list0.append(current_var)
                        local = False

                    params0 = []
                    # print(args['--params'])
                    # print(args['<command-params>'])
                    for current_var in args['--params']:
                        params0.append(current_var)
                    for current_var in args['<command-params>']:
                        params0.append(current_var)

                    suffix = args['--suffix']
                    encoding = args['--encoding']

                    # print(list0)
                    # print(params0)
                    # print(suffix)
                    # print(encoding)

                    cmd_list = []
                    temp_file_name = ""
                    # if (getplatform() == "Windows"):
                    #    cmd_list, temp_file_name = createCmdList0(list0)
                    # else:
                    #    cmd_list, temp_file_name = createCmdList01(list0)
                    # good compatibility
                    cmd_list, temp_file_name, cmd_suffix, cmd_suffix_language = vc_language_createCmdList08(shellenvname, suffix, encoding, current_env, local, list0, params0)

                    # export env
                    current_var = current_env
                    # print (current_var, temp_file_name)
                    vc_export(dict1, current_var, temp_file_name)

                    ret = communicateWithCommandLine(cmd_list)

                    # delete env file and cmd file
                    cmd_prefix = ''
                    temp_file = cmd_prefix + temp_file_name + "_1_exec" + cmd_suffix
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = cmd_prefix + temp_file_name + "_2_exec" + cmd_suffix_language
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)

                    if (getplatform() == "Windows"):
                        temp_file = cmd_prefix + temp_file_name + "_exec.bat"
                        if (os.path.exists(temp_file)):
                            os.remove(temp_file)
                        temp_file = cmd_prefix + temp_file_name + "_effect.bat"
                        if (os.path.exists(temp_file)):
                            os.remove(temp_file)
                        temp_file = cmd_prefix + temp_file_name + "_unset.bat"
                        if (os.path.exists(temp_file)):
                            os.remove(temp_file)
                    else:
                        temp_file = cmd_prefix + temp_file_name + "_exec.sh"
                        if (os.path.exists(temp_file)):
                            os.remove(temp_file)
                        temp_file = cmd_prefix + temp_file_name + "_effect.sh"
                        if (os.path.exists(temp_file)):
                            os.remove(temp_file)
                        temp_file = cmd_prefix + temp_file_name + "_unset.sh"
                        if (os.path.exists(temp_file)):
                            os.remove(temp_file)

                    os._exit(ret)
                    return
                else:
                    ''
                    return
                return
            elif (args['ccvp'] or args['execvp'] or args['exec-with-params'] is True):
                current_env = ""
                if (args['use'] is True):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (current_env == 'current'
                        or rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = rawconfig['environ']['current']

                if (args['<command-name>'] is None):
                    print("please appoint your command")
                    return

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                # print(args['--workroot'])
                if (args['--workroot'] is not None):
                    if (os.path.isdir(args['--workroot'])
                        and os.path.isabs(args['--workroot'])):
                        os.chdir(args['--workroot'])
                    else:
                        print('please input a legal work root.')
                        return

                current_vcvarsall = 'vcvarsall'
                current_vcvarsallparam = 'vcvarsallparam'
                has_set = '0'
                native_dict = {}
                while (True):
                    if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                        native_dict = pymakesystemenviron
                        has_set = "system env:"
                    if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                        native_dict = envcustomlistrawvars
                        has_set = "custom env:"
                    if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                        native_dict = rawconfig['environ'][current_env]
                        has_set = str("env %s:" % current_env)
                    break

                # print(has_set)
                # if(has_set != '0'):
                #    print(native_dict[current_vcvarsall])

                if (has_set == '0'):
                    print("please set env variable: vcvarsall.")
                    return

                if (native_dict.__contains__(current_vcvarsallparam) is False):
                    print("please set env variable: vcvarsallparam.")
                    return

                #print("source file: %s" % sourceconfigfile)

                #print(has_set)
                #print('  "vcvarsall": "%s"' % native_dict[current_vcvarsall])
                #print('  "vcvarsallparam": "%s"' % native_dict[current_vcvarsallparam])

                nowroot = os.getcwd()

                # dict1
                dict1 = copy.deepcopy(rawconfig['environ'][current_env])
                os.chdir(vcroot)
                jsonfile = 'pymake-vc-command.json'
                if (not os.path.exists(jsonfile)):
                    print('please init vc.')
                    return
                dict0 = readJsonData(jsonfile)
                if (dict0.__contains__('environ') is False):
                    print('please init vc.')
                    return
                if (dict0['environ'].__contains__(current_env) is False):
                    print('please init vc for %s env.' % current_env)
                    return
                for (key) in dict0['environ'][current_env]["path+"]:
                    dict1['path+'].append(key)
                for (key, value) in dict0['environ'][current_env].items():
                    if (key == 'path+'):
                        continue
                    dict1[key] = value
                if (dict1.__contains__('VISUALSTUDIOVERSION') is False):
                    print('failed: env var VISUALSTUDIOVERSION is not defined in %s.' % native_dict[current_vcvarsall])
                    return
                vcname = 'vc' + dict1['VISUALSTUDIOVERSION'] + '_' + native_dict[current_vcvarsallparam]
                filename = 'pymake_' + vcname
                shellenvname = vcroot + os.path.sep + filename
                #print(shellenvname)
                os.chdir(nowroot)

                # create cmd_list
                current_var = current_env
                local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                list0 = []
                local = True
                current_var = args['<command-name>']
                if (current_var in dict0):
                    list0.extend(dict0[current_var])
                    local = True
                else:
                    list0.append(current_var)
                    local = False

                params0 = []
                # print(args['--params'])
                # print(args['<command-params>'])
                for current_var in args['--params']:
                    params0.append(current_var)
                for current_var in args['<command-params>']:
                    params0.append(current_var)

                cmd_list = []
                temp_file_name = ""
                # if (getplatform() == "Windows"):
                #    cmd_list, temp_file_name = createCmdList0(list0)
                # else:
                #    cmd_list, temp_file_name = createCmdList01(list0)
                # good compatibility
                cmd_list, temp_file_name = vc_createCmdList08(shellenvname, current_env, local, list0, params0)

                # export env
                current_var = current_env
                # print (current_var, temp_file_name)
                vc_export(dict1, current_var, temp_file_name)

                ret = communicateWithCommandLine(cmd_list)

                # delete env file and cmd file
                if (getplatform() == "Windows"):
                    temp_file = temp_file_name + "_exec.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                else:
                    temp_file = temp_file_name + "_exec.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)

                os._exit(ret)
                return
            else:
                vc_settings(None)
                return
        else:
            ''
        break

    # vc init command
    while (True):
        if(args['vc'] is True):
            if(args['init'] is True):
                if(args['-a'] or args['--all'] is True):
                    current_env = ""

                    if (args['<env-name>'] is not None):
                        if (args['<env-name>'] is None):
                            print("please appoint a environ")
                            return

                        if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                            print("please ensure the environ is right")
                            return

                        current_env = args['<env-name>']
                        if (args['<env-name>'] == "current"):
                            current_env = rawconfig['environ']['current']

                        if (rawconfig['environ'].__contains__(current_env) is False):
                            print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                            return
                    else:
                        current_env = rawconfig['environ']['current']

                    print("source file: %s" % sourceconfigfile)
                    print("init   root: %s" % (vcroot))

                    for (current_env, env_value) in rawconfig['environ'].items():
                        if(current_env == 'current'):
                            continue

                        print('-------------------------------------------------')

                        current_vcvarsall = 'vcvarsall'
                        current_vcvarsallparam = 'vcvarsallparam'
                        has_set = '0'
                        native_dict = {}
                        while (True):
                            if (pymakesystemenviron.__contains__(current_vcvarsall) is True):
                                native_dict = pymakesystemenviron
                                has_set = "system env:"
                            if (envcustomlistrawvars.__contains__(current_vcvarsall) is True):
                                native_dict = envcustomlistrawvars
                                has_set = "custom env:"
                            if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is True):
                                native_dict = rawconfig['environ'][current_env]
                                has_set = str("env %s:" % current_env)
                            break

                        # print(has_set)
                        # if(has_set != '0'):
                        #    print(native_dict[current_vcvarsall])

                        if (has_set == '0'):
                            print('please set env variable vcvarsall in %s, env %s.' % (sourcefile, current_env))
                            continue

                        if (native_dict.__contains__(current_vcvarsallparam) is False):
                            print('please set env variable vcvarsallparam in %s, env %s.' % (sourcefile, current_env))
                            continue

                        print(has_set)
                        print('  "vcvarsall": "%s"' % native_dict[current_vcvarsall])
                        print('  "vcvarsallparam": "%s"' % native_dict[current_vcvarsallparam])

                        plat = getplatform()
                        if (plat != "Windows"):
                            print('pymake vc command cant support non-windows system.')
                            continue

                        if (os.path.isfile(native_dict[current_vcvarsall]) is False):
                            print('failed: %s is not existed.' % native_dict[current_vcvarsall])
                            continue

                        if (debugswitch == '1'):
                            print("debug:")
                            cmd_string = str('call "%s" %s' % (native_dict[current_vcvarsall], native_dict[current_vcvarsallparam]))
                            print("  ", cmd_string)
                            result = subprocess.getoutput(cmd_string)
                            print("  ", result)

                        cmd_string = str('call "%s" %s 1>nul 2>nul & set' % (native_dict[current_vcvarsall], native_dict[current_vcvarsallparam]))
                        result = subprocess.getoutput(cmd_string)
                        # print(result)
                        # print(cmd_string)
                        list1 = result.split('\n')
                        # print(list1)
                        dict1 = {}
                        for l in list1:
                            key = str(l).split('=')[0].strip()
                            value = '='.join(str(l).split('=')[1:]).strip()
                            dict1[key.upper()] = value
                        # print(dict1)
                        # for (key, value) in dict1.items():
                        #    print("%-30s %s" % (key, value))

                        dict2 = {k.upper(): v for k, v in os.environ.items()}
                        # print(dict2)
                        # for (key, value) in dict2.items():
                        #    print("%-30s %s" % (key, value))

                        diff0 = DiffDict(dict1, dict2)
                        if (debugswitch == '1'):
                            print("debug: VC ALL")
                            print('VC ADDED:')
                            for (k, v) in diff0.get_added().items():
                                print('  %-30s %s' % (k, v))
                            print('VC REMOVED:')
                            for (k, v) in diff0.get_removed().items():
                                print('  %-30s %s' % (k, v))
                            print('VC CHANGED:')
                            k1, k2 = diff0.get_changed()
                            for (k, v) in k1.items():
                                print('  %-30s %s' % (k, v))

                        dict11, dict21 = diff0.get_changed()
                        # print(dict11)
                        # print(dict21)
                        if (dict11.__contains__('PATH') is False):
                            print('failed: %s execute failed.' % native_dict[current_vcvarsall])
                            continue

                        diff1 = DiffList(dict11['PATH'].split(os.path.pathsep), dict21['PATH'].split(os.path.pathsep))
                        # print(dict11['PATH'])
                        # print(dict21['PATH'])
                        # print('AAAAA', diff1.get_added())
                        # print('BBBBB', diff1.get_removed())
                        # print('CCCCC', diff1.get_changed())
                        if (debugswitch == '1'):
                            print("debug: VC PATH")
                            print('VC ADDED:')
                            for k in diff1.get_added():
                                print('  %s' % k)
                            print('VC REMOVED:')
                            for k in diff1.get_removed():
                                print('  %s' % k)
                            print('VC CHANGED:')
                            k1, k2 = diff1.get_changed()
                            for k in k1:
                                print('  %s' % k)
                            # print('VC MIXED:')
                            # k1, k2 = diff1.get_mixed()
                            # for k in k1:
                            #    print('%s' % k)

                        dict3 = {}
                        pathlist0, pathlist1 = diff1.get_changed()
                        dict3['path+'] = copy.deepcopy(pathlist0)
                        dict3['path+'].reverse()
                        vardict = copy.deepcopy(diff0.get_added())
                        dict3.update(vardict)
                        # for (key, value) in vardict.items():
                        #    if (key == 'PATH'):
                        #        continue
                        #    if (key == 'path+'):
                        #        continue
                        #    dict3[key]=value
                        # print(dict3)

                        os.chdir(vcroot)

                        if (dict3.__contains__('VISUALSTUDIOVERSION') is False):
                            print('failed: env var VISUALSTUDIOVERSION is not defined in %s.' % native_dict[current_vcvarsall])
                            print('  1. your shell env is not pure.')
                            print('  2. your vcvarsall.bat is not legal.')
                            continue

                        # export json
                        jsonfile = 'pymake-vc-command'
                        f0 = vc_json_export(dict3, current_env, jsonfile)

                        # export
                        vcname = 'vc' + dict3['VISUALSTUDIOVERSION'] + '_' + native_dict[current_vcvarsallparam]
                        filename = 'pymake_' + vcname
                        f11, f12 = vc_export(dict3, current_env, filename)

                        # export powershell
                        f21, f22 = vc_powershell_export(dict3, current_env, filename)

                        print("inited at: %s%s%s" % (vcroot, os.path.sep, f0))
                        print('  %s, %s' % (f11, f12))
                        print('  %s, %s' % (f21, f22))

                    print('-------------------------------------------------')
                    print("successed")
                    return
                else:
                    ''
            else:
                ''
        else:
            ''
        break

    # export2 command
    while (True):
        if( args['export2'] is True ) :
            current_env = args['<env-name>']
            if(args['<env-name>'] is None):
                current_env = rawconfig['environ']['current']
                print(Fore.CYAN + "%s" % current_env)
                for key in rawconfig['environ'].keys() :
                    if(key == 'current'):
                        continue
                    if(key == current_env):
                        continue
                    print("%s" % key)
                return

            if(rawconfig['environ'].__contains__(current_env) is False):
                print("please ensure the environ is right")
                return 1

            if(args['<env-name>'] == "current"):
                current_env = rawconfig['environ']['current']

            if (rawconfig['environ'].__contains__(current_env) is False):
                print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                return 1

            if (args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)
            elif (args['there'] or args['tt'] is True):
                os.chdir(customshellroot)
            elif (args['default'] or args['dd'] is True):
                os.chdir(pymakeshellroot)

            current_var = ""
            cmd_effect = ""
            cmd_unset = ""
            #current_var, cmd_effect, cmd_unset = env_export(current_env, args['<file-name>'])
            env_name = current_env
            file_name = args['<file-name>']

            # select env
            current_var = rawconfig['environ']['current']
            if (env_name is not None):
                current_var = env_name
            dict0 = copy.deepcopy(rawconfig['environ'][current_var])

            if(args['powershell'] is True):
                cmd_suffix = ".ps1"
                cmd_codec = 'ansi'
                if (getplatform_release() == "XP"):
                    cmd_codec = None
                # but windows, it is \r\n, python helpping me?
                cmd_return = "\n"
                cmd_header = "#!/usr/bin/env bash" + cmd_return
                env_set = ''

                # export effect env
                cmd_effect = 'env'
                if (file_name is not None):
                    cmd_effect = "" + file_name
                cmd_effect += '_effect' + cmd_suffix

                lines = ""

                # +system
                if (args['-s'] or args['--system'] is True):
                    # export path
                    # print(envcustomlistrawpaths)
                    for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                        lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

                    # export var
                    for (key, value) in pymakesystemenviron.items():
                        if (key == 'path+'):
                            continue
                        if (str(key).lower() == "path"):
                            continue
                        lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)
                else:
                    ''

                # +local
                if (args['-l'] or args['--local'] is True):
                    # export path
                    for (key) in localenv['path+']:
                        lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

                    # export var
                    for (key, value) in localenv.items():
                        if (key == 'path+'):
                            continue
                        lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)
                else:
                    ''

                # +custom
                if (args['-c'] or args['--custom'] is True):
                    # export path
                    # print(envcustomlistrawpaths)
                    for (key) in envcustomlistrawpaths:
                        lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

                    # export var
                    for (key, value) in envcustomlistrawvars.items():
                        if (key == 'path+'):
                            continue
                        lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)
                else:
                    ''

                # export path
                for (key) in dict0["path+"]:
                    lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

                # export var
                for (key, value) in dict0.items():
                    if (key == 'path+'):
                        continue
                    lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)

                # print(lines.split('\n'))
                with open(cmd_effect, 'w', encoding=cmd_codec) as f:
                    # f.write(cmd_header)
                    f.write(lines)

                # export unset env
                cmd_unset = 'env'
                if (file_name is not None):
                    cmd_unset = "" + file_name
                cmd_unset += '_unset' + cmd_suffix

                lines = ""

                # +system
                if (args['-s'] or args['--system'] is True):
                    # export unset path
                    for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                        lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return

                    # export unset var
                    for (key, value) in pymakesystemenviron.items():
                        if (key == 'path+'):
                            continue
                        if (str(key).lower() == "path"):
                            continue
                        lines += ("${env:%s} = \"\"" % key) + cmd_return
                else:
                    ''

                # +local
                if (args['-l'] or args['--local'] is True):
                    # export unset path
                    for (key) in localenv['path+']:
                        lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return

                    # export unset var
                    for (key, value) in localenv.items():
                        if (key == 'path+'):
                            continue
                        lines += ("${env:%s} = \"\"" % key) + cmd_return
                else:
                    ''

                # +custom
                if (args['-c'] or args['--custom'] is True):
                    # export unset path
                    for (key) in envcustomlistrawpaths:
                        lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return

                    # export unset var
                    for (key, value) in envcustomlistrawvars.items():
                        if (key == 'path+'):
                            continue
                        lines += ("${env:%s} = \"\"" % key) + cmd_return
                else:
                    ''

                # export unset path
                for (key) in dict0["path+"]:
                    # lines += ("$env:Path = $env:Path.Replace(\"%s;\", \"\")" % key) + cmd_return
                    lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return

                # export unset var
                for (key, value) in dict0.items():
                    if (key == 'path+'):
                        continue
                    lines += ("${env:%s} = \"\"" % key) + cmd_return

                with open(cmd_unset, 'w', encoding=cmd_codec) as f:
                    # f.write(cmd_header)
                    f.write(lines)

                # +system
                if (args['-s'] or args['--system'] is True):
                    print("successed: export %s env to %s %s" % ('system', cmd_effect, cmd_unset))
                else:
                    ''
                # +local
                if (args['-l'] or args['--local'] is True):
                    print("successed: export %s env to %s %s" % ('local', cmd_effect, cmd_unset))
                else:
                    ''
                # +custom
                if (args['-c'] or args['--custom'] is True):
                    print("successed: export %s env to %s %s" % ('custom', cmd_effect, cmd_unset))
                else:
                    ''
                print("successed: export %s env to %s %s" % (current_var, cmd_effect, cmd_unset))

                return

            plat = getplatform()
            if (plat == "Windows"):
                cmd_suffix = ".bat"
                cmd_codec = "ansi"
                if (getplatform_release() == "XP"):
                    cmd_codec = None
                cmd_return = "\n"
                cmd_header = "@echo off" + cmd_return
                env_set = 'set '
            else:
                cmd_suffix = ".sh"
                cmd_codec = "utf8"
                cmd_return = "\n"
                cmd_header = "#!/usr/bin/env bash" + cmd_return
                env_set = 'export '

            # export effect env
            cmd_effect = 'env'
            if (file_name is not None):
                cmd_effect = file_name
            cmd_effect += '_effect' + cmd_suffix

            lines = ""

            # +system
            if(args['-s'] or args['--system'] is True):
                # export path
                # print(envcustomlistrawpaths)
                for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                    if (plat == "Windows"):
                        lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
                    else:
                        lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

                # export var
                for (key, value) in pymakesystemenviron.items():
                    if (key == 'path+'):
                        continue
                    if (str(key).lower() == "path"):
                        continue
                    if (plat == "Windows"):
                        lines += (env_set + key + '=' + value + cmd_return)
                    else:
                        lines += (env_set + key + '=\"' + value + '\"' + cmd_return)
            else:
                ''

            # +local
            if(args['-l'] or args['--local'] is True):
                # export path
                for (key) in localenv['path+']:
                    if (plat == "Windows"):
                        lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
                    else:
                        lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

                # export var
                for (key, value) in localenv.items():
                    if (key == 'path+'):
                        continue
                    if (plat == "Windows"):
                        lines += (env_set + key + '=' + value + cmd_return)
                    else:
                        lines += (env_set + key + '=\"' + value + '\"' + cmd_return)
            else:
                ''

            # +custom
            if(args['-c'] or args['--custom'] is True):
                # export path
                # print(envcustomlistrawpaths)
                for (key) in envcustomlistrawpaths:
                    if (plat == "Windows"):
                        lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
                    else:
                        lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

                # export var
                for (key, value) in envcustomlistrawvars.items():
                    if (key == 'path+'):
                        continue
                    if (plat == "Windows"):
                        lines += (env_set + key + '=' + value + cmd_return)
                    else:
                        lines += (env_set + key + '=\"' + value + '\"' + cmd_return)
            else:
                ''

            # export path
            for (key) in dict0["path+"]:
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
                else:
                    lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

            # export var
            for (key, value) in dict0.items():
                if (key == 'path+'):
                    continue
                if (plat == "Windows"):
                    lines += (env_set + key + '=' + value + cmd_return)
                else:
                    lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

            with open(cmd_effect, 'w', encoding=cmd_codec) as f:
                f.write(cmd_header)
                f.write(lines)

            # export unset env
            cmd_unset = 'env'
            if (file_name is not None):
                cmd_unset = file_name
            cmd_unset += '_unset' + cmd_suffix

            lines = ""

            # +system
            if(args['-s'] or args['--system'] is True):
                # export unset path
                for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                    if (plat == "Windows"):
                        lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
                    else:
                        lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

                # export unset var
                for (key, value) in pymakesystemenviron.items():
                    if (key == 'path+'):
                        continue
                    if (str(key).lower() == "path"):
                        continue
                    if (plat == "Windows"):
                        lines += ('set ' + key + '=' + cmd_return)
                    else:
                        lines += ('unset ' + key + cmd_return)
            else:
                ''

            # +local
            if(args['-l'] or args['--local'] is True):
                # export unset path
                for (key) in localenv['path+']:
                    if (plat == "Windows"):
                        lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
                    else:
                        lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

                # export unset var
                for (key, value) in localenv.items():
                    if (key == 'path+'):
                        continue
                    if (plat == "Windows"):
                        lines += ('set ' + key + '=' + cmd_return)
                    else:
                        lines += ('unset ' + key + cmd_return)
            else:
                ''

            # +custom
            if(args['-c'] or args['--custom'] is True):
                # export unset path
                for (key) in envcustomlistrawpaths:
                    if (plat == "Windows"):
                        lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
                    else:
                        lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

                # export unset var
                for (key, value) in envcustomlistrawvars.items():
                    if (key == 'path+'):
                        continue
                    if (plat == "Windows"):
                        lines += ('set ' + key + '=' + cmd_return)
                    else:
                        lines += ('unset ' + key + cmd_return)
            else:
                ''

            # export unset path
            for (key) in dict0["path+"]:
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
                else:
                    lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

            # export unset var
            for (key, value) in dict0.items():
                if (key == 'path+'):
                    continue
                if (plat == "Windows"):
                    lines += ('set ' + key + '=' + cmd_return)
                else:
                    lines += ('unset ' + key + cmd_return)

            with open(cmd_unset, 'w', encoding=cmd_codec) as f:
                f.write(cmd_header)
                f.write(lines)

            if (plat == "Windows"):
                ""
            else:
                os.system("chmod +x " + cmd_effect)
                os.system("chmod +x " + cmd_unset)

            # +system
            if(args['-s'] or args['--system'] is True):
                print("successed: export %s env to %s %s" % ('system', cmd_effect, cmd_unset))
            else:
                ''
            # +local
            if(args['-l'] or args['--local'] is True):
                print("successed: export %s env to %s %s" % ('local', cmd_effect, cmd_unset))
            else:
                ''
            # +custom
            if(args['-c'] or args['--custom'] is True):
                print("successed: export %s env to %s %s" % ('custom', cmd_effect, cmd_unset))
            else:
                ''
            print("successed: export %s env to %s %s" % (current_var, cmd_effect, cmd_unset))

            return
        else:
            ''
        break

    #powershell export env function
    def powershell_environ_export(env_name = None, file_name = None):
        # select env
        current_var = rawconfig['environ']['current']
        if (env_name is not None):
            current_var = env_name
        dict0 = copy.deepcopy(rawconfig['environ'][current_var])

        cmd_suffix = ".ps1"
        cmd_codec = 'ansi'
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_header = "#!/usr/bin/env bash" + cmd_return
        env_set = ''

        # export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = "" + file_name
        cmd_effect += '_effect' + cmd_suffix

        # export path
        lines = ""
        for (key) in dict0["path+"]:
            lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

        # export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)

        # print(lines.split('\n'))
        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header)
            f.write(lines)

        # export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = "" + file_name
        cmd_unset += '_unset' + cmd_suffix

        # export unset path
        lines = ""
        for (key) in dict0["path+"]:
            # lines += ("$env:Path = $env:Path.Replace(\"%s;\", \"\")" % key) + cmd_return
            lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return
        # export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            lines += ("${env:%s} = \"\"" % key) + cmd_return

        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header)
            f.write(lines)

        return current_var, cmd_effect, cmd_unset

    # powershell [windows, unix]
    def createCmdList03(env_name = None, local=True, list0=[], params0=[]):

        cmd_list = []

        if(env_name is None):
            env_name = rawconfig['environ']['current']

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        # print (name)

        #plat = getplatform()

        cmd_status = "echo pymake-command-status:$LASTEXITCODE"
        cmd_sep = ';'
        cmd_suffix = ".ps1"
        cmd_suffix_powershell = cmd_suffix
        cmd_exit = 'exit $LASTEXITCODE'
        cmd_codec = 'ansi'
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_header = "#!/usr/bin/env bash"
        cmd_call = "./"
        # cmd_list.append(cmd_header)
        cmd_list.append("./%s_effect%s" % (name, cmd_suffix))

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        # print(params_string)

        if (local is True):
            for cmd in list0:
                cmd_list.append(cmd)
        else:
            #actually now has only one command.
            for cmd in list0:
                # warning: now pymake is in user setted workroot.
                if(str(cmd).endswith(cmd_suffix_powershell)):
                    cmd_suffix_powershell = ''

                powershellexecfile = ""
                while(True):
                    # find in current path [+workroot]
                    powershellexecfile = os.getcwd() + os.path.sep + cmd + cmd_suffix_powershell
                    if(os.path.exists(powershellexecfile)):
                        break
                    powershellexecfile = pymakeworkpath + os.path.sep + cmd + cmd_suffix_powershell
                    if(os.path.exists(powershellexecfile)):
                        break

                    # find in .json environ
                    separateenvlistpath = os.path.pathsep.join(rawconfig['environ'][env_name]['path+'])
                    separateenvlistpath = separateenvlistpath.split(os.path.pathsep)
                    separateenvlistpath.reverse()
                    #for path0 in separateenvlistpath:
                    #    print(path0)
                    find_flag = 0
                    for path0 in separateenvlistpath:
                        powershellexecfile = path0 + os.path.sep + cmd + cmd_suffix_powershell
                        if (os.path.exists(powershellexecfile)):
                            find_flag = 1
                            break
                    if(find_flag == 1):
                        break

                    # find in basic environ [+custom]
                    env = os.environ
                    find_flag = 0
                    for path0 in env["PATH"].split(os.path.pathsep):
                        powershellexecfile = path0 + os.path.sep + cmd + cmd_suffix_powershell
                        if (os.path.exists(powershellexecfile)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # none? a powershell command, or powershell command-line.
                    powershellexecfile = cmd
                    break

                #print(powershellexecfile)
                #wow
                #cmd_list.append(powershellexecfile + ' ' + params_string)
                if (str(powershellexecfile).__contains__(' ')):
                    if(os.path.isfile(powershellexecfile)):
                        powershellexecfile = powershellexecfile.replace('/', os.path.sep)
                        powershellexecfile = powershellexecfile.replace('\\', os.path.sep)
                        cmd_list.append(". \"%s\" @args" % powershellexecfile)
                    else:
                        cmd_list.append("%s" % powershellexecfile)
                else:
                    if(os.path.isfile(powershellexecfile)):
                        powershellexecfile = powershellexecfile.replace('/', os.path.sep)
                        powershellexecfile = powershellexecfile.replace('\\', os.path.sep)
                        cmd_list.append(". %s @args" % powershellexecfile)
                    else:
                        cmd_list.append("%s" % powershellexecfile)

        # append exit 0
        cmd_list.append(cmd_exit)
        # print( cmd_list )

        cmd_execute = "" + name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        # print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        # if (plat == "Windows"):
        #    ""
        # else:
        #    os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        cmd_list.append(cmd_call + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)
        cmd_list.append(cmd_exit)

        # print (cmd_list)
        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        return cmd_list, name

    #print(args)
    #print(args['powershell'])
    #powershell is using basic, .json, and custom environ data.
    #powershell command
    while (True):
        if (args['powershell'] is True):
            if (args['export'] is True):
                current_env = args['<env-name>']
                if (args['<env-name>'] is None):
                    current_env = rawconfig['environ']['current']
                    print(Fore.CYAN + "%s" % current_env)
                    for key in rawconfig['environ'].keys():
                        if (key == 'current'):
                            continue
                        if (key == current_env):
                            continue
                        print("%s" % key)
                    return

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print("please ensure the environ is right")
                    return

                if (args['<env-name>'] == "current"):
                    current_env = rawconfig['environ']['current']

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                    return

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                current_var = ""
                cmd_effect = ""
                cmd_unset = ""
                current_var, cmd_effect, cmd_unset = powershell_environ_export(current_env, args['<file-name>'])

                print("successed: export %s to %s %s" % (current_var, cmd_effect, cmd_unset))
                return
            elif (args['type'] is True):
                current_env = ""

                if (args['use'] is True):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = rawconfig['environ']['current']

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                if (args['<cmd-name>'] is None):
                    for (key, value) in rawconfig['command'].items():
                        print(Fore.CYAN + "%s" % key)
                    return

                if (rawconfig['command'].__contains__(args['<cmd-name>']) is False):
                    print("please check your command name")
                    return

                if (args['<file-name>'] is None):
                    if (current_env == rawconfig['environ']['current']):
                        list0 = copy.deepcopy(rawconfig['command'][args['<cmd-name>']])
                    else:
                        list0 = copy.deepcopy(raw_command(current_env)[args['<cmd-name>']])

                    for cmd in list0:
                        print(Fore.RED + "%s" % (cmd))
                    return

                cmd_exec = ""
                #cmd_exec = cmd_type(args['<cmd-name>'], args['<file-name>'], current_env)
                cmd_name = args['<cmd-name>']
                file_name = args['<file-name>']
                env_name = current_env

                if (cmd_name is None):
                    for (key, value) in rawconfig['command'].items():
                        print(Fore.CYAN + "%s" % key)
                    return

                if (rawconfig['command'].__contains__(cmd_name) is False):
                    print("please check your command name")
                    return

                if (env_name is None or env_name == rawconfig['environ']['current']):
                    list0 = copy.deepcopy(rawconfig['command'][cmd_name])
                else:
                    list0 = copy.deepcopy(raw_command(env_name)[cmd_name])

                # for cmd in list0:
                #    print(Fore.RED + "%s" % (cmd))

                temp_file_name = ""
                if (file_name is None):
                    temp_file_name = "cmd"
                else:
                    temp_file_name = "" + file_name

                cmd_header = "#!/usr/bin/env bash"
                cmd_codec = "ansi"
                if (getplatform_release() == "XP"):
                    cmd_codec = None
                # but windows, it is \r\n, python helpping me?
                cmd_return = "\n"
                cmd_suffix = "_exec.ps1"

                cmd_exec = temp_file_name + cmd_suffix
                with open(cmd_exec, 'w', encoding=cmd_codec) as f:
                    #f.write(cmd_header + cmd_return)
                    for cmd in list0:
                        f.write(cmd + cmd_return)

                #if (plat == "Windows"):
                #    ""
                #else:
                #    os.system("chmod +x " + cmd_exec)

                print("successed: use %s type %s to %s" % (current_env, args['<cmd-name>'], cmd_exec))
                return
            elif (args['ccvp'] or args['execvp'] or args['exec-with-params'] is True):
                current_env = ""
                if (args['use'] is True):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (current_env == 'current'
                        or rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = rawconfig['environ']['current']

                if (args['<command-name>'] is None):
                    print("please appoint your command")
                    return

                #print(args['hh'])
                #print(args['here'])
                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                #print(args['--workroot'])
                if (args['--workroot'] is not None):
                    if (os.path.isdir(args['--workroot'])
                        and os.path.isabs(args['--workroot'])):
                        os.chdir(args['--workroot'])
                    else:
                        print('please input an existed and legal work root.')
                        return

                # create cmd_list
                current_var = current_env
                local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                list0 = []
                local = True
                current_var = args['<command-name>']
                if (current_var in dict0):
                    list0.extend(dict0[current_var])
                    local = True
                else:
                    list0.append(current_var)
                    local = False

                params0 = []
                # print(args['--params'])
                # print(args['<command-params>'])
                for current_var in args['--params']:
                    params0.append(current_var)
                for current_var in args['<command-params>']:
                    params0.append(current_var)

                #print(list0)
                #print(params0)

                cmd_list = []
                temp_file_name = ""
                # if (getplatform() == "Windows"):
                #    cmd_list, temp_file_name = createCmdList0(list0)
                # else:
                #    cmd_list, temp_file_name = createCmdList01(list0)
                # good compatibility
                cmd_list, temp_file_name = createCmdList03(current_env, local, list0, params0)

                # export env
                current_var = current_env
                # print (current_var, temp_file_name)
                powershell_environ_export(current_var, temp_file_name)

                ret = communicateWithCommandLine3(cmd_list)

                # delete env file and cmd file
                temp_file = "" + temp_file_name + "_exec.ps1"
                if (os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = "" + temp_file_name + "_effect.ps1"
                if (os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = "" + temp_file_name + "_unset.ps1"
                if (os.path.exists(temp_file)):
                    os.remove(temp_file)

                os._exit(ret)
                return
            elif (args['clean'] is True):
                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                plat = getplatform()
                if (plat == "Windows"):
                    os.system("@del /f /q *_effect.ps1 *_unset.ps1 *_exec.ps1")
                else:
                    os.system("rm -f *_effect.ps1 *_unset.ps1 *_exec.ps1")

                return
            elif (args['info'] or args['information'] is True):
                plat = getplatform()
                env = os.environ
                if(plat == "Windows"):
                    print("powershell          : %s\system32\WindowsPowerShell\\v1.0\powershell.exe" % env["SystemRoot"])
                    print("powershell ISE      : %s\system32\WindowsPowerShell\\v1.0\PowerShell_ISE.exe" % env["SystemRoot"])
                    print("powershell(x86)     : %s\syswow64\WindowsPowerShell\\v1.0\powershell.exe" % env["SystemRoot"])
                    print("powershell ISE (x86): %s\syswow64\WindowsPowerShell\\v1.0\PowerShell_ISE.exe" % env["SystemRoot"])
                return
            elif (args['stat'] or args['status'] is True):
                plat = getplatform()
                env = os.environ
                if(plat == "Windows"):
                    powershell = ( "%s\system32\WindowsPowerShell\\v1.0\powershell.exe" % env["SystemRoot"])
                    powershell_ise = ("%s\system32\WindowsPowerShell\\v1.0\powershell_ISE.exe" % env["SystemRoot"])
                    powershell_x86 = ( "%s\syswow64\WindowsPowerShell\\v1.0\powershell.exe" % env["SystemRoot"])
                    powershell_ise_x86 = ("%s\syswow64\WindowsPowerShell\\v1.0\powershell_ISE.exe" % env["SystemRoot"])
                    if(os.path.exists(powershell)):
                        print("powershell          : NORMAL.")
                    else:
                        print("powershell          : UNINSTALL.")
                    if (os.path.exists(powershell_ise)):
                        print("powershell ISE      : NORMAL.")
                    else:
                        print("powershell ISE      : UNINSTALL.")
                    if (os.path.exists(powershell_x86)):
                        print("powershell(x86)     : NORMAL.")
                    else:
                        print("powershell(x86)     : UNINSTALL.")
                    if (os.path.exists(powershell_ise_x86)):
                        print("powershell ISE (x86): NORMAL.")
                    else:
                        print("powershell ISE (x86): UNINSTALL.")
                else:
                    ''
                return
            else:
                plat = getplatform()
                env = os.environ
                if(plat == "Windows"):
                    print("powershell          : %s\system32\WindowsPowerShell\\v1.0\powershell.exe" % env["SystemRoot"])
                    print("powershell ISE      : %s\system32\WindowsPowerShell\\v1.0\PowerShell_ISE.exe" % env["SystemRoot"])
                    print("powershell(x86)     : %s\syswow64\WindowsPowerShell\\v1.0\powershell.exe" % env["SystemRoot"])
                    print("powershell ISE (x86): %s\syswow64\WindowsPowerShell\\v1.0\PowerShell_ISE.exe" % env["SystemRoot"])
                return
        else:
            ''
        break

    # python export function
    def python_env_export (env_name = None, file_name = None):
        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name
        dict0 = copy.deepcopy(rawconfig['environ'][current_var])

        plat = getplatform()
        if (plat == "Windows"):
            cmd_suffix = ".bat"
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_return = "\n"
            cmd_header = "@echo off" + cmd_return
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash" + cmd_return
            env_set = 'export '

        #export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = file_name
        cmd_effect += '_effect' + cmd_suffix

        #export path
        lines = ""
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
            else:
                lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + cmd_return)
            else:
                lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        #export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = file_name
        cmd_unset += '_unset' + cmd_suffix

        #export unset path
        lines = ""
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

        #export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + cmd_return)
            else:
                lines += ('unset ' + key + cmd_return)
        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_effect)
            os.system("chmod +x " + cmd_unset)

        #return file name
        return current_var, cmd_effect, cmd_unset

    # python [windows unix]
    def createCmdList05(env_name = None, local = True, list0 = [], params0 = []):
        cmd_list = []

        if(env_name is None):
            env_name = rawconfig['environ']['current']

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            cmd_call = "call "
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            cmd_list.append("call %s_effect.bat" % name)
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)

        cmd_suffix_python = '.py'
        cmd_codec_python = "utf8"
        cmd_return_python = "\n"

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        pythonexecfile = ''
        if ( local is True):
            #fixed
            pythonexecfile = name + '_exec' + cmd_suffix_python
            with open(pythonexecfile, 'w', encoding=cmd_codec_python) as f:
                for cmd in list0:
                    f.write(cmd + cmd_return_python)
            #print(1, pythonexecfile)
        else:
            #actually now has only one command.
            for cmd in list0:
                # warning: now pymake is in user setted workroot.
                if(str(cmd).endswith(cmd_suffix_python)):
                    cmd_suffix_python = ''

                pythonexecfile = ""
                while(True):
                    # find in current path [+workroot]
                    pythonexecfile = os.getcwd() + os.path.sep + cmd + cmd_suffix_python
                    #print(2, pythonexecfile)
                    if(os.path.exists(pythonexecfile)):
                        break
                    pythonexecfile = pymakeworkpath + os.path.sep + cmd + cmd_suffix_python
                    #print(2, pythonexecfile)
                    if(os.path.exists(pythonexecfile)):
                        break

                    # find in .json environ
                    separateenvlistpath = os.path.pathsep.join(rawconfig['environ'][env_name]['path+'])
                    separateenvlistpath = separateenvlistpath.split(os.path.pathsep)
                    separateenvlistpath.reverse()
                    #for path0 in separateenvlistpath:
                    #    print(path0)
                    find_flag = 0
                    for path0 in separateenvlistpath:
                        pythonexecfile = path0 + os.path.sep + cmd + cmd_suffix_python
                        #print(2, pythonexecfile)
                        if (os.path.exists(pythonexecfile)):
                            find_flag = 1
                            break
                    if(find_flag == 1):
                        break

                    # find in basic environ [custom+]
                    env = os.environ
                    find_flag = 0
                    for path0 in env["PATH"].split(os.path.pathsep):
                        pythonexecfile = path0 + os.path.sep + cmd + cmd_suffix_python
                        #print(2, pythonexecfile)
                        if (os.path.exists(pythonexecfile)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # none? a python command, or python command-line.
                    pythonexecfile = cmd
                    break

                #print(2, pythonexecfile)
                #cmd_list.append(pythonexecfile + ' ' + params_string)

        #print params.
        #print(3, pythonexecfile)

        #get python command.
        pycmd = ''
        if(plat == "Windows"):
            pycmd = 'python.exe'
        else:
            pycmd = 'python3'

        pycmd = which_command(env_name, pycmd)

        #print(pycmd)
        if(plat == "Windows"):
            if(pycmd is None):
                pycmd = 'py'
            elif(pycmd != 'py'):
                pycmd = 'python'
        else:
            pycmd = 'python3'

        if(os.path.isfile(pythonexecfile)):
            if(plat == "Windows"):
                cmd_list.append("call %s \"%s\" %s" % (pycmd, pythonexecfile, '%*'))
            else:
                cmd_list.append("%s \"%s\" %s" % (pycmd, pythonexecfile, '"$@"'))
        else:
            if(plat == "Windows"):
                cmd_list.append("call %s -c \"%s\" %s" % (pycmd, pythonexecfile, '%*'))
            else:
                cmd_list.append("%s -c \"%s\" %s" % (pycmd, pythonexecfile, '"$@"'))

        # append exit 0
        cmd_list.append(cmd_exit)

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        #print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("call " + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("./" + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)

        cmd_list.append(cmd_exit)

        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        return cmd_list, name

    #python command
    while(True):
        if(args['python'] is True):
            plat = getplatform()
            if(args['info'] or args['information'] is True):
                if(plat == "Windows"):
                    print(Fore.CYAN + 'py: %s\py.exe' % pymakesystemenviron['windir'])
                    os.system('py --list-paths')
                    return
                else:
                    print('python: %s' % subprocess.getoutput('which python'))
                    print('python2: %s' % subprocess.getoutput('which python2'))
                    print('python3: %s' % subprocess.getoutput('which python3'))
                return
            elif (args['stat'] or args['status'] is True):
                if(plat == "Windows"):
                    # print('py: %s\py.exe' % pymakesystemenviron['windir'])
                    if (os.path.exists("%s\py.exe" % pymakesystemenviron['windir']) is False):
                        print('please install python3.')
                        return
                    # os.system('py --list-paths')
                    print("installed.")
                else:
                    os.system('find /bin | grep -i python')
                    os.system('find /usr/bin | grep -i python')
                    os.system('find /usr/local/bin | grep -i python')
                return
            elif (args['clean'] is True):
                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                plat = getplatform()
                if (plat == "Windows"):
                    os.system("@del /f /q *_exec.py *_effect.bat *_unset.bat *_exec.bat")
                else:
                    os.system("rm -f *_exec.py *_effect.sh *_unset.sh *_exec.sh")

                return
            elif (args['type'] is True):
                current_env = ""

                if (args['use'] is True):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = rawconfig['environ']['current']

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                if (args['<cmd-name>'] is None):
                    for (key, value) in rawconfig['command'].items():
                        print(Fore.CYAN + "%s" % key)
                    return

                if (rawconfig['command'].__contains__(args['<cmd-name>']) is False):
                    print("please check your command name")
                    return

                if (args['<file-name>'] is None):
                    if (current_env == rawconfig['environ']['current']):
                        list0 = copy.deepcopy(rawconfig['command'][args['<cmd-name>']])
                    else:
                        list0 = copy.deepcopy(raw_command(current_env)[args['<cmd-name>']])

                    for cmd in list0:
                        print(Fore.RED + "%s" % (cmd))
                    return

                cmd_exec = ""
                # cmd_exec = cmd_type(args['<cmd-name>'], args['<file-name>'], current_env)
                cmd_name = args['<cmd-name>']
                file_name = args['<file-name>']
                env_name = current_env

                if (cmd_name is None):
                    for (key, value) in rawconfig['command'].items():
                        print(Fore.CYAN + "%s" % key)
                    return

                if (rawconfig['command'].__contains__(cmd_name) is False):
                    print("please check your command name")
                    return

                if (env_name is None or env_name == rawconfig['environ']['current']):
                    list0 = copy.deepcopy(rawconfig['command'][cmd_name])
                else:
                    list0 = copy.deepcopy(raw_command(env_name)[cmd_name])

                # for cmd in list0:
                #    print(Fore.RED + "%s" % (cmd))

                temp_file_name = ""
                if (file_name is None):
                    temp_file_name = "cmd"
                else:
                    temp_file_name = "" + file_name

                cmd_header = ""
                cmd_codec = "utf8"
                # but windows, it is \r\n, python helpping me?
                cmd_return = "\n"
                cmd_suffix = "_exec.py"

                cmd_exec = temp_file_name + cmd_suffix
                with open(cmd_exec, 'w', encoding=cmd_codec) as f:
                    # f.write(cmd_header + cmd_return)
                    for cmd in list0:
                        f.write(cmd + cmd_return)

                # if (plat == "Windows"):
                #    ""
                # else:
                #    os.system("chmod +x " + cmd_exec)

                print("successed: use %s type %s to %s" % (current_env, args['<cmd-name>'], cmd_exec))
                return
            else:
                ''
        else:
            ''
        break

    # python ccvp command
    while (True):
        if(args['python'] is True):
            if (args['ccvp'] or args['execvp'] or args['exec-with-params'] is True):
                current_env = ""
                if (args['use'] is True):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (current_env == 'current'
                        or rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = rawconfig['environ']['current']

                if (args['<command-name>'] is None):
                    print("please appoint your command")
                    return

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                # print(args['--workroot'])
                if (args['--workroot'] is not None):
                    if (os.path.isdir(args['--workroot'])
                        and os.path.isabs(args['--workroot'])):
                        os.chdir(args['--workroot'])
                    else:
                        print('please input an existed and legal work root.')
                        return

                # create cmd_list
                current_var = current_env
                local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                list0 = []
                local = True
                current_var = args['<command-name>']
                if (current_var in dict0):
                    list0.extend(dict0[current_var])
                    local = True
                else:
                    list0.append(current_var)
                    local = False

                params0 = []
                # print(args['--params'])
                # print(args['<command-params>'])
                for current_var in args['--params']:
                    params0.append(current_var)
                for current_var in args['<command-params>']:
                    params0.append(current_var)

                cmd_list = []
                temp_file_name = ""
                # if (getplatform() == "Windows"):
                #    cmd_list, temp_file_name = createCmdList0(list0)
                # else:
                #    cmd_list, temp_file_name = createCmdList01(list0)
                # good compatibility
                cmd_list, temp_file_name = createCmdList05(current_env, local, list0, params0)

                # export env
                current_var = current_env
                # print (current_var, temp_file_name)
                python_env_export(current_var, temp_file_name)

                ret = communicateWithCommandLine(cmd_list)

                # delete env file and cmd file
                cmd_prefix = ''
                temp_file = cmd_prefix + temp_file_name + "_exec.py"
                if (os.path.exists(temp_file)):
                    os.remove(temp_file)

                if (getplatform() == "Windows"):
                    temp_file = cmd_prefix + temp_file_name + "_exec.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = cmd_prefix + temp_file_name + "_effect.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = cmd_prefix + temp_file_name + "_unset.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                else:
                    temp_file = cmd_prefix + temp_file_name + "_exec.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = cmd_prefix + temp_file_name + "_effect.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = cmd_prefix + temp_file_name + "_unset.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)

                os._exit(ret)
                return
            else:
                plat = getplatform()
                if(plat == "Windows"):
                    print(Fore.CYAN + 'py: %s\py.exe' % pymakesystemenviron['windir'])
                    os.system('py --list-paths')
                    return
                else:
                    print('python: %s' % subprocess.getoutput('which python'))
                    print('python2: %s' % subprocess.getoutput('which python2'))
                    print('python3: %s' % subprocess.getoutput('which python3'))
                return
        else:
            ''
        break

    #print(args)
    #print(args['custom'])
    #print(args['hh'])
    #custom command
    while (True):
        if( args['custom'] is True ):
            #print('gggg')
            if(args['open'] is True):
                customconf.set('custom', 'switch', '1')
                customconf.write(open(pymakecustomini, 'w'))
                print('success: custom environment is opened, you can exec script at any path.')
                return
            elif (args['close'] is True):
                customconf.set('custom', 'switch', '0')
                customconf.write(open(pymakecustomini, 'w'))
                print('success: custom environment is closed, you can use pymake .json environ.')
                return
            elif (args['export'] is True):
                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                plat = getplatform()
                if (plat == "Windows"):
                    cmd_suffix = ".bat"
                    cmd_codec = "ansi"
                    if (getplatform_release() == "XP"):
                        cmd_codec = None
                    cmd_return = "\n"
                    cmd_header = "@echo off" + cmd_return
                    env_set = 'set '
                else:
                    cmd_suffix = ".sh"
                    cmd_codec = "utf8"
                    cmd_return = "\n"
                    cmd_header = "#!/usr/bin/env bash" + cmd_return
                    env_set = 'export '

                # export effect env
                cmd_effect = 'custom.env'
                if (args['<file-name>'] is not None):
                    cmd_effect = "custom." + args['<file-name>']
                cmd_effect += '_effect' + cmd_suffix

                lines = ""
                # export path
                #print(envcustomlistrawpaths)
                for (key) in envcustomlistrawpaths:
                    if (plat == "Windows"):
                        lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
                    else:
                        lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

                # export var
                for (key, value) in envcustomlistrawvars.items():
                    if (key == 'path+'):
                        continue
                    if (plat == "Windows"):
                        lines += (env_set + key + '=' + value + cmd_return)
                    else:
                        lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

                #print("------------------")
                #print(lines)
                with open(cmd_effect, 'w') as f:
                    f.write(cmd_header)
                    f.write(lines)

                # export unset env
                cmd_unset = 'custom.env'
                if (args['<file-name>'] is not None):
                    cmd_unset = "custom." + args['<file-name>']
                cmd_unset += '_unset' + cmd_suffix

                # export unset path
                lines = ""
                for (key) in envcustomlistrawpaths:
                    if (plat == "Windows"):
                        lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
                    else:
                        lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

                # export unset var
                for (key, value) in envcustomlistrawvars.items():
                    if (key == 'path+'):
                        continue
                    if (plat == "Windows"):
                        lines += ('set ' + key + '=' + cmd_return)
                    else:
                        lines += ('unset ' + key + cmd_return)

                #print("------------------")
                #print(lines)
                with open(cmd_unset, 'w') as f:
                    f.write(cmd_header)
                    f.write(lines)

                if (plat == "Windows"):
                    ""
                else:
                    os.system("chmod +x " + cmd_effect)
                    os.system("chmod +x " + cmd_unset)

                print("successed: export custom env to %s %s" % (cmd_effect, cmd_unset))
                return
            elif (args['edit'] is True):
                ''

                #os.chdir(sourceroot)

                cmd_list = []
                cmd_list.append(sourceroot + os.path.sep + 'custom.path+.ini')
                cmd_list.append(sourceroot + os.path.sep + 'custom.var+.ini')
                for file0 in cmd_list:
                    cmd0 = open_file(file0)
                    os.system(cmd0)
                    print('successed: %s' % file0)
                return

            elif(args['info'] or args['information'] is True):
                print("CUSTOM SETTING: %s" % (pymakecustomini))
                print("CUSTOM ENV+   : %s" % (customenvfile))
                print("CUSTOM PATH+  : %s" % (custompathfile))
                return
            elif (args['ccvp'] or args['execvp'] or args['exec-with-params'] is True):
                # print('custom ccvp command.')
                current_env = ""
                if (args['use'] is True):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (current_env == 'current'
                        or rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = None

                if (args['<command-name>'] is None):
                    print("please appoint your command")
                    return

                # print(args['hh'])
                # print(args['here'])
                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                # print(args['--workroot'])
                if (args['--workroot'] is not None):
                    if (os.path.isdir(args['--workroot'])
                        and os.path.isabs(args['--workroot'])):
                        os.chdir(args['--workroot'])
                    else:
                        print('please input an existed and legal work root.')
                        return

                # create cmd_list
                current_var = current_env
                local_command = ''
                if (current_var == None):
                    local_command = raw_command_system()
                else:
                    local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                list0 = []
                local = True
                current_var = args['<command-name>']
                if (current_var in dict0):
                    list0.extend(dict0[current_var])
                    local = True
                else:
                    list0.append(current_var)
                    local = False

                params0 = []
                # print(args['--params'])
                # print(args['<command-params>'])
                for current_var in args['--params']:
                    params0.append(current_var)
                for current_var in args['<command-params>']:
                    params0.append(current_var)

                current_var = current_env
                cmd_list = []
                temp_file_name = ""
                # if (getplatform() == "Windows"):
                #    cmd_list, temp_file_name = createCmdList0(list0)
                # else:
                #    cmd_list, temp_file_name = createCmdList01(list0)
                # good compatibility
                cmd_list, temp_file_name = createCmdList06(current_var, local, list0, params0)

                # export env
                current_var = current_env
                # print (current_var, temp_file_name)
                system_env_export(current_var, temp_file_name)

                ret = communicateWithCommandLine(cmd_list)

                # delete env file and cmd file
                if (getplatform() == "Windows"):
                    temp_file = temp_file_name + "_exec.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                else:
                    temp_file = temp_file_name + "_exec.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)

                os._exit(ret)
                return
            elif (args['path'] is True):
                if(args['<value>'] is None):
                    print(Fore.LIGHTGREEN_EX + "path+:")
                    for (key) in envcustomlistpaths:
                        print(Fore.LIGHTMAGENTA_EX + "  %s" % key)
                    return

                usingcustomenvpaths = copy.deepcopy(storecustompaths)

                if(args['--add'] is True):
                    if(not usingcustomenvpaths.__contains__(args['<value>'])):
                        usingcustomenvpaths.append(args['<value>'])
                        with open(custompathfile, 'w', encoding=cmd_codec) as f:
                            for l in usingcustomenvpaths:
                                f.write(l + cmd_return)
                        print("successed: %s" % args['<value>'])
                    else:
                        print('failed: %s is existed.' % args['<value>'])
                elif(args['--del'] is True):
                    if(usingcustomenvpaths.__contains__(args['<value>'])):
                        usingcustomenvpaths.remove(args['<value>'])
                        with open(custompathfile, 'w', encoding=cmd_codec) as f:
                            for l in usingcustomenvpaths:
                                f.write(l + cmd_return)
                        print("successed: %s" % args['<value>'])
                    else:
                        print('failed: %s is existed.' % args['<value>'])
                else:
                    ''
                return
            elif (args['var'] is True):
                if (args['<key>'] is None):
                    print(Fore.LIGHTGREEN_EX + "variable:")
                    for (key, value) in envcustomlistvars.items():
                        if (key == 'path+'):
                            continue
                        print(Fore.GREEN + "  %-30s %s" % (key, value))
                    return

                usingcustomenvvars = copy.deepcopy(storecustomvars)
                #print(args)
                #print(args['<key>'])
                #print(args['<value>'])
                #print(storecustompaths)
                #print(storecustomvars)
                if(args['--add'] is True):
                    if (args['<key>'] is None or args['<value>'] is None):
                        print(Fore.LIGHTGREEN_EX + "variable:")
                        for (key, value) in envcustomlistvars.items():
                            if (key == 'path+'):
                                continue
                            print(Fore.GREEN + "  %-30s %s" % (key, value))
                        return

                    varkeyvaluestring = args['<key>'] + '=' + args['<value>']
                    if(not usingcustomenvvars.__contains__(varkeyvaluestring)):
                        usingcustomenvvars.append(varkeyvaluestring)
                        with open(customenvfile, 'w', encoding=cmd_codec) as f:
                            for l in usingcustomenvvars:
                                f.write(l + cmd_return)
                        print("successed: %s" % varkeyvaluestring)
                    else:
                        print('failed: %s is existed.' % varkeyvaluestring)
                elif(args['--del'] is True):
                    if (args['<key>'] is None):
                        print(Fore.LIGHTGREEN_EX + "variable:")
                        for (key, value) in envcustomlistvars.items():
                            if (key == 'path+'):
                                continue
                            print(Fore.GREEN + "  %-30s %s" % (key, value))
                        return

                    varkeystring = args['<key>']

                    clean_list = []
                    for l in usingcustomenvvars:
                        if(str(l).split('=')[0] == varkeystring):
                            clean_list.append(l)
                    for l in clean_list:
                        if(usingcustomenvvars.__contains__(l)):
                            usingcustomenvvars.remove(l)

                    if(usingcustomenvvars != storecustomvars):
                        with open(customenvfile, 'w', encoding=cmd_codec) as f:
                            for l in usingcustomenvvars:
                                f.write(l + cmd_return)
                        print("successed: %s" % varkeystring)
                    else:
                        print('failed: %s is not existed.' % varkeystring)
                else:
                    ''
                return
            elif (args['env'] is True):
                #print(args)
                print (Fore.CYAN+ "custom env")

                envcustomlist0 = envcustomlistpaths
                envcustomlist1 = envcustomlistvars
                if(args['--raw'] is True):
                    envcustomlist0 = envcustomlistrawpaths
                    envcustomlist1 = envcustomlistrawvars

                print(Fore.LIGHTGREEN_EX + "path+:")
                for (key) in envcustomlist0:
                    print(Fore.LIGHTMAGENTA_EX + "  %s" % key)
                print(Fore.LIGHTGREEN_EX + "variable:")
                for (key, value) in envcustomlist1.items():
                    if (key == 'path+'):
                        continue
                    print(Fore.GREEN + "  %-30s %s" % (key, value))

                return
            elif (args['stat'] or args['status'] is True):
                status = "closed"
                if(switch0 == '1'):
                    status = "opened"
                print("custom env: %s." % status)
                return
            else:
                status = "closed"
                if(switch0 == '1'):
                    status = "opened"
                print("custom env: %s." % status)
                if(switch0 == '1'):
                    print(Fore.LIGHTGREEN_EX + "path+:")
                    for (key) in envcustomlistrawpaths:
                        print(Fore.LIGHTMAGENTA_EX + "  %s" % key)
                    print(Fore.LIGHTGREEN_EX + "variable:")
                    for (key, value) in envcustomlistrawvars.items():
                        if (key == 'path+'):
                            continue
                        print(Fore.GREEN + "  %-30s %s" % (key, value))
                return
        else:
            ''
        break

    #system command
    while (True):
        if(args['sys'] or args['system'] is True):
            ''
            if(args['stat'] or args['status'] is True):
                plat = getplatform()
                if(plat == "Windows"):
                    print("Normal")
                else:
                    from pycore.pyenviron import MyUnixEnviron
                    sysenv = MyUnixEnviron()
                    root0, root1 = sysenv.information()
                    print(Fore.LIGHTGREEN_EX + "system:")
                    for value in root0:
                        print(Fore.LIGHTRED_EX + "  %-30s [%s]" % (value, os.path.exists(value)))
                    print(Fore.LIGHTGREEN_EX + 'user:')
                    for value in root1:
                        print(Fore.LIGHTRED_EX + "  %-30s [%s]" % (value, os.path.exists(value)))
                return
            elif(args['info'] or args['information'] is True):
                ''
                plat = getplatform()
                if(plat == "Windows"):
                    from pycore.pyenviron import MyWin32Environ
                    sysenv = MyWin32Environ()
                    root0, root1 = sysenv.information()
                    print(Fore.LIGHTGREEN_EX + "system:")
                    for value in root0:
                        print(Fore.LIGHTRED_EX + "  %s" % value)
                    print(Fore.LIGHTGREEN_EX + 'user:')
                    for value in root1:
                        print(Fore.LIGHTRED_EX + "  %s" % value)
                else:
                    from pycore.pyenviron import MyUnixEnviron
                    sysenv = MyUnixEnviron()
                    root0, root1 = sysenv.information()
                    print(Fore.LIGHTGREEN_EX + "system:")
                    for value in root0:
                        print(Fore.LIGHTRED_EX + "  %s" % value)
                    print(Fore.LIGHTGREEN_EX + 'user:')
                    for value in root1:
                        print(Fore.LIGHTRED_EX + "  %s" % value)
                return
            elif (args['path'] is True):
                ''
                return
            elif(args['var'] is True):
                ''
                return
            else:
                print (Fore.CYAN + "system env")
                sysenv = copy.deepcopy(pymakesystemenviron)
                print(Fore.LIGHTGREEN_EX + "path+:")
                for (key) in sysenv['PATH'].split(os.path.pathsep):
                    print(Fore.LIGHTRED_EX + "  %s" % key)
                print(Fore.LIGHTGREEN_EX + "variable:")
                for (key, value) in sysenv.items():
                    if (key == 'path+'):
                        continue
                    if( str(key).lower() == "path"):
                        continue
                    print(Fore.LIGHTRED_EX + "  %-30s %s" % (key, value))
                return
        else:
            ''
        break

    # language export function
    def language_env_export (env_name = None, file_name = None):
        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name
        dict0 = copy.deepcopy(rawconfig['environ'][current_var])

        plat = getplatform()
        if (plat == "Windows"):
            cmd_suffix = ".bat"
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_return = "\n"
            cmd_header = "@echo off" + cmd_return
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash" + cmd_return
            env_set = 'export '

        #export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = file_name
        cmd_effect += '_effect' + cmd_suffix

        #export path
        lines = ""
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
            else:
                lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + cmd_return)
            else:
                lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        #export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = file_name
        cmd_unset += '_unset' + cmd_suffix

        #export unset path
        lines = ""
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

        #export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + cmd_return)
            else:
                lines += ('unset ' + key + cmd_return)
        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_effect)
            os.system("chmod +x " + cmd_unset)

        #return file name
        return current_var, cmd_effect, cmd_unset

    # language [ .bat .sh .ps1 .py ...] [windows unix] --suffix --encoding
    def createCmdList07(suffix = None, encoding = None, env_name = None, local = True, list0 = [], params0 = []):
        cmd_list = []

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            cmd_call = "call "
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            cmd_list.append("call %s_effect.bat" % name)
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)

        if(env_name is None):
            env_name = rawconfig['environ']['current']
        if(env_name == "current"):
            env_name = rawconfig['environ']['current']

        cmd_suffix_language = cmd_suffix
        cmd_codec_language = cmd_codec
        cmd_return_language = cmd_return

        if(suffix is not None):
            cmd_suffix_language = suffix
        if(encoding is not None):
            cmd_codec_language = encoding

        list1 = []
        # for current_var in str(args['<command-param>']).split():
        #    list1.append(current_var)
        if (params0.__len__() > 0):
            current_var = params0[0]
            list1.append(current_var)
            params0.pop(0)
        #print(list1)

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        local2 = True
        if (list1.__len__() > 0):
            current_var = list1[0]
            if (current_var in rawconfig['command']):
                local2 = True
            else:
                local2 = False

        languageparams = ''
        #actually only one param.
        if (local2 is True):
            for param1 in list1:
                languageparams += param1
        else:
            for param1 in list1:
                # warning: now pymake is in user setted workroot.

                languageparams = ""
                while (True):
                    # find in current path [+--workroot]
                    languageparams = os.getcwd() + os.path.sep + param1
                    # print(2, languageparams)
                    if (os.path.exists(languageparams)):
                        break
                    languageparams = pymakeworkpath + os.path.sep + param1
                    # print(2, languageparams)
                    if (os.path.exists(languageparams)):
                        break

                    # find in .json environ
                    separateenvlistpath = os.path.pathsep.join(rawconfig['environ'][env_name]['path+'])
                    separateenvlistpath = separateenvlistpath.split(os.path.pathsep)
                    separateenvlistpath.reverse()
                    #for path0 in separateenvlistpath:
                    #    print(path0)
                    find_flag = 0
                    for path0 in separateenvlistpath:
                        languageparams = path0 + os.path.sep + param1
                        #print(2, languageparams)
                        if (os.path.exists(languageparams)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # find in basic environ [custom+]
                    env = os.environ
                    find_flag = 0
                    for path0 in env["PATH"].split(os.path.pathsep):
                        languageparams = path0 + os.path.sep + param1
                        # print(2, languageparams)
                        if (os.path.exists(languageparams)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # none? a language command, or language command-line.
                    languageparams = param1
                    break

                    # print(2, languageparams)
                    # cmd_list.append(languageparams + ' ' + params_string)

        if(list1.__len__() >0):
            ''
            if(local2 is True):
                ''
                current_var = env_name
                local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                inside_name = name + '_2'
                languageparams = inside_name + '_exec' + cmd_suffix_language

                with open(languageparams, 'w', encoding=cmd_codec_language) as f:
                    for cmd1 in list1:
                        for cmd in dict0[cmd1]:
                            f.write(cmd + cmd_return_language)

                #print(1, cmd_suffix_language)
                #print(1, cmd_return_language)
                #print(1, cmd_codec_language)
                #print(1, languageparams)
            else:
                ''

        #print(3, languageparams)
        if(list1.__len__() >0 ):
            if(local2 is True):
                params_string = languageparams + ' ' + params_string
            else:
                if(str(languageparams).__contains__(' ')):
                    params_string = '"' + languageparams + '"' + ' ' + params_string
                else:
                    params_string = languageparams + ' ' + params_string
        #print(params_string)

        languageexecfile = ''
        if ( local is True):
            #fixed
            #inside_name = name
            #inside_name = hex( int( inside_name, 16 ) + 1).split('x')[1]
            inside_name = name + '_1'
            #print(inside_name)
            languageexecfile = inside_name + '_exec' + cmd_suffix
            with open(languageexecfile, 'w', encoding=cmd_codec) as f:
                for cmd in list0:
                    f.write(cmd + cmd_return)
            #print(1, languageexecfile)
        else:
            languageexecfile = ''
            #actually now has only one command.
            for cmd in list0:
                #actually this is a command.
                if (str(cmd).__contains__(' ')):
                    pycmd = which_command(env_name, str(cmd))
                    #print(cmd)
                    #print(pycmd)
                    if(pycmd is not None and os.path.isfile(pycmd)):
                        languageexecfile = '"' + cmd + '"'
                    else:
                        languageexecfile = cmd
                else:
                    languageexecfile = cmd

        #print(3, languageexecfile)
        if(plat == "Windows"):
            cmd_list.append("call %s %s" % (languageexecfile, '%*'))
        else:
            if(languageexecfile.endswith('.sh')):
                cmd_list.append("sh %s %s" % (languageexecfile, '"$@"'))
            else:
                cmd_list.append("%s %s" % (languageexecfile, '"$@"'))

        # append exit 0
        cmd_list.append(cmd_exit)

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("call " + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + ' '+ params_string + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("./" + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)

        cmd_list.append(cmd_exit)

        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        return cmd_list, name, cmd_suffix, cmd_suffix_language

    #language command
    while (True):
        if(args['language'] is True):
            if(args['stat'] or args['status'] is True):
                plat = getplatform()
                if(plat == "Windows"):
                    print("Normal")
                else:
                    print("Normal")
                return
            elif(args['info'] or args['information'] is True):
                plat = getplatform()
                if(plat == "Windows"):
                    print("Normal")
                else:
                    print("Normal")
                return
            elif(args['clean'] is True):
                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                #print(args['--suffix'])
                suffix = args['--suffix']
                if(suffix is None):
                    suffix  = ''
                filename = str("*_exec%s" % suffix)

                plat = getplatform()
                if (plat == "Windows"):
                    os.system(str("@del /f /q %s *_effect.bat *_unset.bat *_exec.bat" % filename))
                else:
                    os.system(str("rm -f %s *_effect.sh *_unset.sh *_exec.sh" % filename))

                return
            elif (args['type'] is True):
                current_env = ""

                if (args['use'] is True):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = rawconfig['environ']['current']

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                if (args['<cmd-name>'] is None):
                    for (key, value) in rawconfig['command'].items():
                        print(Fore.CYAN + "%s" % key)
                    return

                if (rawconfig['command'].__contains__(args['<cmd-name>']) is False):
                    print("please check your command name")
                    return

                if (args['<file-name>'] is None):
                    if (current_env == rawconfig['environ']['current']):
                        list0 = copy.deepcopy(rawconfig['command'][args['<cmd-name>']])
                    else:
                        list0 = copy.deepcopy(raw_command(current_env)[args['<cmd-name>']])

                    for cmd in list0:
                        print(Fore.RED + "%s" % (cmd))
                    return

                cmd_exec = ""
                # cmd_exec = cmd_type(args['<cmd-name>'], args['<file-name>'], current_env)
                cmd_name = args['<cmd-name>']
                file_name = args['<file-name>']
                env_name = current_env

                if (cmd_name is None):
                    for (key, value) in rawconfig['command'].items():
                        print(Fore.CYAN + "%s" % key)
                    return

                if (rawconfig['command'].__contains__(cmd_name) is False):
                    print("please check your command name")
                    return

                if (env_name is None or env_name == rawconfig['environ']['current']):
                    list0 = copy.deepcopy(rawconfig['command'][cmd_name])
                else:
                    list0 = copy.deepcopy(raw_command(env_name)[cmd_name])

                # for cmd in list0:
                #    print(Fore.RED + "%s" % (cmd))

                temp_file_name = ""
                if (file_name is None):
                    temp_file_name = "cmd"
                else:
                    temp_file_name = "" + file_name

                cmd_header = ""
                cmd_codec = "utf8"
                # but windows, it is \r\n, python helpping me?
                cmd_return = "\n"
                cmd_suffix = "_exec"
                if(getplatform() == "Windows"):
                    cmd_codec = "ansi"
                    if (getplatform_release() == "XP"):
                        cmd_codec = None
                    cmd_suffix = "_exec.bat"
                else:
                    cmd_codec = 'utf8'
                    cmd_suffix = "_exec.sh"

                suffix = args['--suffix']
                if(suffix is not None):
                    cmd_suffix = str("_exec%s" % suffix)

                encoding = args['--encoding']
                if(encoding is not None):
                    cmd_codec = encoding

                cmd_exec = temp_file_name + cmd_suffix
                with open(cmd_exec, 'w', encoding=cmd_codec) as f:
                    # f.write(cmd_header + cmd_return)
                    for cmd in list0:
                        f.write(cmd + cmd_return)

                # if (plat == "Windows"):
                #    ""
                # else:
                #    os.system("chmod +x " + cmd_exec)

                #print(cmd_codec)
                #print(cmd_suffix)
                #print(cmd_exec)

                print("successed: use %s type %s to %s" % (current_env, args['<cmd-name>'], cmd_exec))
                return
            elif (args['ccvp'] or args['execvp'] or args['exec-with-params'] is True):
                current_env = ""
                if (args['use'] is True):
                    if (args['<env-name>'] is None):
                        print("please appoint a environ")
                        return

                    if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                        print("please ensure the environ is right")
                        return

                    current_env = args['<env-name>']
                    if (args['<env-name>'] == "current"):
                        current_env = rawconfig['environ']['current']

                    if (current_env == 'current'
                        or rawconfig['environ'].__contains__(current_env) is False):
                        print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                        return
                else:
                    current_env = rawconfig['environ']['current']

                if (args['<command-name>'] is None):
                    print("please appoint your command")
                    return

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                # print(args['--workroot'])
                if (args['--workroot'] is not None):
                    if (os.path.isdir(args['--workroot'])
                        and os.path.isabs(args['--workroot'])):
                        os.chdir(args['--workroot'])
                    else:
                        print('please input an existed and legal work root.')
                        return

                # create cmd_list
                current_var = current_env
                local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                list0 = []
                local = True
                current_var = args['<command-name>']
                if (current_var in dict0):
                    list0.extend(dict0[current_var])
                    local = True
                else:
                    list0.append(current_var)
                    local = False

                params0 = []
                #print(args['--params'])
                #print(args['<command-params>'])
                for current_var in args['--params']:
                    params0.append(current_var)
                for current_var in args['<command-params>']:
                    params0.append(current_var)

                suffix = args['--suffix']
                encoding = args['--encoding']

                #print(list0)
                #print(params0)
                #print(suffix)
                #print(encoding)

                cmd_list = []
                temp_file_name = ""
                # if (getplatform() == "Windows"):
                #    cmd_list, temp_file_name = createCmdList0(list0)
                # else:
                #    cmd_list, temp_file_name = createCmdList01(list0)
                # good compatibility
                cmd_list, temp_file_name, cmd_suffix, cmd_suffix_language = createCmdList07(suffix, encoding, current_env, local, list0, params0)

                # export env
                current_var = current_env
                # print (current_var, temp_file_name)
                language_env_export(current_var, temp_file_name)

                ret = communicateWithCommandLine(cmd_list)

                # delete env file and cmd file
                cmd_prefix = ''
                temp_file = cmd_prefix + temp_file_name + "_1_exec" + cmd_suffix
                if (os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = cmd_prefix + temp_file_name + "_2_exec" + cmd_suffix_language
                if (os.path.exists(temp_file)):
                    os.remove(temp_file)

                if (getplatform() == "Windows"):
                    temp_file = cmd_prefix + temp_file_name + "_exec.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = cmd_prefix + temp_file_name + "_effect.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = cmd_prefix + temp_file_name + "_unset.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                else:
                    temp_file = cmd_prefix + temp_file_name + "_exec.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = cmd_prefix + temp_file_name + "_effect.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = cmd_prefix + temp_file_name + "_unset.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)

                os._exit(ret)
                return
            else:
                print("Normal.")
                return
        else:
            ''
        break

    # cmd type2 function
    def cmd_type2 (cmd_name = None, file_name = None, env_name = None):

        if (cmd_name is None):
            for (key, value) in rawconfig['command'].items():
                print(Fore.CYAN + "%s" % key)
            return

        if (rawconfig['command'].__contains__(cmd_name) is False):
            print("please check your command name")
            return

        if (env_name is None or env_name == rawconfig['environ']['current']):
            list0 = copy.deepcopy(rawconfig['command'][cmd_name])
        else:
            list0 = copy.deepcopy(raw_command(env_name)[cmd_name])

        # for cmd in list0:
        #    print(Fore.RED + "%s" % (cmd))

        temp_file_name = ""
        if (file_name is None):
            temp_file_name = "cmd"
        else:
            temp_file_name = "" + file_name

        cmd_header = ""
        cmd_codec = "utf8"
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_suffix = ""
        if (getplatform() == "Windows"):
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_header = "@echo off"
            cmd_suffix = ".bat"
        else:
            cmd_codec = 'utf8'
            cmd_header = "#!/usr/bin/env bash"
            cmd_suffix = ".sh"

        suffix = args['--suffix']
        if (suffix is not None):
            cmd_suffix = str("%s" % suffix)

        encoding = args['--encoding']
        if (encoding is not None):
            cmd_codec = encoding

        cmd_exec = temp_file_name + cmd_suffix
        with open(cmd_exec, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header + cmd_return)
            cmd = ''
            #add shebang line
            if(list(list0).__len__()>0):
                cmd = list0[0]
            #print(".....")
            if(getplatform() == "Windows"):
                if (cmd_suffix == '.bat'):
                    if (cmd.startswith('@echo') is False):
                        f.write(cmd_header + cmd_return)
            else:
                if (cmd_suffix == '.sh'):
                    if (cmd.startswith('#!') is False):
                        f.write(cmd_header + cmd_return)

            for cmd in list0:
                f.write(cmd + cmd_return)

        if (plat == "Windows"):
            ""
        else:
            if(cmd_suffix == '.sh'):
                os.system("chmod +x " + cmd_exec)

        # print(cmd_codec)
        # print(cmd_suffix)
        # print(cmd_exec)

        return cmd_exec

    # type2 command
    while (True):
        if (args['type2'] == True):
            current_env = ""

            if (args['use'] is True):
                if (args['<env-name>'] is None):
                    print("please appoint a environ")
                    return

                if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                    print("please ensure the environ is right")
                    return

                current_env = args['<env-name>']
                if (args['<env-name>'] == "current"):
                    current_env = rawconfig['environ']['current']

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                    return
            else:
                current_env = rawconfig['environ']['current']

            if (args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)
            elif (args['there'] or args['tt'] is True):
                os.chdir(customshellroot)
            elif (args['default'] or args['dd'] is True):
                os.chdir(pymakeshellroot)

            if(args['-a'] or args['--all'] is True):
                ''
                keys = config['command']
                for cmd in keys:
                    cmd_name = cmd
                    file_name = cmd
                    cmd_exec = cmd_type2(cmd_name, file_name, current_env)
                    print("successed: use %s type %s cmd to %s" % (current_env, file_name, cmd_exec))
                return

            if (args['<cmd-name>'] is None):
                for (key, value) in rawconfig['command'].items():
                    print(Fore.CYAN + "%s" % key)
                return

            if (rawconfig['command'].__contains__(args['<cmd-name>']) is False):
                print("please check your command name")
                return

            if(args['--samename'] is True):
                args['<file-name>'] = args['<cmd-name>']

            if (args['<file-name>'] is None):
                if (current_env == rawconfig['environ']['current']):
                    list0 = copy.deepcopy(rawconfig['command'][args['<cmd-name>']])
                else:
                    list0 = copy.deepcopy(raw_command(current_env)[args['<cmd-name>']])

                for cmd in list0:
                    print(Fore.RED + "%s" % (cmd))
                return

            cmd_exec = cmd_type2(args['<cmd-name>'], args['<file-name>'], current_env)
            print("successed: use %s type %s cmd to %s" % (current_env, args['<cmd-name>'], cmd_exec))
            return
        else:
            ""
        break

    # open command
    while (True):
        if (args['open'] is True):
            ''
            if (args['<path-name>'] == []):
                ''
                dict0 = copy.deepcopy(rawconfig['path-assemblage'])
                pos0 = 0
                for (key, value) in dict0.items():
                    pos0 = pos0 + 1
                    if (pos0 % 3 == 0):
                        print("%-30s" % key)
                        continue
                    print("%-30s" % key, end=' ')
                return

            if (args['-c'] or args['--custom'] is True):
                ''

            current_env = None
            if (args['--current'] is True):
                current_env = rawconfig['environ']['current']

            if (args['--envname'] is not None):
                current_var = args['--envname']
                if (current_var is None):
                    current_var = rawconfig['environ']['current']
                elif (current_var == "current"):
                    current_var = rawconfig['environ']['current']
                current_env = current_var

            if (args['<env-name>'] is not None):
                current_var = args['<env-name>']
                if (current_var is None):
                    current_var = rawconfig['environ']['current']
                elif (current_var == "current"):
                    current_var = rawconfig['environ']['current']
                current_env = current_var

            if(current_env is not None):
                if (rawconfig['environ'].__contains__(current_env) is False):
                    print("please ensure the environ is right")
                    return

            pathname = args['<path-name>']
            #print(pathname)
            #print(current_env)
            cmd_list = open_command(pathlist0=pathname, env_name=current_env)
            for cmd in cmd_list:
                os.system(cmd)
                print('successed: %s' % cmd)
            return
        else:
            ''
        break

    # clean *_effect *_unset *_exec .bat[.sh]
    while (True):
        if (args['clean'] == True):
            if (args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)
            elif (args['there'] or args['tt'] is True):
                os.chdir(customshellroot)
            elif (args['default'] or args['dd'] is True):
                os.chdir(pymakeshellroot)

            plat = getplatform()
            if(plat == "Windows"):
                os.system("@del /f /q *_effect.bat *_unset.bat *_exec.bat")
            else:
                os.system("rm -f *_effect.sh *_unset.sh *_exec.sh")

            return
        else:
            ""
        break

    # list show
    while (True):
        if (args['show'] or args['list'] is True):

            list_config = config
            if ( args['--raw'] is True ):
                list_config = rawconfig

            if( args['path'] == True):
                dict0 = copy.deepcopy(list_config['path-assemblage'])
                if (args['<name>'] is not None):
                    if(dict0.__contains__(args['<name>']) is False):
                        print("there is no this path item in path assemblage.")
                        return
                    value = dict0[args['<name>']]
                    print(Fore.GREEN + "%s" % (value))
                else:
                    for (k, v) in dict0.items():
                        print(Fore.MAGENTA+ "%-24s %s" % (k, v) )

            elif( args['env'] == True):
                env = os.environ

                current_var = args['<name>']
                if (args['<name>'] is None):
                    current_var = list_config['environ']['current']
                elif (args['<name>'] is not None):
                    current_var = args['<name>']
                    if (current_var == "current"):
                        current_var = list_config['environ']['current']
                    if (list_config['environ'].__contains__(current_var) is False):
                        print("please ensure the environ is right")
                        return

                dict0 = copy.deepcopy(list_config['environ'][current_var])

                print (Fore.CYAN+ "env %s" % current_var)
                print(Fore.MAGENTA + "path+:")
                for (key) in dict0["path+"]:
                    print(Fore.MAGENTA + "  %s" % key)
                if(args['-a'] or args['--all'] is True):
                    for path in env["PATH"].split(os.path.pathsep):
                        print(Fore.MAGENTA + "  %s" % path)
                print(Fore.MAGENTA + "variable:")
                for (key, value) in dict0.items():
                    if (key == 'path+'):
                        continue
                    print(Fore.GREEN + "  %-30s %s" % (key, value))
                if (args['-a'] or args['--all'] is True):
                    for (key, value) in env.items():
                        if (key == 'PATH'):
                            continue
                        print(Fore.GREEN + "  %-30s %s" % (key, value))

            elif( args['cmd'] == True):
                dict0 = copy.deepcopy(list_config['command'])
                if (args['<name>'] is not None):
                    #print(Fore.CYAN + "group: %s" % args['<name>'])
                    if(dict0.__contains__(args['<name>']) is False):
                        print("there is no this cmd in command group.")
                        return
                    value = dict0[args['<name>']]
                    step = 1
                    for cmd in value:
                        print(Fore.RED + "%-3s %s" % (step, cmd))
                        step += 1
                else:
                    for (key, value) in dict0.items():
                        if (args['-a'] is not True and args['--all'] is not True):
                            print(Fore.CYAN + "%s" % key)
                            continue
                        print(Fore.CYAN + "group: %s" % key)
                        step = 1
                        for cmd in value:
                            print(Fore.RED + "%-3s %s" % (step, cmd))
                            step += 1
            else:
                current_var = rawconfig['environ']['current']
                print(Fore.CYAN + "%s" % current_var)
                for key in rawconfig['environ'].keys() :
                    if(key == 'current'):
                        continue
                    if(key == current_var):
                        continue
                    print("%s" % key)
            return
        else:
            ''
        break

    # have has
    while (True):
        if (args['have'] or args['has'] is True):

            list_config = config
            if ( args['--raw'] is True ):
                list_config = rawconfig

            if( args['env'] == True):
                if ( args['path'] == True):
                    #print(args['<group>'], args['<name>'])
                    if (args['<group>'] is None):
                        print ("please input your env name.")
                        return

                    current_env = args['<group>']
                    if (current_env == "current"):
                        current_env = list_config['environ']['current']

                    if (args['<name>'] is None):
                        print ("please input your path value.")
                        return
                    current_name = args['<name>']

                    if (list_config['environ'][current_env]['path+'].__contains__(current_name) is True):
                        print("True")
                    else:
                        print("False")
                    return

                #env name is empty
                if ( args['<group>'] is None ):
                    current_env = list_config['environ']['current']
                    if (list_config['environ'].__contains__(current_env) is True):
                        print("True")
                    else:
                        print("False")
                    return

                current_env = args['<group>']
                if (current_env == "current"):
                    current_env = list_config['environ']['current']

                # item var name is empty
                if ( args['<name>'] is None ):
                    if(list_config['environ'].__contains__(current_env) is True):
                        print("True")
                    else:
                        print("False")
                    return

                current_name = args['<name>']
                if( current_name == "path+" ):
                    print("please ensure your var name is legal.")
                    return

                #env name is ok
                #env-var name is ok
                if (list_config['environ'].__contains__(current_env) is True):
                    if (list_config['environ'][current_env].__contains__(current_name) is True):
                        print("True")
                    else:
                        print("False")
                    return
                else:
                    print("False")
                return

            elif( args['path'] == True):
                dict0 = copy.deepcopy(list_config['path-assemblage'])
                for (k, v) in dict0.items():
                    if( k == args['<name>']):
                        print ("True")
                        return
                print ("False")
                return

            elif( args['cmd'] == True):
                dict0 = copy.deepcopy(list_config['command'])
                for (k, v) in dict0.items():
                    if( k == args['<name>']):
                        print ("True")
                        return
                print ("False")
                return

            else:
                print("please ensure your assemblage name.")
                return

            return
        else:
            ''
        break

    # need return, set return, default break.
    # get
    while (True):
        if (args['get'] == True):
            if (args['all'] is True):
                if (args['stat'] is True):
                    print("%s" % pymakeworkpath)
                    print("%s" % customshellroot)
                    print("%s" % pymakeshellroot)
                    print("%s" % workroottype)
                    print("%s" % shellroot)
                    return
                elif (args['status'] is True):
                    print("EXECUTE ROOT [HERE    ]: %s" % pymakeworkpath)
                    print("EXECUTE ROOT [THERE   ]: %s" % customshellroot)
                    print("EXECUTE ROOT [DEFAULT ]: %s" % pymakeshellroot)
                    print("EXECUTE ROOT [TYPE    ]: %s" % workroottype)
                    print("EXECUTE ROOT [STARTING]: %s" % shellroot)
                    return
                elif (args['info'] is True):
                    if(config.__contains__("environ") is True):
                        if (config['environ'].__contains__("current") is True):
                            print("%s" % (config["environ"]["current"]))
                        else:
                            print("failed: .json file is broken, environ section lost current key, please use set command fix it.")
                    else:
                        print("failed: please check your .json file content, it is not now version .json.")

                    r = conf.get('source', 'root')
                    f = conf.get('source', 'config')
                    print("%s%s%s" % (r, os.path.sep, f))
                    print("%s" % (r))
                    print("%s" % (f))
                    print("-----------------------------------------")
                    print("%s" % os.path.realpath(__file__))
                    print("%s" % os.path.split(os.path.realpath(__file__))[0])
                    print("%s" % os.path.split(os.path.realpath(__file__))[1])
                    print("-----------------------------------------")
                    print("%s" % (pymakeini))
                    print("%s" % (pymakeroot))
                    print("%s" % (os.path.split(os.path.realpath(pymakeini))[1]))
                    print("-----------------------------------------")
                    print("%s" % portinifile)
                    print("%s" % os.path.split(os.path.realpath(portinifile))[0])
                    print("%s" % os.path.split(os.path.realpath(portinifile))[1])
                    return
                elif (args['information'] is True):
                    if(config.__contains__("environ") is True):
                        if (config['environ'].__contains__("current") is True):
                            print("CURRENT ENVIRON %s" % (config["environ"]["current"]))
                        else:
                            print("CURRENT ENVIRON failed: .json file is broken, environ section lost current key, please use set command fix it.")
                    else:
                        print("CURRENT ENVIRON failed: please check your .json file content, it is not compatible version .json.")

                    r = conf.get('source', 'root')
                    f = conf.get('source', 'config')
                    print("SOURCE        : %s%s%s" % (r, os.path.sep, f))
                    print("SOURCE ROOT   : %s" % (r))
                    print("SOURCE CONFIG : %s" % (f))
                    print("-----------------------------------------")
                    print("PROGRAM       : %s" % os.path.realpath(__file__))
                    print("PROGRAM ROOT  : %s" % os.path.split(os.path.realpath(__file__))[0])
                    print("PROGRAM FILE  : %s" % os.path.split(os.path.realpath(__file__))[1])
                    print("-----------------------------------------")
                    print("CONFIGURE     : %s" % (pymakeini))
                    print("CONFIGURE ROOT: %s" % (pymakeroot))
                    print("CONFIGURE FILE: %s" % (os.path.split(os.path.realpath(pymakeini))[1]))
                    print("-----------------------------------------")
                    print("PORT INI      : %s" % portinifile)
                    print("PORT INI ROOT : %s" % os.path.split(os.path.realpath(portinifile))[0])
                    print("PORT INI CONF : %s" % os.path.split(os.path.realpath(portinifile))[1])
                    return
                elif (args['settings'] is True):
                    #print(args['-l'], args['--local'])
                    #print(args['-c'], args['--custom'])
                    #print(args['-s'], args['--system'])
                    #print(args['--envname'], args['<env-name>'])
                    #return

                    if (args['-s'] or args['--system'] is True):
                        dict0 = copy.deepcopy(pymakesystemenviron)
                        print(Fore.CYAN + "system env")
                        print(Fore.MAGENTA + "path+:")
                        for (key) in dict0["PATH"].split(os.path.pathsep):
                            print(Fore.MAGENTA + "  %s" % key)
                        print(Fore.MAGENTA + "variable:")
                        for (key, value) in dict0.items():
                            if (key == 'path+'):
                                continue
                            if (str(key).lower() == 'path'):
                                continue

                            print(Fore.GREEN + "  %-30s %s" % (key, value))
                        return

                    elif (args['-l'] or args['--local'] is True):
                        if (int(localswitch) == 0):
                            print("local env is closed manually.")
                            return

                        dict0 = copy.deepcopy(localenv)
                        print(Fore.CYAN + "local env")
                        print(Fore.MAGENTA + "path+:")
                        for (key) in dict0["path+"]:
                            print(Fore.MAGENTA + "  %s" % key)
                        print(Fore.MAGENTA + "variable:")
                        for (key, value) in dict0.items():
                            if (key == 'path+'):
                                continue
                            print(Fore.GREEN + "  %-30s %s" % (key, value))
                        return

                    elif (args['-c'] or args['--custom'] is True):
                        if (int(switch0) == 0):
                            print("custom env is closed.")
                            return

                        print(Fore.CYAN + "custom env")
                        print(Fore.MAGENTA + "path+:")
                        for (key) in envcustomlistrawpaths:
                            print(Fore.MAGENTA + "  %s" % key)
                        print(Fore.MAGENTA + "variable:")
                        for (key, value) in envcustomlistrawvars.items():
                            if (key == 'path+'):
                                continue
                            print(Fore.GREEN + "  %-30s %s" % (key, value))
                        return

                    elif (args['--current'] is True):
                        current_env = rawconfig['environ']['current']
                        if (rawconfig['environ'].__contains__(current_env) is False):
                            print("please ensure the environ is right")
                            return

                        dict0 = copy.deepcopy(rawconfig['environ'][current_env])
                        print(Fore.CYAN + "env %s" % current_env)
                        print(Fore.LIGHTGREEN_EX + "path+:")
                        for (key) in dict0["path+"]:
                            print(Fore.LIGHTMAGENTA_EX + "  %s" % key)
                        print(Fore.LIGHTGREEN_EX + "variable:")
                        for (key, value) in dict0.items():
                            if (key == 'path+'):
                                continue
                            print(Fore.GREEN + "  %-30s %s" % (key, value))
                        return

                    elif (args['--envname'] is not None):
                        current_var = args['--envname']
                        if(current_var is None):
                            current_var = rawconfig['environ']['current']
                            for key in rawconfig['environ'].keys():
                                if (key == 'current'):
                                    continue
                                if (key == current_var):
                                    print(Fore.CYAN + "%s" % current_var)
                                    continue
                                print("%s" % key)
                            return

                        if (current_var == "current"):
                            current_var = rawconfig['environ']['current']
                        if (rawconfig['environ'].__contains__(current_var) is False):
                            print("please ensure the environ is right")
                            return

                        dict0 = copy.deepcopy(rawconfig['environ'][current_var])
                        print(Fore.CYAN + "env %s" % current_var)
                        print(Fore.LIGHTGREEN_EX + "path+:")
                        for (key) in dict0["path+"]:
                            print(Fore.LIGHTMAGENTA_EX + "  %s" % key)
                        print(Fore.LIGHTGREEN_EX + "variable:")
                        for (key, value) in dict0.items():
                            if (key == 'path+'):
                                continue
                            print(Fore.GREEN + "  %-30s %s" % (key, value))
                        return

                    else:
                        ''

                    #print('break to display backward.')
                    #important break [ + get all settings ]
                    break

                else:
                    if(config.__contains__("environ") is True):
                        if (config['environ'].__contains__("current") is True):
                            print("CURRENT ENVIRON %s" % (config["environ"]["current"]))
                        else:
                            print("CURRENT ENVIRON failed: .json file is broken, environ section lost current key, please use set command fix it.")
                    else:
                        print("CURRENT ENVIRON failed: please check your .json file content, it is not compatible version .json.")

                    r = conf.get('source', 'root')
                    f = conf.get('source', 'config')
                    print("SOURCE        : %s%s%s" % (r, os.path.sep, f))
                    print("SOURCE ROOT   : %s" % (r))
                    print("SOURCE CONFIG : %s" % (f))
                    print("-----------------------------------------")
                    print("PROGRAM       : %s" % os.path.realpath(__file__))
                    print("PROGRAM ROOT  : %s" % os.path.split(os.path.realpath(__file__))[0])
                    print("PROGRAM FILE  : %s" % os.path.split(os.path.realpath(__file__))[1])
                    print("-----------------------------------------")
                    print("CONFIGURE     : %s" % (pymakeini))
                    print("CONFIGURE ROOT: %s" % (pymakeroot))
                    print("CONFIGURE FILE: %s" % (os.path.split(os.path.realpath(pymakeini))[1]))
                    print("-----------------------------------------")
                    print("PORT INI      : %s" % portinifile)
                    print("PORT INI ROOT : %s" % os.path.split(os.path.realpath(portinifile))[0])
                    print("PORT INI CONF : %s" % os.path.split(os.path.realpath(portinifile))[1])
                    print("-----------------------------------------")
                    print("EXECUTE ROOT [HERE    ]: %s" % pymakeworkpath)
                    print("EXECUTE ROOT [THERE   ]: %s" % customshellroot)
                    print("EXECUTE ROOT [DEFAULT ]: %s" % pymakeshellroot)
                    print("EXECUTE ROOT [TYPE    ]: %s" % workroottype)
                    print("EXECUTE ROOT [STARTING]: %s" % shellroot)
                    print("-----------------------------------------")
                    plat = getplatform()
                    if (plat == "Windows"):
                        print("INSTALL ROOT  : %s" % "C:\Windows")
                    else:
                        print("INSTALL ROOT  : %s" % "/usr/local/bin")
                    return
            elif (args['env'] is True):
                #if (args['default'] or args['current'] or args['cur'] is True):
                #else:
                #    ""
                if (config['environ'].__contains__("current") is True):
                    print("%s" % (config["environ"]["current"]))
                    return
                else:
                    print("failed: .json file is broken, environ section lost current key, please use set command fix it.")
                    return
                #import return [ - env command ]
                return
            else:
                ''
        else:
            ''
        break

    # get
    while (True):
        if (args['get'] is True):
            if (args['all'] is True):
                if (args['settings'] is True):
                    list_config = config
                    if (args['--raw'] is True):
                        list_config = rawconfig

                    if (args['env'] == True):
                        env = os.environ
                        if (args['<name>'] is not None):
                            current_var = args['<name>']
                            if (current_var == "current"):
                                current_var = list_config['environ']['current']
                            if (list_config['environ'].__contains__(current_var) is False):
                                print("please ensure the environ is right")
                                return
                            dict0 = copy.deepcopy(list_config['environ'][current_var])
                            print(Fore.CYAN + "env %s" % current_var)
                            print(Fore.MAGENTA + "path+:")
                            for (key) in dict0["path+"]:
                                print(Fore.MAGENTA + "  %s" % key)
                            if (args['-a'] or args['--all'] is True):
                                for path in env["PATH"].split(os.path.pathsep):
                                    print(Fore.MAGENTA + "  %s" % path)
                            print(Fore.MAGENTA + "variable:")
                            for (key, value) in dict0.items():
                                if (key == 'path+'):
                                    continue
                                print(Fore.GREEN + "  %-30s %s" % (key, value))
                            if (args['-a'] or args['--all'] is True):
                                for (key, value) in env.items():
                                    if (key == 'PATH'):
                                        continue
                                    print(Fore.GREEN + "  %-30s %s" % (key, value))
                            return

                        for current_var in list_config['environ'].keys():
                            if (current_var == "current"):
                                continue
                            dict0 = copy.deepcopy(list_config['environ'][current_var])
                            print(Fore.RESET + "env %s" % current_var)
                            print(Fore.MAGENTA + "path+:")
                            for (key) in dict0["path+"]:
                                print(Fore.MAGENTA + "  %s" % key)
                            if (args['-a'] or args['--all'] is True):
                                for path in env["PATH"].split(os.path.pathsep):
                                    print(Fore.MAGENTA + "  %s" % path)
                            print(Fore.MAGENTA + "variable:")
                            for (key, value) in dict0.items():
                                if (key == 'path+'):
                                    continue
                                print(Fore.GREEN + "  %-30s %s" % (key, value))
                            if (args['-a'] or args['--all'] is True):
                                for (key, value) in env.items():
                                    if (key == 'PATH'):
                                        continue
                                    print(Fore.GREEN + "  %-30s %s" % (key, value))
                        return
                    elif (args['cmd'] == True):
                        dict0 = copy.deepcopy(list_config['command'])
                        if (args['<name>'] is not None):
                            # print(Fore.CYAN + "group: %s" % args['<name>'])
                            if (dict0.__contains__(args['<name>']) is False):
                                print("there is no this cmd in command group.")
                                return
                            value = dict0[args['<name>']]
                            step = 1
                            for cmd in value:
                                print(Fore.RED + "%-3s %s" % (step, cmd))
                                step += 1
                            return
                        else:
                            for (key, value) in dict0.items():
                                if (args['-a'] is not True and args['--all'] is not True):
                                    print(Fore.CYAN + "%s" % key)
                                    continue
                                print(Fore.CYAN + "group: %s" % key)
                                step = 1
                                for cmd in value:
                                    print(Fore.RED + "%-3s %s" % (step, cmd))
                                    step += 1
                            return
                    else:
                        ''
                else:
                    ''
            else:
                ''
        else:
            ''
        break

    # env environ
    while (True):
        if (args['environ'] or args['env'] is True):

            list_config = config
            if ( args['--raw'] is True ):
                list_config = rawconfig

            env = os.environ

            current_var = args['<name>']
            if(args['<name>'] is None):
                current_var = list_config['environ']['current']
            elif (args['<name>'] is not None):
                current_var = args['<name>']
                if(current_var == "current"):
                    current_var = list_config['environ']['current']
                if (list_config['environ'].__contains__(current_var) is False):
                    print("please ensure the environ is right")
                    return

            dict0 = copy.deepcopy(list_config['environ'][current_var])

            if( args['-p'] or args['--path'] is True):
                print (Fore.CYAN+ "env %s" % current_var)
                print(Fore.LIGHTGREEN_EX + "path+:")
                for (key) in dict0["path+"]:
                    print(Fore.LIGHTMAGENTA_EX + "  %s" % key)
                if(args['-a'] or args['--all'] is True):
                    for path in env["PATH"].split(os.path.pathsep):
                        print(Fore.LIGHTMAGENTA_EX + "  %s" % path)

            elif (args['-v'] or args['--var'] is True):
                print (Fore.CYAN+ "env %s" % current_var)
                print(Fore.LIGHTGREEN_EX + "variable:")
                for (key, value) in dict0.items():
                    if (key == 'path+'):
                        continue
                    print(Fore.GREEN + "  %-30s %s" % (key, value))
                if (args['-a'] or args['--all'] is True):
                    for (key, value) in env.items():
                        if (key == 'PATH'):
                            continue
                        print(Fore.GREEN + "  %-30s %s" % (key, value))

            elif (args['<name>'] is not None):
                print (Fore.CYAN+ "env %s" % current_var)
                print(Fore.LIGHTGREEN_EX + "path+:")
                for (key) in dict0["path+"]:
                    print(Fore.LIGHTMAGENTA_EX + "  %s" % key)
                if(args['-a'] or args['--all'] is True):
                    for path in env["PATH"].split(os.path.pathsep):
                        print(Fore.LIGHTMAGENTA_EX + "  %s" % path)
                print(Fore.LIGHTGREEN_EX + "variable:")
                for (key, value) in dict0.items():
                    if (key == 'path+'):
                        continue
                    print(Fore.GREEN + "  %-30s %s" % (key, value))
                if (args['-a'] or args['--all'] is True):
                    for (key, value) in env.items():
                        if (key == 'PATH'):
                            continue
                        print(Fore.GREEN + "  %-30s %s" % (key, value))

            else:
                current_var = rawconfig['environ']['current']
                print(Fore.CYAN + "%s" % current_var)
                for key in rawconfig['environ'].keys() :
                    if(key == 'current'):
                        continue
                    if(key == current_var):
                        continue
                    print("%s" % key)
            return
        else:
            ''
        break

    # cmd_type function
    def cmd_type (cmd_name = None, file_name = None, env_name = None):
        if (cmd_name is None):
            for (key, value) in rawconfig['command'].items():
                print(Fore.CYAN + "%s" % key)
            return ""

        if (rawconfig['command'].__contains__(cmd_name) is False):
            print("please check your command name")
            return ""

        if(env_name is None or env_name == rawconfig['environ']['current']):
            list0 = copy.deepcopy(rawconfig['command'][cmd_name])
        else:
            list0 = copy.deepcopy(raw_command(env_name)[cmd_name])

        #for cmd in list0:
        #    print(Fore.RED + "%s" % (cmd))

        temp_file_name = ""
        if (file_name is None):
            temp_file_name = "cmd"
        else:
            temp_file_name = file_name

        if (getplatform() == "Windows"):
            cmd_header = "@echo off"
            cmd_suffix = "_exec.bat"
        else:
            cmd_header = "#!/usr/bin/env bash"
            cmd_suffix = "_exec.sh"

        cmd_exec = temp_file_name + cmd_suffix
        with open(cmd_exec, 'w', encoding=cmd_codec) as f:
            cmd = ''
            #add shebang line
            if(list(list0).__len__()>0):
                cmd = list0[0]
            #print(".....")
            if(getplatform() == "Windows"):
                if (cmd.startswith('@echo') is False):
                    f.write(cmd_header + cmd_return)
            else:
                if (cmd.startswith('#!') is False):
                    f.write(cmd_header + cmd_return)
            for cmd in list0:
                f.write(cmd + cmd_return)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_exec)

        return cmd_exec

    # use - see/ss/cmd
    while (True):
        if (args['use'] is True):
            if(args['<env-name>'] is None):
                print("please appoint a environ")
                return

            if(rawconfig['environ'].__contains__(args['<env-name>']) is False):
                print("please ensure the environ is right")
                return

            current_env = args['<env-name>']
            if(args['<env-name>'] == "current"):
                current_env = rawconfig['environ']['current']

            if (rawconfig['environ'].__contains__(current_env) is False):
                print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                return

            if (args['ss'] or args['see'] or args['cmd'] is True):
                local_command = config['command']
                if ( args['--raw'] is True ):
                    local_command = raw_command(current_env)

                if (args['<cmd-name>'] is None):
                    for (key, value) in local_command.items():
                        if (args['-a'] is not True and args['--all'] is not True):
                            print(Fore.CYAN + "%s" % key)
                            continue
                        print(Fore.CYAN + "group: %s" % key)
                        step = 1
                        for cmd in value:
                            print(Fore.RED + "%-3s %s" % (step, cmd))
                            step += 1
                    return

                if (args['<cmd-name>'] is not None):
                    if (local_command.__contains__(args['<cmd-name>']) is False):
                        print("please check your command name")
                        return
                    value = local_command[args['<cmd-name>']]
                    step = 1
                    for cmd in value:
                        if(args['-l'] or args['--linenumber'] is True):
                            print(Fore.RED + "%-3s %s" % (step, cmd))
                        else:
                            print(Fore.RED + "%s" % (cmd))
                        step += 1
                    return
        else:
            ""
        break

    # see ss cmd
    while (True):
        if (args['ss'] or args['see'] or args['cmd'] is True):
            list_config = config
            if ( args['--raw'] is True ):
                list_config = rawconfig

            if (args['<cmd-name>'] is None):
                for (key, value) in list_config['command'].items():
                    if (args['-a'] is not True and args['--all'] is not True):
                        print(Fore.CYAN + "%s" % key)
                        continue
                    print(Fore.CYAN + "group: %s" % key)
                    step = 1
                    for cmd in value:
                        print(Fore.RED + "%-3s %s" % (step, cmd))
                        step += 1
                return

            if (args['<cmd-name>'] is not None):
                if (list_config['command'].__contains__(args['<cmd-name>']) is False):
                    print("please check your command name")
                    return
                value = list_config['command'][args['<cmd-name>']]
                step = 1
                for cmd in value:
                    if (args['-l'] or args['--linenumber'] is True):
                        print(Fore.RED + "%-3s %s" % (step, cmd))
                    else:
                        print(Fore.RED + "%s" % (cmd))
                    step += 1
                return
        else:
            ""
        break

    # use env type command
    while (True):
        if (args['use'] is True):
            if(args['<env-name>'] is None):
                print("please appoint a environ")
                return

            if(rawconfig['environ'].__contains__(args['<env-name>']) is False):
                print("please ensure the environ is right")
                return

            current_env = args['<env-name>']
            if(args['<env-name>'] == "current"):
                current_env = rawconfig['environ']['current']

            if (rawconfig['environ'].__contains__(current_env) is False):
                print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                return

            if (args['type'] == True):
                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                if(args['<cmd-name>'] is None):
                    for (key, value) in rawconfig['command'].items():
                        print(Fore.CYAN + "%s" % key)
                    return

                if (rawconfig['command'].__contains__(args['<cmd-name>']) is False):
                    print("please check your command name")
                    return

                if (args['<file-name>'] is None):
                    if (current_env == rawconfig['environ']['current']):
                        list0 = copy.deepcopy(rawconfig['command'][args['<cmd-name>']])
                    else:
                        list0 = copy.deepcopy(raw_command(current_env)[args['<cmd-name>']])

                    for cmd in list0:
                       print(Fore.RED + "%s" % (cmd))
                    return

                cmd_exec = cmd_type(args['<cmd-name>'], args['<file-name>'], current_env )

                print("successed: use %s type %s to %s" % (current_env, args['<cmd-name>'], cmd_exec))
                return
            else:
                ""
        else:
            ""
        break

    # type
    while (True):
        if (args['type'] == True):
            if (args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)
            elif (args['there'] or args['tt'] is True):
                os.chdir(customshellroot)
            elif (args['default'] or args['dd'] is True):
                os.chdir(pymakeshellroot)

            if (args['<cmd-name>'] is None):
                for (key, value) in rawconfig['command'].items():
                    print(Fore.CYAN + "%s" % key)
                return

            if (rawconfig['command'].__contains__(args['<cmd-name>']) is False):
                print("please check your command name")
                return

            if (args['<file-name>'] is None):
                list0 = copy.deepcopy(rawconfig['command'][args['<cmd-name>']])
                for cmd in list0:
                    print(Fore.RED + "%s" % (cmd))
                return

            cmd_exec = cmd_type(args['<cmd-name>'], args['<file-name>'] )

            print("successed: type %s to %s" % (args['<cmd-name>'], cmd_exec))
            return

        else:
            ""
        break

    # export function
    def env_export (env_name = None, file_name = None):
        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name
        dict0 = copy.deepcopy(rawconfig['environ'][current_var])

        plat = getplatform()
        if (plat == "Windows"):
            cmd_suffix = ".bat"
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_return = "\n"
            cmd_header = "@echo off" + cmd_return
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash" + cmd_return
            env_set = 'export '

        #export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = file_name
        cmd_effect += '_effect' + cmd_suffix

        #export path
        lines = ""
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
            else:
                lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + cmd_return)
            else:
                lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        #export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = file_name
        cmd_unset += '_unset' + cmd_suffix

        #export unset path
        lines = ""
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

        #export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + cmd_return)
            else:
                lines += ('unset ' + key + cmd_return)
        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_effect)
            os.system("chmod +x " + cmd_unset)

        #return file name
        return current_var, cmd_effect, cmd_unset

    # export
    while (True):
        if (args['export'] == True):
            current_env = args['<env-name>']
            if(args['<env-name>'] is None):
                current_env = rawconfig['environ']['current']
                print(Fore.CYAN + "%s" % current_env)
                for key in rawconfig['environ'].keys() :
                    if(key == 'current'):
                        continue
                    if(key == current_env):
                        continue
                    print("%s" % key)
                return

            if(rawconfig['environ'].__contains__(current_env) is False):
                print("please ensure the environ is right")
                return

            if(args['<env-name>'] == "current"):
                current_env = rawconfig['environ']['current']

            if (rawconfig['environ'].__contains__(current_env) is False):
                print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                return

            if (args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)
            elif (args['there'] or args['tt'] is True):
                os.chdir(customshellroot)
            elif (args['default'] or args['dd'] is True):
                os.chdir(pymakeshellroot)

            current_var, cmd_effect, cmd_unset = env_export(current_env, args['<file-name>'])

            print("successed: export %s to %s %s" % (current_var, cmd_effect, cmd_unset))
            return
        else:
            ""
        break

    # get
    while (True):
        if (args['get'] is True):
            if (args['all'] is True):
                if (args['settings'] is True):

                    list_config = config
                    if (args['--raw'] is True):
                        list_config = rawconfig

                    if (args['path'] == True):
                        dict0 = copy.deepcopy(list_config['path-assemblage'])
                        if (args['<name>'] is not None):
                            if (dict0.__contains__(args['<name>']) is False):
                                print("there is no this path item in path assemblage.")
                                return
                            value = dict0[args['<name>']]
                            print(Fore.GREEN + "%s" % (value))
                        else:
                            for (k, v) in dict0.items():
                                print(Fore.MAGENTA + "%-24s %s" % (k, v))

                    elif (args['env'] == True):
                        env = os.environ
                        if (args['<name>'] is not None):
                            current_var = args['<name>']
                            if (current_var == "current"):
                                current_var = list_config['environ']['current']
                            if (list_config['environ'].__contains__(current_var) is False):
                                print("please ensure the environ is right")
                                return
                            dict0 = copy.deepcopy(list_config['environ'][current_var])
                            print(Fore.CYAN + "env %s" % current_var)
                            print(Fore.MAGENTA + "path+:")
                            for (key) in dict0["path+"]:
                                print(Fore.MAGENTA + "  %s" % key)
                            if (args['-a'] or args['--all'] is True):
                                for path in env["PATH"].split(os.path.pathsep):
                                    print(Fore.MAGENTA + "  %s" % path)
                            print(Fore.MAGENTA + "variable:")
                            for (key, value) in dict0.items():
                                if (key == 'path+'):
                                    continue
                                print(Fore.GREEN + "  %-30s %s" % (key, value))
                            if (args['-a'] or args['--all'] is True):
                                for (key, value) in env.items():
                                    if (key == 'PATH'):
                                        continue
                                    print(Fore.GREEN + "  %-30s %s" % (key, value))
                            return

                        for current_var in list_config['environ'].keys():
                            if (current_var == "current"):
                                continue
                            dict0 = copy.deepcopy(list_config['environ'][current_var])
                            print(Fore.RESET + "env %s" % current_var)
                            print(Fore.MAGENTA + "path+:")
                            for (key) in dict0["path+"]:
                                print(Fore.MAGENTA + "  %s" % key)
                            if (args['-a'] or args['--all'] is True):
                                for path in env["PATH"].split(os.path.pathsep):
                                    print(Fore.MAGENTA + "  %s" % path)
                            print(Fore.MAGENTA + "variable:")
                            for (key, value) in dict0.items():
                                if (key == 'path+'):
                                    continue
                                print(Fore.GREEN + "  %-30s %s" % (key, value))
                            if (args['-a'] or args['--all'] is True):
                                for (key, value) in env.items():
                                    if (key == 'PATH'):
                                        continue
                                    print(Fore.GREEN + "  %-30s %s" % (key, value))

                    else:
                        print(Fore.BLACK + "path-assemblage:")
                        for (k, v) in list_config['path-assemblage'].items():
                            print(Fore.MAGENTA + "%-24s %s" % (k, v))

                        print(Fore.BLACK + "environ:")
                        env = os.environ
                        for current_var in list_config['environ'].keys():
                            if (current_var == "current"):
                                continue

                            dict0 = copy.deepcopy(list_config['environ'][current_var])

                            print(Fore.RESET + "env %s" % current_var)
                            print(Fore.MAGENTA + "path+:")
                            for (key) in dict0["path+"]:
                                print(Fore.MAGENTA + "  %s" % key)
                            if (args['-a'] or args['--all'] is True):
                                for path in env["PATH"].split(os.path.pathsep):
                                    print(Fore.MAGENTA + "  %s" % path)
                            print(Fore.MAGENTA + "variable:")
                            for (key, value) in dict0.items():
                                if (key == 'path+'):
                                    continue
                                print(Fore.GREEN + "  %-30s %s" % (key, value))
                            if (args['-a'] or args['--all'] is True):
                                for (key, value) in env.items():
                                    if (key == 'PATH'):
                                        continue
                                    print(Fore.GREEN + "  %-30s %s" % (key, value))

                        print(Fore.BLACK + "command:")
                        current_var = args['<name>']
                        if (args['<name>'] is not None):
                            if (args['<name>'] == "current"):
                                current_var = list_config['environ']['current']

                            if (list_config['environ'].__contains__(current_var) is False):
                                print('please ensure your env name is right.')
                                return

                            local_command = list_config['command']
                            if (args['--raw'] is True):
                                local_command = raw_command(current_var)

                            dict0 = copy.deepcopy(local_command)
                        else:
                            dict0 = copy.deepcopy(list_config['command'])

                        for (key, value) in dict0.items():
                            print(Fore.CYAN + "cmd %s" % key)
                            step = 1
                            for cmd in value:
                                print(Fore.RED + "%-3s %s" % (step, cmd))
                                step += 1

                    return
                else:
                    ''
            else:
                ''
        else:
            ''
        break

    # .bat .sh, windows unix
    def createCmdList0(list0):

        cmd_list = []

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            cmd_list.append("call %s_effect.bat" % name)
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)

        for cmd in list0:
            cmd_list.append(cmd)

        # append exit 0
        cmd_list.append(cmd_exit)
        # print( cmd_list )

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + ' ' + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + ' ' + cmd_sep + ' ' + cmd_status)
        cmd_list.append(cmd_exit)

        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        # print (cmd_list)
        return cmd_list, name

    #.bat .sh, windows not compatibility, unix only [ignore]
    def createCmdList01(list0):

        cmd_list = []

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%errorlevel%"
            cmd_sep = '&'
            cmd_header = "@echo off"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            # window close echo, close promot
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call %s_effect.bat" % name + ' ' + cmd_sep + ' ' + cmd_status)
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_exit = 'exit $?'
            cmd_header = "#!/usr/bin/env bash"
            cmd_list.append("source %s_effect.sh" % name + ' ' + cmd_sep + ' ' + cmd_status)

        for cmd in list0:
            cmd_list.append(cmd + ' ' + cmd_sep + ' ' + cmd_status)

        # append exit 0
        cmd_list.append(cmd_exit)
        # print( cmd_list )
        return cmd_list, name

    # use env exec command
    while (True):
        if (args['use'] is True):
            if(args['<env-name>'] is None):
                print("please appoint a environ")
                return

            if(rawconfig['environ'].__contains__(args['<env-name>']) is False):
                print("please ensure the environ is right")
                return

            current_env = args['<env-name>']
            if(args['<env-name>'] == "current"):
                current_env = rawconfig['environ']['current']

            if (current_env == 'current'
                or rawconfig['environ'].__contains__(current_env) is False):
                print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                return

            if (args['cc'] or args['exec'] is True):
                if(args['<command-names>'] == []):
                    print("please appoint your commands")
                    return

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                # create cmd_list
                current_var = current_env
                local_command = raw_command(current_var)

                dict0 = copy.deepcopy(local_command)
                list0 = []
                for current_var in args['<command-names>']:
                    if (current_var in dict0):
                        list0.extend(dict0[current_var])
                    else:
                        cmd = current_var
                        env_name = current_env
                        if (str(cmd).__contains__(' ')):
                            pycmd = which_command(env_name, str(cmd))
                            # print(pycmd)
                            if (pycmd is not None and os.path.isfile(pycmd)):
                                list0.append('"' + cmd + '"')
                            else:
                                list0.append(cmd)
                        else:
                            list0.append(cmd)

                cmd_list = []
                temp_file_name = ""
                #if(getplatform()=="Windows"):
                #    cmd_list, temp_file_name = createCmdList0(list0)
                #else:
                #    cmd_list, temp_file_name = createCmdList01(list0)
                # good compatibility
                cmd_list, temp_file_name = createCmdList0(list0)

                # export env
                current_var = current_env
                #print (current_var, temp_file_name)
                env_export(current_var, temp_file_name)

                ret = communicateWithCommandLine(cmd_list)

                # delete env file and cmd file
                if(getplatform()=="Windows"):
                    temp_file = temp_file_name + "_exec.bat"
                    if(os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.bat"
                    if(os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.bat"
                    if(os.path.exists(temp_file)):
                        os.remove(temp_file)
                else :
                    temp_file = temp_file_name + "_exec.sh"
                    if(os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.sh"
                    if(os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.sh"
                    if(os.path.exists(temp_file)):
                        os.remove(temp_file)

                os._exit(ret)
                return
        else :
            ""
        break

    # cc exec
    while (True):
        if (args['cc'] or args['exec'] is True):
            if (args['<command-names>'] == []):
                print("please appoint your commands")
                return

            current_env = rawconfig['environ']['current']
            if (current_env == 'current'
                or rawconfig['environ'].__contains__(current_env) is False):
                print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                return

            if (args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)
            elif (args['there'] or args['tt'] is True):
                os.chdir(customshellroot)
            elif (args['default'] or args['dd'] is True):
                os.chdir(pymakeshellroot)

            #print ("group %s" % current_vars)
            dict0 = copy.deepcopy(rawconfig['command'])

            list0 = []
            for current_var in args['<command-names>']:
                if (current_var in dict0):
                    list0.extend(dict0[current_var])
                else:
                    cmd = current_var
                    env_name = current_env
                    if (str(cmd).__contains__(' ')):
                        pycmd = which_command(env_name, str(cmd))
                        # print(pycmd)
                        if (pycmd is not None and os.path.isfile(pycmd)):
                            list0.append('"' + cmd + '"')
                        else:
                            list0.append(cmd)
                    else:
                        list0.append(cmd)

            cmd_list = []
            temp_file_name = ""
            #if(getplatform()=="Windows"):
            #    cmd_list, temp_file_name = createCmdList0(list0)
            #else:
            #    cmd_list, temp_file_name = createCmdList01(list0)
            # good compatibility
            cmd_list, temp_file_name = createCmdList0(list0)

            current_var = rawconfig['environ']['current']
            env_export(current_var, temp_file_name)

            ret = communicateWithCommandLine(cmd_list)

            # delete env file and cmd file
            if(getplatform()=="Windows"):
                temp_file = temp_file_name + "_exec.bat"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = temp_file_name + "_effect.bat"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = temp_file_name + "_unset.bat"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
            else :
                temp_file = temp_file_name + "_exec.sh"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = temp_file_name + "_effect.sh"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = temp_file_name + "_unset.sh"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)

            os._exit(ret)
            return
        else:
            ""
        break

    #.bat .sh, windows, unix
    def createCmdList02(env_name = None, local = True, list0 = [], params0 = []):

        cmd_list = []

        if(env_name is None):
            env_name = rawconfig['environ']['current']
        #print(env_name)

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            cmd_call = "call "
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            cmd_list.append("call %s_effect.bat" % name)
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)

        #print(params0)
        params_string = ""
        for param in params0:
            #print(param)
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        if ( local is True):
            for cmd in list0:
                cmd_list.append(cmd)
        else:
            for cmd in list0:
                if(str(cmd).__contains__(' ')):
                    pycmd = which_command(env_name, str(cmd))
                    #print(str(cmd))
                    #print(Fore.RED + "which command:", pycmd)
                    if(pycmd is not None and os.path.isfile(pycmd)):
                        cmd_list.append('"' + cmd + '"' + ' ' + params_string)
                    else:
                        cmd_list.append(cmd + ' ' + params_string)
                else:
                    cmd_list.append(cmd + ' ' + params_string)

        # append exit 0
        cmd_list.append(cmd_exit)
        #print( cmd_list )

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        #print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("call " + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("./" + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)

        cmd_list.append(cmd_exit)

        # print (cmd_list)
        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        return cmd_list, name

    # use env exec-with-params/execvp/ccvp command
    while (True):
        if (args['use'] is True):
            if (args['<env-name>'] is None):
                print("please appoint a environ")
                return

            if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                print("please ensure the environ is right")
                return

            current_env = args['<env-name>']
            if (args['<env-name>'] == "current"):
                current_env = rawconfig['environ']['current']

            if (current_env == 'current'
                or rawconfig['environ'].__contains__(current_env) is False):
                print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                return

            if (args['exec-with-params'] or args['execvp'] or args['ccvp'] is True):

                if (args['<command-name>'] is None):
                    print("please appoint your command")
                    return

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)
                elif (args['there'] or args['tt'] is True):
                    os.chdir(customshellroot)
                elif (args['default'] or args['dd'] is True):
                    os.chdir(pymakeshellroot)

                # print(args['--workroot'])
                if (args['--workroot'] is not None):
                    if (os.path.isdir(args['--workroot'])
                        and os.path.isabs(args['--workroot'])):
                        os.chdir(args['--workroot'])
                    else:
                        print('please input a legal work root.')
                        return

                #print(localenv['PYMAKEWORKROOT'])
                #print(os.getcwd())

                # create cmd_list
                current_var = current_env
                local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                list0 = []
                local = True
                current_var = args['<command-name>']
                if (current_var in dict0):
                    list0.extend(dict0[current_var])
                    local = True
                else:
                    list0.append(current_var)
                    local = False

                params0 = []
                # print(args['--params'])
                # print(args['<command-params>'])
                for current_var in args['--params']:
                    params0.append(current_var)
                for current_var in args['<command-params>']:
                    params0.append(current_var)

                cmd_list = []
                temp_file_name = ""
                # if (getplatform() == "Windows"):
                #    cmd_list, temp_file_name = createCmdList0(list0)
                # else:
                #    cmd_list, temp_file_name = createCmdList01(list0)
                # good compatibility
                cmd_list, temp_file_name = createCmdList02(current_env, local, list0, params0)

                # export env
                current_var = current_env
                # print (current_var, temp_file_name)
                env_export(current_var, temp_file_name)

                ret = communicateWithCommandLine(cmd_list)

                # delete env file and cmd file
                if (getplatform() == "Windows"):
                    temp_file = temp_file_name + "_exec.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.bat"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                else:
                    temp_file = temp_file_name + "_exec.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.sh"
                    if (os.path.exists(temp_file)):
                        os.remove(temp_file)

                os._exit(ret)
                return
        else:
            ''
        break

    # exec-with-params ccvp execvp
    while (True):
        if (args['exec-with-params'] or args['execvp'] or args['ccvp'] is True):
            #print(args)
            if (args['<command-name>'] is None):
                print("please appoint your command")
                return

            current_env = rawconfig['environ']['current']
            if (current_env == 'current'
                or rawconfig['environ'].__contains__(current_env) is False):
                print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                return

            #print(args['here'])
            #print(args['hh'])
            if (args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)
            elif (args['there'] or args['tt'] is True):
                os.chdir(customshellroot)
            elif (args['default'] or args['dd'] is True):
                os.chdir(pymakeshellroot)

            #print(args['--workroot'])
            if(args['--workroot'] is not None):
                if(os.path.isdir(args['--workroot'])
                   and os.path.isabs(args['--workroot'])):
                    os.chdir(args['--workroot'])
                else:
                    print('please input a legal work root.')
                    return

            #print ("group %s" % current_vars)
            dict0 = copy.deepcopy(rawconfig['command'])

            list0 = []
            local = True
            current_var = args['<command-name>']
            if (current_var in dict0):
                list0.extend(dict0[current_var])
                local = True
            else:
                list0.append(current_var)
                local = False

            params0 = []
            #print(args['<command-name>'])
            #print(args['--params'])
            #print(args['<command-params>'])
            for current_var in args['--params']:
                params0.append(current_var)
            for current_var in args['<command-params>']:
                params0.append(current_var)

            cmd_list = []
            temp_file_name = ""
            # if (getplatform() == "Windows"):
            #    cmd_list, temp_file_name = createCmdList0(list0)
            # else:
            #    cmd_list, temp_file_name = createCmdList01(list0)
            # good compatibility
            cmd_list, temp_file_name = createCmdList02(current_env, local, list0, params0)

            current_var = rawconfig['environ']['current']
            env_export(current_var, temp_file_name)

            ret = communicateWithCommandLine(cmd_list)

            # delete env file and cmd file
            if(getplatform()=="Windows"):
                temp_file = temp_file_name + "_exec.bat"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = temp_file_name + "_effect.bat"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = temp_file_name + "_unset.bat"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
            else :
                temp_file = temp_file_name + "_exec.sh"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = temp_file_name + "_effect.sh"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = temp_file_name + "_unset.sh"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)

            os._exit(ret)
            return
        else:
            ""
        break

    # here [False]
    while (False):
        if (args['here'] or args['hh'] is True):
            os.chdir(pymakeworkpath)

            if (args['clean'] == True):
                plat = getplatform()
                if (plat == "Windows"):
                    os.system("@del /f /q *_effect.bat *_unset.bat *_exec.bat")
                else:
                    os.system("rm -f *_effect.sh *_unset.sh *_exec.sh")
                return

            if (args['export'] == True):
                current_env = args['<env-name>']
                if (args['<env-name>'] is None):
                    current_env = rawconfig['environ']['current']

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print("please ensure the environ is right")
                    return

                if (args['<env-name>'] == "current"):
                    current_env = rawconfig['environ']['current']

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                    return

                current_var, cmd_effect, cmd_unset = env_export(current_env, args['<file-name>'])
                print("successed: export %s to %s %s" % (current_var, cmd_effect, cmd_unset))
                return

            if (args['type'] == True):
                if (args['<cmd-name>'] is None):
                    for (key, value) in rawconfig['command'].items():
                        print(Fore.CYAN + "%s" % key)
                    return

                if (rawconfig['command'].__contains__(args['<cmd-name>']) is False):
                    print("please check your command name")
                    return

                cmd_exec = cmd_type(args['<cmd-name>'], args['<file-name>'])

                print("successed: type %s to %s" % (args['<cmd-name>'], cmd_exec))
                return

        else:
            ""
        break

    # there [False]
    while (False):
        if (args['there'] or args['tt'] is True):
            os.chdir(customshellroot)

            if (args['clean'] == True):
                plat = getplatform()
                if (plat == "Windows"):
                    os.system("@del /f /q *_effect.bat *_unset.bat *_exec.bat")
                else:
                    os.system("rm -f *_effect.sh *_unset.sh *_exec.sh")
                return

            if (args['export'] == True):
                current_env = args['<env-name>']
                if (args['<env-name>'] is None):
                    current_env = rawconfig['environ']['current']

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print("please ensure the environ is right")
                    return

                if (args['<env-name>'] == "current"):
                    current_env = rawconfig['environ']['current']

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                    return

                current_var, cmd_effect, cmd_unset = env_export(current_env, args['<file-name>'])
                print("successed: export %s to %s %s" % (current_var, cmd_effect, cmd_unset))
                return

            if (args['type'] == True):
                if (args['<cmd-name>'] is None):
                    for (key, value) in rawconfig['command'].items():
                        print(Fore.CYAN + "%s" % key)
                    return

                if (rawconfig['command'].__contains__(args['<cmd-name>']) is False):
                    print("please check your command name")
                    return

                cmd_exec = cmd_type(args['<cmd-name>'], args['<file-name>'])

                print("successed: type %s to %s" % (args['<cmd-name>'], cmd_exec))
                return

        else:
            ""
        break

    # default [False]
    while (False):
        if (args['default'] or args['dd'] is True):
            os.chdir(pymakeshellroot)

            if (args['clean'] == True):
                plat = getplatform()
                if (plat == "Windows"):
                    os.system("@del /f /q *_effect.bat *_unset.bat *_exec.bat")
                else:
                    os.system("rm -f *_effect.sh *_unset.sh *_exec.sh")
                return

            if (args['export'] == True):
                current_env = args['<env-name>']
                if (args['<env-name>'] is None):
                    current_env = rawconfig['environ']['current']

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print("please ensure the environ is right")
                    return

                if (args['<env-name>'] == "current"):
                    current_env = rawconfig['environ']['current']

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                    return

                current_var, cmd_effect, cmd_unset = env_export(current_env, args['<file-name>'])
                print("successed: export %s to %s %s" % (current_var, cmd_effect, cmd_unset))
                return

            if (args['type'] == True):
                if (args['<cmd-name>'] is None):
                    for (key, value) in rawconfig['command'].items():
                        print(Fore.CYAN + "%s" % key)
                    return

                if (rawconfig['command'].__contains__(args['<cmd-name>']) is False):
                    print("please check your command name")
                    return

                cmd_exec = cmd_type(args['<cmd-name>'], args['<file-name>'])

                print("successed: type %s to %s" % (args['<cmd-name>'], cmd_exec))
                return

        else:
            ""
        break

    return

if __name__ == '__main__':
    ret = main_function()
    if(ret == None):
        ret = 0
    os._exit(ret)
