#import "elsearticle/elsearticle.typ": *

#set heading(numbering: "1.1")
#set text(lang: "es")
#show figure: set block(breakable: true)

#show: elsearticle.with(
  title: "Benchmark Comparativo de Algoritmos de Detección de Objetos para el Reconocimiento de Defectos Superficiales en Madera",
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
    La inspección automatizada de calidad en la industria maderera mediante visión por computadora requiere localizar e identificar imperfecciones superficiales en líneas de producción de alta velocidad. Los defectos naturales presentan variaciones de forma, textura y contraste que dificultan la estandarización de los procesos de control de calidad. Adicionalmente, la distribución física de las anomalías genera un severo desequilibrio de clases donde ciertos defectos críticos ocurren con bajas frecuencias. Este estudio propone una evaluación matricial que intersecta tres paradigmas de detección de objetos con cuatro estrategias de aumento de datos sobre un conjunto de datos industrial de madera. Los detectores evaluados incluyen Cascade R-CNN como modelo convolucional de dos etapas, YOLO26 como detector convolucional de una etapa en tiempo real y RF-DETR como modelo basado en transformers de detección. Las estrategias de aumento abarcan la línea base original, transformaciones fotométricas tradicionales con Albumentations, aumento de cajas delimitadoras con BoxAug y composición sintética neuronal mediante LibCom con PCT-Net y Latent Bridge Matching. Los resultados identifican la sensibilidad de cada arquitectura ante la inyección sintética de datos y establecen las fronteras de precisión y latencia para la inspección automatizada de madera.
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

= Introducción <sec:intro>

La manufactura industrial moderna depende de sistemas de control de calidad automatizados para mantener la eficiencia operativa y reducir costos en las cadenas de suministro @yang2020using. La integración de tecnologías de visión por computadora y aprendizaje automático ha transformado los procesos de inspección industrial, permitiendo la detección de anomalías con velocidades y niveles de precisión que superan a los métodos manuales @czimmermann2020visual. La automatización de la inspección de calidad se ha convertido en un componente esencial de la Industria 4.0, particularmente en sectores donde la variabilidad del material natural dificulta la estandarización de los procesos productivos @Ramos2021Industry4. La industria maderera representa un sector económico significativo a nivel global, donde la madera se constituye como un recurso renovable de alta importancia tanto estructural como comercial @Yin2021Drying. El procesamiento de madera involucra múltiples etapas que van desde el aserrado hasta el acabado final, y en cada una de ellas la calidad del material determina directamente su valor y aplicabilidad @Chen2023Recognition. El aprovechamiento total de la madera en procesos productivos alcanza únicamente entre el 50% y el 70% del volumen, debido a la presencia de defectos que deben ser identificados y removidos @Chen2023Recognition. Esta tasa de desperdicio resalta la necesidad urgente de sistemas de inspección más eficientes que permitan maximizar el aprovechamiento del recurso @Kryl2020Inspection. La integración de estos sistemas en plantas automatizadas se coordina con brazos robóticos y celdas de manipulación autónoma de material @Ericsson2021Quality.

El reconocimiento automatizado de defectos superficiales en madera presenta desafíos técnicos específicos que lo distinguen de otras aplicaciones de detección de objetos @Shah2026Review. Las anomalías superficiales abarcan nudos vivos, nudos muertos, grietas de secado, bolsas de resina, manchas de hongo y daños mecánicos @Chen2023Recognition. La alta varianza intraclase de los defectos, donde un mismo tipo de anomalía puede presentar apariencias visuales muy diferentes, constituye uno de los principales obstáculos @Kodytek2022Dataset. El bajo contraste entre ciertos defectos y la veta de la madera sana dificulta la segmentación precisa de las regiones anómalas @minaee2022survey. Las condiciones de iluminación variables en los entornos de los aserraderos, combinadas con la velocidad de las líneas de producción que pueden alcanzar valores de 9.6 m/s, imponen requisitos estrictos sobre los tiempos de inferencia de los algoritmos de detección @Kodytek2022Dataset. Adicionalmente, los datasets industriales sufren un severo desequilibrio de clases en distribución de cola larga, donde defectos raros como médula o nudos faltantes quedan subrepresentados frente a la alta prevalencia de nudos estándar @Kodytek2022Dataset. Estos factores convergen en un problema de investigación que requiere soluciones algorítmicas especializadas de alta localización espacial y baja latencia @prunella2023deep.

