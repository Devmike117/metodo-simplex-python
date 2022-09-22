<h1 align="center">• ─── ⋆⋅☆⋅⋆ ─── •</h1>
<h2 align="center">
  CALCULADORA DE MÉTODO SIMPLEX
</h2>
<h1 align="center">• ─── ⋆⋅☆⋅⋆ ─── •</h1>

## 📄 Resumen

<p align="justify">
  Programa que permite realizar ejercicios de programación lineal de maximización implementando el método simplex. Además, permite planificar proyectos en los que hace falta coordinar un gran número de actividades, gracias a la implementación de la metodología Pert.
  
  Desarrollado usando PyQt5, que es un binding de la librería Qt para el lenguaje de programación Python.
</p>

</div>

[![Build status (GitHub)](https://img.shields.io/github/workflow/status/JustArchiNET/ArchiSteamFarm/ASF-ci/main?label=GitHub&logo=github&cacheSeconds=600)](https://github.com/JustArchiNET/ArchiSteamFarm/actions?query=workflow%3AASF-ci+branch%3Amain)
[![Build status (Docker)](https://img.shields.io/github/workflow/status/JustArchiNET/ArchiSteamFarm/ASF-docker-publish-main.svg?label=Docker&logo=docker&cacheSeconds=600)](https://hub.docker.com/r/justarchi/archisteamfarm)
[![Github last commit date](https://img.shields.io/github/last-commit/JustArchiNET/ArchiSteamFarm.svg?label=Updated&logo=github&cacheSeconds=600)](https://github.com/JustArchiNET/ArchiSteamFarm/commits)
[![License](https://img.shields.io/github/license/JustArchiNET/ArchiSteamFarm.svg?label=License&logo=apache&cacheSeconds=2592000)](https://github.com/JustArchiNET/ArchiSteamFarm/blob/main/LICENSE.txt)

[![Steam group](https://img.shields.io/badge/Steam-group-yellowgreen.svg?logo=steam)](https://steamcommunity.com/groups/archiasf)
[![Discord](https://img.shields.io/discord/267292556709068800.svg?color=7289da&label=Discord&logo=discord&logoColor=white&cacheSeconds=3600)](https://discord.com/invite/uTGDBd2jgr)

[![Crypto donate](https://img.shields.io/badge/Crypto-donate-f7931a.svg?logo=bitcoin)](https://commerce.coinbase.com/checkout/0c23b844-c51b-45f4-9135-8db7c6fcf98e)
[![PayPal.me donate](https://img.shields.io/badge/PayPal.me-donate-00457c.svg?logo=paypal)](https://paypal.me/MikeeUwU?country.x=MX&locale.x=es_XC)
[![PayPal donate](https://img.shields.io/badge/PayPal-donate-00457c.svg?logo=paypal)]([https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=HD2P2P3WGS5Y4](https://paypal.me/MikeeUwU?country.x=MX&locale.x=es_XC))
[![Revolut donate](https://img.shields.io/badge/Revolut-donate-0075eb.svg?logo=revolut)](https://pay.revolut.com/justarchi)
[![Steam donate](https://img.shields.io/badge/Steam-donate-000000.svg?logo=steam)](https://steamcommunity.com/tradeoffer/new/?partner=1101291397&token=-pop0PGF)

---
## 📜 Uso del Programa
<h3>Simplex</h3>
<p align="justify">
  Tiene una intefaz sencilla, en la cual se deben ingresar la cantidad de variables y de restricciones que emplea el problema, 
  esto permite generar las el espacio para que el usuario ingrese su función objetivo y las diferentes restricciones. El software valida 
  que estos valores sean ya sea enteros o decimales, de lo contrario, si se ubica un caracter o se deja vacío, mostrará un mensaje de error.
  Una vez validado, se podrá generar la primer tabla y mostrar la función objetiva y restricciones con sus respectivas variables de holgura.
  Se pueden ir generando tablas tanto el ejercicio las permita, así mismo por cada tabla hay un botón que calcula su pivote, variable de entrada y de salida.
  Se puede retroceder de tabla, y al finalizar se mostrará el resultado y se habilitará el botón de imprimir.
</p>

<h3>Pert</h3>
<p align="justify">
  Una interfaz sencilla, debe ingresar la cantidad de actividades que se van a realizar, se desplegará una tabla, la cual se debe llenar con la descripción de las actividades, sus predecesores, y los respectivos tiempos optimistas, normal y pesimista. Además, tendrá las opciones de escoger los días que no va a laborar y un calendario para elegir la fecha de inicio del las actividades.
  Una vez ingrese los datos correctamente, se mostrará una nueva tabla con los resultados finales, donde se observan las fechas de inicio y final, la ruta crítica de actividades y un resumen del ejercio. Se activará el botón de guardar el cual permite generar un reporte de la tabla.
</p>

### 🔨 Ejecutable del programa

[Click aquí para descargar](https://github.com/Mike538/metodo-simplex-python/releases/download/untagged-c57ac8b258d920f57663/Calculadora.Simplex-Pert.exe)

<h1 align="left"><img src="https://i.pinimg.com/originals/5a/93/c2/5a93c26aca8989b11d6c40d953c5cc14.gif" width="200" height="200" /> </h1>
