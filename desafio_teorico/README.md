# Desafío Teórico
Consigna

## Procesos, hilos y corrutinas

● Un caso en el que usarías procesos para resolver un problema y por qué.
 - En un escenario donde sabemos que podemos ejecutar varias tareas pesadas e independientes y sin que el fallo en una tarea provoque problemas en las otras. Por ejemplo, el procesamiento archivos multimedia para transformarlos de una formato a otro. Este tipo de tareas son independientes, por lo que deberían tener su propio espacio de memoria, ademas de ejecutarse en diferentes núcleos de CPU, por tanto, se haría un uso eficiente de todos los núcleo disponibles

● Un caso en el que usarías threads para resolver un problema y por qué.
 - Para el caso de un servidor web, necesita atender multiples peticiones livianas (en términos de consumo de recursos de computo) de varios usuario al mismo tiempo y de manera simultanea. Los hilos son mas livianos que los procesos en cuanto al uso de memoria y procesador, ya que usan un espacio de memoria compartido que permite comunicarse entre los hilos, ademas es posible ejecutar varios hilos sobre un mismo núcleo, y por tanto permite ejecutar simultáneamente varias tareas sin que estas bloqueen el hilo principal; debido a esto son adecuados para sistemas que requieran un alto volumen de solicitudes simultaneas.

● Un caso en el que usarías corrutinas para resolver un problema y por qué.
 - LAs corrutinas se pueden ejecutar sobre un mismo hilo, aunque no de manera simultanea, pausando tareas y reanundandolas donde quedaron, por lo que este mecanismo es adecuado para tareas que son asíncronas como consultas a APIs externas o consultas a disco y que su tiempo de respuesta es variable. Las corritunas son mas fáciles de gestionar sin la complejidad de manejar los estado de los hilos de ejecución.



##  Optimización de recursos del sistema operativo
Si tuvieras 1.000.000 de elementos y tuvieras que consultar para cada uno de ellos información en una API HTTP. ¿Cómo lo harías? Explicar.

La cantidad de elementos es considerable ya que podría sobrecargar la API que se esta consultando, por lo que habría que tener en cuenta varios criterios para decidir el modo de implementación:
 - Si la API permite consultas en lotes es mucho mas eficiente que enviar las consultar de manera independiente.
 - Hacer uso de corrutinas para manejar solicitudes asíncronas que no bloqueen el hilo principal y que permita ejecutar mas peticiones al tiempo, mientras espera respuestas de otras anteriores peticiones.
 - Aunque se utilicen corritinas para hacer varias peticiones al  tiempo hay que controlar el numero máximo de peticiones simultaneas, para evitar sobrecargar el API externos.
 - Si existen peticiones duplicadas de otras peticiones anteriores, considerar usar un sistema de cache para obtener resultados mas rápidos y sin sobrecargar el API externo.


## Análisis de complejidad
● Dados 4 algoritmos A, B, C y D que cumplen la misma funcionalidad, con
complejidades O(n^2), O(n^3), O(2^n) y O(n log n), respectivamente, ¿Cuál de los
algoritmos favorecerías y cuál descartarías en principio? Explicar por qué.

Los primeros algoritmos que descartaría son aquellos que tiene las complejidades exponenciales por que tienden a crecer su consumo de recursos o de tiempo de computo según aumente la cantidad de registros o elementos a procesar. Si todos los algoritmos hacen los mismo, a primera vista no hay ganancia al escoger aquellos que consumen mas recursos que otro, por tanto el algoritmo de menor complejidad O(n log n) seria el que escogería debido a que su tendencia es mucho mas baja con respecto a los otros para grandes cantidades de datos. 

Para pequeñas cantidades de datos, el algoritmo que corresponde a la complejidad O(n^2), debido a que la diferencia no es mucha con respeto al primer escogido, y puede que sea factible o fácil de usar según el caso o el problema al que nos estamos enfrentando.


● Asume que dispones de dos bases de datos para utilizar en diferentes
problemas a resolver. La primera llamada AlfaDB tiene una complejidad de O(1)
en consulta y O(n2) en escritura. La segunda llamada BetaDB que tiene una
complejidad de O(log n) tanto para consulta, como para escritura. ¿Describe en
forma sucinta, qué casos de uso podrías atacar con cada una?

- La elección de la base de datos AlfaDB o BetaDB, depende mucho de el tipo de operación que ma se efectúe sobre la base de datos, si es para una aplicación que es principalmente para operaciones de lectura, es mejor usar AlfaDB. y BetaDB para el caso en que la cantidad de operaciones de escritura sean mayores o iguales a la de lectura.

Puede haber una tercera opción para cuando el numero de operaciones de escritura es igual a las de lectura, y sea necesario mejorar el rendimiento de lectura que forma independiente ninguna base de datos lo proporciona. Podríamos usar las dos bases datos funcionando al tiempo y conectadas asincronamente para que la base de datos BetaDB reciba las operaciones de escritura y, posteriormente, y de manera asíncrona, envíe la información hacia la base de datos AlfaDB, la cual esta ultima se usaría para, por ejemplo, consultas de reportes o análisis de datos; en cuyo caso tendríamos lo mejor de ambas bases de datos, aunque perdiendo la posibilidad de consultar datos en tiempo real. 

