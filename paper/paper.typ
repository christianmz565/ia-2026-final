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
    La inspección automatizada de defectos superficiales en madera enfrenta desafíos derivados del severo desequilibrio de clases en distribuciones de cola larga y de la alta variabilidad intraclase de las anomalías orgánicas. Este artículo presenta un benchmark comparativo que evalúa la intersección de tres paradigmas de detección de objetos: una etapa, dos etapas y transformers con cuatro estrategias de aumento de datos: sin augmentación, Albumentations con balanceo de clases, BoxAug con transformaciones de ruido, y Boxaug con armonización neuronal mediante LibCom. El estudio se ejecuta sobre un dataset de 4,000 imágenes con 8,736 anotaciones distribuidas en 8 categorías de defectos, empleando un pipeline reproducible de cinco etapas con caché por pasos. Los resultados experimentales demuestran que Cascade R-CNN alcanza la mayor precisión con mAP\@0.5 de 0.711, mientras que YOLO26 presenta la mayor sensibilidad a la augmentación de datos con una mejora relativa del 16.3% respecto a su baseline. Las estrategias de aumento por objeto no producen una mejora universal: BoxAug estándar degrada el rendimiento de RF-DETR en un 1.9%. El análisis por clase revela que cuarcita obtiene una precisión promedio de 0.0 con YOLO26 baseline, evidenciando el impacto crítico del desbalance. Se discuten las razones de la ausencia de mejora generalizada y se proponen direcciones futuras incluyendo ponderación por clase y augmentación basada en difusión.
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

El resto del artículo se organiza de la siguiente manera. La @sec:related presenta los trabajos relacionados con la detección de defectos en madera utilizando técnicas de aprendizaje profundo. La @sec:methods describe los materiales y métodos utilizados, incluyendo los fundamentos teóricos, las herramientas y tecnologías empleadas, las características del dataset y el método propuesto para el desarrollo. La @sec:results detalla los resultados obtenidos, incluyendo métricas de rendimiento y análisis comparativo. La @sec:discussion interpreta los hallazgos principales, comparándolos con la literatura existente y analizando las interacciones entre arquitecturas y estrategias de aumento. La @sec:conclusions resume las contribuciones del estudio. Finalmente, la @sec:future presenta trabajos futuros y posibles extensiones de la investigación.

// ============================================================
// 2. TRABAJOS RELACIONADOS
// ============================================================

= Trabajos relacionados <sec:related>

Urbonas et al. @urbonas2019automated abordaron la identificación automatizada de defectos en superficies de chapa de madera utilizando la arquitectura Faster R-CNN con técnicas de aprendizaje por transferencia y aumento de datos. El objetivo fue evaluar la viabilidad de redes regionales propuestas preentrenadas para la detección de defectos en un entorno industrial controlado. El aporte principal fue demostrar que el aprendizaje por transferencia con modelos ResNet152 alcanza una precisión del 96.1% en la clasificación combinada de defectos. La metodología empleó cuatro redes neuronales preentrenadas, AlexNet, VGG16, BNInception y ResNet152, con aumento de datos por rotación y volteo. Los resultados mostraron que ResNet152 obtuvo el mejor rendimiento con 80.6% de precisión en clasificación de defectos individuales. Como deficiencia, el estudio se limitó a un dataset de 4,729 imágenes con solo 353 muestras defectuosas, lo que restringió la generalización de los resultados.

Fang et al. @fang2021yolov5knots propusieron un sistema automatizado para la detección precisa de nudos superficiales en madera aserrada utilizando el modelo YOLO-v5. El objetivo fue desarrollar un detector en tiempo real capaz de identificar múltiples tipos de nudos con alta precisión. El aporte fue la validación de YOLO-v5 como alternativa eficiente a los detectores de dos etapas para la inspección de madera. La metodología consistió en el fine-tuning de YOLO-v5 con dos datasets de nudos de madera, evaluando métricas de precisión, recall y F1-score. Los resultados alcanzaron un F-Score del 91.7% en el primer dataset y del 97.7% en el segundo, superando a YOLO-v3 SPP y Faster R-CNN en velocidad y tamaño de modelo. La deficiencia identificada fue que el modelo se evaluó únicamente en la clase de nudos, sin considerar otros tipos de defectos como grietas o manchas.

Han et al. @han2023improved presentaron una versión mejorada del algoritmo YOLOv5 para la detección de defectos superficiales en madera, incorporando mecanismos de atención en la arquitectura. El objetivo fue mejorar la capacidad del modelo para detectar defectos pequeños y de bajo contraste. El aporte principal fue la integración de módulos de atención que permiten al modelo enfocarse en regiones relevantes de la imagen. La metodología modificó la backbone y el neck de YOLOv5 con capas de atención espacial y de canal. Los resultados demostraron mejoras significativas en la detección de defectos pequeños comparado con el modelo base. La deficiencia fue la falta de una comparación estandarizada con otros detectores estado del arte en el mismo dataset.

Zheng et al. @zheng2024gbcdyolo desarrollaron GBCD-YOLO, un modelo ligero y de alta precisión para la detección de defectos en madera, basado en modificaciones arquitectónicas de YOLOv5s. El objetivo fue reducir la complejidad computacional manteniendo la precisión de detección. El aporte fue la combinación de bloques Ghost Bottleneck, atención BiFormer, upsampling CARAFE y dinámica DyHead con pérdida CIoU. La metodología incluyó optimización de la arquitectura y evaluación en un dataset de defectos de madera con 10 categorías. Los resultados mostraron un mAP\@0.5 del 88.72%, una mejora del 13.45% sobre YOLOv5s base, con reducción del 15.49% en parámetros y aumento del 6.25% en FPS. La deficiencia fue que el modelo no se comparó con arquitecturas basadas en transformers o detectores de dos etapas.

