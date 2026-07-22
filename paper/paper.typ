#import "elsearticle/elsearticle.typ": *

#set heading(numbering: "1.1")

#show: elsearticle.with(
  title: "Benchmark comparativo de algoritmos de detección de objetos para el reconocimiento de defectos superficiales en madera",
  authors: (
    (
      name: "Chambilla Perca Ricardo Mauricio",
      affiliations: ("a",),
      corresponding: true,
      email: "rchambillap@unsa.edu.pe",
    ),
    (
      name: "Jara Mamani Mariel Alison",
      affiliations: ("a",),
      corresponding: true,
      email: "mjarama@unsa.edu.pe",
    ),
    (
      name: "Mestas Zegarra Christian Raul",
      affiliations: ("a",),
      corresponding: true,
      email: "cmestasz@unsa.edu.pe",
    ),
    (
      name: "Noa Camino Yenaro Joel",
      affiliations: ("a",),
      corresponding: true,
      email: "ynoa@unsa.edu.pe",
    ),
    (
      name: "Sequeiros Condori Luis Gustavo",
      affiliations: ("a",),
      corresponding: true,
      email: "lsequeiros@unsa.edu.pe",
    ),
  ),
  affiliations: (
    "a": [Universidad Nacional de San Agustín de Arequipa, Facultad de Ingeniería de Producción y Servicios, Arequipa, Perú],
  ),
  abstract: [
    Si
  ],
  keywords: (
    "detección de defectos",
    "visión por computadora",
    "aprendizaje profundo",
    "procesamiento de madera",
    "benchmark comparativo",
  ),
  format: "5p",
  paper: "a4",
)

// ============================================================
// 1. INTRODUCCIÓN
// ============================================================

= Introducción

La manufactura moderna depende de sistemas de control de calidad automatizados para mantener la eficiencia operativa y reducir costos en las cadenas de suministro @yang2020using. La integración de tecnologías de visión por computadora y aprendizaje automático ha transformado los procesos de inspección industrial, permitiendo la detección de anomalías con velocidades y niveles de precisión que superan los métodos manuales @czimmermann2020visual. En este contexto, la automatización de la inspección de calidad se ha convertido en un componente esencial de la Industria 4.0, particularmente en sectores donde la variabilidad del material natural dificulta la estandarización de los procesos productivos @Ramos2021Industry4.

La industria maderera representa un sector económico significativo a nivel global, donde la madera se constituye como un recurso renovable de alta importancia tanto estructural como comercial @Yin2021Drying. El procesamiento de madera involucra múltiples etapas que van desde el aserrado hasta el acabado final, y en cada una de ellas la calidad del material determina directamente su valor y aplicabilidad @Chen2023Recognition. El aprovechamiento total de la madera en procesos productivos alcanza únicamente entre el 50% y el 70% del volumen, debido a la presencia de defectos que deben ser identificados y removidos @Chen2023Recognition. Esta tasa de desperdicio resalta la necesidad urgente de sistemas de inspección más eficientes que permitan maximizar el aprovechamiento del recurso.

Los defectos superficiales de la madera constituyen una de las principales causas de degradación de la calidad del material procesado. Entre los defectos más frecuentes se encuentran los nudos vivos y muertos, las grietas de secado, las bolsas de resina, las manchas azules por hongos y los daños causados por insectos @Shah2026Review. Cada tipo de defecto presenta firmas visuales distintas que van desde variaciones sutiles en la textura hasta alteraciones significativas en la geometría y el color de la superficie @Kodytek2022Dataset. La presencia de estos defectos no solo afecta las propiedades estéticas de la madera, sino que también puede comprometer su integridad mecánica, especialmente en aplicaciones estructurales donde la resistencia es un requisito crítico @Yin2021Drying.

Históricamente, la inspección de defectos en madera ha dependido de personal capacitado que examina visualmente las superficies en busca de imperfecciones @Kryl2020Inspection. Este enfoque manual presenta limitaciones significativas en términos de velocidad, consistencia y escalabilidad. La fatiga visual del operador, la subjetividad en la evaluación y la incapacidad para procesar grandes volúmenes de material en tiempo real son problemas recurrentes que afectan la fiabilidad del proceso @Kodytek2022Dataset. Estudios previos han demostrado que la inspección manual rara vez supera el 70% de acierto en entornos industriales de alta velocidad @Kodytek2022Dataset. Estas limitaciones justifican la búsqueda de alternativas automatizadas que superen las deficiencias de los métodos tradicionales.

