#!/bin/bash
# Удаляет старые ревизии привязок
# ЗАКРОЙТЕ ВСЕ ПРИВЯЗКИ ПЕРЕД ЗАПУСКОМ ЭТОГО СКРИПТА
set -eu
snap list --all | awk '/disabled/{print $1, $3}' |
    while read snapname revision; do
        snap remove "$snapname" --revision="$revision"
    done