Históricamente, la inspección de defectos en madera dependió de personal capacitado que examinaba visualmente las superficies en busca de imperfecciones @Kryl2020Inspection. Este enfoque manual presenta limitaciones significativas en términos de velocidad, consistencia y escalabilidad @Kryl2020Inspection. La fatiga visual del operador, la subjetividad en la evaluación y la incapacidad para procesar grandes volúmenes de material en tiempo real son problemas recurrentes que afectan la fiabilidad del proceso @Kryl2020Inspection. Estudios previos han demostrado que la inspección manual rara vez supera el 70% de acierto en entornos industriales de alta velocidad @Kodytek2022Dataset. Para superar estas deficiencias, el estado del arte evolucionó progresivamente desde sistemas basados en sensores optoelectrónicos y visión por computadora clásica @ren2022state. Los enfoques clásicos utilizaban técnicas de procesamiento de imágenes como matrices de coocurrencia de niveles de gris, patrones binarios locales y descriptores de gradientes orientados (HOG) @dalal2005hog, combinados con clasificadores de máquinas de vectores de soporte (SVM) @sugiarto2017wood, @nurthohari2019wood. El marco de trabajo Viola-Jones @viola2001rapid representó un avance pionero en la detección de objetos en tiempo real mediante características de tipo Haar @lienhart2002extended y clasificadores en cascada AdaBoost @arxiv2022tracking. El emparejamiento de imágenes evolucionó desde descriptores diseñados manualmente (SIFT, SURF, HOG) hacia representaciones jerárquicas profundas @ma2021image. Sin embargo, si bien estos métodos clásicos ofrecen interpretabilidad, su capacidad para manejar la alta variabilidad natural y el bajo contraste de los defectos superficiales orgánicos en la madera resulta severamente limitada @prunella2023deep.

La transición hacia redes neuronales profundas convolucionales (CNN) ha permitido la extracción automática de características jerárquicas que capturan patrones espaciales complejos @alzubaidi2021review. El ecosistema tecnológico contemporáneo ofrece marcos de trabajo para el desarrollo de detectores profundos de alto rendimiento @jiao2019survey. Las arquitecturas basadas en convoluciones profundas evolucionaron a través de detectores regionales de dos etapas como Faster R-CNN @ren2016faster y Mask R-CNN @he2017mask, así como detectores de una etapa basados en anclajes como Single Shot MultiBox Detector (SSD) @liu2016ssd, Feature Pyramid Networks (FPN) @lin2017fpn y modelos libres de anclajes como FCOS @tian2019fcos. La familia YOLO impulsó la detección en tiempo real desde sus primeras versiones YOLOv1 @redmon2016yolo, YOLOv2 @redmon2017yolo9000, YOLOv3 @redmon2018yolov3, YOLOv4 @bochkovskiy2020yolov4, hasta revisiones completas del paradigma YOLOv1 a YOLOv8 @hussain2023yolo. Más recientemente, los modelos basados en Vision Transformers (ViT) introdujeron mecanismos de autoatención global que capturan dependencias espaciales de largo alcance en inspección visual industrial @hutten2022vision.

Frente a los descriptores clásicos y detectores heredados, el estado del arte actual demanda la evaluación rigurosa de paradigmas profundos de última generación combinados con técnicas de balanceo sintético de datos. Las arquitecturas convolucionales avanzadas como Cascade R-CNN @cai2018cascade proporcionan refinamiento multietapa de cajas delimitadoras, mientras que YOLO26 @jocher2026ultralyticsyolo26unifiedrealtime incorpora un diseño de cabeza dual para inferencia end-to-end en tiempo real sin etapa NMS y optimizador MuSGD @jocher2026ultralyticsyolo26unifiedrealtime. En el dominio de transformers, RF-DETR @robinson2026rfdetrneuralarchitecturesearch establece la frontera de precisión y latencia mediante búsqueda de arquitectura neuronal @robinson2026rfdetrneuralarchitecturesearch. En paralelo, las técnicas de aumento de objetos (BoxAug @LEE2022104138, Simple Copy-Paste @ghiasi2021simple) integradas con frameworks de composición profunda y armonización neuronal (LibCom @niu2021making, PCT-Net @Guerreiro_2023_CVPR, Latent Bridge Matching @chadebec2025lbmlatentbridgematching) permiten mitigar el desequilibrio de clases sin introducir artefactos visuales. El objetivo principal de este artículo es proporcionar una evaluación matricial de 3 por 4 que intersecta estos tres paradigmas profundos con cuatro estrategias de aumento de datos en el reconocimiento de defectos superficiales en madera.

