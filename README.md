<div id="top"></div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#motivación,-objetivos-y-funcionalidad">Motivación, objetivos y funcionalidad</a></li>
    <li><a href="#roadmap">Codificación y estructura</a></li>
    <li><a href="#contributing">Estado y mejoras futuras</a></li>
    <li><a href="#contact">Instalación</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



## Motivación, objetivos y funcionalidad

La motivación principal de este módulo de Odoo es agilizar y optimizar ciertos aspectos del trabajo de mi padre. Al ser encargado de obra, debe llevar un registro del material, personal, maquinaria, dietas y demás aspectos de su día a día, que anota en una agenda al acabar su jornada. Entonces me dí cuenta de que le podría ser de gran ayuda un módulo de Odoo vistoso e intuitivo, en lugar de una simple agenda. 



## Codificación y estructura

Mi módulo se compone de un total de 5 modelos. Estos están relacionados entre sí con **relaciones** Many2many, Many2one y One2many y también están compuestos por **fields** calculados y de tipo Date. Por último el modelo _Employee_ hereda por delegación de **res.partner**, creando una tabla nueva con los campos nuevos definidos por mí, y cumpliendo así el último de los requisitos. En la siguiente imagen podemos ver de una forma más visual la estructura de estos:


<img src="https://user-images.githubusercontent.com/100152588/159137899-4c763c38-b490-4955-a65a-e93afcf0d98b.png"/>





## Estado y mejoras futuras

El estado actual del módulo es bastante básico. Se compone de 2 tipos de views para cada modelo (tree y form view) y una kanban para las construcciones. Además, para ser un módulo totalmente funcional, tendría que añadir algún campo más a cada modelo para que no queden tan escuetos y añadir algún tipo de vista más visual. Por esto, algunos de los posibles cambios que en un futuro debería de cumplir mi módulo serían los siguientes: 

  * Añadir campos a los modelos para acabar de completarlos
  * Crear un campo para incluír imágenes para cada obra y mejorar así el aspecto visual de la vista kanban
  * Añadir más vistas para los demás modelos
  * Implementar datos de muestra con el archivo 'demo.xml'
  


## Instalación

Este repositorio tiene como carpeta raíz la propia carpeta del modulo, entonces solo es necesario clonar el repositorio en la carpeta que odoo asigna por defecto en el addons_path. Sigue los siguiente pasos para añadir este módulo a tu instacia de Odoo:

1. Clonar el repositorio en la carpeta **/opt/odoo/src/OCB/addons** 
   ```sh
   cd /opt/odoo/src/OCB/addons
   
   git clone https://github.com/cristian-mb-sxe/construction-schedule
   ```
2. Asegúrate de que la ruta figura en el archivo **odoo.conf**
   ```sh
   addons_path = /opt/odoo/src/OCB/addons
   ```
   
   
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">Ir al principio</a>)</p>