Zheng et al. @cwbyolo2024 propusieron CWB-YOLOv8, una mejora del algoritmo YOLOv8 mediante la incorporación de Convolución Condicional Paramétrica, Wise-IoU y BiFormer para la detección de defectos en madera. El objetivo fue mejorar la capacidad de detección de defectos variados en tamaño y apariencia. El aporte principal fue la combinación de tres módulos que mejoran la extracción de características, la función de pérdida y la atención multi-escala. La metodología empleó un dataset personalizado de 6,134 imágenes con defectos de especies de pino radiata, eucalipto y árbol de Tuna. Los resultados alcanzaron un mAP\@0.5 del 89.2%, con mejoras del 3.5% sobre YOLOv8 estándar y detección precisa de grietas con 96% de recall y resina con 93% de recall. La deficiencia fue la ausencia de evaluación de métricas de eficiencia computacional como latencia en tiempo real.

Sun @wood2022multicriteria implementó un sistema de detección de defectos de calidad en madera basado en aprendizaje profundo y un framework multicriterio. El objetivo fue desarrollar un sistema que combinara la detección automática de defectos con un sistema de evaluación multicriterio para la clasificación de calidad. El aporte fue la integración de un framework de decisión multicriterio con redes neuronales profundas para la evaluación integral de la calidad de la madera. La metodología utilizó CNN para la detección de defectos internos combinado con análisis multicriterio para la clasificación de calidad. Los resultados reportaron una tasa de detección del 99.8% para defectos internos y un IOU promedio del 74.3%. La deficiencia fue que el estudio se enfocó en defectos internos sin una validación extensiva en datasets públicos de referencia.

Kilic et al. @kilic2025wd presentaron WD Detector, un diseño híbrido de sensor basado en aprendizaje profundo para la detección de defectos en madera, que combina extracción de características con CNN y clasificadores de aprendizaje automático clásico. El objetivo fue desarrollar un sistema híbrido que aproveche las fortalezas tanto del aprendizaje profundo como del aprendizaje automático tradicional. El aporte fue la demostración de que la combinación de características extraídas por Xception con clasificadores como CatBoost supera a las CNN puras. La metodología empleó Xception para la extracción de características y 12 clasificadores de ML para la clasificación final. Los resultados alcanzaron una precisión del 99.32% con CatBoost como el mejor clasificador. La deficiencia fue que el sistema requiere un pipeline de dos etapas que incrementa la complejidad de implementación.

Ji et al. @ji2024online desarrollaron un algoritmo basado en aprendizaje profundo para la detección en línea de defectos de objetivo pequeño en madera aserrada de gran tamaño. El objetivo fue resolver el problema de detectar defectos pequeños en imágenes de alta resolución de tablones industriales. El aporte fue la integración de red ELAN (Efficient Layer Aggregation Network) con YOLO y costura de imágenes mediante SIFT para manejar el procesamiento de madera de gran formato. La metodología combinó detección de keypoints SIFT para la unión de imágenes con una arquitectura YOLO modificada para la detección de defectos pequeños. Los resultados reportaron una precisión del 90.37% con una velocidad de procesamiento de 40 m/min. La deficiencia fue la dependencia del algoritmo SIFT para la costura de imágenes, que puede ser computacionalmente costosa en entornos de alta velocidad.

Wolszczak et al. @wolszczak2024bluestain abordaron la detección de manchas azules causadas por hongos en un sistema de inspección de madera en aserraderos, utilizando redes neuronales entrenadas para la clasificación automática de este tipo específico de defecto. El objetivo fue desarrollar un sistema automatizado capaz de identificar manchas azules en superficies de madera durante el proceso de producción. El aporte fue la aplicación específica de redes neuronales para un tipo de defecto particularmente difícil de detectar por métodos tradicionales. La metodología empleó una red neuronal entrenada con imágenes de manchas azules capturadas en un entorno industrial real. Los resultados demostraron la viabilidad del enfoque para la detección automatizada de este tipo de defecto. La deficiencia fue que el estudio se limitó a una sola categoría de defecto sin evaluar el rendimiento en un escenario multi-clase.

Chen et al. @chen2022edgeglued propusieron un sistema de detección de defectos en paneles de madera encolada utilizando técnicas de aprendizaje profundo. El objetivo fue desarrollar un sistema WDD-DL que combinara filtros de procesamiento de imágenes con clasificación por redes neuronales. El aporte fue la combinación de filtros de Gabor, detección de esquinas de Harris y morfología matemática con la red InceptionResNetV2 para la clasificación. La metodología implementó un pipeline de dos etapas: pre-procesamiento con filtros clásicos y clasificación con CNN. Los resultados alcanzaron una precisión de 0.97, un recall de 0.90 y un F1-score de 0.92. La deficiencia fue la complejidad del pipeline de dos etapas que dificulta la implementación en tiempo real.

Shah et al. @Shah2026Review realizaron una revisión comprehensiva de la detección automática de defectos en inspección de superficies de madera, comparando modelos de una etapa (YOLO y variantes) y de dos etapas (Faster R-CNN), e investigando enfoques emergentes de aprendizaje zero-shot. El objetivo fue proporcionar una visión general del estado del arte en detección de defectos de madera. El aporte fue la comparación sistemática de modelos una etapa y dos etapas, más la introducción de enfoques zero-shot basados en modelos visión-lenguaje como CLIP. La metodología revisó literatura reciente, analizó datasets públicos y comparó métricas de rendimiento. Los resultados mostraron que los modelos YOLO son preferidos para aplicaciones en tiempo real, mientras que Faster R-CNN ofrece mayor precisión a costa de velocidad. La deficiencia fue que la revisión no incluyó modelos basados en transformers como representantes de la nueva generación de detectores. La @fig:tabla-resumen resume los trabajos revisados en la literatura. Ninguno de los estudios existentes evalúa la matriz cruzada entre los tres paradigmas de detección y las técnicas avanzadas de aumento por objeto con armonización neuronal bajo desequilibrio severo de clases.

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

