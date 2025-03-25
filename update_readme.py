import subprocess

# Obtener la canción actual con playerctl
try:
    var = subprocess.check_output(["playerctl", "metadata", "--format", "{{ artist }} - {{ title }}"], text=True).strip()
except subprocess.CalledProcessError:
    var = "No se está reproduciendo música"

# Leer el archivo y modificar solo la línea que empieza con '## Spotify:'
file_path = "/home/sx1ngth/Documentos/sx1ngthD4ck3r/README.md"
with open(file_path, "r") as file:
    lines = file.readlines()

with open(file_path, "w") as file:
    found = False
    for line in lines:
        if line.startswith("## Spotify:"):
            file.write(f"## Spotify: {var}\n")
            found = True
        else:
            file.write(line)
    
    # Si no se encontró la línea, agregarla al inicio
    if not found:
        file.seek(0, 0)
        file.write(f"## Spotify: {var}\n" + "".join(lines))

print("✅ Archivo actualizado con la canción actual.")
