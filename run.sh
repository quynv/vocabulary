#!/bin/sh

while true; do
	RESULT=$(python -c 'import jp; print(jp.get_vocabulary())')
	VIETNAMESE=${RESULT##*:}
	JAPANESE=${RESULT%%:*}
	if [ -z "$VIETNAMESE" ]; then
		continue
	fi
	osascript -e 'display notification "'"$VIETNAMESE"'" with title "'"$JAPANESE"'"'
	sleep 30m
done
exit