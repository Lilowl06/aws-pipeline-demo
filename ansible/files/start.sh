nohup node app.js > start.out 2>&1 &
echo $! > pid.txt #neregistrement du pid du dernier processus lancé par l'utilisateur courant 