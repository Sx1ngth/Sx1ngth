
#!/bin/bash

cancion_actual=""

while true; do
    nueva_cancion=$(playerctl metadata --format "{{ artist }} - {{ title }}" 2>/dev/null)

    if [[ "$nueva_cancion" != "$cancion_actual" && -n "$nueva_cancion" ]]; then

        
        python /home/sx1ngth/Documentos/sx1ngthD4ck3r/update_readme.py
        git add README.md && git commit -m "update" && git push origin main
        cancion_actual="$nueva_cancion"
    fi

    sleep 1  # Espera 1 segundo antes de verificar de nuevo
done