El resto del artículo se organiza de la siguiente manera. La @sec:related presenta los trabajos relacionados con la detección de defectos en madera utilizando técnicas de aprendizaje profundo. La @sec:methods describe los materiales y métodos utilizados, incluyendo los fundamentos teóricos, las herramientas y tecnologías empleadas, las características del dataset y el método propuesto para el desarrollo. La @sec:results detalla los resultados obtenidos, incluyendo métricas de rendimiento y análisis comparativo. La @sec:conclusions discute las conclusiones derivadas del estudio, destacando las implicaciones prácticas y las limitaciones del trabajo. Finalmente, la @sec:future presenta trabajos futuros y posibles extensiones de la investigación.

// ============================================================
// 2. TRABAJOS RELACIONADOS
// ============================================================

= Trabajos relacionados <sec:related>

Urbonas et al. @urbonas2019automated abordaron la identificación automatizada de defectos en superficies de chapa de madera utilizando la arquitectura Faster R-CNN con técnicas de transfer learning y aumento de datos. El objetivo fue evaluar la viabilidad de redes regionales propuestas preentrenadas para la detección de defectos en un entorno industrial controlado. El aporte principal fue demostrar que el aprendizaje por transferencia con modelos ResNet152 alcanza una precisión del 96.1% en la clasificación combinada de defectos. La metodología empleó cuatro redes neuronales preentrenadas (AlexNet, VGG16, BNInception y ResNet152) con aumento de datos por rotación y volteo. Los resultados mostraron que ResNet152 obtuvo el mejor rendimiento con 80.6% de precisión en clasificación de defectos individuales. Como deficiencia, el estudio se limitó a un dataset de 4,729 imágenes con solo 353 muestras defectuosas, lo que restringió la generalización de los resultados.

Fang et al. @fang2021yolov5knots propusieron un sistema automatizado para la detección precisa de nudos superficiales en madera aserrada utilizando el modelo YOLO-v5. El objetivo fue desarrollar un detector en tiempo real capaz de identificar múltiples tipos de nudos con alta precisión. El aporte fue la validación de YOLO-v5 como alternativa eficiente a los detectores de dos etapas para la inspección de madera. La metodología consistió en el fine-tuning de YOLO-v5 con dos datasets de nudos de madera, evaluando métricas de precisión, recall y F1-score. Los resultados alcanzaron un F-Score del 91.7% en el primer dataset y del 97.7% en el segundo, superando a YOLO-v3 SPP y Faster R-CNN en velocidad y tamaño de modelo. La deficiencia identificada fue que el modelo se evaluó únicamente en la clase de nudos, sin considerar otros tipos de defectos como grietas o manchas.

Han et al. @han2023improved presentaron una versión mejorada del algoritmo YOLOv5 para la detección de defectos superficiales en madera, incorporando mecanismos de atención en la arquitectura. El objetivo fue mejorar la capacidad del modelo para detectar defectos pequeños y de bajo contraste. El aporte principal fue la integración de módulos de atención que permiten al modelo enfocarse en regiones relevantes de la imagen. La metodología modificó la backbone y el neck de YOLOv5 con capas de atención espacial y de canal. Los resultados demostraron mejoras significativas en la detección de defectos pequeños comparado con el modelo base. La deficiencia fue la falta de una comparación estandarizada con otros detectores state-of-the-art en el mismo dataset.

Zheng et al. @zheng2024gbcdyolo desarrollaron GBCD-YOLO, un modelo ligero y de alta precisión para la detección de defectos en madera, basado en modificaciones arquitectónicas de YOLOv5s. El objetivo fue reducir la complejidad computacional manteniendo la precisión de detección. El aporte fue la combinación de bloques Ghost Bottleneck, atención BiFormer, upsampling CARAFE y dinámica DyHead con pérdida CIoU. La metodología incluyó optimización de la arquitectura y evaluación en un dataset de defectos de madera con 10 categorías. Los resultados mostraron un mAP\@0.5 del 88.72%, una mejora del 13.45% sobre YOLOv5s base, con reducción del 15.49% en parámetros y aumento del 6.25% en FPS. La deficiencia fue que el modelo no se comparó con arquitecturas basadas en transformers o detectores de dos etapas.