El reconocimiento automatizado de defectos superficiales en madera presenta desafíos técnicos específicos que lo distinguen de otras aplicaciones de detección de objetos. La alta varianza intraclase de los defectos, donde un mismo tipo de anomalía puede presentar apariencias visualmente muy diferentes, constituye uno de los principales obstáculos @Shah2026Review. El bajo contraste entre ciertos defectos y la veta de la madera sana dificulta la segmentación precisa de las regiones anómalas @Chen2023Recognition. Las condiciones de iluminación variables en los entornos de los aserraderos, combinadas con la velocidad de las líneas de producción que pueden alcanzar valores de 9.6 m/s, imponen requisitos estrictos sobre los tiempos de inferencia de los algoritmos de detección @Kodytek2022Dataset. Estos factores convergen en un problema de investigación que requiere soluciones algorítmicas especializadas.

El estado del arte actual en detección de defectos ha experimentado una evolución significativa desde los métodos basados en sensores optoelectrónicos básicos hasta sistemas avanzados de visión por computadora @ren2022state. Los enfoques clásicos utilizaban técnicas de procesamiento de imágenes como matrices de co-ocurrencia de niveles de gris, patrones binarios locales y descriptores de gradientes orientados, combinados con clasificadores de máquinas de vectores de soporte @nurthohari2019wood. Si bien estos métodos ofrecen interpretabilidad, su capacidad para manejar la variabilidad de los defectos naturales es limitada @sugiarto2017wood. La transición hacia redes neuronales profundas convolucionales ha permitido la extracción automática de características jerárquicas que capturan patrones espaciales complejos @alzubaidi2021review.

El ecosistema tecnológico contemporáneo ofrece herramientas y marcos de trabajo que facilitan el desarrollo de sistemas de detección de objetos de alto rendimiento. Las arquitecturas basadas en convoluciones profundas, representadas por la familia YOLO y las redes regionales propuestas, han demostrado resultados prometedores en aplicaciones industriales @jiao2019survey. Más recientemente, los modelos basados en transformers como DETR y sus variantes han introducido mecanismos de autoatención global que capturan dependencias espaciales de largo alcance @hutten2022vision. La disponibilidad de frameworks como PyTorch y Ultralytics, junto con datasets públicos anotados, ha democratizado el acceso a estas tecnologías para la investigación aplicada @alzubaidi2021review.

El objetivo principal de este artículo es proporcionar un análisis comparativo riguroso de tres paradigmas de detección de objetos aplicados al reconocimiento de defectos superficiales en tablones de madera: Faster R-CNN como representante de los detectores de dos etapas basados en anclajes, YOLOv8 como representante de los detectores de una etapa basados en CNN, y RT-DETR como representante de los detectores basados en transformers. El estudio evalúa estos modelos en el dataset Large-scale Image Dataset of Wood Surface Defects @Kodytek2022Dataset, empleando métricas estándar de detección de objetos e indicadores de eficiencia computacional. El análisis busca identificar las fortalezas y debilidades de cada paradigma arquitectónico en el contexto específico de la inspección de madera, proporcionando evidencia empírica para orientar la selección de modelos en aplicaciones industriales.

El resto del artículo se organiza de la siguiente manera. La sección 2 presenta los trabajos relacionados con la detección de defectos en madera utilizando técnicas de aprendizaje profundo. La sección 3 describe los materiales y métodos utilizados, incluyendo los fundamentos teóricos, las herramientas y tecnologías empleadas, y las características del dataset. La sección 4 detalla el método propuesto, incluyendo el framework de evaluación comparativa y el pipeline de entrenamiento. La sección 5 presenta los resultados experimentales y su discusión. Finalmente, la sección 6 resume las conclusiones y propone líneas de investigación futuras.

// ============================================================
// 2. TRABAJOS RELACIONADOS
// ============================================================

= Trabajos relacionados

Urbonas et al. @urbonas2019automated abordaron la identificación automatizada de defectos en superficies de chapa de madera utilizando la arquitectura Faster R-CNN con técnicas de transfer learning y aumento de datos. El objetivo fue evaluar la viabilidad de redes regionales propuestas pre-entrenadas para la detección de defectos en un entorno industrial controlado. El aporte principal fue demostrar que el aprendizaje por transferencia con modelos ResNet152 alcanza una precisión del 96.1% en la clasificación combinada de defectos. La metodología empleó cuatro redes neuronales pre-entrenadas (AlexNet, VGG16, BNInception y ResNet152) con aumento de datos por rotación y volteo. Los resultados mostraron que ResNet152 obtuvo el mejor rendimiento con 80.6% de precisión en clasificación de defectos individuales. Como deficiencia, el estudio se limitó a un dataset de 4,729 imágenes con solo 353 muestras defectuosas, lo que restringió la generalización de los resultados.