Cascade R-CNN representa la arquitectura convolucional de dos etapas orientada a alta precisión espacial @cai2018cascade. La primera etapa emplea una Red de Propuesta de Regiones para seleccionar candidatos sobre mapas de características convolucionales. La segunda etapa ejecuta una secuencia de cabezales de detección entrenados con umbrales de Intersección sobre Unión progresivamente más estrictos. Este diseño en cascada refina gradualmente las coordenadas de las cajas delimitadoras y minimiza los falsos positivos en escenarios de alta densidad de defectos @cai2018cascade. El costo computacional asociado al refinamiento multietapa se traduce en tiempos de inferencia mayores respecto a detectores de una etapa, pero la ganancia en precisión de localización justifica su aplicación en escenarios donde la tasa de falsos positivos es crítica @cai2018cascade.

YOLO26 representa la arquitectura convolucional de una etapa diseñada para inferencia en tiempo real @jocher2026ultralyticsyolo26unifiedrealtime. Adopta una formulación libre de anclajes que predice directamente los centros y dimensiones de las cajas delimitadoras desde mapas de características multiescala. Su diseño de cabeza dual elimina la necesidad de la etapa de supresión de no máximos en la inferencia, optimizando la velocidad de procesamiento y la latencia computacional @jocher2026ultralyticsyolo26unifiedrealtime. La ausencia de la etapa NMS reduce significativamente el tiempo de post-procesamiento, lo cual es ventajoso para aplicaciones en tiempo real donde cada milisegundo es crítico @jocher2026ultralyticsyolo26unifiedrealtime. Sin embargo, la arquitectura de una etapa puede ser más susceptible a la falta de datos de entrenamiento en comparación con los detectores de dos etapas.

RF-DETR representa la arquitectura basada en Vision Transformers optimizada para detección en tiempo real @robinson2026rfdetrneuralarchitecturesearch. Utiliza mecanismos de autoatención global bidireccional para capturar dependencias espaciales de largo alcance a lo largo de toda la superficie de la imagen @zhao2023detrs. Mediante Búsqueda de Arquitectura Neuronal, RF-DETR descubre configuraciones estructurales óptimas en la frontera de Pareto entre precisión de localización y latencia de procesamiento @robinson2026rfdetrneuralarchitecturesearch. A diferencia de los detectores puramente convolucionales, los transformers procesan la imagen completa mediante tokenización y capas de autoatención, lo que les permite modelar relaciones globales entre regiones distantes @zhao2023detrs. Esta capacidad resulta particularmente relevante para la inspección de madera, donde los defectos pueden distribuirse de manera dispersa a lo largo de la superficie del tablón.

La cuantificación del rendimiento de los detectores de objetos integra métricas de precisión espacial y eficiencia computacional @Shah2026Review. La precisión mide la proporción de predicciones positivas correctas, mientras que el recall evalúa la proporción de defectos reales detectados @Shah2026Review. El puntaje F1 representa la media armónica de ambas métricas. La Intersección sobre Unión evalúa la superposición espacial entre la caja predicha y la anotación real. La precisión promedio media mAP\@0.5 y mAP\@0.5:0.95 agrega el rendimiento a través de múltiples umbrales de superposición, aislando las fortalezas algorítmicas en clases desequilibradas @Shah2026Review. Las métricas de eficiencia computacional comprenden el tiempo de inferencia expresado en milisegundos por imagen, el rendimiento en cuadros por segundo, el número de parámetros flotantes en millones y el tamaño del modelo almacenado en disco en megabytes @prunella2023deep.

== Herramientas y Tecnologías <sec:tools>

El desarrollo del pipeline de experimentación se ejecuta sobre el lenguaje de programación Python en su versión 3.12. El framework de aprendizaje profundo principal corresponde a PyTorch versión 2.7.0 con aceleración por GPU mediante bibliotecas CUDA 12.8. Las operaciones suplementarias de visión computacional emplean torchvision versión 0.22.0. La arquitectura Cascade R-CNN se implementa mediante la librería MMDetection versión 3.2.0, soportada por MMCV versión 2.2.0 y MMEngine versión 0.10.7. El detector YOLO26 y el detector RT-DETR se ejecutan utilizando el marco Ultralytics en su versión 8.2.0. La arquitectura RF-DETR se compila desde el motor oficial RF-DETR versión 1.3.0.

El procesamiento de datos sintéticos y aumentos fotométricos utiliza Albumentations versión 1.4.0. Las primitivas de composición e inserción de objetos emplean la librería LibCom versión 0.2.0 integrada en el entorno de desarrollo. La gestión estricta de configuraciones de la tubería se programa mediante Pydantic versión 2.6.1. La manipulación acelerada de tablas de metadatos utiliza Polars versión 1.43.0 y OpenCV versión 5.0.0. El entorno virtual y la resolución de dependencias se administran mediante el gestor uv versión 0.6+. Todos los modelos fueron entrenados y evaluados en una GPU NVIDIA RTX 5070 Ti, lo cual establece el punto de referencia para las mediciones de tiempo de inferencia y rendimiento computacional reportadas en este estudio.