Zheng et al. @cwbyolo2024 propusieron CWB-YOLOv8, una mejora del algoritmo YOLOv8 mediante la incorporación de Convolución Condicional Paramétrica, Wise-IoU y BiFormer para la detección de defectos en madera. El objetivo fue mejorar la capacidad de detección de defectos variados en tamaño y apariencia. El aporte principal fue la combinación de tres módulos que mejoran la extracción de características, la función de pérdida y la atención multi-escala. La metodología empleó un dataset personalizado de 6,134 imágenes con defectos de especies de pino radiata, eucalipto y árbol de Tuna. Los resultados alcanzaron un mAP\@0.5 del 89.2%, con mejoras del 3.5% sobre YOLOv8 estándar y detección precisa de grietas (96%) y resina (93%). La deficiencia fue la ausencia de evaluación de métricas de eficiencia computacional como latencia en tiempo real.

Sun @wood2022multicriteria implementó un sistema de detección de defectos de calidad en madera basado en aprendizaje profundo y un framework multicriterio. El objetivo fue desarrollar un sistema que combinara la detección automática de defectos con un sistema de evaluación multicriterio para la clasificación de calidad. El aporte fue la integración de un framework de decisión multicriterio con redes neuronales profundas para la evaluación integral de la calidad de la madera. La metodología utilizó CNN para la detección de defectos internos combinado con análisis multicriterio para la clasificación de calidad. Los resultados reportaron una tasa de detección del 99.8% para defectos internos y un IOU promedio del 74.3%. La deficiencia fue que el estudio se enfocó en defectos internos sin una validación extensiva en datasets públicos de referencia.

Kilic et al. @kilic2025wd presentaron WD Detector, un diseño híbrido de sensor basado en aprendizaje profundo para la detección de defectos en madera, que combina extracción de características con CNN y clasificadores de aprendizaje automático clásico. El objetivo fue desarrollar un sistema híbrido que aproveche las fortalezas tanto del aprendizaje profundo como del aprendizaje automático tradicional. El aporte fue la demostración de que la combinación de features extraídas por Xception con clasificadores como CatBoost supera a las CNN puras. La metodología empleó Xception para la extracción de características y 12 clasificadores de ML para la clasificación final. Los resultados alcanzaron una precisión del 99.32% con CatBoost como el mejor clasificador. La deficiencia fue que el sistema requiere un pipeline de dos etapas que incrementa la complejidad de implementación.

Ji et al. @ji2024online desarrollaron un algoritmo basado en aprendizaje profundo para la detección en línea de defectos de objetivo pequeño en madera aserrada de gran tamaño. El objetivo fue resolver el problema de detectar defectos pequeños en imágenes de alta resolución de tablones industriales. El aporte fue la integración de red ELAN (Efficient Layer Aggregation Network) con YOLO y costura de imágenes mediante SIFT para manejar el procesamiento de madera de gran formato. La metodología combinó detección de keypoints SIFT para la unión de imágenes con una arquitectura YOLO modificada para la detección de defectos pequeños. Los resultados reportaron una precisión del 90.37% con una velocidad de procesamiento de 40 m/min. La deficiencia fue la dependencia del algoritmo SIFT para la costura de imágenes, que puede ser computacionalmente costosa en entornos de alta velocidad.

Wolszczak et al. @wolszczak2024bluestain abordaron la detección de manchas azules causadas por hongos en un sistema de inspección de madera en aserraderos, utilizando redes neuronales entrenadas para la clasificación automática de este tipo específico de defecto. El objetivo fue desarrollar un sistema automatizado capaz de identificar manchas azules en superficies de madera durante el proceso de producción. El aporte fue la aplicación específica de redes neuronales para un tipo de defecto particularmente difícil de detectar por métodos tradicionales. La metodología empleó una red neuronal entrenada con imágenes de manchas azules capturadas en un entorno industrial real. Los resultados demostraron la viabilidad del enfoque para la detección automatizada de este tipo de defecto. La deficiencia fue que el estudio se limitó a una sola categoría de defecto sin evaluar el rendimiento en un escenario multi-clase.