Fang et al. @fang2021yolov5knots propusieron un sistema automatizado para la detección precisa de nudos superficiales en madera aserrada utilizando el modelo YOLO-v5. El objetivo fue desarrollar un detector en tiempo real capaz de identificar múltiples tipos de nudos con alta precisión. El aporte fue la validación de YOLO-v5 como alternativa eficiente a los detectores de dos etapas para la inspección de madera. La metodología consistió en el fine-tuning de YOLO-v5 con dos datasets de nudos de madera, evaluando métricas de precisión, recall y F1-score. Los resultados alcanzaron un F-Score del 91.7% en el primer dataset y del 97.7% en el segundo, superando a YOLO-v3 SPP y Faster R-CNN en velocidad y tamaño de modelo. La deficiencia identificada fue que el modelo se evaluó únicamente en la clase de nudos, sin considerar otros tipos de defectos como grietas o manchas.

Han et al. @han2023improved presentaron una versión mejorada del algoritmo YOLOv5 para la detección de defectos superficiales en madera, incorporando mecanismos de atención en la arquitectura. El objetivo fue mejorar la capacidad del modelo para detectar defectos pequeños y de baja contraste. El aporte principal fue la integración de módulos de atención que permiten al modelo enfocarse en regiones relevantes de la imagen. La metodología modificó la backbone y el neck de YOLOv5 con capas de atención espacial y de canal. Los resultados demostraron mejoras significativas en la detección de defectos pequeños comparado con el modelo base. La deficiencia fue la falta de una comparación estandarizada con otros detectores state-of-the-art en el mismo dataset.

Zheng et al. @zheng2024gbcdyolo desarrollaron GBCD-YOLO, un modelo ligero y de alta precisión para la detección de defectos en madera, basado en modificaciones arquitectónicas de YOLOv5s. El objetivo fue reducir la complejidad computacional manteniendo la precisión de detección. El aporte fue la combinación de bloques Ghost Bottleneck, atención BiFormer, upsampling CARAFE y dinámica DyHead con pérdida CIoU. La metodología incluyó optimización de la arquitectura y evaluación en un dataset de defectos de madera con 10 categorías. Los resultados mostraron un mAP\@0.5 del 88.72%, una mejora del 13.45% sobre YOLOv5s base, con reducción del 15.49% en parámetros y aumento del 6.25% en FPS. La deficiencia fue que el modelo no se comparó con arquitecturas basadas en transformers o detectores de dos etapas.

Zheng et al. @cwbyolo2024 propusieron CWB-YOLOv8, una mejora del algoritmo YOLOv8 mediante la incorporación de Convolución Condicional Paramétrica, Wise-IoU y BiFormer para la detección de defectos en madera. El objetivo fue mejorar la capacidad de detección de defectos variados en tamaño y apariencia. El aporte principal fue la combinación de tres módulos que mejoran la extracción de características, la función de pérdida y la atención multi-escala. La metodología empleó un dataset personalizado de 6,134 imágenes con defectos de especies de pino radiata, eucalipto y árbol de Tuna. Los resultados alcanzaron un mAP\@0.5 del 89.2%, con mejoras del 3.5% sobre YOLOv8 estándar y detección precisa de grietas (96%) y resina (93%). La deficiencia fue la ausencia de evaluación de métricas de eficiencia computacional como latencia en tiempo real.

Sun @wood2022multicriteria implementó un sistema de detección de defectos de calidad en madera basado en aprendizaje profundo y un framework multicriterio. El objetivo fue desarrollar un sistema que combinara la detección automática de defectos con un sistema de evaluación multicriterio para la clasificación de calidad. El aporte fue la integración de un framework de decisión multicriterio con redes neuronales profundas para la evaluación integral de la calidad de la madera. La metodología utilizó CNN para la detección de defectos internos combinado con análisis multicriterio para la clasificación de calidad. Los resultados reportaron una tasa de detección del 99.8% para defectos internos y un IOU promedio del 74.3%. La deficiencia fue que el estudio se enfocó en defectos internos sin una validación extensiva en datasets públicos de referencia.