== Dataset <sec:dataset>

El estudio utiliza la versión filtrada y anotada en formato YOLO disponible en Kaggle @Nomihsa2024KaggleWood, derivada del conjunto de datos original Large-scale Image Dataset of Wood Surface Defects publicado por Kodytek et al. @Kodytek2022Dataset. El dataset original fue adquirido en un entorno industrial real durante la producción de un aserradero mediante una cámara de escaneo lineal JAI SW-4000TL-PMCL a una frecuencia de línea de 66 kHz @Kodytek2022Dataset. La versión filtrada empleada en este trabajo @Nomihsa2024KaggleWood ha sido preprocesada para incluir exclusivamente imágenes que contienen defectos y sus anotaciones han sido convertidas al formato YOLO estándar para la evaluación directa de modelos de detección de objetos. El dataset filtrado contiene un total de 4,000 imágenes en formato JPG con una resolución espacial fija de 2800 por 1024 píxeles @Nomihsa2024KaggleWood. El conjunto almacena 8,736 cajas delimitadoras anotadas distribuidas en 8 categorías de defectos superficiales. En promedio, cada imagen contiene 2.18 defectos, alcanzando un máximo de 15 defectos por imagen. La @fig:piechart-clases ilustra la distribución porcentual de frecuencia para cada clase de defecto.

#figure(
  image("figures/dataset/barchart_classes.svg", width: 95%),
  caption: [Distribución de clases de defectos en el dataset filtrado @Nomihsa2024KaggleWood.],
  kind: image,
) <fig:piechart-clases>

Las anotaciones proporcionan coordenadas normalizadas de cajas delimitadoras en formato YOLO. La distribución de clases refleja las condiciones reales de producción industrial @Kodytek2022Dataset. Las categorías mayoritarias corresponden a nudos vivos con 3,905 anotaciones, siendo el 44.7%, y nudos muertos con 2,835 anotaciones, siendo el 32.5%, combinando el 77.2% del conjunto. Las categorías intermedias incluyen resina con 639 anotaciones, siendo el 7.3%, grietas con 505 anotaciones, siendo el 5.8%, y nudos con grietas con 410 anotaciones, siendo el 4.7%. Las categorías minoritarias comprenden médula con 204 anotaciones, siendo el 2.3%, cuarcita con 129 anotaciones, siendo el 1.5%, y nudos faltantes con 109 anotaciones, siendo el 1.2%. El ratio de desequilibrio calculado alcanza un valor aproximado de 35.82. La @fig:defectos-ejemplo muestra ejemplos representativos de las ocho categorías de defectos anotadas en el conjunto de datos.

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

El método propuesto implementa un pipeline de experimentación de cinco etapas diseñado para garantizar la reproducibilidad y la comparabilidad justa entre configuraciones. Las etapas comprenden: (1) preparación de datos, (2) aumento de datos, (3) entrenamiento de modelos, (4) evaluación y (5) análisis de resultados. Cada etapa se ejecuta de forma independiente mediante un sistema de caché por pasos que almacena los resultados intermedios en disco, permitiendo la re-ejecución parcial sin reprocesar etapas completas. La configuración de toda la tubería se gestiona mediante modelos Pydantic tipados que garantizan la validación de parámetros en tiempo de compilación @colvin2024pydantic. La interfaz de línea de comandos permite la personalización de cualquier parámetro anidado mediante notación de puntos, facilitando la experimentación reproducible.

La etapa de preparación de datos aplica tres operaciones secuenciales sobre el dataset crudo. Primero, se recortan los bordes negros mediante segmentación por umbralización de Otsu @otsu1979threshold y operaciones morfológicas de cierre, aislando la región válida del tablón de madera. Segundo, las imágenes se reducen a la mitad de su resolución original mediante interpolación de área. Tercero, las anotaciones de cajas delimitadoras se transforman al espacio coordinado resultante y se filtran aquellas con dimensiones inferiores a 4 píxeles post-escalado, eliminando anotaciones demasiado pequeñas para ser útiles en el entrenamiento. El conjunto resultante se particiona en entrenamiento con 80%, validación con 10% y prueba con 10% mediante muestreo estratificado que preserva la distribución de clases en cada partición @kubat2000addressing.

Se evaluaron tres estrategias de aumento diseñadas para mitigar el desequilibrio de clases, dirigidas a alcanzar una proporción del 33% entre la clase minoritaria y la mayoritaria. Se diseñó cada estrategia para producir un conjunto de datos augmentado del mismo tamaño que el conjunto de entrenamiento original, evitando la introducción de sesgos por tamaño de dataset. Para la comparativa entre los paradigmas, se configuraron tres arquitecturas representativas de cada enfoque de detección de objetos. La evaluación se realiza en el conjunto de prueba de 400 imágenes utilizando las métricas COCO estándar: mAP\@0.5, mAP\@0.5:0.95, precisión, recall y F1. El tiempo de inferencia se mide promediando el tiempo total de procesamiento sobre todas las imágenes del conjunto de prueba.

Para aislar el efecto de las estrategias de aumento, todas las arquitecturas se entrenaron sin ponderación por clase, utilizando la función de pérdida estándar de cada modelo. Si bien técnicas como Focal Loss @lin2017focal, class-balanced loss @cui2019classbalanced y Seesaw Loss @wang2021seesaw están diseñadas para mitigar el desequilibrio de clases, incluirlas simultáneamente con las augmentaciones haría imposible atribuir las mejoras al origen correcto. Se evalúa estrictamente el aporte de las augmentaciones en el nivel de datos, dejando la combinación con estrategias de pérdida como trabajo futuro. Los modelos se evalúan sin post-procesamiento adicional más allá de los umbrales de confianza por defecto de cada arquitectura.