Chen et al. @chen2022edgeglued propusieron un sistema de detección de defectos en paneles de madera encolada utilizando técnicas de aprendizaje profundo. El objetivo fue desarrollar un sistema WDD-DL que combinara filtros de procesamiento de imágenes con clasificación por redes neuronales. El aporte fue la combinación de filtros de Gabor, detección de esquinas de Harris y morfología matemática con la red InceptionResNetV2 para la clasificación. La metodología implementó un pipeline de dos etapas: pre-procesamiento con filtros clásicos y clasificación con CNN. Los resultados alcanzaron una precisión de 0.97, un recall de 0.90 y un F1-score de 0.92. La deficiencia fue la complejidad del pipeline de dos etapas que dificulta la implementación en tiempo real.

Shah et al. @Shah2026Review realizaron una revisión comprehensiva de la detección automática de defectos en inspección de superficies de madera, comparando modelos de una etapa (YOLO y variantes) y de dos etapas (Faster R-CNN), e investigando enfoques emergentes de aprendizaje zero-shot. El objetivo fue proporcionar una visión general del estado del arte en detección de defectos de madera. El aporte fue la comparación sistemática de modelos single-stage y two-stage, más la introducción de enfoques zero-shot basados en modelos visión-lenguaje como CLIP. La metodología revisó literatura reciente, analizó datasets públicos y comparó métricas de rendimiento. Los resultados mostraron que los modelos YOLO son preferidos para aplicaciones en tiempo real, mientras que Faster R-CNN ofrece mayor precisión a costa de velocidad. La deficiencia fue que la revisión no incluyó modelos basados en transformers como representantes de la nueva generación de detectores.

La @fig:tabla-resumen resume los trabajos revisados en la literatura. Ninguno de los estudios existentes evalúa la matriz cruzada entre los tres paradigmas de detección y las técnicas avanzadas de aumento por objeto con armonización neuronal bajo desequilibrio severo de clases.

#figure(
  table(
    columns: (1fr, 1.5fr, 1fr, 1fr),
    align: (left, left, center, center),
    table.header([Autor], [Enfoque], [Métrica principal], [Deficiencia]),
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
    [Shah et al. @Shah2026Review], [Revisión general], [Comparación cualitativa], [Sin benchmark matricial empírico],
  ),
  caption: [Resumen comparativo de trabajos relacionados con detección de defectos en madera.],
  scope: "parent",
  kind: table,
  placement: auto,
) <fig:tabla-resumen>

// ============================================================
// 3. MATERIALES Y MÉTODOS
// ============================================================

= Materiales y Métodos <sec:methods>

== Fundamentos teóricos <sec:fundamentals>

La formación de defectos superficiales en la madera responde a factores fisiológicos del árbol y a tensiones mecánicas durante el procesamiento @Yin2021Drying. Los nudos vivos corresponden a bases de ramas integradas en el tejido leñoso, mientras que los nudos muertos representan ramas separadas que generan cavidades discontinuas @Chen2023Recognition. Las grietas se originan por tensiones de tracción perpendicular durante las fases de secado del material @Yin2021Drying. Las acumulaciones de resina, la médula central y las inclusiones minerales de cuarcita alteran la homogeneidad física de la superficie @Chen2023Recognition. Las líneas de producción modernas trasladan los tablones cepillados a velocidades lineales de 9.6 m/s ante cámaras de escaneo lineal @Kodytek2022Dataset. El tiempo disponible para capturar, procesar y clasificar cada imagen se restringe a intervalos de pocos milisegundos @Kodytek2022Dataset. La alta variabilidad en el grano de la madera de fondo disminuye el contraste visual de las regiones defectuosas @Chen2023Recognition.

La recolección de datos en entornos industriales produce conjuntos anotados con un severo desequilibrio de clases @zhang2021deep. En una distribución de cola larga, una fracción reducida de categorías acapara la mayoría de las observaciones @zhang2021deep. El ratio de desequilibrio mide la relación entre la frecuencia de la clase mayoritaria y la clase minoritaria. En conjuntos con un ratio superior a 30, las funciones de pérdida estándar quedan dominadas por los gradientes de las categorías dominantes @cui2019classbalanced. La red neuronal suprime las predicciones de las categorías raras al asignarles puntajes de confianza deficientes @tan2020equalization. Este fenómeno provoca un colapso en la capacidad discriminativa del modelo sobre anomalías poco frecuentes pero estructuralmente peligrosas @wang2021seesaw.