Kilic et al. @kilic2025wd presentaron WD Detector, un diseño híbrido de sensor basado en aprendizaje profundo para la detección de defectos en madera, que combina extracción de características con CNN y clasificadores de aprendizaje automático clásico. El objetivo fue desarrollar un sistema híbrido que aproveche las fortalezas tanto del aprendizaje profundo como del aprendizaje automático tradicional. El aporte fue la demostración de que la combinación de features extraídas por Xception con clasificadores como CatBoost supera a las CNN puras. La metodología empleó Xception para la extracción de características y 12 clasificadores de ML para la clasificación final. Los resultados alcanzaron una precisión del 99.32% con CatBoost como el mejor clasificador. La deficiencia fue que el sistema requiere un pipeline de dos etapas que incrementa la complejidad de implementación.

Ji et al. @ji2024online desarrollaron un algoritmo basado en aprendizaje profundo para la detección en línea de defectos de objetivo pequeño en madera aserrada de gran tamaño. El objetivo fue resolver el problema de detectar defectos pequeños en imágenes de alta resolución de tablones industriales. El aporte fue la integración de red ELAN (Efficient Layer Aggregation Network) con YOLO y costura de imágenes mediante SIFT para manejar el procesamiento de madera de gran formato. La metodología combinó detección de keypoints SIFT para la unión de imágenes con una arquitectura YOLO modificada para la detección de defectos pequeños. Los resultados reportaron una precisión del 90.37% con una velocidad de procesamiento de 40 m/min. La deficiencia fue la dependencia del algoritmo SIFT para la costura de imágenes, que puede ser computacionalmente costosa en entornos de alta velocidad.

Wolszczak et al. @wolszczak2024bluestain abordaron la detección de manchas azules causadas por hongos en un sistema de inspección de madera en aserraderos, utilizando redes neuronales entrenadas para la clasificación automática de este tipo específico de defecto. El objetivo fue desarrollar un sistema automatizado capaz de identificar manchas azules en superficies de madera durante el proceso de producción. El aporte fue la aplicación específica de redes neuronales para un tipo de defecto particularmente difícil de detectar por métodos tradicionales. La metodología empleó una red neuronal entrenada con imágenes de manchas azules capturadas en un entorno industrial real. Los resultados demostraron la viabilidad del enfoque para la detección automatizada de este tipo de defecto. La deficiencia fue que el estudio se limitó a una sola categoría de defecto sin evaluar el rendimiento en un escenario multi-clase.

Chen et al. @chen2022edgeglued propusieron un sistema de detección de defectos en paneles de madera encolada utilizando técnicas de aprendizaje profundo. El objetivo fue desarrollar un sistema WDD-DL que combinara filtros de procesamiento de imágenes con clasificación por redes neuronales. El aporte fue la combinación de filtros de Gabor, detección de esquinas de Harris y morfología matemática con la red InceptionResNetV2 para la clasificación. La metodología implementó un pipeline de dos etapas: pre-procesamiento con filtros clásicos y clasificación con CNN. Los resultados alcanzaron una precisión de 0.97, un recall de 0.90 y un F1-score de 0.92. La deficiencia fue la complejidad del pipeline de dos etapas que dificulta la implementación en tiempo real.

Shah et al. @Shah2026Review realizaron una revisión comprehensiva de la detección automática de defectos en inspección de superficies de madera, comparando modelos de una etapa (YOLO y variantes) y de dos etapas (Faster R-CNN), e investigando enfoques emergentes de aprendizaje zero-shot. El objetivo fue proporcionar una visión general del estado del arte en detección de defectos de madera. El aporte fue la comparación sistemática de modelos single-stage y two-stage, más la introducción de enfoques zero-shot basados en modelos visión-lenguaje como CLIP. La metodología revisó literatura reciente, analizó datasets públicos y comparó métricas de rendimiento. Los resultados mostraron que los modelos YOLO son preferidos para aplicaciones en tiempo real, mientras que Faster R-CNN ofrece mayor precisión a costa de velocidad. La deficiencia fue que la revisión no incluyó modelos basados en transformers como representantes de la nueva generación de detectores.