Albumentations con balanceo de clases emplea siete transformaciones a nivel de píxel con las siguientes probabilidades de aplicación: voltea horizontal a 0.5, voltea vertical a 0.5, rotación aleatoria de 90° a 0.5, rotación-escala-traslación a 0.5, contraste y brillo aleatorios a 0.4, variación de color a 0.3 y desenfoque gaussiano a 0.2. La generación del dataset identifica las clases raras por debajo del umbral objetivo y aumenta selectivamente las imágenes que las contienen, mientras decrementa proporcionalmente las imágenes con solo clases mayoritarias para mantener el tamaño constante del conjunto de entrenamiento.

BoxAug estándar implementa un enfoque de recorte y pegado de objetos. Para cada clase rara, recorta instancias de un banco de objetos construido previamente, aplica transformaciones estocásticas a nivel de parche, incluyendo jitter de escala entre 0.8 y 1.2, rotación, voltea, recorte aleatorio, diferentes tipos de ruido, y operaciones morfológicas, y las pega en posiciones espaciales válidas calculadas a partir de guías de ubicación por clase. Las guías espaciales codifican conocimiento del dominio: por ejemplo, los nudos faltantes tienden a localizarse en los bordes de la imagen, mientras que la cuarcita aparece predominantemente en la región central.

BoxAug con LibCom utiliza el mismo procedimiento de recorte y pegado que BoxAug estándar, pero reemplaza la inserción directa por composición profunda mediante la librería LibCom @niu2021making. Las operaciones de borde emplean modos de armonización neuronal que eliminan las discontinuidades visuales en los márgenes entre el fondo y la imagen superpuesta. Las transformaciones geométricas se limitan a jitter de escala y volteo horizontal/vertical, excluyendo transformaciones de ruido a nivel de píxel.

Cascade R-CNN representa al paradigma de dos etapas. Posee una arquitectura convolucional basada en ResNet-50 con Feature Pyramid Network (FPN) @cai2018cascade. Se entrena durante 12 épocas con optimizador AdamW con learning rate de 0.0001 y weight decay de 0.0001, batch size de 8 y resolución de entrada de 640 por 640 píxeles. La evaluación de validación se ejecuta en cada época utilizando la métrica COCO bbox, y se selecciona el checkpoint con mayor mAP bbox. Esta configuración de entrenamiento relativamente conservadora con learning rate bajo busca explotar las capacidades de refinamiento multietapa de la arquitectura sin riesgo de divergencia @cai2018cascade.

YOLO26 representa al paradigma de una etapa. Posee una arquitectura convolucional libre de anclajes con diseño de cabeza dual que elimina la etapa NMS @jocher2026ultralyticsyolo26unifiedrealtime. Se configura con la variante yolo26m, resolución de 640 por 640 píxeles, batch size de 16 y learning rate inicial de 0.01. El entrenamiento utiliza early stopping con paciencia de 10 épocas y guarda checkpoints cada 5 épocas. El número máximo de épocas es 100.

RF-DETR representa al paradigma basado en transformers. Posee una arquitectura con búsqueda de arquitectura neuronal @robinson2026rfdetrneuralarchitecturesearch. Se utiliza la variante rfdetr-m con resolución de 512 por 512 píxeles, batch size de 8, learning rate de 0.001 y weight decay de 1e-4. El entrenamiento incluye warmup de 5 épocas, early stopping con paciencia de 10, y gradient checkpointing para reducir el consumo de memoria. El número máximo de épocas es 50.

= Resultados <sec:results>

La @fig:matrix-map50 presenta la matriz de rendimiento mAP\@0.5 para las 12 combinaciones de modelo y estrategia de aumento. Cascade R-CNN domina la fila superior con valores entre 0.701 y 0.711, mostrando una variación mínima entre estrategias de aumento con un rango de 0.010. RF-DETR ocupa la posición intermedia con valores entre 0.633 y 0.668, y YOLO26 muestra la mayor dispersión con valores entre 0.539 y 0.626. Este patrón indica que la sensibilidad a la augmentación varía significativamente entre paradigmas, siendo los detectores de una etapa más receptivos a las transformaciones de datos que los de dos etapas.

#figure(
  image("figures/results/aug_paradigm_map50_heatmap.png", width: 95%),
  caption: [Matriz de rendimiento mAP\@0.5 intersectando tres paradigmas de detección con cuatro estrategias de aumento.],
  kind: image,
) <fig:matrix-map50>

La @fig:tabla-principal resume las métricas completas de las 12 configuraciones. Cascade R-CNN con Albumentations obtiene el mayor mAP\@0.5 de 0.711, mientras que Cascade R-CNN con BoxAug LibCom alcanza el mejor mAP\@0.5:0.95 de 0.409, la mayor precisión de 0.546 y el mejor F1 de 0.471. YOLO26 baseline presenta el menor rendimiento en todas las métricas, con mAP\@0.5 de 0.539 y F1 de 0.307. Estos resultados confirman que Cascade R-CNN ofrece la mejor localización espacial, mientras que YOLO26 tiene mayor margen de mejora mediante augmentación de datos.

