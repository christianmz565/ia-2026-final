# Cosas a mejorar del Articulo de IA

## Pag 1

- [x] Poner Nombres Apellidos, no tienen que estar en orden alfabeticos. Agregarme a mi como autor
- [x] Va primero Escuela, Facultad, Universidad, Direcion postal, Ciudad, Pais. La facultad puede obviarse.
- [x] Ademas de los correos poner los orcid de cada autor

## Pag 7

- [x] Necesitan poner un diagrama para el pipeline implementado en la seccion 3.4
- [ ] Revisar todas las imagenes que deben tener todos los textos en ingles. De ser posible mejorrar la resolución de las imagenes o ponerlas mas grandes

## Pag 8

- [ ] Cascade R-CNN se entrenó solo por 12 épocas, RF-DETR por 50 y YOLO26 por 100. Hay que justificar
- [ ] Cascade R-CNN y YOLO26 procesan imágenes a 640x640, mientras que RF-DETR se configuró a 512x512. Hay que justificar
- [ ] Hay que poner una Tabla con los hiperparametros usados en el entrenamiento y hay que justificar según la bibliografía porque esos hiperparametros se usaron

## Pag 9

- [ ] Figura muy pequeña
- [x] Las palabras Figure y Table no van en azul, el hipervinculo solo va al numero de la Figura y la Tabla
- [ ] Hay que hacer multiples corridas o cross-validation para obtener intervalos de confianza mAP+-std. Minimo 3 corridas

## Pag 10

- [ ] Figura muy pequeña
- [ ] Figura muy pequeña
- [ ] Figura muy pequeña
- [ ] Figura muy pequeña
- [ ] Agregar un panel visual de inferencias (imágenes con bounding boxes predichos vs. ground truth). Incluir ejemplos donde los modelos fallan (falsos positivos/negativos) enriquecería sustancialmente la sección de resultados.

## Pag 11

- [ ] Figura muy pequeña
- [ ] Ampliar teóricamente la razón por la cual los parches de BoxAug Std degradan los mecanismos de atención global en RF-DETR.

## Pag 12

- [ ] Ampliar un o dos parrafos mas las conclusiones

## Pag 13

- [ ] Asi no se pone esto

  Author Contribution Statement
  Chambilla Perca R.M. declares roles in Software
  and Writing. Jara Mamani M.A. declares roles in
  Data Curation, Resources, and Methodology. Mestas
  Zegarra C.R. declares roles in Project Administration, Conceptualization, and Writing. Noa Camino
  Y.J. declares roles in Acquisition and Investigation.
  Sequeiros Condori L.G. declares roles in Conceptualization, Investigation, and Software.

- [x] Eliminar
- [x] Eliminar
- [x] Eliminar
- [x] Poner que no se recibió financiamiento