El aumento de datos a nivel de objeto modifica directamente la distribución de frecuencias de las clases anotadas @LEE2022104138. A diferencia de las transformaciones afines globales, la técnica BoxAug aísla parches recortados pertenecientes a categorías de la cola @LEE2022104138. Los parches son multiplicados aplicando transformaciones estocásticas de escala, rotación y volteo horizontal @LEE2022104138. Mediante el procedimiento Simple Copy-Paste, los parches transformados se reinsertan en imágenes de entrenamiento con baja densidad de defectos @ghiasi2021simple. Para eliminar las discontinuidades visuales del pegado directo, el framework LibCom proporciona algoritmos de composición profunda @niu2021making. El modelo PCT-Net estima transformaciones de color a nivel de píxel para igualar la luminancia regional @Guerreiro_2023_CVPR. El método Latent Bridge Matching aplica un mapeo en espacio latente para generar sombras y adaptaciones fotométricas en un solo paso de inferencia @chadebec2025lbmlatentbridgematching. Las muestras sintéticas resultantes preservan las etiquetas de ubicación a la vez que ofrecen coherencia fotométrica con la madera receptora @capogrosso2024diffusion.

Cascade R-CNN representa la arquitectura convolucional de dos etapas orientada a alta precisión espacial @cai2018cascade. La primera etapa emplea una Red de Propuesta de Regiones para seleccionar candidatos sobre mapas de características convolucionales. La segunda etapa ejecuta una secuencia de cabezales de detección entrenados con umbrales de Intersección sobre Unión progresivamente más estrictos. Este diseño en cascada refina gradualmente las coordenadas de las cajas delimitadoras y minimiza los falsos positivos en escenarios de alta densidad de defectos @cai2018cascade.

YOLO26 representa la arquitectura convolucional de una etapa diseñada para inferencia en tiempo real @jocher2026ultralyticsyolo26unifiedrealtime. Adopta una formulación libre de anclajes que predice directamente los centros y dimensiones de las cajas delimitadoras desde mapas de características multiescala. Su diseño de cabeza dual elimina la necesidad de la etapa de supresión de no máximos en la inferencia, optimizando la velocidad de procesamiento y la latencia computacional @jocher2026ultralyticsyolo26unifiedrealtime.

RF-DETR representa la arquitectura basada en Vision Transformers optimizada para detección en tiempo real @robinson2026rfdetrneuralarchitecturesearch. Utiliza mecanismos de autoatención global bidireccional para capturar dependencias espaciales de largo alcance a lo largo de toda la superficie de la imagen @zhao2023detrs. Mediante Búsqueda de Arquitectura Neuronal, RF-DETR descubre configuraciones estructurales óptimas en la frontera de Pareto entre precisión de localización y latencia de procesamiento @robinson2026rfdetrneuralarchitecturesearch.

La cuantificación del rendimiento de los detectores de objetos integra métricas de precisión espacial y eficiencia computacional @Shah2026Review. La precisión mide la proporción de predicciones positivas correctas, mientras que el recall evalúa la proporción de defectos reales detectados @Shah2026Review. El puntaje F1 representa la media armónica de ambas métricas. La Intersección sobre Unión evalúa la superposición espacial entre la caja predicha y la anotación real. La precisión promedio media mAP\@0.5 y mAP\@0.5:0.95 agrega el rendimiento a través de múltiples umbrales de superposición, aislando las fortalezas algorítmicas en clases desequilibradas @Shah2026Review. Las métricas de eficiencia computacional comprenden el tiempo de inferencia expresado en milisegundos por imagen, el rendimiento en cuadros por segundo, el número de parámetros flotantes en millones y el tamaño del modelo almacenado en disco en megabytes @prunella2023deep.

== Herramientas y Tecnologías <sec:tools>

El desarrollo del pipeline de experimentación se ejecuta sobre el lenguaje de programación Python en su versión 3.12. El framework de aprendizaje profundo principal corresponde a PyTorch versión 2.7.0 con aceleración por GPU mediante bibliotecas CUDA 12.8. Las operaciones suplementarias de visión computacional emplean torchvision versión 0.22.0. La arquitectura Cascade R-CNN se implementa mediante la librería MMDetection versión 3.2.0, soportada por MMCV versión 2.2.0 y MMEngine versión 0.10.7. El detector YOLO26 y el detector RT-DETR se ejecutan utilizando el marco Ultralytics en su versión 8.2.0. La arquitectura RF-DETR se compila desde el motor oficial RF-DETR versión 1.3.0.