#figure(
  table(
    columns: (1fr, 1fr, 0.7fr, 0.7fr, 0.7fr, 0.7fr, 0.7fr),
    align: (left, left, center, center, center, center, center),
    table.header([Modelo], [Aumentación], [mAP\@50], [mAP\@50:95], [Precisión], [Recall], [F1]),
    [Cascade R-CNN], [Albumentations], [0.711], [0.400], [0.495], [0.396], [0.440],
    [Cascade R-CNN], [Baseline], [0.704], [0.400], [0.494], [0.406], [0.446],
    [Cascade R-CNN], [BoxAug LibCom], [0.702], [0.409], [0.546], [0.414], [0.471],
    [Cascade R-CNN], [BoxAug Std], [0.701], [0.406], [0.542], [0.411], [0.468],
    [RF-DETR], [Albumentations], [0.668], [0.377], [0.508], [0.391], [0.442],
    [RF-DETR], [Baseline], [0.646], [0.371], [0.493], [0.366], [0.420],
    [RF-DETR], [BoxAug LibCom], [0.648], [0.384], [0.505], [0.368], [0.426],
    [RF-DETR], [BoxAug Std], [0.633], [0.367], [0.479], [0.367], [0.416],
    [YOLO26], [Albumentations], [0.618], [0.348], [0.482], [0.357], [0.410],
    [YOLO26], [Baseline], [0.539], [0.286], [0.333], [0.284], [0.307],
    [YOLO26], [BoxAug LibCom], [0.605], [0.341], [0.403], [0.334], [0.365],
    [YOLO26], [BoxAug Std], [0.626], [0.350], [0.433], [0.341], [0.381],
  ),
  caption: [Métricas de rendimiento en el conjunto de prueba para las 12 configuraciones del benchmark.],
  scope: "parent",
  kind: table,
  placement: auto,
) <fig:tabla-principal>

La @fig:delta-baseline muestra el impacto de cada estrategia de aumento respecto al baseline para cada modelo. YOLO26 presenta la mayor sensibilidad a la augmentación: Albumentations aporta +0.080, BoxAug LibCom +0.067 y BoxAug estándar +0.088 de mejora absoluta en mAP\@0.5. En contraste, Cascade R-CNN es prácticamente insensible: las tres estrategias producen cambios dentro del rango de -0.003 a +0.007. RF-DETR muestra un comportamiento mixto: Albumentations aporta +0.022, pero BoxAug estándar degrada el rendimiento en -0.012.

#figure(
  image("figures/results/aug_delta_vs_baseline.png", width: 95%),
  caption: [Impacto de las estrategias de augmentación respecto al baseline (Δ mAP\@0.5).],
  kind: image,
) <fig:delta-baseline>

La @fig:heatmap-clase presenta el AP promedio por clase en mAP\@0.5:0.95 para las 12 configuraciones. La clase más fácil es médula, con AP de hasta 0.506 con Cascade R-CNN, mientras que cuarcita es la más difícil, con AP entre 0.0 y 0.153. YOLO26 baseline y YOLO26 BoxAug estándar obtienen AP = 0.0 para cuarcita, indicando una falla completa de detección para esta clase. Los nudos vivos y nudos muertos muestran valores de AP moderados de 0.198 a 0.250 a pesar de ser las clases mayoritarias, lo que sugiere alta varianza intraclase.

#figure(
  image("figures/results/per_class_ap_heatmap.png", width: 95%),
  caption: [Mapa de calor de precisión promedio por clase de defecto (AP\@0.5:0.95).],
  kind: image,
) <fig:heatmap-clase>

La @fig:velocidad-precision ilustra el compromiso entre velocidad de inferencia y precisión. YOLO26 procesa cada imagen en 5.4 ms en promedio de las cuatro configuraciones, RF-DETR en 10.3 ms y Cascade R-CNN en 24.5 ms. Cascade R-CNN es 4.5 veces más lento que YOLO26 pero alcanza un mAP\@0.5 14.2% mayor. RF-DETR ofrece un punto intermedio con 10.3 ms y mAP\@0.5 de 0.649 promedio.

#figure(
  image("figures/results/speed_accuracy_tradeoff.png", width: 95%),
  caption: [Compromiso entre velocidad de inferencia (ms/imagen) y precisión (mAP\@0.5).],
  kind: image,
) <fig:velocidad-precision>

La @fig:curvas-convergencia muestra las curvas de convergencia de mAP\@0.5 en validación a lo largo de las épocas. RF-DETR converge más temprano, con mejor época entre 8 y 21, Cascade R-CNN se estabiliza alrededor de la época 9 y 12, y YOLO26 requiere más épocas para alcanzar su máximo, entre 16 y 28. Las curvas de YOLO26 presentan mayor oscilación, particularmente en la configuración BoxAug estándar. Este patrón de convergencia sugiere que los transformers necesitan menos iteraciones para capturar las características relevantes, mientras que las arquitecturas convolucionales de una etapa requieren más épocas para estabilizar sus pesos. La oscilación en YOLO26 puede indicar sensibilidad a la variabilidad de las muestras de entrenamiento en cada lote.

#figure(
  image("figures/results/training_curves_map.png", width: 95%),
  caption: [Curvas de convergencia de mAP\@0.5 en validación durante el entrenamiento.],
  kind: image,
) <fig:curvas-convergencia>

La @fig:tiempo-entrenamiento compara el tiempo total de entrenamiento por configuración. YOLO26 es el más eficiente, entre 0.24 y 0.37 horas, seguido por Cascade R-CNN, entre 0.46 y 0.49 horas, y RF-DETR, entre 0.40 y 0.68 horas. El tiempo de entrenamiento de RF-DETR varía significativamente entre configuraciones debido al early stopping: el baseline entrena 31 épocas durante 0.68 h mientras que Albumentations entrena solo 18 épocas durante 0.40 h. Esta variabilidad en RF-DETR indica que la augmentación de datos puede acelerar la convergencia al proporcionar muestras más representativas.