La @fig:tabla-resumen resume los trabajos revisados, evidenciando que ninguno de ellos aborda simultáneamente la comparación de los tres paradigmas arquitectónicos (dos etapas, una etapa CNN, una etapa transformer) en un mismo benchmark estandarizado. La mayoría de los estudios se enfocan en variantes de YOLO o en Faster R-CNN de forma aislada, sin una evaluación comparativa que permita identificar las fortalezas relativas de cada paradigma en el contexto específico de la detección de defectos superficiales en madera.

#figure(
  table(
    columns: (1fr, 1.5fr, 1fr, 1fr),
    align: (left, left, center, center),
    table.header([*Autor*], [*Enfoque*], [*Métrica principal*], [*Deficiencia*]),
    [Urbonas et al. @urbonas2019automated], [Faster R-CNN + TL], [96.1% acc.], [Dataset pequeño],
    [Fang et al. @fang2021yolov5knots], [YOLO-v5], [97.7% F1], [Solo nudos],
    [Han et al. @han2023improved], [YOLOv5 + atención], [Mejora sobre base], [Sin comparación],
    [Zheng et al. @zheng2024gbcdyolo], [GBCD-YOLO], [88.7% mAP], [Sin transformers],
    [Zheng et al. @cwbyolo2024], [CWB-YOLOv8], [89.2% mAP], [Sin eficiencia],
    [Sun @wood2022multicriteria], [CNN + multicriterio], [99.8% det.], [Dataset limitado],
    [Kilic et al. @kilic2025wd], [Xception + ML], [99.3% acc.], [Pipeline dos etapas],
    [Ji et al. @ji2024online], [YOLO + ELAN + SIFT], [90.4% acc.], [Dependencia SIFT],
    [Wolszczak et al. @wolszczak2024bluestain], [Red neuronal], [Clasif. binaria], [Una sola clase],
    [Chen et al. @chen2022edgeglued], [Filtros + InceptionResNet], [0.92 F1], [Pipeline complejo],
  ),
  caption: [Resumen comparativo de trabajos relacionados con detección de defectos en madera.],
) <fig:tabla-resumen>

// ============================================================
// 3. MATERIALES Y MÉTODOS
// ============================================================

= Materiales y Métodos

== Fundamentos teóricos

=== Defectos superficiales de la madera

La madera es un material biológico cuyo crecimiento está sujeto a factores ambientales, genéticos y mecánicos que generan variaciones naturales en su estructura @Yin2021Drying. Estas variaciones se manifiestan como defectos superficiales que afectan tanto las propiedades mecánicas como la apariencia estética del material procesado @Chen2023Recognition. Los defectos se clasifican en tres categorías principales según su origen: defectos de crecimiento debido a razones fisiológicas, defectos causados por plagas y enfermedades de naturaleza patológica, y defectos de procesamiento resultantes de operaciones humanas de aserrado y secado @Chen2023Recognition. Cada categoría presenta firmas visuales distintas que requieren estrategias de detección diferenciadas.

Los defectos de crecimiento constituyen la categoría más prevalente e incluyen nudos vivos, nudos muertos, grietas, hendiduras, rebabas y cápsulas de resina @Chen2023Recognition. Los nudos vivos mantienen las fibras de la madera intactas y conectadas al tronco, mientras que los nudos muertos representan ramas que han muerto y se han separado @Shah2026Review. Las grietas de secado se forman cuando el proceso de secado genera tensiones internas en la madera, y su longitud es proporcional a su profundidad y anchura @Shah2026Review. Las manchas azules son el resultado de la colonización por hongos que alteran el color de la superficie sin comprometer significativamente las propiedades mecánicas @wolszczak2024bluestain. Los defectos causados por insectos se manifiestan en forma de agujeros y surcos que pueden comprometer la integridad estructural del material @Chen2023Recognition.

La severidad de un defecto y, por lo tanto, la clasificación y el valor del material, se determinan principalmente por cuatro criterios: el tamaño, la ubicación, el tipo de defecto y el propósito para el cual se utilizará el producto de madera @Kodytek2022Dataset. En la industria maderera, la tasa de utilización combinada del material alcanza únicamente entre el 50% y el 70%, debido a la presencia de defectos que deben ser identificados y removidos durante el procesamiento @Chen2023Recognition. Esta tasa de desperdicio representa una pérdida económica significativa que la automatización de la inspección busca mitigar.

=== Integración en la cadena de producción

