---
title: Java and Pythoninstallation
layout: utils
permalink: /utils/installation
---
# Java Installation

## Java on Mac OS X

1. **Descargar el JDK**:
    - Ve a la página [AdoptOpenJDK](https://adoptopenjdk.net/).
    - Descarga el instalador para macOS.

2. **Instalar el JDK**:
    - Abre el archivo `.dmg` o `.pkg` descargado y sigue las instrucciones de instalación.

3. **Configurar el entorno**:
    - Abre una terminal.
    - Verifica la versión instalada:
      ```sh
      java -version
      ```
    - Si no se reconoce, es posible que necesites configurar la variable de entorno `JAVA_HOME`. Añade lo siguiente a tu `~/.zshrc` o `~/.bash_profile` (dependiendo de tu shell):
      ```sh
      export JAVA_HOME=$(/usr/libexec/java_home)
      export PATH=$JAVA_HOME/bin:$PATH
      ```
    - Recarga tu perfil:
      ```sh
      source ~/.zshrc
      ```

## Java on Windows


### Paso 1: Descargar e Instalar Java 22

1. **Descargar el JDK**:
    - Ve a la [página de descarga de Oracle JDK](https://www.oracle.com/java/technologies/javase-jdk22-downloads.html) o una fuente alternativa como [AdoptOpenJDK](https://adoptopenjdk.net/).
    - Descarga el instalador para Windows.

2. **Instalar el JDK**:
    - Abre el archivo `.exe` descargado y sigue las instrucciones del instalador.
    - Durante la instalación, toma nota del directorio de instalación (por ejemplo, `C:\Program Files\Java\jdk-22`).

### Paso 2: Configurar Variables de Entorno

1. **Configurar la variable `JAVA_HOME`**:
    - Abre el Panel de Control y ve a **Sistema y Seguridad** > **Sistema** > **Configuración avanzada del sistema**.
    - En la ventana de **Propiedades del sistema**, haz clic en **Variables de entorno**.
    - En la sección **Variables del sistema**, haz clic en **Nuevo...** y crea una nueva variable con el nombre `JAVA_HOME` y el valor del directorio de instalación del JDK (por ejemplo, `C:\Program Files\Java\jdk-22`).

2. **Agregar `JAVA_HOME` al `PATH`**:
    - En la sección **Variables del sistema**, encuentra la variable `Path` y selecciónala. Luego, haz clic en **Editar...**.
    - En la ventana de **Editar variable de entorno**, haz clic en **Nuevo** e ingresa `%JAVA_HOME%\bin`.
    - Asegúrate de que esta entrada esté en la lista de rutas y haz clic en **Aceptar** en todas las ventanas abiertas para aplicar los cambios.

### Paso 3: Verificar la Instalación

1. **Abrir una ventana de comando**:
    - Presiona `Win + R`, escribe `cmd` y presiona Enter para abrir una ventana de comandos.

2. **Verificar la versión de Java**:
    - En la ventana de comandos, escribe:
      ```sh
      java -version
      ```
    - Deberías ver la versión de Java instalada, confirmando que Java 22 está correctamente configurado.

## Java on Linux

### Paso 1: Descargar e Instalar Java 22

1. **Descargar el JDK**:
    - Ve a la [página de descarga de Oracle JDK](https://www.oracle.com/java/technologies/javase-jdk22-downloads.html) o una fuente alternativa como [AdoptOpenJDK](https://adoptopenjdk.net/).
    - Descarga el tarball (`.tar.gz`) para Linux.

2. **Instalar el JDK**:
    - Abre una terminal y navega al directorio donde descargaste el archivo.
    - Extrae el tarball:
      ```sh
      tar -xzf jdk-22_linux-x64_bin.tar.gz
      ```
    - Mueve el JDK al directorio `/opt`:
      ```sh
      sudo mv jdk-22 /opt/
      ```

### Paso 2: Configurar Variables de Entorno

1. **Configurar la variable `JAVA_HOME`**:
    - Abre el archivo de configuración de tu shell (por ejemplo, `~/.bashrc` o `~/.zshrc`) en un editor de texto.
    - Añade las siguientes líneas al final del archivo:
      ```sh
      export JAVA_HOME=/opt/jdk-22
      export PATH=$JAVA_HOME/bin:$PATH
      ```
    - Guarda y cierra el archivo.
    - Recarga el archivo de configuración:
      ```sh
      source ~/.bashrc
      ```

### Paso 3: Verificar la Instalación

1. **Verificar la versión de Java**:
    - En la terminal, escribe:
      ```sh
      java -version
      ```
    - Deberías ver la versión de Java instalada, confirmando que Java 22 está correctamente configurado.


---
Crear y Ejecutar un Programa Simple "Hello World"

1. **Crear un archivo Java**:
    - Abre un editor de texto y escribe el siguiente código:
      ```java
      public class HelloWorld {
          public static void main(String[] args) {
              System.out.println("Hello, World!");
          }
      }
      ```
    - Guarda el archivo como `HelloWorld.java`.

2. **Compilar el archivo Java**:
    - Abre una terminal y navega al directorio donde guardaste `HelloWorld.java`.
    - Compila el archivo:
      ```sh
      javac HelloWorld.java
      ```

3. **Ejecutar el programa compilado**:
    - Ejecuta el programa:
      ```sh
      java HelloWorld
      ```

Deberías ver la salida:

```Hello, World!```

Esto confirma que Java 22 está correctamente instalado y funcionando en tu Mac.


--- 
# Python Installation

## Python on OS X

### Installing Homebrew
Homebrew is a package manager for OS X ( and Linux )
Open a terminal window by going to Launchpad -> Other -> Terminal. You can also press command-spacebar, type terminal, and then press enter. Then paste the following command in the terminal
```commandline
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
( Enter to https://brew.sh/ for more information about Homebrew )

After downloading and installing Homebrew with the previous command you can install python3 by writing the command
```commandline
brew install python3
```

Finally, you can check the python version installed with
```commandline
$ python3
Python 3.9.10 (main, Jan 15 2022, 11:48:00)
[Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

When you’ve seen this output, press ctrl-D or enter exit&#40;&#41; to leave the Python prompt and return to a terminal prompt.


## Python on Linux

Open a terminal window by running the Terminal application on your system &#40;in Ubuntu, you can press ctrl-alt-T&#41;. Then run the following commands
```commandline
sudo apt-get update
sudo apt-get install python3
```

Finally, you can check the python version installed with
```commandline
$ python3
Python 3.9.10 (main, Jan 15 2022, 11:48:00)
[Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

When you’ve seen this output, press ctrl-D or enter exit&#40;&#41; to leave the Python prompt and return to a terminal prompt.

[//]: # ()
[//]: # (This output means you also have Python 3 installed, so you’ll be)

[//]: # (able to use either version. Whenever you see the python command in this book, enter python3 instead. Most Linux distributions have Python already installed, but if for some reason yours didn’t or if your system came with Python 2 and you want to install Python 3, refer to Appendix A.)


## Python on Windows
Windows doesn’t always come with Python, so you’ll probably need to download and install it, and then download and install a text editor.

First, check whether Python is installed on your system. Open a command window by entering command into the Start menu or by holding down the shift key while right-clicking on your desktop and selecting Open command window here. In the terminal window, enter python in lowercase. If you get a Python prompt (>>>), Python is installed on your system. However, you’ll probably see an error message telling you that python is not a recognized command or the Microsoft Store application loading.
In that case, download a Python installer for Windows. Go to http://python.org/downloads/. Click the `Download Python 3.10.3` button, which should automatically start downloading the correct installer for your system. After you’ve downloaded the file, run the installer. Make sure you check the option Add Python to PATH, which will make it easier to config- ure your system correctly.

![img.png](windows.png)


Open a command window and enter python in lowercase. If you get a Python prompt (>>>), Windows has found the version of Python you just installed:
```commandline
C:\> py
Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

When you’ve seen this output, press ctrl-Z or enter exit&#40;&#41; to leave the Python prompt and return to a terminal prompt.