El procesamiento de datos sintéticos y aumentos fotométricos utiliza Albumentations versión 1.4.0. Las primitivas de composición e inserción de objetos emplean la librería LibCom versión 0.2.0 integrada en el entorno de desarrollo. La gestión estricta de configuraciones de la tubería se programa mediante Pydantic versión 2.6.1. La manipulación acelerada de tablas de metadatos utiliza Polars versión 1.43.0 y OpenCV versión 5.0.0. El entorno virtual y la resolución de dependencias se administran mediante el gestor uv versión 0.6+, mientras que la extracción documental procesa los archivos mediante PyMuPDF versión 1.25.0.

== Dataset <sec:dataset>

El estudio utiliza la versión filtrada y anotada en formato YOLO disponible en Kaggle @Nomihsa2024KaggleWood, derivada del conjunto de datos original Large-scale Image Dataset of Wood Surface Defects publicado por Kodytek et al. @Kodytek2022Dataset. El dataset original fue adquirido en un entorno industrial real durante la producción de un aserradero mediante una cámara de escaneo lineal JAI SW-4000TL-PMCL a una frecuencia de línea de 66 kHz @Kodytek2022Dataset. La versión filtrada empleada en este trabajo @Nomihsa2024KaggleWood ha sido preprocesada para incluir exclusivamente imágenes que contienen defectos y sus anotaciones han sido convertidas al formato YOLO estándar para la evaluación directa de modelos de detección de objetos.

El dataset filtrado contiene un total de 4,000 imágenes en formato JPG con una resolución espacial fija de 2800 por 1024 píxeles @Nomihsa2024KaggleWood. El conjunto almacena 8,736 cajas delimitadoras anotadas distribuidas en 8 categorías de defectos superficiales. En promedio, cada imagen contiene 2.18 defectos, alcanzando un máximo de 15 defectos por imagen. La @fig:piechart-clases ilustra la distribución porcentual de frecuencia para cada clase de defecto.

#figure(
  image("figures/dataset/barchart_classes.svg", width: 95%),
  caption: [Distribución de clases de defectos en el dataset filtrado @Nomihsa2024KaggleWood.],
  kind: image,
) <fig:piechart-clases>

Las anotaciones proporcionan coordenadas normalizadas de cajas delimitadoras en formato YOLO. La distribución de clases refleja las condiciones reales de producción industrial @Kodytek2022Dataset. Las categorías mayoritarias corresponden a nudos vivos con 3,905 anotaciones (44.7%) y nudos muertos con 2,835 anotaciones (32.5%), representando el 77.2% del total. Las categorías intermedias incluyen resina con 639 anotaciones (7.3%), grietas con 505 anotaciones (5.8%) y nudos con grietas con 410 anotaciones (4.7%). Las categorías minoritarias comprenden médula con 204 anotaciones (2.3%), cuarcita con 129 anotaciones (1.5%) y nudos faltantes con 109 anotaciones (1.2%). El ratio de desequilibrio calculado alcanza un valor aproximado de 35.82. La @fig:defectos-ejemplo muestra ejemplos representativos de las ocho categorías de defectos anotadas en el conjunto de datos.

#[
  #set image(width: 95%)
  #figure(
    grid(
      columns: 4,
      rows: 2,
      gutter: 4pt,
      image("figures/dataset/Live_Knot.jpg"), image("figures/dataset/Dead_Knot.jpg"),
      image("figures/dataset/resin.jpg"), image("figures/dataset/knot_with_crack.jpg"),
      image("figures/dataset/Crack.jpg"), image("figures/dataset/Marrow.jpg"),
      image("figures/dataset/Quartzity.jpg"), image("figures/dataset/Knot_missing.jpg"),
    ),
    caption: [Ejemplos de las ocho clases de defectos anotadas en el dataset de madera @Nomihsa2024KaggleWood.],
    kind: image,
    scope: "parent",
    placement: auto,
  ) <fig:defectos-ejemplo>
]

== Método propuesto <sec:proposed>

#lorem(100) \
#lorem(100) \
#lorem(100) \

= Resultados <sec:results>

#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \

= Conclusiones <sec:conclusions>

#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \

= Trabajos Futuros <sec:future>

#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \
#lorem(100) \

= Conflictos de Intereses

#lorem(100) \

= Financiación

#lorem(100) \

= Consentimientos

#lorem(100) \

= Fuentes de Datos

#lorem(100) \

= Disponibilidad de Datos

#lorem(100) \

= Contribución de Autoría

#lorem(100) \

#bibliography("sources/references.bib", style: "ieee", title: [Referencias])