La detección de defectos se ubica estratégicamente dentro del flujo de producción de un aserradero o planta de manufactura moderna @Ramos2021Industry4. En las líneas de producción actuales, los sistemas de inspección operan después del cepillado y antes de la clasificación final, donde la velocidad de procesamiento puede alcanzar valores de 9.6 m/s @Kodytek2022Dataset. Esta velocidad impone restricciones estrictas sobre los tiempos de inferencia de los algoritmos de detección, que deben procesar cada imagen en milisegundos para no bloquear el flujo productivo. Los sistemas comerciales como WoodEye, WEINIG y Microtec CT utilizan arquitecturas multi-sensor que combinan detección láser con reconocimiento de imágenes para lograr la precisión requerida @Chen2023Recognition. La integración de estos sistemas con plataformas de automatización como robots de marcado y sistemas de gestión de producción representa el estado actual de la Industria 4.0 aplicada al sector maderero @Ericsson2021Quality.

=== Localización y clasificación de defectos

La visión por computadora ofrece tres niveles de análisis para la inspección de superficies de madera @minaee2022survey. La clasificación de imágenes estándar determina si un tablón contiene o no defectos, proporcionando una respuesta binaria sobre el estado general del material. La detección de objetos localiza las regiones defectuosas mediante cajas delimitadoras que definen la posición y extensión de cada anomalía. La segmentación semántica e instance labeling identifica los píxeles exactos que pertenecen a cada defecto, proporcionando la información más detallada sobre la geometría de las imperfecciones @minaee2022survey. La selección de la detección de objetos como tarea principal se justifica por la disponibilidad de anotaciones con cajas delimitadoras en los datasets de referencia, como el dataset Large-scale Image Dataset of Wood Surface Defects @Kodytek2022Dataset, que proporciona tanto etiquetas de segmentación semántica como coordenadas de bounding boxes para 10 tipos de defectos.

=== El cambio de paradigma del aprendizaje profundo

El procesamiento de imágenes ha experimentado una transformación fundamental desde la ingeniería de características diseñada manualmente hacia la extracción de características jerárquica basada en datos @ma2021image. Los métodos clásicos utilizaban descriptores como SIFT, SURF y HOG, que requerían un conocimiento experto del dominio para su diseño y adaptación @dalal2005hog. Las redes neuronales profundas convolucionales permitieron que el modelo aprendiera automáticamente las representaciones más relevantes a partir de los datos de entrenamiento @alzubaidi2021review. Esta transición ha sido particularmente significativa en la detección de defectos industriales, donde la variabilidad de las anomalías supera la capacidad de los descriptores manuales para capturar todas las variaciones posibles @prunella2023deep.

=== Cascadas de Haar y el marco Viola-Jones

El marco de trabajo Viola-Jones representó un avance pionero en la detección de objetos en tiempo real @viola2001rapid. Este enfoque utiliza características tipo Haar que capturan diferencias de contraste en regiones rectangulares de la imagen, calculadas eficientemente mediante imágenes integrales @lienhart2002extended. El algoritmo de aprendizaje AdaBoost selecciona las características más discriminativas y las organiza en una estructura de cascada donde las etapas más simples rechazan rápidamente las regiones negativas @viola2001rapid. Si bien este enfoque es altamente eficiente computacionalmente, su dependencia de diferencias de contraste rígidas lo hace propenso a altas tasas de falsos positivos cuando se enfrenta a texturas irregulares y orgánicas como la veta de la madera @arxiv2022tracking.

=== Histograma de gradientes orientados y máquinas de vectores de soporte

El descriptor HOG captura la distribución de orientaciones del gradiente en porciones localizadas de la imagen, proporcionando una representación robusta de perfiles de formas y bordes @dalal2005hog. Este descriptor se calcula dividiendo la imagen en celdas de tamaño uniforme, computando histogramas de gradientes orientados en cada celda y normalizando los vectores resultantes en bloques superpuestos @dalal2005hog. Los vectores de características HOG se pasan a una SVM que busca el hiperplano de separación óptimo entre las clases de defecto y fondo @nurthohari2019wood. Estudios previos han aplicado exitosamente esta combinación para la clasificación de calidad de madera, alcanzando precisiones del 90% en clasificación de 5 clases de madera de cedro @nurthohari2019wood. Sin embargo, las dificultades ante apariencias altamente variables intraclase de las anomalías naturales limitan la generalización de estos métodos @sugiarto2017wood.

=== Faster R-CNN: detectores de dos etapas