#figure(
  image("figures/results/training_time_comparison.png", width: 95%),
  caption: [Comparación del tiempo total de entrenamiento por configuración.],
  kind: image,
) <fig:tiempo-entrenamiento>

= Discusión <sec:discussion>

Los resultados obtenidos en este benchmark revelan patrones que ameritan un análisis detallado sobre las interacciones entre arquitecturas de detección y estrategias de aumento de datos en el contexto del desequilibrio severo de clases propio de la inspección industrial de madera. La superioridad de Cascade R-CNN en precisión absoluta, con mAP\@0.5 de 0.711, resulta consistente con su diseño de dos etapas orientado a alta localización espacial @cai2018cascade. El mecanismo de refinamiento progresivo de cajas delimitadoras mediante la Red de Propuesta de Regiones y los cabezales en cascada con umbrales de Intersección sobre Unión crecientes minimiza los falsos positivos en escenarios de alta densidad de defectos @cai2018cascade. Sin embargo, la insensibilidad de Cascade R-CNN a las estrategias de aumento, con variaciones dentro del rango de -0.003 a +0.007 en mAP\@0.5, indica que las arquitecturas de dos etapas con mayor capacidad de representación pueden estar limitadas por factores distintos al volumen de datos, como la arquitectura de la red o la función de pérdida estándar.

YOLO26 presenta la mayor sensibilidad a la augmentación de datos, con mejoras relativas de hasta el 16.3% respecto a su baseline, pasando de un mAP\@0.5 de 0.539 a 0.626 con BoxAug estándar. Este comportamiento es consistente con la literatura que indica que los detectores de una etapa son más dependientes del volumen de datos de entrenamiento @hussain2023yolo. La augmentación mitiga efectivamente la subrepresentación de clases raras para esta arquitectura, como lo evidencia la mejora de cuarcita de AP = 0.0 en baseline a AP = 0.192 con BoxAug estándar. La mayor oscilación observada en las curvas de convergencia de YOLO26, particularmente en la configuración BoxAug estándar, puede atribuirse a la variabilidad introducida por las muestras sintéticas en un modelo que carece del mecanismo de refinamiento multietapa de Cascade R-CNN. Este resultado sugiere que los detectores de una etapa son los principales beneficiarios de las técnicas de aumento por objeto en escenarios de desequilibrio severo.

RF-DETR muestra un comportamiento mixto: Albumentations mejora el rendimiento en +0.022, pero BoxAug estándar lo degrada en -0.012. Este resultado es particularmente relevante para la comunidad de investigación en transformers para visión industrial @hutten2022vision. Las transformaciones de ruido a nivel de parche introducen artefactos que los mecanismos de autoatención global bidireccional interpretan como patrones relevantes, generando confusión durante el entrenamiento. A diferencia de los modelos convolucionales, que procesan información local mediante filtros deslizantes, los transformers capturan dependencias espaciales de largo alcance que pueden amplificar la influencia de artefactos locales @zhao2023detrs. Este resultado sugiere que las estrategias de aumento por objeto requieren una adaptación cuidadosa cuando se aplican a arquitecturas basadas en autoatención.

El análisis por clase revela resultados contraintuitivos que desafían la suposición de que la frecuencia de clase determina directamente la dificultad de detección. Cuarcita, con solo 129 anotaciones (1.5% del dataset), obtiene el peor rendimiento con AP entre 0.0 y 0.153, lo cual es esperable dado su bajo contraste visual contra la veta de la madera. Sin embargo, médula, siendo la segunda clase menos frecuente con solo 204 anotaciones, obtiene el mayor AP de hasta 0.506. Esta disparidad indica que la distinguibilidad visual del defecto es un factor determinante que interactúa con la frecuencia de clase. Los defectos con patrones visuales distintivos, como la médula con su apariencia característica de línea central, son más susceptibles a la detección automática independientemente de su representación en el dataset @Chen2023Recognition.

Los nudos vivos y nudos muertos, que representan conjuntamente el 77.2% del dataset, muestran valores de AP moderados de 0.198 a 0.250 a pesar de su alta prevalencia. Este hallazgo confirma que la alta varianza intraclase de estos defectos, donde un mismo tipo de anomalía puede presentar apariencias visuales muy diferentes @Kodytek2022Dataset, constituye un desafío que no se resuelve únicamente con mayor volumen de datos. La variabilidad en el grano de la madera de fondo, combinada con las diferentes presentaciones de nudos vivos y muertos, genera una distribución de características que dificulta la convergencia del modelo hacia representaciones discriminativas robustas. La ausencia de ponderación por clase en las funciones de pérdida amplifica el efecto del desequilibrio, particularmente visible en cuarcita, que obtiene AP = 0.0 con YOLO26 baseline. Este resultado confirma que la augmentación de datos por sí sola es insuficiente para clases con representación inferior al 2% del dataset @cui2019classbalanced. La combinación de técnicas de aumento a nivel de datos con estrategias de pérdida como Focal Loss @lin2017focal o Seesaw Loss @wang2021seesaw podría ofrecer una solución más integral para el desequilibrio severo de clases.

