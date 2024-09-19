## Primer Parcial (Ejemplo)
# Neuquén Líneas Aéreas
Siguiendo el incremento en la actividad económica de la provincia de Neuquén durante el 2058,
la gobernadora ha decidido comenzar con el proyecto de la creación de una aerolínea de
bandera para la provincia. Para ello, la provincia ha contratado personal que se dedicará a la
mecánica, el pilotaje, la venta de tickets y la atención a clientes, entre otros. Además, se
contrató a su empresa de desarrollo de software, para que implemente el sistema de reservas
de tickets para esta nueva aerolínea, NLA (Neuquén Líneas Aéreas).

Su tarea en esta primera jornada de trabajo será implementar un sistema de clases que
represente el problema a resolver y que contemple los siguientes comportamientos:

```
1. Se pueden crear pasajeros, aportando información de su documentación y datos de contacto
2. Se pueden crear vuelos, indicando el trayecto a realizar y el horario para el que está
programado, así como la capacidad del mismo 
3. Se pueden crear reservas, donde una reserva está asociada a un único usuario y un único
vuelo, siempre que haya espacio disponible
4. Se pueden listar los pasajeros de un vuelo
5. Se pueden listar los vuelos con espacio disponible, en un determinado trayecto
```
Pueden crear todas las clases que consideren necesarias. Dentro de ellas pueden crear tantos
métodos como les sea conveniente.
### Criterios de aprobación:
```
- Todas las clases deben estar bien definidas
- Todos los métodos deben estar bien definidos y sus implementaciones deben ser las
correctas
- Se debe respetar el principio de encapsulamiento de la POO
- Deben existir tests para las implementaciones de los métodos más relevantes
- Al menos una de las implementaciones de los métodos debe ser recursiva, para que 
podamos evaluar su entendimiento de la recursividad. Por Favor indicar en la definición
del método que es el que han elegido para este propósito
