# 📦 Proyecto de Respaldo de Carpetas en Python

Este es un sencillo pero poderoso script en Python que permite **respaldar el contenido de una carpeta** en un archivo `.zip`, mostrando una **barra de progreso** durante el proceso y organizando los respaldos de forma ordenada.

---

## 🚀 Características

- ✅ Comprime cualquier carpeta en un archivo `.zip`.
- ✅ Muestra barra de progreso con `tqdm`.
- ✅ Evita incluir archivos bloqueados o con errores.
- ✅ Soporta archivos grandes (>2 GB) con `Zip64`.
- ✅ Protege contra respaldos dentro de la misma carpeta.
- ✅ Mensajes visuales claros y amigables.

2. Ingresa las rutas cuando se te solicite:
Ruta de la carpeta a respaldar.
Ruta donde deseas guardar el respaldo.
⚠️ Asegúrate de que la carpeta de destino no esté dentro de la carpeta que vas a respaldar.

📦 Requisitos
Python 3.8 o superior
Librería tqdm para la barra de progreso:
pip install tqdm

🧪 Ejemplo
📁 Ingresa la ruta de la carpeta que quieres respaldar: C:\MisDocumentos
📂 Ingresa la ruta donde deseas guardar el respaldo: D:\Respaldos
🔄 Creando respaldo: 100%|████████████████████████████| 250/250 archivos
✅ Respaldo completado con éxito en: D:\Respaldos\respaldos\respaldo_2025-04-03_20-15-42.zip

📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.

🤝 Contribuciones
¿Tienes ideas o mejoras? ¡Eres bienvenido a contribuir! Puedes hacer un fork del repositorio y enviar un pull request 🛠️.

👤 Autor
Juan Escobar
💻 Proyecto creado con cariño y café ☕