En términos de eficiencia computacional, el compromiso entre velocidad y precisión se manifiesta de manera diferenciada entre los tres paradigmas. YOLO26 ofrece la mejor relación velocidad-precisión para despliegue en tiempo real con 5.4 ms por imagen y mAP\@0.5 de 0.626, lo cual es relevante para líneas de producción con velocidades de hasta 9.6 m/s @Kodytek2022Dataset. Cascade R-CNN es preferido cuando la precisión es prioritaria sobre la latencia con 24.5 ms por imagen y mAP\@0.5 de 0.711, siendo 4.5 veces más lento que YOLO26. RF-DETR ofrece un punto intermedio con 10.3 ms y mAP\@0.5 de 0.649 promedio, posicionándose como una alternativa viable para aplicaciones donde el compromiso velocidad-precisión debe balancearse con la capacidad de capturar dependencias espaciales de largo alcance. La selección del arquitectura óptima dependerá de los requisitos específicos de la aplicación industrial, considerando factores como la velocidad de la línea de producción, la tolerancia a falsos positivos y los recursos computacionales disponibles.

= Conclusiones <sec:conclusions>

Este estudio presentó un benchmark comparativo de tres paradigmas de detección de objetos con cuatro estrategias de aumento de datos para el reconocimiento de defectos superficiales en madera, evaluando 12 configuraciones sobre un dataset con desequilibrio severo de 1 a 35.82. Los resultados principales demuestran que Cascade R-CNN alcanza la mayor precisión absoluta con mAP\@0.5 de 0.711, YOLO26 presenta la mayor sensibilidad a la augmentación con una mejora relativa del 16.3%, y RF-DETR muestra un comportamiento mixto donde BoxAug estándar degrada el rendimiento. El análisis por clase revela que la dificultad de detección depende tanto de la frecuencia como de la distinguibilidad visual del defecto. La augmentación de datos por sí sola resulta insuficiente para clases con representación inferior al 2% del dataset, lo que subraya la necesidad de estrategias complementarias de ponderación por clase.

= Limitaciones y Trabajos Futuros <sec:future>

Los resultados de este estudio abren varias líneas de investigación prometedoras. La línea más inmediata corresponde a la incorporación de ponderación por clase en las funciones de pérdida. Técnicas como Focal Loss @lin2017focal, class-balanced loss @cui2019classbalanced y Seesaw Loss @wang2021seesaw están diseñadas específicamente para mitigar el sesgo hacia clases mayoritarias. Dado que cuarcita obtiene AP = 0.0 con YOLO26 baseline, la combinación de augmentación de datos con ponderación por clase podría recuperar instancias de esta clase que actualmente se pierden completamente. La segunda línea prioritaria corresponde a la augmentación basada en modelos de difusión. Los métodos de cut-and-paste evaluados, como BoxAug, están limitados por la cantidad de instancias raras disponibles para recortar del dataset original. Con solo 129 anotaciones de cuarcita, el banco de objetos es demasiado pequeño para generar augmentación diversa. Los modelos de difusión condicional como Stable Diffusion con ControlNet pueden generar instancias sintéticas de clases raras sin depender de crops existentes, ofreciendo una alternativa potencialmente más efectiva para desbalance severo @capogrosso2024diffusion.

La expansión del dataset hacia otras especies de madera con diferentes patrones de grano y defectos es esencial para validar la generalización más allá de la especie y entorno industrial actuales. En paralelo, la cuantización de modelos a INT8 y FP16 podría reducir tiempos de inferencia para el despliegue en líneas de producción con restricciones de hardware, mientras que la evaluación de arquitecturas transformer como DINO y Grounding DINO podría determinar si los mecanismos de autoatención global mejoran la detección de defectos de bajo contraste. La combinación de múltiples líneas de investigación, incluyendo ponderación por clase, augmentación basada en difusión y optimización de modelos, podría conducir a sistemas de inspección más robustos y eficientes para la industria maderera. Estas direcciones futuras buscan abordar las limitaciones identificadas en el presente benchmark y acercar los sistemas de detección automatizada a los requisitos operativos de las plantas de procesamiento de madera. El desarrollo de pipelines experimentales reproducibles, como el empleado en este estudio, facilitará la evaluación comparativa de las nuevas técnicas que surjan de estas líneas de investigación.

#heading(numbering: none)[Declaración de Contribución de Autoría]
Chambilla Perca R.M. se declara bajo los roles de Software y Writing. Jara Mamani M.A. se declara bajo los roles de Data Curation, Conceptualization y Validation. Mestas Zegarra C.R. se declara bajo los roles de Project Administration, Methodology y Writing. Noa Camino Y.J. se declara bajo los roles de Acquisition e Investigation. Sequeiros Condori L.G. se declara bajo los roles de Conceptualization, Investigation y Software.

#heading(numbering: none)[Declaración de Conflictos de Intereses]

Los autores declaran que no tienen ningún conflicto de intereses económicos conocido ni relaciones personales que pudieran dar la impresión de influir en el trabajo presentado en este artículo.


#heading(numbering: none)[Declaración Ética]

Este estudio no implica ningún experimento con seres humanos ni con animales, por lo que no se requirió ninguna autorización ética. Por lo tanto, no procede incluir una declaración ética.
.
#heading(numbering: none)[Consentimiento para Participación]

No aplicable

#heading(numbering: none)[Consentimiento para Publicación]

No aplicable

#heading(numbering: none)[Financiamiento]

No aplicable

#heading(numbering: none)[Reconocimientos]

No aplicable

#heading(numbering: none)[Disponibilidad de Código]

Los scripts de análisis personalizados y código fuente generados durante este estudio están públicamente disponibles en el repositorio de GitHub: https://github.com/christianmz565/ia-2026-final, licenciado bajo la licencia AGPL-3.0.

#heading(numbering: none)[Disponibilidad de Datos]

Los datos utilizados en este estudio están disponibles públicamente en Kaggle: https://www.kaggle.com/datasets/nomihsa965/large-scale-image-dataset-of-wood-surface-defects, licenciados bajo la licencia CC BY 4.0.

#bibliography("references.bib", style: "ieee", title: [Referencias])