Faster R-CNN introdujo la Red de Propuesta de Regiones (RPN) que comparte características convolucionales con el detector, eliminando la necesidad de calcular propuestas de regiones de forma independiente @ren2016faster. En la primera etapa, la RPN genera candidatas a cajas delimitadoras utilizando anclajes (anchor boxes) de múltiples escalas y relaciones de aspecto. En la segunda etapa, las propuestas se refinan y clasifican mediante una red de interés alineado (RoI Align) que preserva la información espacial precisa @he2017mask. Esta arquitectura de dos etapas ofrece alta precisión de localización a expensas de la sobrecarga computacional, alcanzando velocidades de 5 FPS con backbone VGG-16 @ren2016faster. Cascade R-CNN extiende este paradigma entrenando una secuencia de cabezales de detección con umbrales de IoU progresivamente más altos, minimizando los falsos positivos en escenarios de defectos densos @cai2018cascade.

=== SSD: detectores de una etapa

El Single Shot MultiBox Detector (SSD) elimina la etapa de propuesta de regiones utilizando mapas de características multiescala y cajas de anclaje a través de diferentes capas de la red @liu2016ssd. Esta arquitectura detecta objetos de varios tamaños en una sola pasada hacia adelante, equilibrando la velocidad y la invariancia de escala @liu2016ssd. Los mapas de características de menor resolución capturan objetos grandes, mientras que las capas de mayor resolución detectan objetos pequeños @lin2017fpn. El SSD con backbone VGG-16 alcanza 74.3% de mAP a 59 FPS en VOC 2007, superando a YOLO en precisión @liu2016ssd. Sin embargo, los detectores de una etapa basados en anclajes pueden presentar dificultades con objetos de tamaños extremos o relaciones de aspecto inusuales, lo que motivó el desarrollo de arquitecturas libre de anclajes como FCOS @tian2019fcos.

=== Evolución de YOLO

La familia YOLO ha impulsado la evolución de los detectores de una etapa hacia el rendimiento extremo en tiempo real @redmon2016yolo. YOLOv1 trató la detección como un problema de regresión que mapea directamente píxeles a coordenadas de cajas delimitadoras @redmon2016yolo. YOLOv2 incorporó normalización por lotes, cajas de anclaje y entrenamiento multi-escala @redmon2017yolo9000. YOLOv3 introdujo predicciones multi-escala tipo FPN y clasificación con entropía cruzada binaria @redmon2018yolov3. YOLOv4 optimizó la velocidad y precisión con CSPDarknet53, SPP y PANet @bochkovskiy2020yolov4. Las iteraciones modernas como YOLOv8 incorporan mecanismos de atención espacial y funciones de pérdida avanzadas, manteniendo la eficiencia estructural @hussain2023yolo. RT-DETR representa el cambio hacia arquitecturas basadas en transformers para detectores en tiempo real @hutten2022vision.

=== Vision Transformers en inspección industrial

Los Vision Transformers (ViT) introdujeron el mecanismo de autoatención global al procesamiento de imágenes, capturando dependencias espaciales de largo alcance a lo largo de toda la imagen @hutten2022vision. A diferencia de las convoluciones locales de las CNN, los transformers permiten que la red contextualice un defecto en relación con el patrón general de la veta de la madera no defectuosa @hutten2022vision. Arquitecturas como Swin Transformer utilizan ventanas desplazadas para reducir la complejidad computacional manteniendo la capacidad de capturar relaciones a gran escala @hutten2022vision. En inspección industrial, los ViT han demostrado ser competitivos con las CNN, con la ventaja adicional de manejar mejor las dependencias globales que son relevantes para la detección de defectos que interactúan con el patrón general de la veta de la madera @hutten2022vision.

=== Métricas de evaluación

La evaluación del rendimiento de detectores de objetos requiere métricas que capturen tanto la calidad de las predicciones como la eficiencia computacional @Shah2026Review. La precisión (Precision) mide la proporción de predicciones positivas que son correctas, mientras que el recall (exhaustividad) indica la proporción de defectos reales que fueron detectados @Shah2026Review. El puntaje F1 combina ambas métricas en una única medida armónica. La Intersección sobre Unión (IoU) evalúa la superposición entre la caja delimitadora predicha y la caja del ground truth, siendo el umbral estándar de 0.5 el más utilizado para la evaluación de detectores @Shah2026Review. La precisión promedio media (mAP\@0.5 y mAP\@0.5:0.95) agrega el rendimiento a través de múltiples umbrales de IoU, proporcionando una evaluación comprehensiva que aísla las fortalezas y debilidades algorítmicas a través de clases de defectos altamente desequilibradas @Shah2026Review. Las métricas de eficiencia incluyen la latencia de inferencia en milisegundos por imagen tanto en CPU como en GPU, el número de parámetros del modelo en millones y el tamaño del modelo en disco en megabytes @prunella2023deep.

