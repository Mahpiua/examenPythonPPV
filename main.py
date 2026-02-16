from modelo.database import *
from vista.ventana_principal import ventana

# Se crean las tablas
crear_bd()

# Se inicializan los datos
iniciar_carga()



pantalla_principal = ventana

pantalla_principal.mainloop()