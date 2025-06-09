```markdown
    # Repositorio de Evaluación de Competencias en Inteligencia Artificial

    <div align="center">
      </div>

    ¡Bienvenido/a al repositorio de evaluación de competencias en IA!

    Este proyecto ha sido diseñado para evaluar tus habilidades prácticas en áreas clave de la Inteligencia Artificial, adaptado a diferentes perfiles profesionales.

    ---

    ## 🎯 Propósito de la Evaluación

    El objetivo principal es que demuestres tu capacidad para resolver problemas prácticos utilizando Python y librerías de IA, así como tu comprensión de conceptos relevantes para tu perfil.

    > [!IMPORTANT]
    > La duración máxima para completar el caso de estudio asignado es de **2 horas**. Te recomendamos encarecidamente gestionar tu tiempo de manera eficiente. Si no logras completar todas las tareas, enfócate en la calidad y funcionalidad de lo que sí completes.

    ---

    ## 🚀 Guía Paso a Paso para el Evaluado

    Sigue estos pasos para comenzar y entregar tu solución:

    ### 1. Clonar el Repositorio

    Abre tu terminal y clona este repositorio en tu máquina local:

    ```bash
    git clone [https://github.com/tu-usuario/mi-repositorio-evaluacion-ia.git](https://github.com/tu-usuario/mi-repositorio-evaluacion-ia.git)
    cd mi-repositorio-evaluacion-ia
    ```
    *(**Nota:** Reemplaza `https://github.com/tu-usuario/mi-repositorio-evaluacion-ia.git` con la [enlace sospechoso eliminado](https://github.com/tu-usuario/mi-repositorio-evaluacion-ia) una vez que lo subas a GitHub).*

    ### 2. Configurar el Entorno Virtual e Instalar Dependencias

    Es **altamente recomendado** crear un entorno virtual para instalar las dependencias y evitar conflictos con otras instalaciones de Python en tu sistema. Luego, instala las librerías necesarias:

    <details>
      <summary><b>Pasos Detallados para la Configuración del Entorno</b></summary>

      Para crear y activar tu entorno virtual:

      ```bash
      # Crear el entorno virtual (solo la primera vez)
      python -m venv .venv

      # Activar el entorno virtual
      # En Linux/macOS:
      source .venv/bin/activate
      # En Windows (CMD):
      # .venv\Scripts\activate.bat
      # En Windows (PowerShell):
      # .venv\Scripts\Activate.ps1
      ```
      Una vez activado el entorno virtual, instala las librerías:
      ```bash
      pip install -r entorno/requirements.txt
      ```
      Puedes ver la lista completa de paquetes requeridos en [`entorno/requirements.txt`](entorno/requirements.txt).
    </details>

    ---

    ### 3. Elegir tu Perfil y Navegar al Caso de Estudio

    Este repositorio contiene casos de estudio específicos para diferentes perfiles de IA. Dirígete a la carpeta correspondiente a tu perfil asignado:

    | Perfil Asignado | Descripción | Carpeta de Acceso |
    |---|---|---|
    | **Programador Junior en Python** | Evalúa habilidades fundamentales de Python y conceptos básicos de IA. | [`perfiles/programador`](perfiles/programador) |
    | **Especialista en Datos** | Evalúa habilidades en análisis, manipulación de datos y Machine Learning. | [`perfiles/especialista_datos`](perfiles/especialista_datos) |
    | **Especialista en IA Generativa** | Evalúa conocimientos y habilidades en modelos de IA generativa (LLMs, etc.). | [`perfiles/especialista_ia_generativa`](perfiles/especialista_ia_generativa) |

    Una vez dentro de tu carpeta de perfil, **lee cuidadosamente el `README.md` específico** de ese perfil. Contendrá las instrucciones detalladas de tu caso de estudio, los objetivos específicos y los criterios de evaluación.

    ---

    ### 4. Desarrollar tu Solución

    Trabaja en los archivos del caso de estudio según las indicaciones del `README.md` de tu perfil. Recuerda la restricción de tiempo y concéntrate en la calidad y funcionalidad de lo que logres completar.

    Te recomendamos hacer `git commit` de forma regular a medida que avanzas en tu solución.

    ---

    ### 5. Entregar tu Solución

    Para entregar tu trabajo, te pedimos que sigas el procedimiento estándar de GitHub de hacer un *fork* y luego un *Pull Request*:

    <details>
      <summary><b>Detalles del Proceso de Entrega</b></summary>

      1.  **Haz un Fork de este repositorio** a tu propia cuenta de GitHub. (En la página de GitHub, busca el botón "Fork" en la esquina superior derecha).
      2.  **Clona tu *fork* localmente.** Si ya clonaste este repositorio original, deberías añadir tu fork como un nuevo "remote" o, para simplificar, volver a clonar tu *fork*.
      3.  **Crea una nueva rama (branch)** para tu solución (ej. `git checkout -b solucion-tu-nombre`).
      4.  **Asegúrate de que todos tus cambios estén comiteados** en esta rama antes de subirla.
      5.  **Sube tu rama** a tu repositorio *forkeado*: `git push origin solucion-tu-nombre`.
      6.  **Crea un "Pull Request" (PR)** desde tu rama en tu *fork* (ej. `solucion-tu-nombre`) hacia la rama `main` de este repositorio original. En la descripción del PR, puedes añadir cualquier comentario relevante sobre tu solución, supuestos o decisiones tomadas.

      > [!NOTE]
      > *Si tienes algún inconveniente con el proceso de Git/GitHub, por favor comunícalo al equipo de evaluación lo antes posible para recibir asistencia.*
    </details>

    ---

    ## ✉️ Contacto y Soporte

    Si tienes alguna pregunta o encuentras algún problema durante la evaluación, por favor contacta a [Tu Nombre/Email/Canal de Comunicación].

    ---
    ```bash
git clone [https://github.com/tu-usuario/evalua_ia.git](https://github.com/tu-usuario/evalua_ia.git)
cd evalua_ia