== Herramientas y Tecnologías

El ecosistema de software utilizado en este estudio se fundamenta en Python como lenguaje principal de programación, seleccionado por su ecosistema consolidado de herramientas para visión por computadora y aprendizaje profundo @alzubaidi2021review. Para la manipulación de metadatos y análisis exploratorio de datos se emplea Polars, una librería de DataFrames multifilamento y de alto rendimiento que supera los cuellos de botella de memoria de las herramientas tradicionales como pandas. El procesamiento de imágenes se realiza mediante OpenCV y torchvision, que proporcionan operaciones optimizadas para el pre-procesamiento y aumento de datos de imágenes industriales @alzubaidi2021review.

El framework principal de aprendizaje profundo es PyTorch, acompañado por el ecosistema Ultralytics para la implementación de YOLOv8 y RT-DETR, y MMdetection para la implementación de Faster R-CNN @alzubaidi2021review. El entorno de aceleración por hardware CUDA/GPU garantiza evaluaciones comparativas reproducibles con tiempos de inferencia consistentes. Todas las dependencias se gestionan mediante uv como gestor de paquetes, y las versiones se especifican en el archivo pyproject.toml del proyecto para garantizar la reproducibilidad de los experimentos @alzubaidi2021review.

== Dataset

El dataset utilizado en este estudio corresponde a una versión filtrada y anotada en formato YOLO del conjunto de datos Large-scale Image Dataset of Wood Surface Defects @Kodytek2022Dataset, disponible públicamente en Kaggle (https://www.kaggle.com/datasets/nomihsa965/large-scale-image-dataset-of-wood-surface-defects). El dataset original, denominado "A large-scale image dataset of wood surface defects for automated vision-based quality control processes", fue adquirido en un entorno industrial real durante el proceso de producción de un aserradero, utilizando una cámara de escaneo lineal JAI SW-4000TL-PMCL con resolución de $3 times 4096$ píxeles por línea a una frecuencia de adquisición de 66 kHz @Kodytek2022Dataset. La versión empleada en este trabajo ha sido pre-procesada para incluir únicamente imágenes con defectos y suas anotaciones han sido convertidas al formato YOLO estándar, facilitando la evaluación directa de modelos de detección de objetos.

El dataset filtrado contiene un total de 3,612 imágenes de superficies de madera aserrada, cada una con una resolución de $2800 times 1024$ píxeles en formato JPG. El conjunto incluye 8 tipos de defectos superficiales con 9,211 anotaciones de cajas delimitadoras: nudos vivos (Live_Knot, 44.2%), nudos muertos (Dead_Knot, 31.9%), resina (resin, 7.1%), nudos con grietas (knot_with_crack, 5.9%), grietas (Crack, 5.6%), médula (Marrow, 2.2%), cuarcita (Quartzity, 1.9%) y nudos faltantes (Knot_missing, 1.3%). En promedio, cada imagen contiene 2.55 defectos, con un máximo de 15 defectos por imagen.

Las anotaciones proporcionan coordenadas normalizadas de cajas delimitadoras en formato YOLO, donde cada archivo de texto contiene una línea por defecto con el identificador de clase y las coordenadas del centro y dimensiones de la caja. La distribución de clases presenta un desequilibrio significativo, con los nudos vivos y muertos representando conjuntamente el 76.1% de todas las anotaciones, lo que refleja las condiciones reales de producción industrial @Kodytek2022Dataset.

El análisis exploratorio de geometría de las cajas delimitadoras revela diferencias sustanciales entre tipos de defectos. Los nudos presentan relaciones de aspecto cercanas a la unidad (Live_Knot: 0.75, Dead_Knot: 0.76), indicando formas aproximadamente circulares. En contraste, las grietas (0.12), la médula (0.12) y la cuarcita (0.15) presentan relaciones de aspecto bajas, correspondiendo a formas alargadas y estrechas. La resina intermedia (0.24) muestra formas semi-alargadas. El área promedio de las cajas es del 0.76% del área total de la imagen, confirmando que los defectos son generalmente pequeños en relación con la superficie del tablón.

#bibliography("sources/references.bib", style: "ieee", title: [Referencias])
